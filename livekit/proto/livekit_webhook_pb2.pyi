from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import livekit_egress_pb2 as _livekit_egress_pb2
import livekit_ingress_pb2 as _livekit_ingress_pb2
import livekit_models_pb2 as _livekit_models_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class WebhookEvent(_message.Message):
    __slots__ = [
        "created_at",
        "egress_info",
        "event",
        "id",
        "ingress_info",
        "num_dropped",
        "participant",
        "room",
        "track",
    ]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EGRESS_INFO_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INGRESS_INFO_FIELD_NUMBER: _ClassVar[int]
    NUM_DROPPED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    created_at: int
    egress_info: _livekit_egress_pb2.EgressInfo
    event: str
    id: str
    ingress_info: _livekit_ingress_pb2.IngressInfo
    num_dropped: int
    participant: _livekit_models_pb2.ParticipantInfo
    room: _livekit_models_pb2.Room
    track: _livekit_models_pb2.TrackInfo
    def __init__(
        self,
        event: _Optional[str] = ...,
        room: _Optional[_Union[_livekit_models_pb2.Room, _Mapping]] = ...,
        participant: _Optional[
            _Union[_livekit_models_pb2.ParticipantInfo, _Mapping]
        ] = ...,
        egress_info: _Optional[_Union[_livekit_egress_pb2.EgressInfo, _Mapping]] = ...,
        ingress_info: _Optional[
            _Union[_livekit_ingress_pb2.IngressInfo, _Mapping]
        ] = ...,
        track: _Optional[_Union[_livekit_models_pb2.TrackInfo, _Mapping]] = ...,
        id: _Optional[str] = ...,
        created_at: _Optional[int] = ...,
        num_dropped: _Optional[int] = ...,
    ) -> None: ...
