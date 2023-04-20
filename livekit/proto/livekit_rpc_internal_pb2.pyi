from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import livekit_egress_pb2 as _livekit_egress_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class EgressRequest(_message.Message):
    __slots__ = ["egress_id", "request_id", "sender_id", "stop", "update_stream"]
    EGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_STREAM_FIELD_NUMBER: _ClassVar[int]
    egress_id: str
    request_id: str
    sender_id: str
    stop: _livekit_egress_pb2.StopEgressRequest
    update_stream: _livekit_egress_pb2.UpdateStreamRequest
    def __init__(
        self,
        egress_id: _Optional[str] = ...,
        request_id: _Optional[str] = ...,
        sender_id: _Optional[str] = ...,
        update_stream: _Optional[
            _Union[_livekit_egress_pb2.UpdateStreamRequest, _Mapping]
        ] = ...,
        stop: _Optional[_Union[_livekit_egress_pb2.StopEgressRequest, _Mapping]] = ...,
    ) -> None: ...

class EgressResponse(_message.Message):
    __slots__ = ["error", "info", "request_id"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    error: str
    info: _livekit_egress_pb2.EgressInfo
    request_id: str
    def __init__(
        self,
        info: _Optional[_Union[_livekit_egress_pb2.EgressInfo, _Mapping]] = ...,
        error: _Optional[str] = ...,
        request_id: _Optional[str] = ...,
    ) -> None: ...

class StartEgressRequest(_message.Message):
    __slots__ = [
        "egress_id",
        "request_id",
        "room_composite",
        "room_id",
        "sender_id",
        "sent_at",
        "token",
        "track",
        "track_composite",
        "web",
        "ws_url",
    ]
    EGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_COMPOSITE_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TRACK_COMPOSITE_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    WEB_FIELD_NUMBER: _ClassVar[int]
    WS_URL_FIELD_NUMBER: _ClassVar[int]
    egress_id: str
    request_id: str
    room_composite: _livekit_egress_pb2.RoomCompositeEgressRequest
    room_id: str
    sender_id: str
    sent_at: int
    token: str
    track: _livekit_egress_pb2.TrackEgressRequest
    track_composite: _livekit_egress_pb2.TrackCompositeEgressRequest
    web: _livekit_egress_pb2.WebEgressRequest
    ws_url: str
    def __init__(
        self,
        egress_id: _Optional[str] = ...,
        request_id: _Optional[str] = ...,
        sender_id: _Optional[str] = ...,
        sent_at: _Optional[int] = ...,
        room_composite: _Optional[
            _Union[_livekit_egress_pb2.RoomCompositeEgressRequest, _Mapping]
        ] = ...,
        track_composite: _Optional[
            _Union[_livekit_egress_pb2.TrackCompositeEgressRequest, _Mapping]
        ] = ...,
        track: _Optional[
            _Union[_livekit_egress_pb2.TrackEgressRequest, _Mapping]
        ] = ...,
        web: _Optional[_Union[_livekit_egress_pb2.WebEgressRequest, _Mapping]] = ...,
        room_id: _Optional[str] = ...,
        token: _Optional[str] = ...,
        ws_url: _Optional[str] = ...,
    ) -> None: ...
