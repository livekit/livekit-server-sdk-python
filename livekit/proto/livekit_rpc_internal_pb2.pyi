from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import livekit_egress_pb2 as _livekit_egress_pb2
import livekit_ingress_pb2 as _livekit_ingress_pb2
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

class GetIngressInfoRequest(_message.Message):
    __slots__ = ["ingress_id", "request_id", "sender_id", "sent_at", "stream_key"]
    INGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    STREAM_KEY_FIELD_NUMBER: _ClassVar[int]
    ingress_id: str
    request_id: str
    sender_id: str
    sent_at: int
    stream_key: str
    def __init__(
        self,
        ingress_id: _Optional[str] = ...,
        stream_key: _Optional[str] = ...,
        request_id: _Optional[str] = ...,
        sender_id: _Optional[str] = ...,
        sent_at: _Optional[int] = ...,
    ) -> None: ...

class GetIngressInfoResponse(_message.Message):
    __slots__ = ["error", "info", "request_id", "token", "ws_url"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    WS_URL_FIELD_NUMBER: _ClassVar[int]
    error: str
    info: _livekit_ingress_pb2.IngressInfo
    request_id: str
    token: str
    ws_url: str
    def __init__(
        self,
        info: _Optional[_Union[_livekit_ingress_pb2.IngressInfo, _Mapping]] = ...,
        token: _Optional[str] = ...,
        ws_url: _Optional[str] = ...,
        error: _Optional[str] = ...,
        request_id: _Optional[str] = ...,
    ) -> None: ...

class IngressRequest(_message.Message):
    __slots__ = ["delete", "ingress_id", "request_id", "sender_id", "update"]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    INGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    delete: _livekit_ingress_pb2.DeleteIngressRequest
    ingress_id: str
    request_id: str
    sender_id: str
    update: _livekit_ingress_pb2.UpdateIngressRequest
    def __init__(
        self,
        ingress_id: _Optional[str] = ...,
        request_id: _Optional[str] = ...,
        sender_id: _Optional[str] = ...,
        update: _Optional[
            _Union[_livekit_ingress_pb2.UpdateIngressRequest, _Mapping]
        ] = ...,
        delete: _Optional[
            _Union[_livekit_ingress_pb2.DeleteIngressRequest, _Mapping]
        ] = ...,
    ) -> None: ...

class IngressResponse(_message.Message):
    __slots__ = ["error", "request_id", "state"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    error: str
    request_id: str
    state: _livekit_ingress_pb2.IngressState
    def __init__(
        self,
        state: _Optional[_Union[_livekit_ingress_pb2.IngressState, _Mapping]] = ...,
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

class UpdateIngressStateRequest(_message.Message):
    __slots__ = ["ingress_id", "state"]
    INGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ingress_id: str
    state: _livekit_ingress_pb2.IngressState
    def __init__(
        self,
        ingress_id: _Optional[str] = ...,
        state: _Optional[_Union[_livekit_ingress_pb2.IngressState, _Mapping]] = ...,
    ) -> None: ...
