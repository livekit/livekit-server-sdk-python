from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import livekit_models_pb2 as _livekit_models_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
H264_1080P_30FPS_1_LAYER: IngressVideoEncodingPreset
H264_1080P_30FPS_3_LAYERS: IngressVideoEncodingPreset
H264_540P_25FPS_2_LAYERS: IngressVideoEncodingPreset
H264_720P_30FPS_1_LAYER: IngressVideoEncodingPreset
H264_720P_30FPS_3_LAYERS: IngressVideoEncodingPreset
OPUS_MONO_64KBS: IngressAudioEncodingPreset
OPUS_STEREO_96KBPS: IngressAudioEncodingPreset
RTMP_INPUT: IngressInput

class CreateIngressRequest(_message.Message):
    __slots__ = [
        "audio",
        "input_type",
        "name",
        "participant_identity",
        "participant_name",
        "room_name",
        "video",
    ]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    audio: IngressAudioOptions
    input_type: IngressInput
    name: str
    participant_identity: str
    participant_name: str
    room_name: str
    video: IngressVideoOptions
    def __init__(
        self,
        input_type: _Optional[_Union[IngressInput, str]] = ...,
        name: _Optional[str] = ...,
        room_name: _Optional[str] = ...,
        participant_identity: _Optional[str] = ...,
        participant_name: _Optional[str] = ...,
        audio: _Optional[_Union[IngressAudioOptions, _Mapping]] = ...,
        video: _Optional[_Union[IngressVideoOptions, _Mapping]] = ...,
    ) -> None: ...

class DeleteIngressRequest(_message.Message):
    __slots__ = ["ingress_id"]
    INGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    ingress_id: str
    def __init__(self, ingress_id: _Optional[str] = ...) -> None: ...

class IngressAudioEncodingOptions(_message.Message):
    __slots__ = ["audio_codec", "bitrate", "channels", "disable_dtx"]
    AUDIO_CODEC_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DTX_FIELD_NUMBER: _ClassVar[int]
    audio_codec: _livekit_models_pb2.AudioCodec
    bitrate: int
    channels: int
    disable_dtx: bool
    def __init__(
        self,
        audio_codec: _Optional[_Union[_livekit_models_pb2.AudioCodec, str]] = ...,
        bitrate: _Optional[int] = ...,
        disable_dtx: bool = ...,
        channels: _Optional[int] = ...,
    ) -> None: ...

class IngressAudioOptions(_message.Message):
    __slots__ = ["name", "options", "preset", "source"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRESET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    options: IngressAudioEncodingOptions
    preset: IngressAudioEncodingPreset
    source: _livekit_models_pb2.TrackSource
    def __init__(
        self,
        name: _Optional[str] = ...,
        source: _Optional[_Union[_livekit_models_pb2.TrackSource, str]] = ...,
        preset: _Optional[_Union[IngressAudioEncodingPreset, str]] = ...,
        options: _Optional[_Union[IngressAudioEncodingOptions, _Mapping]] = ...,
    ) -> None: ...

class IngressInfo(_message.Message):
    __slots__ = [
        "audio",
        "ingress_id",
        "input_type",
        "name",
        "participant_identity",
        "participant_name",
        "reusable",
        "room_name",
        "state",
        "stream_key",
        "url",
        "video",
    ]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    INGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_NAME_FIELD_NUMBER: _ClassVar[int]
    REUSABLE_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STREAM_KEY_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    audio: IngressAudioOptions
    ingress_id: str
    input_type: IngressInput
    name: str
    participant_identity: str
    participant_name: str
    reusable: bool
    room_name: str
    state: IngressState
    stream_key: str
    url: str
    video: IngressVideoOptions
    def __init__(
        self,
        ingress_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        stream_key: _Optional[str] = ...,
        url: _Optional[str] = ...,
        input_type: _Optional[_Union[IngressInput, str]] = ...,
        audio: _Optional[_Union[IngressAudioOptions, _Mapping]] = ...,
        video: _Optional[_Union[IngressVideoOptions, _Mapping]] = ...,
        room_name: _Optional[str] = ...,
        participant_identity: _Optional[str] = ...,
        participant_name: _Optional[str] = ...,
        reusable: bool = ...,
        state: _Optional[_Union[IngressState, _Mapping]] = ...,
    ) -> None: ...

class IngressState(_message.Message):
    __slots__ = [
        "audio",
        "ended_at",
        "error",
        "room_id",
        "started_at",
        "status",
        "tracks",
        "video",
    ]

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_BUFFERING: IngressState.Status
    ENDPOINT_ERROR: IngressState.Status
    ENDPOINT_INACTIVE: IngressState.Status
    ENDPOINT_PUBLISHING: IngressState.Status
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    audio: InputAudioState
    ended_at: int
    error: str
    room_id: str
    started_at: int
    status: IngressState.Status
    tracks: _containers.RepeatedCompositeFieldContainer[_livekit_models_pb2.TrackInfo]
    video: InputVideoState
    def __init__(
        self,
        status: _Optional[_Union[IngressState.Status, str]] = ...,
        error: _Optional[str] = ...,
        video: _Optional[_Union[InputVideoState, _Mapping]] = ...,
        audio: _Optional[_Union[InputAudioState, _Mapping]] = ...,
        room_id: _Optional[str] = ...,
        started_at: _Optional[int] = ...,
        ended_at: _Optional[int] = ...,
        tracks: _Optional[
            _Iterable[_Union[_livekit_models_pb2.TrackInfo, _Mapping]]
        ] = ...,
    ) -> None: ...

class IngressVideoEncodingOptions(_message.Message):
    __slots__ = ["frame_rate", "layers", "video_codec"]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CODEC_FIELD_NUMBER: _ClassVar[int]
    frame_rate: float
    layers: _containers.RepeatedCompositeFieldContainer[_livekit_models_pb2.VideoLayer]
    video_codec: _livekit_models_pb2.VideoCodec
    def __init__(
        self,
        video_codec: _Optional[_Union[_livekit_models_pb2.VideoCodec, str]] = ...,
        frame_rate: _Optional[float] = ...,
        layers: _Optional[
            _Iterable[_Union[_livekit_models_pb2.VideoLayer, _Mapping]]
        ] = ...,
    ) -> None: ...

class IngressVideoOptions(_message.Message):
    __slots__ = ["name", "options", "preset", "source"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRESET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    options: IngressVideoEncodingOptions
    preset: IngressVideoEncodingPreset
    source: _livekit_models_pb2.TrackSource
    def __init__(
        self,
        name: _Optional[str] = ...,
        source: _Optional[_Union[_livekit_models_pb2.TrackSource, str]] = ...,
        preset: _Optional[_Union[IngressVideoEncodingPreset, str]] = ...,
        options: _Optional[_Union[IngressVideoEncodingOptions, _Mapping]] = ...,
    ) -> None: ...

class InputAudioState(_message.Message):
    __slots__ = ["channels", "mime_type", "sample_rate"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    channels: int
    mime_type: str
    sample_rate: int
    def __init__(
        self,
        mime_type: _Optional[str] = ...,
        channels: _Optional[int] = ...,
        sample_rate: _Optional[int] = ...,
    ) -> None: ...

class InputVideoState(_message.Message):
    __slots__ = ["framerate", "height", "mime_type", "width"]
    FRAMERATE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    framerate: int
    height: int
    mime_type: str
    width: int
    def __init__(
        self,
        mime_type: _Optional[str] = ...,
        width: _Optional[int] = ...,
        height: _Optional[int] = ...,
        framerate: _Optional[int] = ...,
    ) -> None: ...

class ListIngressRequest(_message.Message):
    __slots__ = ["room_name"]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    room_name: str
    def __init__(self, room_name: _Optional[str] = ...) -> None: ...

class ListIngressResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[IngressInfo]
    def __init__(
        self, items: _Optional[_Iterable[_Union[IngressInfo, _Mapping]]] = ...
    ) -> None: ...

class UpdateIngressRequest(_message.Message):
    __slots__ = [
        "audio",
        "ingress_id",
        "name",
        "participant_identity",
        "participant_name",
        "room_name",
        "video",
    ]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    INGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    audio: IngressAudioOptions
    ingress_id: str
    name: str
    participant_identity: str
    participant_name: str
    room_name: str
    video: IngressVideoOptions
    def __init__(
        self,
        ingress_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        room_name: _Optional[str] = ...,
        participant_identity: _Optional[str] = ...,
        participant_name: _Optional[str] = ...,
        audio: _Optional[_Union[IngressAudioOptions, _Mapping]] = ...,
        video: _Optional[_Union[IngressVideoOptions, _Mapping]] = ...,
    ) -> None: ...

class IngressInput(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IngressAudioEncodingPreset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IngressVideoEncodingPreset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
