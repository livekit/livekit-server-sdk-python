"""LiveKit Server SDK

Modeled after the official LiveKit Server SDK:
https://docs.livekit.io/server-sdk-js/
"""

__all__ = [
    # utils
    "utils",
    "AccessToken",
    "VideoGrant",
    # analytics
    "AnalyticsRecorderServiceClient",
    "AnalyticsRecorderServiceServer",
    # models
    "DataPacketKind",
    "ParticipantInfo",
    "Room",
    "TrackInfo",
    # room
    "CreateRoomRequest",
    "DeleteRoomRequest",
    "DeleteRoomResponse",
    "ListParticipantsRequest",
    "ListParticipantsResponse",
    "ListRoomsRequest",
    "ListRoomsResponse",
    "MuteRoomTrackRequest",
    "MuteRoomTrackResponse",
    "RemoveParticipantResponse",
    "RoomParticipantIdentity",
    "SendDataRequest",
    "SendDataResponse",
    "UpdateParticipantRequest",
    "UpdateRoomMetadataRequest",
    "UpdateSubscriptionsRequest",
    "UpdateSubscriptionsResponse",
    # recording
    "RecordingServiceClient",
    "RecordingServiceServer",
    # room service
    "RoomServiceClient",
    "RoomServiceServer",
]

__version__ = "0.2.4"

import calendar
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta
from enum import IntEnum
from typing import List, Optional

import jwt
from twirp.context import Context  # noqa

from livekit import utils
from livekit.proto.livekit_analytics_pb2 import *
from livekit.proto.livekit_models_pb2 import *
from livekit.proto.livekit_room_pb2 import *
from livekit.twirp.livekit_analytics_twirp import *
from livekit.twirp.livekit_recording_twirp import *
from livekit.twirp.livekit_room_twirp import RoomServiceClient as TwirpRoomServiceClient
from livekit.twirp.livekit_room_twirp import RoomServiceServer

DEFAULT_TOKEN_TTL = timedelta(hours=6)


@dataclass
class VideoGrant:
    room_create: Optional[bool] = None
    room_join: Optional[bool] = None
    room_list: Optional[bool] = None
    room_record: Optional[bool] = None
    room_admin: Optional[bool] = None
    room: Optional[str] = None
    can_publish: Optional[bool] = None
    can_subscribe: Optional[bool] = None
    can_publish_data: Optional[bool] = None
    hidden: Optional[bool] = None


@dataclass
class AccessToken:
    api_key: str
    api_secret: str
    grant: VideoGrant = field(default_factory=VideoGrant)
    identity: Optional[str] = None
    ttl: timedelta = DEFAULT_TOKEN_TTL
    metadata: Optional[str] = None

    def __post_init__(self):
        if self.grant.room_join and self.identity is None:
            raise ValueError("identity is required for room_join grant")
        if self.ttl.total_seconds() <= 0:
            raise ValueError("AccessToken must expire in the future.")

    def to_jwt(self) -> str:
        payload = {
            "video": asdict(self.grant, dict_factory=utils.camel_case_dict),
            "iss": self.api_key,
            "nbf": calendar.timegm(datetime.utcnow().utctimetuple()),
            "exp": calendar.timegm((datetime.utcnow() + self.ttl).utctimetuple()),
        }
        if self.metadata is not None:
            payload["metadata"] = self.metadata
        if self.identity is not None:
            payload["sub"] = self.identity
        return jwt.encode(payload, self.api_secret)


class DataPacketKind(IntEnum):
    RELIABLE = 0
    LOSSY = 1


class RoomServiceClient:
    """
    Client to access Room APIs
    """

    def __init__(self, host: str, api_key: str, api_secret: str):
        self._client = TwirpRoomServiceClient(host)
        self._api_key = api_key
        self._api_secret = api_secret

    def _create_context(self, **grant_kwargs):
        grant = VideoGrant(**grant_kwargs)
        access_token = AccessToken(
            self._api_key,
            self._api_secret,
            grant=grant,
            ttl=timedelta(minutes=10),
        )
        return Context(headers={"Authorization": f"Bearer {access_token.to_jwt()}"})

    def create_room(
        self,
        name: str,
        empty_timeout: Optional[int] = None,
        max_participants: Optional[int] = None,
    ) -> Room:
        """
        Creates a new room. Explicit room creation is not required, since rooms will
        be automatically created when the first participant joins. This method can be
        used to customize room settings.
        """

        ctx = self._create_context(room_create=True)
        request = CreateRoomRequest(
            name=name,
            empty_timeout=empty_timeout,
            max_participants=max_participants,
        )
        return self._client.CreateRoom(ctx=ctx, request=request)

    def list_rooms(self) -> List[Room]:
        """
        List rooms that are active on the server.
        """
        ctx = self._create_context(room_list=True)
        request = ListRoomsRequest()
        response = self._client.ListRooms(ctx=ctx, request=request)
        return [r for r in response.rooms]

    def delete_room(self, room: str):
        """
        Deletes an existing room by name or id. Will disconnect all participants that
        are currently in the room.
        """
        # TODO: seems like only `room_create` should be necessary
        ctx = self._create_context(room_create=True, room_admin=True, room=room)
        request = DeleteRoomRequest(room=room)
        self._client.DeleteRoom(ctx=ctx, request=request)

    def list_participants(self, room: str) -> List[ParticipantInfo]:
        """
        Lists participants in a room
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = ListParticipantsRequest(room=room)
        response = self._client.ListParticipants(ctx=ctx, request=request)
        return [p for p in response.participants]

    def get_participant(self, room: str, identity: str) -> ParticipantInfo:
        """
        Gets information on a specific participant
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = RoomParticipantIdentity(room=room, identity=identity)
        return self._client.GetParticipant(ctx=ctx, request=request)

    def remove_participant(self, room: str, identity: str):
        """
        Removes a participant from room.
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = RoomParticipantIdentity(room=room, identity=identity)
        self._client.RemoveParticipant(ctx=ctx, request=request)

    def mute_published_track(
        self,
        room: str,
        identity: str,
        track_sid: str,
        muted: bool,
    ):
        """
        Mute/unmute a participant's track.
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = MuteRoomTrackRequest(
            room=room,
            identity=identity,
            track_sid=track_sid,
            muted=muted,
        )
        self._client.MutePublishedTrack(ctx=ctx, request=request)

    def update_participant(
        self,
        room: str,
        identity: str,
        metadata: str = "",
        permission: Optional[ParticipantPermission] = None,
    ):
        """
        Update participant metadata, will cause updates to be broadcasted to everyone
        in the room.
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = UpdateParticipantRequest(
            room=room,
            identity=identity,
            metadata=metadata,
            permission=permission,
        )
        self._client.UpdateParticipant(ctx=ctx, request=request)

    def update_subscriptions(
        self,
        room: str,
        identity: str,
        track_sids: List[str],
        subscribe: bool,
    ):
        """
        Subscribes or unsubscribe a participant from tracks.

        As an admin, you can subscribe a participant to a track even if they do not
        have canSubscribe permission.
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = UpdateSubscriptionsRequest(
            room=room,
            identity=identity,
            track_sids=track_sids,
            subscribe=subscribe,
        )
        self._client.UpdateSubscriptions(ctx=ctx, request=request)

    def update_room_metadata(self, room: str, metadata: str):
        """
        Update room level metadata.

        This API allows you to attach user-defined metadata to a room.
        Changes to metadata will be broadcasted to all participants in the room.
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = UpdateRoomMetadataRequest(room=room, metadata=metadata)
        self._client.UpdateRoomMetadata(ctx=ctx, request=request)

    def send_data(
        self,
        room: str,
        data: bytes,
        kind: DataPacketKind,
        destination_sids: Optional[List[str]] = None,
    ):
        """
        Sends data messages to participants, triggering `onDataReceived` event on clients.
        """
        if destination_sids is None:
            destination_sids = []
        ctx = self._create_context(room_admin=True, room=room)
        request = SendDataRequest(
            room=room,
            data=data,
            kind=kind.value,
            destination_sids=destination_sids,
        )
        self._client.SendData(ctx=ctx, request=request)
