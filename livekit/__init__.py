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

__version__ = "0.1.1"

import calendar
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta
from typing import Optional

import jwt
from twirp.context import Context  # noqa

from livekit import utils
from livekit.proto.livekit_analytics_pb2 import *
from livekit.proto.livekit_room_pb2 import *
from livekit.proto.livekit_models_pb2 import *
from livekit.twirp.livekit_analytics_twirp import *
from livekit.twirp.livekit_recording_twirp import *
from livekit.twirp.livekit_room_twirp import *

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
    ttl: Optional[timedelta] = DEFAULT_TOKEN_TTL

    def __post_init__(self):
        if self.grant.room_join and self.identity is None:
            raise ValueError("identity is required for room_join grant")

    def to_jwt(self) -> str:
        payload = {
            "video": asdict(self.grant, dict_factory=utils.camel_case_dict),
            "iss": self.api_key,
            "nbf": calendar.timegm(datetime.utcnow().utctimetuple()),
            "exp": calendar.timegm((datetime.utcnow() + self.ttl).utctimetuple()),
        }
        if self.identity is not None:
            payload["sub"] = self.identity
        return jwt.encode(payload, self.api_secret)
