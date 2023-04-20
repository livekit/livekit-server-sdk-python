from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import livekit_egress_pb2 as _livekit_egress_pb2
import livekit_ingress_pb2 as _livekit_ingress_pb2
import livekit_models_pb2 as _livekit_models_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
DOWNSTREAM: StreamType
EGRESS_ENDED: AnalyticsEventType
EGRESS_STARTED: AnalyticsEventType
INGRESS_CREATED: AnalyticsEventType
INGRESS_DELETED: AnalyticsEventType
INGRESS_ENDED: AnalyticsEventType
INGRESS_STARTED: AnalyticsEventType
PARTICIPANT_ACTIVE: AnalyticsEventType
PARTICIPANT_JOINED: AnalyticsEventType
PARTICIPANT_LEFT: AnalyticsEventType
PARTICIPANT_RESUMED: AnalyticsEventType
RECONNECTED: AnalyticsEventType
ROOM_CREATED: AnalyticsEventType
ROOM_ENDED: AnalyticsEventType
TRACK_MAX_SUBSCRIBED_VIDEO_QUALITY: AnalyticsEventType
TRACK_MUTED: AnalyticsEventType
TRACK_PUBLISHED: AnalyticsEventType
TRACK_PUBLISHED_UPDATE: AnalyticsEventType
TRACK_PUBLISH_REQUESTED: AnalyticsEventType
TRACK_PUBLISH_STATS: AnalyticsEventType
TRACK_SUBSCRIBED: AnalyticsEventType
TRACK_SUBSCRIBE_FAILED: AnalyticsEventType
TRACK_SUBSCRIBE_REQUESTED: AnalyticsEventType
TRACK_SUBSCRIBE_STATS: AnalyticsEventType
TRACK_UNMUTED: AnalyticsEventType
TRACK_UNPUBLISHED: AnalyticsEventType
TRACK_UNSUBSCRIBED: AnalyticsEventType
UPSTREAM: StreamType

class AnalyticsClientMeta(_message.Message):
    __slots__ = [
        "client_addr",
        "client_connect_time",
        "connection_type",
        "node",
        "reconnect_reason",
        "region",
    ]
    CLIENT_ADDR_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONNECT_TIME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    RECONNECT_REASON_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    client_addr: str
    client_connect_time: int
    connection_type: str
    node: str
    reconnect_reason: _livekit_models_pb2.ReconnectReason
    region: str
    def __init__(
        self,
        region: _Optional[str] = ...,
        node: _Optional[str] = ...,
        client_addr: _Optional[str] = ...,
        client_connect_time: _Optional[int] = ...,
        connection_type: _Optional[str] = ...,
        reconnect_reason: _Optional[
            _Union[_livekit_models_pb2.ReconnectReason, str]
        ] = ...,
    ) -> None: ...

class AnalyticsEvent(_message.Message):
    __slots__ = [
        "analytics_key",
        "client_info",
        "client_meta",
        "egress",
        "egress_id",
        "error",
        "ingress",
        "ingress_id",
        "max_subscribed_video_quality",
        "mime",
        "participant",
        "participant_id",
        "publisher",
        "room",
        "room_id",
        "rtp_stats",
        "timestamp",
        "track",
        "track_id",
        "type",
        "video_layer",
    ]
    ANALYTICS_KEY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_META_FIELD_NUMBER: _ClassVar[int]
    EGRESS_FIELD_NUMBER: _ClassVar[int]
    EGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    INGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_SUBSCRIBED_VIDEO_QUALITY_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    RTP_STATS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_LAYER_FIELD_NUMBER: _ClassVar[int]
    analytics_key: str
    client_info: _livekit_models_pb2.ClientInfo
    client_meta: AnalyticsClientMeta
    egress: _livekit_egress_pb2.EgressInfo
    egress_id: str
    error: str
    ingress: _livekit_ingress_pb2.IngressInfo
    ingress_id: str
    max_subscribed_video_quality: _livekit_models_pb2.VideoQuality
    mime: str
    participant: _livekit_models_pb2.ParticipantInfo
    participant_id: str
    publisher: _livekit_models_pb2.ParticipantInfo
    room: _livekit_models_pb2.Room
    room_id: str
    rtp_stats: _livekit_models_pb2.RTPStats
    timestamp: _timestamp_pb2.Timestamp
    track: _livekit_models_pb2.TrackInfo
    track_id: str
    type: AnalyticsEventType
    video_layer: int
    def __init__(
        self,
        type: _Optional[_Union[AnalyticsEventType, str]] = ...,
        timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        room_id: _Optional[str] = ...,
        room: _Optional[_Union[_livekit_models_pb2.Room, _Mapping]] = ...,
        participant_id: _Optional[str] = ...,
        participant: _Optional[
            _Union[_livekit_models_pb2.ParticipantInfo, _Mapping]
        ] = ...,
        track_id: _Optional[str] = ...,
        track: _Optional[_Union[_livekit_models_pb2.TrackInfo, _Mapping]] = ...,
        analytics_key: _Optional[str] = ...,
        client_info: _Optional[_Union[_livekit_models_pb2.ClientInfo, _Mapping]] = ...,
        client_meta: _Optional[_Union[AnalyticsClientMeta, _Mapping]] = ...,
        egress_id: _Optional[str] = ...,
        ingress_id: _Optional[str] = ...,
        max_subscribed_video_quality: _Optional[
            _Union[_livekit_models_pb2.VideoQuality, str]
        ] = ...,
        publisher: _Optional[
            _Union[_livekit_models_pb2.ParticipantInfo, _Mapping]
        ] = ...,
        mime: _Optional[str] = ...,
        egress: _Optional[_Union[_livekit_egress_pb2.EgressInfo, _Mapping]] = ...,
        ingress: _Optional[_Union[_livekit_ingress_pb2.IngressInfo, _Mapping]] = ...,
        error: _Optional[str] = ...,
        rtp_stats: _Optional[_Union[_livekit_models_pb2.RTPStats, _Mapping]] = ...,
        video_layer: _Optional[int] = ...,
    ) -> None: ...

class AnalyticsEvents(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[AnalyticsEvent]
    def __init__(
        self, events: _Optional[_Iterable[_Union[AnalyticsEvent, _Mapping]]] = ...
    ) -> None: ...

class AnalyticsStat(_message.Message):
    __slots__ = [
        "analytics_key",
        "kind",
        "mime",
        "node",
        "participant_id",
        "room_id",
        "room_name",
        "score",
        "streams",
        "time_stamp",
        "track_id",
    ]
    ANALYTICS_KEY_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    analytics_key: str
    kind: StreamType
    mime: str
    node: str
    participant_id: str
    room_id: str
    room_name: str
    score: float
    streams: _containers.RepeatedCompositeFieldContainer[AnalyticsStream]
    time_stamp: _timestamp_pb2.Timestamp
    track_id: str
    def __init__(
        self,
        analytics_key: _Optional[str] = ...,
        kind: _Optional[_Union[StreamType, str]] = ...,
        time_stamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        node: _Optional[str] = ...,
        room_id: _Optional[str] = ...,
        room_name: _Optional[str] = ...,
        participant_id: _Optional[str] = ...,
        track_id: _Optional[str] = ...,
        score: _Optional[float] = ...,
        streams: _Optional[_Iterable[_Union[AnalyticsStream, _Mapping]]] = ...,
        mime: _Optional[str] = ...,
    ) -> None: ...

class AnalyticsStats(_message.Message):
    __slots__ = ["stats"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[AnalyticsStat]
    def __init__(
        self, stats: _Optional[_Iterable[_Union[AnalyticsStat, _Mapping]]] = ...
    ) -> None: ...

class AnalyticsStream(_message.Message):
    __slots__ = [
        "firs",
        "frames",
        "jitter",
        "nacks",
        "packets_lost",
        "padding_bytes",
        "padding_packets",
        "plis",
        "primary_bytes",
        "primary_packets",
        "retransmit_bytes",
        "retransmit_packets",
        "rtt",
        "ssrc",
        "video_layers",
    ]
    FIRS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    JITTER_FIELD_NUMBER: _ClassVar[int]
    NACKS_FIELD_NUMBER: _ClassVar[int]
    PACKETS_LOST_FIELD_NUMBER: _ClassVar[int]
    PADDING_BYTES_FIELD_NUMBER: _ClassVar[int]
    PADDING_PACKETS_FIELD_NUMBER: _ClassVar[int]
    PLIS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_BYTES_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PACKETS_FIELD_NUMBER: _ClassVar[int]
    RETRANSMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
    RETRANSMIT_PACKETS_FIELD_NUMBER: _ClassVar[int]
    RTT_FIELD_NUMBER: _ClassVar[int]
    SSRC_FIELD_NUMBER: _ClassVar[int]
    VIDEO_LAYERS_FIELD_NUMBER: _ClassVar[int]
    firs: int
    frames: int
    jitter: int
    nacks: int
    packets_lost: int
    padding_bytes: int
    padding_packets: int
    plis: int
    primary_bytes: int
    primary_packets: int
    retransmit_bytes: int
    retransmit_packets: int
    rtt: int
    ssrc: int
    video_layers: _containers.RepeatedCompositeFieldContainer[AnalyticsVideoLayer]
    def __init__(
        self,
        ssrc: _Optional[int] = ...,
        primary_packets: _Optional[int] = ...,
        primary_bytes: _Optional[int] = ...,
        retransmit_packets: _Optional[int] = ...,
        retransmit_bytes: _Optional[int] = ...,
        padding_packets: _Optional[int] = ...,
        padding_bytes: _Optional[int] = ...,
        packets_lost: _Optional[int] = ...,
        frames: _Optional[int] = ...,
        rtt: _Optional[int] = ...,
        jitter: _Optional[int] = ...,
        nacks: _Optional[int] = ...,
        plis: _Optional[int] = ...,
        firs: _Optional[int] = ...,
        video_layers: _Optional[_Iterable[_Union[AnalyticsVideoLayer, _Mapping]]] = ...,
    ) -> None: ...

class AnalyticsVideoLayer(_message.Message):
    __slots__ = ["bytes", "frames", "layer", "packets"]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    PACKETS_FIELD_NUMBER: _ClassVar[int]
    bytes: int
    frames: int
    layer: int
    packets: int
    def __init__(
        self,
        layer: _Optional[int] = ...,
        packets: _Optional[int] = ...,
        bytes: _Optional[int] = ...,
        frames: _Optional[int] = ...,
    ) -> None: ...

class StreamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AnalyticsEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
