from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import livekit_egress_pb2 as _livekit_egress_pb2
import livekit_models_pb2 as _livekit_models_pb2
import livekit_room_pb2 as _livekit_room_pb2
import livekit_rtc_pb2 as _livekit_rtc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

CONTROLLER: NodeType
DESCRIPTOR: _descriptor.FileDescriptor
ICT_NONE: ICECandidateType
ICT_TCP: ICECandidateType
ICT_TLS: ICECandidateType
MEDIA: NodeType
SERVER: NodeType
SERVING: NodeState
SHUTTING_DOWN: NodeState
STARTING_UP: NodeState
SWEEPER: NodeType
TURN: NodeType

class EndSession(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ICEConfig(_message.Message):
    __slots__ = ["preference_publisher", "preference_subscriber"]
    PREFERENCE_PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_SUBSCRIBER_FIELD_NUMBER: _ClassVar[int]
    preference_publisher: ICECandidateType
    preference_subscriber: ICECandidateType
    def __init__(
        self,
        preference_subscriber: _Optional[_Union[ICECandidateType, str]] = ...,
        preference_publisher: _Optional[_Union[ICECandidateType, str]] = ...,
    ) -> None: ...

class KeepAlive(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Node(_message.Message):
    __slots__ = ["id", "ip", "num_cpus", "region", "state", "stats", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    NUM_CPUS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    ip: str
    num_cpus: int
    region: str
    state: NodeState
    stats: NodeStats
    type: NodeType
    def __init__(
        self,
        id: _Optional[str] = ...,
        ip: _Optional[str] = ...,
        num_cpus: _Optional[int] = ...,
        stats: _Optional[_Union[NodeStats, _Mapping]] = ...,
        type: _Optional[_Union[NodeType, str]] = ...,
        state: _Optional[_Union[NodeState, str]] = ...,
        region: _Optional[str] = ...,
    ) -> None: ...

class NodeStats(_message.Message):
    __slots__ = [
        "bytes_in",
        "bytes_in_per_sec",
        "bytes_out",
        "bytes_out_per_sec",
        "cpu_load",
        "load_avg_last15min",
        "load_avg_last1min",
        "load_avg_last5min",
        "memory_load",
        "memory_total",
        "memory_used",
        "nack_per_sec",
        "nack_total",
        "num_clients",
        "num_cpus",
        "num_rooms",
        "num_track_publish_attempts",
        "num_track_publish_success",
        "num_track_subscribe_attempts",
        "num_track_subscribe_success",
        "num_tracks_in",
        "num_tracks_out",
        "packets_in",
        "packets_in_per_sec",
        "packets_out",
        "packets_out_per_sec",
        "participant_rtc_connected",
        "participant_rtc_connected_per_sec",
        "participant_rtc_init",
        "participant_rtc_init_per_sec",
        "participant_signal_connected",
        "participant_signal_connected_per_sec",
        "retransmit_bytes_out",
        "retransmit_bytes_out_per_sec",
        "retransmit_packets_out",
        "retransmit_packets_out_per_sec",
        "started_at",
        "sys_packets_dropped",
        "sys_packets_dropped_pct_per_sec",
        "sys_packets_dropped_per_sec",
        "sys_packets_out",
        "sys_packets_out_per_sec",
        "track_publish_attempts_per_sec",
        "track_publish_success_per_sec",
        "track_subscribe_attempts_per_sec",
        "track_subscribe_success_per_sec",
        "updated_at",
    ]
    BYTES_IN_FIELD_NUMBER: _ClassVar[int]
    BYTES_IN_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    BYTES_OUT_FIELD_NUMBER: _ClassVar[int]
    BYTES_OUT_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    CPU_LOAD_FIELD_NUMBER: _ClassVar[int]
    LOAD_AVG_LAST15MIN_FIELD_NUMBER: _ClassVar[int]
    LOAD_AVG_LAST1MIN_FIELD_NUMBER: _ClassVar[int]
    LOAD_AVG_LAST5MIN_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LOAD_FIELD_NUMBER: _ClassVar[int]
    MEMORY_TOTAL_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USED_FIELD_NUMBER: _ClassVar[int]
    NACK_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    NACK_TOTAL_FIELD_NUMBER: _ClassVar[int]
    NUM_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    NUM_CPUS_FIELD_NUMBER: _ClassVar[int]
    NUM_ROOMS_FIELD_NUMBER: _ClassVar[int]
    NUM_TRACKS_IN_FIELD_NUMBER: _ClassVar[int]
    NUM_TRACKS_OUT_FIELD_NUMBER: _ClassVar[int]
    NUM_TRACK_PUBLISH_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    NUM_TRACK_PUBLISH_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    NUM_TRACK_SUBSCRIBE_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    NUM_TRACK_SUBSCRIBE_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    PACKETS_IN_FIELD_NUMBER: _ClassVar[int]
    PACKETS_IN_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    PACKETS_OUT_FIELD_NUMBER: _ClassVar[int]
    PACKETS_OUT_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_RTC_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_RTC_CONNECTED_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_RTC_INIT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_RTC_INIT_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_SIGNAL_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_SIGNAL_CONNECTED_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    RETRANSMIT_BYTES_OUT_FIELD_NUMBER: _ClassVar[int]
    RETRANSMIT_BYTES_OUT_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    RETRANSMIT_PACKETS_OUT_FIELD_NUMBER: _ClassVar[int]
    RETRANSMIT_PACKETS_OUT_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    SYS_PACKETS_DROPPED_FIELD_NUMBER: _ClassVar[int]
    SYS_PACKETS_DROPPED_PCT_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    SYS_PACKETS_DROPPED_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    SYS_PACKETS_OUT_FIELD_NUMBER: _ClassVar[int]
    SYS_PACKETS_OUT_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    TRACK_PUBLISH_ATTEMPTS_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    TRACK_PUBLISH_SUCCESS_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    TRACK_SUBSCRIBE_ATTEMPTS_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    TRACK_SUBSCRIBE_SUCCESS_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    bytes_in: int
    bytes_in_per_sec: float
    bytes_out: int
    bytes_out_per_sec: float
    cpu_load: float
    load_avg_last15min: float
    load_avg_last1min: float
    load_avg_last5min: float
    memory_load: float
    memory_total: int
    memory_used: int
    nack_per_sec: float
    nack_total: int
    num_clients: int
    num_cpus: int
    num_rooms: int
    num_track_publish_attempts: int
    num_track_publish_success: int
    num_track_subscribe_attempts: int
    num_track_subscribe_success: int
    num_tracks_in: int
    num_tracks_out: int
    packets_in: int
    packets_in_per_sec: float
    packets_out: int
    packets_out_per_sec: float
    participant_rtc_connected: int
    participant_rtc_connected_per_sec: float
    participant_rtc_init: int
    participant_rtc_init_per_sec: float
    participant_signal_connected: int
    participant_signal_connected_per_sec: float
    retransmit_bytes_out: int
    retransmit_bytes_out_per_sec: float
    retransmit_packets_out: int
    retransmit_packets_out_per_sec: float
    started_at: int
    sys_packets_dropped: int
    sys_packets_dropped_pct_per_sec: float
    sys_packets_dropped_per_sec: float
    sys_packets_out: int
    sys_packets_out_per_sec: float
    track_publish_attempts_per_sec: float
    track_publish_success_per_sec: float
    track_subscribe_attempts_per_sec: float
    track_subscribe_success_per_sec: float
    updated_at: int
    def __init__(
        self,
        started_at: _Optional[int] = ...,
        updated_at: _Optional[int] = ...,
        num_rooms: _Optional[int] = ...,
        num_clients: _Optional[int] = ...,
        num_tracks_in: _Optional[int] = ...,
        num_tracks_out: _Optional[int] = ...,
        num_track_publish_attempts: _Optional[int] = ...,
        track_publish_attempts_per_sec: _Optional[float] = ...,
        num_track_publish_success: _Optional[int] = ...,
        track_publish_success_per_sec: _Optional[float] = ...,
        num_track_subscribe_attempts: _Optional[int] = ...,
        track_subscribe_attempts_per_sec: _Optional[float] = ...,
        num_track_subscribe_success: _Optional[int] = ...,
        track_subscribe_success_per_sec: _Optional[float] = ...,
        bytes_in: _Optional[int] = ...,
        bytes_out: _Optional[int] = ...,
        packets_in: _Optional[int] = ...,
        packets_out: _Optional[int] = ...,
        nack_total: _Optional[int] = ...,
        bytes_in_per_sec: _Optional[float] = ...,
        bytes_out_per_sec: _Optional[float] = ...,
        packets_in_per_sec: _Optional[float] = ...,
        packets_out_per_sec: _Optional[float] = ...,
        nack_per_sec: _Optional[float] = ...,
        num_cpus: _Optional[int] = ...,
        load_avg_last1min: _Optional[float] = ...,
        load_avg_last5min: _Optional[float] = ...,
        load_avg_last15min: _Optional[float] = ...,
        cpu_load: _Optional[float] = ...,
        memory_load: _Optional[float] = ...,
        memory_total: _Optional[int] = ...,
        memory_used: _Optional[int] = ...,
        sys_packets_out: _Optional[int] = ...,
        sys_packets_dropped: _Optional[int] = ...,
        sys_packets_out_per_sec: _Optional[float] = ...,
        sys_packets_dropped_per_sec: _Optional[float] = ...,
        sys_packets_dropped_pct_per_sec: _Optional[float] = ...,
        retransmit_bytes_out: _Optional[int] = ...,
        retransmit_packets_out: _Optional[int] = ...,
        retransmit_bytes_out_per_sec: _Optional[float] = ...,
        retransmit_packets_out_per_sec: _Optional[float] = ...,
        participant_signal_connected: _Optional[int] = ...,
        participant_signal_connected_per_sec: _Optional[float] = ...,
        participant_rtc_connected: _Optional[int] = ...,
        participant_rtc_connected_per_sec: _Optional[float] = ...,
        participant_rtc_init: _Optional[int] = ...,
        participant_rtc_init_per_sec: _Optional[float] = ...,
    ) -> None: ...

class RTCNodeMessage(_message.Message):
    __slots__ = [
        "connection_id",
        "delete_room",
        "identity",
        "keep_alive",
        "mute_track",
        "participant_key",
        "participant_key_b62",
        "remove_participant",
        "request",
        "room_name",
        "send_data",
        "sender_time",
        "start_session",
        "update_participant",
        "update_room_metadata",
        "update_subscriptions",
    ]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_ROOM_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    MUTE_TRACK_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_KEY_B62_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_KEY_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    SENDER_TIME_FIELD_NUMBER: _ClassVar[int]
    SEND_DATA_FIELD_NUMBER: _ClassVar[int]
    START_SESSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ROOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    delete_room: _livekit_room_pb2.DeleteRoomRequest
    identity: str
    keep_alive: KeepAlive
    mute_track: _livekit_room_pb2.MuteRoomTrackRequest
    participant_key: str
    participant_key_b62: str
    remove_participant: _livekit_room_pb2.RoomParticipantIdentity
    request: _livekit_rtc_pb2.SignalRequest
    room_name: str
    send_data: _livekit_room_pb2.SendDataRequest
    sender_time: int
    start_session: StartSession
    update_participant: _livekit_room_pb2.UpdateParticipantRequest
    update_room_metadata: _livekit_room_pb2.UpdateRoomMetadataRequest
    update_subscriptions: _livekit_room_pb2.UpdateSubscriptionsRequest
    def __init__(
        self,
        participant_key: _Optional[str] = ...,
        sender_time: _Optional[int] = ...,
        connection_id: _Optional[str] = ...,
        participant_key_b62: _Optional[str] = ...,
        room_name: _Optional[str] = ...,
        identity: _Optional[str] = ...,
        start_session: _Optional[_Union[StartSession, _Mapping]] = ...,
        request: _Optional[_Union[_livekit_rtc_pb2.SignalRequest, _Mapping]] = ...,
        remove_participant: _Optional[
            _Union[_livekit_room_pb2.RoomParticipantIdentity, _Mapping]
        ] = ...,
        mute_track: _Optional[
            _Union[_livekit_room_pb2.MuteRoomTrackRequest, _Mapping]
        ] = ...,
        update_participant: _Optional[
            _Union[_livekit_room_pb2.UpdateParticipantRequest, _Mapping]
        ] = ...,
        delete_room: _Optional[
            _Union[_livekit_room_pb2.DeleteRoomRequest, _Mapping]
        ] = ...,
        update_subscriptions: _Optional[
            _Union[_livekit_room_pb2.UpdateSubscriptionsRequest, _Mapping]
        ] = ...,
        send_data: _Optional[_Union[_livekit_room_pb2.SendDataRequest, _Mapping]] = ...,
        update_room_metadata: _Optional[
            _Union[_livekit_room_pb2.UpdateRoomMetadataRequest, _Mapping]
        ] = ...,
        keep_alive: _Optional[_Union[KeepAlive, _Mapping]] = ...,
    ) -> None: ...

class RemoveParticipant(_message.Message):
    __slots__ = ["participant_id"]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    participant_id: str
    def __init__(self, participant_id: _Optional[str] = ...) -> None: ...

class RoomInternal(_message.Message):
    __slots__ = ["track_egress"]
    TRACK_EGRESS_FIELD_NUMBER: _ClassVar[int]
    track_egress: _livekit_egress_pb2.AutoTrackEgress
    def __init__(
        self,
        track_egress: _Optional[
            _Union[_livekit_egress_pb2.AutoTrackEgress, _Mapping]
        ] = ...,
    ) -> None: ...

class SignalNodeMessage(_message.Message):
    __slots__ = ["connection_id", "end_session", "response"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    END_SESSION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    end_session: EndSession
    response: _livekit_rtc_pb2.SignalResponse
    def __init__(
        self,
        connection_id: _Optional[str] = ...,
        response: _Optional[_Union[_livekit_rtc_pb2.SignalResponse, _Mapping]] = ...,
        end_session: _Optional[_Union[EndSession, _Mapping]] = ...,
    ) -> None: ...

class StartSession(_message.Message):
    __slots__ = [
        "adaptive_stream",
        "auto_subscribe",
        "client",
        "connection_id",
        "grants_json",
        "hidden",
        "identity",
        "name",
        "participant_id",
        "reconnect",
        "reconnect_reason",
        "recorder",
        "room_name",
        "subscriber_allow_pause",
    ]
    ADAPTIVE_STREAM_FIELD_NUMBER: _ClassVar[int]
    AUTO_SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    GRANTS_JSON_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECONNECT_FIELD_NUMBER: _ClassVar[int]
    RECONNECT_REASON_FIELD_NUMBER: _ClassVar[int]
    RECORDER_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_ALLOW_PAUSE_FIELD_NUMBER: _ClassVar[int]
    adaptive_stream: bool
    auto_subscribe: bool
    client: _livekit_models_pb2.ClientInfo
    connection_id: str
    grants_json: str
    hidden: bool
    identity: str
    name: str
    participant_id: str
    reconnect: bool
    reconnect_reason: _livekit_models_pb2.ReconnectReason
    recorder: bool
    room_name: str
    subscriber_allow_pause: bool
    def __init__(
        self,
        room_name: _Optional[str] = ...,
        identity: _Optional[str] = ...,
        connection_id: _Optional[str] = ...,
        reconnect: bool = ...,
        auto_subscribe: bool = ...,
        hidden: bool = ...,
        client: _Optional[_Union[_livekit_models_pb2.ClientInfo, _Mapping]] = ...,
        recorder: bool = ...,
        name: _Optional[str] = ...,
        grants_json: _Optional[str] = ...,
        adaptive_stream: bool = ...,
        participant_id: _Optional[str] = ...,
        reconnect_reason: _Optional[
            _Union[_livekit_models_pb2.ReconnectReason, str]
        ] = ...,
        subscriber_allow_pause: bool = ...,
    ) -> None: ...

class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class NodeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ICECandidateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
