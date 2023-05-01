"""LiveKit Server SDK

Loosely modeled after the official LiveKit Server SDK:
https://docs.livekit.io/server-sdk-js/
"""

__version__ = "1.0.0"

import calendar
import dataclasses
import datetime
import typing as t

import jwt
from twirp.context import Context as _TwirpContext

from livekit import _utils
from livekit import models as _models
from livekit import room as _room
from livekit import twirp as _twirp

DEFAULT_TOKEN_TTL = datetime.timedelta(hours=6)


@dataclasses.dataclass
class VideoGrant:
    room_create: t.Optional[bool] = None
    room_join: t.Optional[bool] = None
    room_list: t.Optional[bool] = None
    room_record: t.Optional[bool] = None
    room_admin: t.Optional[bool] = None
    room: t.Optional[str] = None
    can_publish: t.Optional[bool] = None
    can_subscribe: t.Optional[bool] = None
    can_publish_data: t.Optional[bool] = None
    hidden: t.Optional[bool] = None


@dataclasses.dataclass
class AccessToken:
    api_key: str
    api_secret: str
    grant: VideoGrant = dataclasses.field(default_factory=VideoGrant)
    identity: t.Optional[str] = None
    name: t.Optional[str] = None
    ttl: datetime.timedelta = DEFAULT_TOKEN_TTL
    metadata: t.Optional[str] = None

    def __post_init__(self):
        if self.grant.room_join and self.identity is None:
            raise ValueError("identity is required for room_join grant")
        if self.ttl.total_seconds() <= 0:
            raise ValueError("AccessToken must expire in the future.")

    def to_jwt(self) -> str:
        payload = {
            "video": dataclasses.asdict(
                self.grant, dict_factory=_utils.camel_case_dict
            ),
            "iss": self.api_key,
            "nbf": calendar.timegm(datetime.datetime.utcnow().utctimetuple()),
            "exp": calendar.timegm(
                (datetime.datetime.utcnow() + self.ttl).utctimetuple()
            ),
        }
        if self.metadata is not None:
            payload["metadata"] = self.metadata
        if self.identity is not None:
            payload["sub"] = self.identity
        if self.name:
            payload["name"] = self.name
        return jwt.encode(payload, self.api_secret)


class RoomServiceClient:
    """
    Client to access Room APIs
    """

    def __init__(self, host: str, api_key: str, api_secret: str):
        self._client = _twirp.RoomServiceClient(host)
        self._api_key = api_key
        self._api_secret = api_secret

    def _create_context(self, **grant_kwargs):
        grant = VideoGrant(**grant_kwargs)
        access_token = AccessToken(
            self._api_key,
            self._api_secret,
            grant=grant,
            ttl=datetime.timedelta(minutes=10),
        )
        return _TwirpContext(
            headers={"Authorization": f"Bearer {access_token.to_jwt()}"}
        )

    def create_room(
        self,
        name: str,
        empty_timeout: t.Optional[int] = None,
        max_participants: t.Optional[int] = None,
    ) -> _models.Room:
        """
        Creates a new room. Explicit room creation is not required, since rooms will
        be automatically created when the first participant joins. This method can be
        used to customize room settings.
        """

        ctx = self._create_context(room_create=True)
        request = _room.CreateRoomRequest(
            name=name,
            empty_timeout=empty_timeout,
            max_participants=max_participants,
        )
        return self._client.CreateRoom(ctx=ctx, request=request)

    def list_rooms(self) -> t.List[_models.Room]:
        """
        List rooms that are active on the server.
        """
        ctx = self._create_context(room_list=True)
        request = _room.ListRoomsRequest()
        response = self._client.ListRooms(ctx=ctx, request=request)
        return [r for r in response.rooms]

    def delete_room(self, room: str):
        """
        Deletes an existing room by name or id. Will disconnect all participants that
        are currently in the room.
        """
        ctx = self._create_context(room_create=True, room_admin=True, room=room)
        request = _room.DeleteRoomRequest(room=room)
        self._client.DeleteRoom(ctx=ctx, request=request)

    def list_participants(self, room: str) -> t.List[_models.ParticipantInfo]:
        """
        Lists participants in a room
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = _room.ListParticipantsRequest(room=room)
        response = self._client.ListParticipants(ctx=ctx, request=request)
        return [p for p in response.participants]

    def get_participant(self, room: str, identity: str) -> _models.ParticipantInfo:
        """
        Gets information on a specific participant
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = _room.RoomParticipantIdentity(room=room, identity=identity)
        return self._client.GetParticipant(ctx=ctx, request=request)

    def remove_participant(self, room: str, identity: str):
        """
        Removes a participant from room.
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = _room.RoomParticipantIdentity(room=room, identity=identity)
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
        request = _room.MuteRoomTrackRequest(
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
        permission: t.Optional[_models.ParticipantPermission] = None,
    ):
        """
        Update participant metadata, will cause updates to be broadcasted to everyone
        in the room.
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = _room.UpdateParticipantRequest(
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
        track_sids: t.List[str],
        subscribe: bool,
    ):
        """
        Subscribes or unsubscribe a participant from tracks.

        As an admin, you can subscribe a participant to a track even if they do not
        have canSubscribe permission.
        """
        ctx = self._create_context(room_admin=True, room=room)
        request = _room.UpdateSubscriptionsRequest(
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
        request = _room.UpdateRoomMetadataRequest(room=room, metadata=metadata)
        self._client.UpdateRoomMetadata(ctx=ctx, request=request)

    def send_data(
        self,
        room: str,
        data: bytes,
        kind: _models.DataPacket.Kind,
        destination_sids: t.Optional[t.List[str]] = None,
    ):
        """
        Sends data messages to participants, triggering `onDataReceived` event on clients.
        """
        if destination_sids is None:
            destination_sids = []
        ctx = self._create_context(room_admin=True, room=room)
        request = _room.SendDataRequest(
            room=room,
            data=data,
            kind=kind,
            destination_sids=destination_sids,
        )
        self._client.SendData(ctx=ctx, request=request)
