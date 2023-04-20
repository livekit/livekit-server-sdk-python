from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

AAC: AudioCodec
AUDIO: TrackType
CAMERA: TrackSource
CLIENT_INITIATED: DisconnectReason
DATA: TrackType
DEFAULT_AC: AudioCodec
DEFAULT_VC: VideoCodec
DESCRIPTOR: _descriptor.FileDescriptor
DISABLED: ClientConfigSetting
DUPLICATE_IDENTITY: DisconnectReason
ENABLED: ClientConfigSetting
EXCELLENT: ConnectionQuality
GOOD: ConnectionQuality
H264_BASELINE: VideoCodec
H264_HIGH: VideoCodec
H264_MAIN: VideoCodec
HIGH: VideoQuality
JOIN_FAILURE: DisconnectReason
LOW: VideoQuality
MEDIUM: VideoQuality
MICROPHONE: TrackSource
OFF: VideoQuality
OPUS: AudioCodec
PARTICIPANT_REMOVED: DisconnectReason
POOR: ConnectionQuality
ROOM_DELETED: DisconnectReason
RR_PUBLISHER_FAILED: ReconnectReason
RR_SIGNAL_DISCONNECTED: ReconnectReason
RR_SUBSCRIBER_FAILED: ReconnectReason
RR_SWITCH_CANDIDATE: ReconnectReason
RR_UNKOWN: ReconnectReason
SCREEN_SHARE: TrackSource
SCREEN_SHARE_AUDIO: TrackSource
SERVER_SHUTDOWN: DisconnectReason
STATE_MISMATCH: DisconnectReason
UNKNOWN: TrackSource
UNKNOWN_REASON: DisconnectReason
UNSET: ClientConfigSetting
VIDEO: TrackType
VP8: VideoCodec

class ActiveSpeakerUpdate(_message.Message):
    __slots__ = ["speakers"]
    SPEAKERS_FIELD_NUMBER: _ClassVar[int]
    speakers: _containers.RepeatedCompositeFieldContainer[SpeakerInfo]
    def __init__(
        self, speakers: _Optional[_Iterable[_Union[SpeakerInfo, _Mapping]]] = ...
    ) -> None: ...

class ClientConfiguration(_message.Message):
    __slots__ = [
        "disabled_codecs",
        "force_relay",
        "resume_connection",
        "screen",
        "video",
    ]
    DISABLED_CODECS_FIELD_NUMBER: _ClassVar[int]
    FORCE_RELAY_FIELD_NUMBER: _ClassVar[int]
    RESUME_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    disabled_codecs: DisabledCodecs
    force_relay: ClientConfigSetting
    resume_connection: ClientConfigSetting
    screen: VideoConfiguration
    video: VideoConfiguration
    def __init__(
        self,
        video: _Optional[_Union[VideoConfiguration, _Mapping]] = ...,
        screen: _Optional[_Union[VideoConfiguration, _Mapping]] = ...,
        resume_connection: _Optional[_Union[ClientConfigSetting, str]] = ...,
        disabled_codecs: _Optional[_Union[DisabledCodecs, _Mapping]] = ...,
        force_relay: _Optional[_Union[ClientConfigSetting, str]] = ...,
    ) -> None: ...

class ClientInfo(_message.Message):
    __slots__ = [
        "address",
        "browser",
        "browser_version",
        "device_model",
        "network",
        "os",
        "os_version",
        "protocol",
        "sdk",
        "version",
    ]

    class SDK(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ANDROID: ClientInfo.SDK
    BROWSER_FIELD_NUMBER: _ClassVar[int]
    BROWSER_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    FLUTTER: ClientInfo.SDK
    GO: ClientInfo.SDK
    JS: ClientInfo.SDK
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    REACT_NATIVE: ClientInfo.SDK
    RUST: ClientInfo.SDK
    SDK_FIELD_NUMBER: _ClassVar[int]
    SWIFT: ClientInfo.SDK
    UNITY: ClientInfo.SDK
    UNKNOWN: ClientInfo.SDK
    VERSION_FIELD_NUMBER: _ClassVar[int]
    address: str
    browser: str
    browser_version: str
    device_model: str
    network: str
    os: str
    os_version: str
    protocol: int
    sdk: ClientInfo.SDK
    version: str
    def __init__(
        self,
        sdk: _Optional[_Union[ClientInfo.SDK, str]] = ...,
        version: _Optional[str] = ...,
        protocol: _Optional[int] = ...,
        os: _Optional[str] = ...,
        os_version: _Optional[str] = ...,
        device_model: _Optional[str] = ...,
        browser: _Optional[str] = ...,
        browser_version: _Optional[str] = ...,
        address: _Optional[str] = ...,
        network: _Optional[str] = ...,
    ) -> None: ...

class Codec(_message.Message):
    __slots__ = ["fmtp_line", "mime"]
    FMTP_LINE_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    fmtp_line: str
    mime: str
    def __init__(
        self, mime: _Optional[str] = ..., fmtp_line: _Optional[str] = ...
    ) -> None: ...

class DataPacket(_message.Message):
    __slots__ = ["kind", "speaker", "user"]

    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    KIND_FIELD_NUMBER: _ClassVar[int]
    LOSSY: DataPacket.Kind
    RELIABLE: DataPacket.Kind
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    kind: DataPacket.Kind
    speaker: ActiveSpeakerUpdate
    user: UserPacket
    def __init__(
        self,
        kind: _Optional[_Union[DataPacket.Kind, str]] = ...,
        user: _Optional[_Union[UserPacket, _Mapping]] = ...,
        speaker: _Optional[_Union[ActiveSpeakerUpdate, _Mapping]] = ...,
    ) -> None: ...

class DisabledCodecs(_message.Message):
    __slots__ = ["codecs"]
    CODECS_FIELD_NUMBER: _ClassVar[int]
    codecs: _containers.RepeatedCompositeFieldContainer[Codec]
    def __init__(
        self, codecs: _Optional[_Iterable[_Union[Codec, _Mapping]]] = ...
    ) -> None: ...

class Encryption(_message.Message):
    __slots__ = []

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CUSTOM: Encryption.Type
    GCM: Encryption.Type
    NONE: Encryption.Type
    def __init__(self) -> None: ...

class ParticipantInfo(_message.Message):
    __slots__ = [
        "identity",
        "is_publisher",
        "joined_at",
        "metadata",
        "name",
        "permission",
        "region",
        "sid",
        "state",
        "tracks",
        "version",
    ]

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: ParticipantInfo.State
    DISCONNECTED: ParticipantInfo.State
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    JOINED: ParticipantInfo.State
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    JOINING: ParticipantInfo.State
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    identity: str
    is_publisher: bool
    joined_at: int
    metadata: str
    name: str
    permission: ParticipantPermission
    region: str
    sid: str
    state: ParticipantInfo.State
    tracks: _containers.RepeatedCompositeFieldContainer[TrackInfo]
    version: int
    def __init__(
        self,
        sid: _Optional[str] = ...,
        identity: _Optional[str] = ...,
        state: _Optional[_Union[ParticipantInfo.State, str]] = ...,
        tracks: _Optional[_Iterable[_Union[TrackInfo, _Mapping]]] = ...,
        metadata: _Optional[str] = ...,
        joined_at: _Optional[int] = ...,
        name: _Optional[str] = ...,
        version: _Optional[int] = ...,
        permission: _Optional[_Union[ParticipantPermission, _Mapping]] = ...,
        region: _Optional[str] = ...,
        is_publisher: bool = ...,
    ) -> None: ...

class ParticipantPermission(_message.Message):
    __slots__ = [
        "can_publish",
        "can_publish_data",
        "can_publish_sources",
        "can_subscribe",
        "can_update_metadata",
        "hidden",
        "recorder",
    ]
    CAN_PUBLISH_DATA_FIELD_NUMBER: _ClassVar[int]
    CAN_PUBLISH_FIELD_NUMBER: _ClassVar[int]
    CAN_PUBLISH_SOURCES_FIELD_NUMBER: _ClassVar[int]
    CAN_SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    CAN_UPDATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    RECORDER_FIELD_NUMBER: _ClassVar[int]
    can_publish: bool
    can_publish_data: bool
    can_publish_sources: _containers.RepeatedScalarFieldContainer[TrackSource]
    can_subscribe: bool
    can_update_metadata: bool
    hidden: bool
    recorder: bool
    def __init__(
        self,
        can_subscribe: bool = ...,
        can_publish: bool = ...,
        can_publish_data: bool = ...,
        can_publish_sources: _Optional[_Iterable[_Union[TrackSource, str]]] = ...,
        hidden: bool = ...,
        recorder: bool = ...,
        can_update_metadata: bool = ...,
    ) -> None: ...

class ParticipantTracks(_message.Message):
    __slots__ = ["participant_sid", "track_sids"]
    PARTICIPANT_SID_FIELD_NUMBER: _ClassVar[int]
    TRACK_SIDS_FIELD_NUMBER: _ClassVar[int]
    participant_sid: str
    track_sids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        participant_sid: _Optional[str] = ...,
        track_sids: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class RTPStats(_message.Message):
    __slots__ = [
        "bitrate",
        "bitrate_duplicate",
        "bitrate_padding",
        "bytes",
        "bytes_duplicate",
        "bytes_padding",
        "duration",
        "end_time",
        "firs",
        "frame_rate",
        "frames",
        "gap_histogram",
        "header_bytes",
        "header_bytes_duplicate",
        "header_bytes_padding",
        "jitter_current",
        "jitter_max",
        "key_frames",
        "last_fir",
        "last_key_frame",
        "last_layer_lock_pli",
        "last_pli",
        "layer_lock_plis",
        "nack_acks",
        "nack_misses",
        "nack_repeated",
        "nacks",
        "packet_duplicate_rate",
        "packet_loss_percentage",
        "packet_loss_rate",
        "packet_padding_rate",
        "packet_rate",
        "packets",
        "packets_duplicate",
        "packets_lost",
        "packets_out_of_order",
        "packets_padding",
        "plis",
        "rtt_current",
        "rtt_max",
        "start_time",
    ]

    class GapHistogramEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(
            self, key: _Optional[int] = ..., value: _Optional[int] = ...
        ) -> None: ...
    BITRATE_DUPLICATE_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    BITRATE_PADDING_FIELD_NUMBER: _ClassVar[int]
    BYTES_DUPLICATE_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    BYTES_PADDING_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FIRS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    GAP_HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    HEADER_BYTES_DUPLICATE_FIELD_NUMBER: _ClassVar[int]
    HEADER_BYTES_FIELD_NUMBER: _ClassVar[int]
    HEADER_BYTES_PADDING_FIELD_NUMBER: _ClassVar[int]
    JITTER_CURRENT_FIELD_NUMBER: _ClassVar[int]
    JITTER_MAX_FIELD_NUMBER: _ClassVar[int]
    KEY_FRAMES_FIELD_NUMBER: _ClassVar[int]
    LAST_FIR_FIELD_NUMBER: _ClassVar[int]
    LAST_KEY_FRAME_FIELD_NUMBER: _ClassVar[int]
    LAST_LAYER_LOCK_PLI_FIELD_NUMBER: _ClassVar[int]
    LAST_PLI_FIELD_NUMBER: _ClassVar[int]
    LAYER_LOCK_PLIS_FIELD_NUMBER: _ClassVar[int]
    NACKS_FIELD_NUMBER: _ClassVar[int]
    NACK_ACKS_FIELD_NUMBER: _ClassVar[int]
    NACK_MISSES_FIELD_NUMBER: _ClassVar[int]
    NACK_REPEATED_FIELD_NUMBER: _ClassVar[int]
    PACKETS_DUPLICATE_FIELD_NUMBER: _ClassVar[int]
    PACKETS_FIELD_NUMBER: _ClassVar[int]
    PACKETS_LOST_FIELD_NUMBER: _ClassVar[int]
    PACKETS_OUT_OF_ORDER_FIELD_NUMBER: _ClassVar[int]
    PACKETS_PADDING_FIELD_NUMBER: _ClassVar[int]
    PACKET_DUPLICATE_RATE_FIELD_NUMBER: _ClassVar[int]
    PACKET_LOSS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PACKET_LOSS_RATE_FIELD_NUMBER: _ClassVar[int]
    PACKET_PADDING_RATE_FIELD_NUMBER: _ClassVar[int]
    PACKET_RATE_FIELD_NUMBER: _ClassVar[int]
    PLIS_FIELD_NUMBER: _ClassVar[int]
    RTT_CURRENT_FIELD_NUMBER: _ClassVar[int]
    RTT_MAX_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    bitrate: float
    bitrate_duplicate: float
    bitrate_padding: float
    bytes: int
    bytes_duplicate: int
    bytes_padding: int
    duration: float
    end_time: _timestamp_pb2.Timestamp
    firs: int
    frame_rate: float
    frames: int
    gap_histogram: _containers.ScalarMap[int, int]
    header_bytes: int
    header_bytes_duplicate: int
    header_bytes_padding: int
    jitter_current: float
    jitter_max: float
    key_frames: int
    last_fir: _timestamp_pb2.Timestamp
    last_key_frame: _timestamp_pb2.Timestamp
    last_layer_lock_pli: _timestamp_pb2.Timestamp
    last_pli: _timestamp_pb2.Timestamp
    layer_lock_plis: int
    nack_acks: int
    nack_misses: int
    nack_repeated: int
    nacks: int
    packet_duplicate_rate: float
    packet_loss_percentage: float
    packet_loss_rate: float
    packet_padding_rate: float
    packet_rate: float
    packets: int
    packets_duplicate: int
    packets_lost: int
    packets_out_of_order: int
    packets_padding: int
    plis: int
    rtt_current: int
    rtt_max: int
    start_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        duration: _Optional[float] = ...,
        packets: _Optional[int] = ...,
        packet_rate: _Optional[float] = ...,
        bytes: _Optional[int] = ...,
        header_bytes: _Optional[int] = ...,
        bitrate: _Optional[float] = ...,
        packets_lost: _Optional[int] = ...,
        packet_loss_rate: _Optional[float] = ...,
        packet_loss_percentage: _Optional[float] = ...,
        packets_duplicate: _Optional[int] = ...,
        packet_duplicate_rate: _Optional[float] = ...,
        bytes_duplicate: _Optional[int] = ...,
        header_bytes_duplicate: _Optional[int] = ...,
        bitrate_duplicate: _Optional[float] = ...,
        packets_padding: _Optional[int] = ...,
        packet_padding_rate: _Optional[float] = ...,
        bytes_padding: _Optional[int] = ...,
        header_bytes_padding: _Optional[int] = ...,
        bitrate_padding: _Optional[float] = ...,
        packets_out_of_order: _Optional[int] = ...,
        frames: _Optional[int] = ...,
        frame_rate: _Optional[float] = ...,
        jitter_current: _Optional[float] = ...,
        jitter_max: _Optional[float] = ...,
        gap_histogram: _Optional[_Mapping[int, int]] = ...,
        nacks: _Optional[int] = ...,
        nack_acks: _Optional[int] = ...,
        nack_misses: _Optional[int] = ...,
        nack_repeated: _Optional[int] = ...,
        plis: _Optional[int] = ...,
        last_pli: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        firs: _Optional[int] = ...,
        last_fir: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        rtt_current: _Optional[int] = ...,
        rtt_max: _Optional[int] = ...,
        key_frames: _Optional[int] = ...,
        last_key_frame: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        layer_lock_plis: _Optional[int] = ...,
        last_layer_lock_pli: _Optional[
            _Union[_timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class Room(_message.Message):
    __slots__ = [
        "active_recording",
        "creation_time",
        "empty_timeout",
        "enabled_codecs",
        "max_participants",
        "metadata",
        "name",
        "num_participants",
        "sid",
        "turn_password",
    ]
    ACTIVE_RECORDING_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    EMPTY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_CODECS_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    TURN_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    active_recording: bool
    creation_time: int
    empty_timeout: int
    enabled_codecs: _containers.RepeatedCompositeFieldContainer[Codec]
    max_participants: int
    metadata: str
    name: str
    num_participants: int
    sid: str
    turn_password: str
    def __init__(
        self,
        sid: _Optional[str] = ...,
        name: _Optional[str] = ...,
        empty_timeout: _Optional[int] = ...,
        max_participants: _Optional[int] = ...,
        creation_time: _Optional[int] = ...,
        turn_password: _Optional[str] = ...,
        enabled_codecs: _Optional[_Iterable[_Union[Codec, _Mapping]]] = ...,
        metadata: _Optional[str] = ...,
        num_participants: _Optional[int] = ...,
        active_recording: bool = ...,
    ) -> None: ...

class ServerInfo(_message.Message):
    __slots__ = ["debug_info", "edition", "node_id", "protocol", "region", "version"]

    class Edition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    Cloud: ServerInfo.Edition
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    EDITION_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    Standard: ServerInfo.Edition
    VERSION_FIELD_NUMBER: _ClassVar[int]
    debug_info: str
    edition: ServerInfo.Edition
    node_id: str
    protocol: int
    region: str
    version: str
    def __init__(
        self,
        edition: _Optional[_Union[ServerInfo.Edition, str]] = ...,
        version: _Optional[str] = ...,
        protocol: _Optional[int] = ...,
        region: _Optional[str] = ...,
        node_id: _Optional[str] = ...,
        debug_info: _Optional[str] = ...,
    ) -> None: ...

class SimulcastCodecInfo(_message.Message):
    __slots__ = ["cid", "layers", "mid", "mime_type"]
    CID_FIELD_NUMBER: _ClassVar[int]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    cid: str
    layers: _containers.RepeatedCompositeFieldContainer[VideoLayer]
    mid: str
    mime_type: str
    def __init__(
        self,
        mime_type: _Optional[str] = ...,
        mid: _Optional[str] = ...,
        cid: _Optional[str] = ...,
        layers: _Optional[_Iterable[_Union[VideoLayer, _Mapping]]] = ...,
    ) -> None: ...

class SpeakerInfo(_message.Message):
    __slots__ = ["active", "level", "sid"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    level: float
    sid: str
    def __init__(
        self,
        sid: _Optional[str] = ...,
        level: _Optional[float] = ...,
        active: bool = ...,
    ) -> None: ...

class TimedVersion(_message.Message):
    __slots__ = ["ticks", "unix_micro"]
    TICKS_FIELD_NUMBER: _ClassVar[int]
    UNIX_MICRO_FIELD_NUMBER: _ClassVar[int]
    ticks: int
    unix_micro: int
    def __init__(
        self, unix_micro: _Optional[int] = ..., ticks: _Optional[int] = ...
    ) -> None: ...

class TrackInfo(_message.Message):
    __slots__ = [
        "codecs",
        "disable_dtx",
        "disable_red",
        "encryption",
        "height",
        "layers",
        "mid",
        "mime_type",
        "muted",
        "name",
        "sid",
        "simulcast",
        "source",
        "stereo",
        "type",
        "width",
    ]
    CODECS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DTX_FIELD_NUMBER: _ClassVar[int]
    DISABLE_RED_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    SIMULCAST_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STEREO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    codecs: _containers.RepeatedCompositeFieldContainer[SimulcastCodecInfo]
    disable_dtx: bool
    disable_red: bool
    encryption: Encryption.Type
    height: int
    layers: _containers.RepeatedCompositeFieldContainer[VideoLayer]
    mid: str
    mime_type: str
    muted: bool
    name: str
    sid: str
    simulcast: bool
    source: TrackSource
    stereo: bool
    type: TrackType
    width: int
    def __init__(
        self,
        sid: _Optional[str] = ...,
        type: _Optional[_Union[TrackType, str]] = ...,
        name: _Optional[str] = ...,
        muted: bool = ...,
        width: _Optional[int] = ...,
        height: _Optional[int] = ...,
        simulcast: bool = ...,
        disable_dtx: bool = ...,
        source: _Optional[_Union[TrackSource, str]] = ...,
        layers: _Optional[_Iterable[_Union[VideoLayer, _Mapping]]] = ...,
        mime_type: _Optional[str] = ...,
        mid: _Optional[str] = ...,
        codecs: _Optional[_Iterable[_Union[SimulcastCodecInfo, _Mapping]]] = ...,
        stereo: bool = ...,
        disable_red: bool = ...,
        encryption: _Optional[_Union[Encryption.Type, str]] = ...,
    ) -> None: ...

class UserPacket(_message.Message):
    __slots__ = ["destination_sids", "participant_sid", "payload", "topic"]
    DESTINATION_SIDS_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_SID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    destination_sids: _containers.RepeatedScalarFieldContainer[str]
    participant_sid: str
    payload: bytes
    topic: str
    def __init__(
        self,
        participant_sid: _Optional[str] = ...,
        payload: _Optional[bytes] = ...,
        destination_sids: _Optional[_Iterable[str]] = ...,
        topic: _Optional[str] = ...,
    ) -> None: ...

class VideoConfiguration(_message.Message):
    __slots__ = ["hardware_encoder"]
    HARDWARE_ENCODER_FIELD_NUMBER: _ClassVar[int]
    hardware_encoder: ClientConfigSetting
    def __init__(
        self, hardware_encoder: _Optional[_Union[ClientConfigSetting, str]] = ...
    ) -> None: ...

class VideoLayer(_message.Message):
    __slots__ = ["bitrate", "height", "quality", "ssrc", "width"]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    SSRC_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    bitrate: int
    height: int
    quality: VideoQuality
    ssrc: int
    width: int
    def __init__(
        self,
        quality: _Optional[_Union[VideoQuality, str]] = ...,
        width: _Optional[int] = ...,
        height: _Optional[int] = ...,
        bitrate: _Optional[int] = ...,
        ssrc: _Optional[int] = ...,
    ) -> None: ...

class AudioCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class VideoCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TrackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TrackSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class VideoQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ConnectionQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ClientConfigSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DisconnectReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ReconnectReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
