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

DEFAULT_FILETYPE: EncodedFileType
DEFAULT_PROTOCOL: StreamProtocol
DEFAULT_SEGMENTED_FILE_PROTOCOL: SegmentedFileProtocol
DESCRIPTOR: _descriptor.FileDescriptor
EGRESS_ABORTED: EgressStatus
EGRESS_ACTIVE: EgressStatus
EGRESS_COMPLETE: EgressStatus
EGRESS_ENDING: EgressStatus
EGRESS_FAILED: EgressStatus
EGRESS_LIMIT_REACHED: EgressStatus
EGRESS_STARTING: EgressStatus
H264_1080P_30: EncodingOptionsPreset
H264_1080P_60: EncodingOptionsPreset
H264_720P_30: EncodingOptionsPreset
H264_720P_60: EncodingOptionsPreset
HLS_PROTOCOL: SegmentedFileProtocol
INDEX: SegmentedFileSuffix
MP4: EncodedFileType
OGG: EncodedFileType
PORTRAIT_H264_1080P_30: EncodingOptionsPreset
PORTRAIT_H264_1080P_60: EncodingOptionsPreset
PORTRAIT_H264_720P_30: EncodingOptionsPreset
PORTRAIT_H264_720P_60: EncodingOptionsPreset
RTMP: StreamProtocol
TIMESTAMP: SegmentedFileSuffix

class AliOSSUpload(_message.Message):
    __slots__ = ["access_key", "bucket", "endpoint", "region", "secret"]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    access_key: str
    bucket: str
    endpoint: str
    region: str
    secret: str
    def __init__(
        self,
        access_key: _Optional[str] = ...,
        secret: _Optional[str] = ...,
        region: _Optional[str] = ...,
        endpoint: _Optional[str] = ...,
        bucket: _Optional[str] = ...,
    ) -> None: ...

class AutoTrackEgress(_message.Message):
    __slots__ = ["azure", "disable_manifest", "filepath", "gcp", "s3"]
    AZURE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    GCP_FIELD_NUMBER: _ClassVar[int]
    S3_FIELD_NUMBER: _ClassVar[int]
    azure: AzureBlobUpload
    disable_manifest: bool
    filepath: str
    gcp: GCPUpload
    s3: S3Upload
    def __init__(
        self,
        filepath: _Optional[str] = ...,
        disable_manifest: bool = ...,
        s3: _Optional[_Union[S3Upload, _Mapping]] = ...,
        gcp: _Optional[_Union[GCPUpload, _Mapping]] = ...,
        azure: _Optional[_Union[AzureBlobUpload, _Mapping]] = ...,
    ) -> None: ...

class AzureBlobUpload(_message.Message):
    __slots__ = ["account_key", "account_name", "container_name"]
    ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    account_key: str
    account_name: str
    container_name: str
    def __init__(
        self,
        account_name: _Optional[str] = ...,
        account_key: _Optional[str] = ...,
        container_name: _Optional[str] = ...,
    ) -> None: ...

class DirectFileOutput(_message.Message):
    __slots__ = ["aliOSS", "azure", "disable_manifest", "filepath", "gcp", "s3"]
    ALIOSS_FIELD_NUMBER: _ClassVar[int]
    AZURE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    GCP_FIELD_NUMBER: _ClassVar[int]
    S3_FIELD_NUMBER: _ClassVar[int]
    aliOSS: AliOSSUpload
    azure: AzureBlobUpload
    disable_manifest: bool
    filepath: str
    gcp: GCPUpload
    s3: S3Upload
    def __init__(
        self,
        filepath: _Optional[str] = ...,
        disable_manifest: bool = ...,
        s3: _Optional[_Union[S3Upload, _Mapping]] = ...,
        gcp: _Optional[_Union[GCPUpload, _Mapping]] = ...,
        azure: _Optional[_Union[AzureBlobUpload, _Mapping]] = ...,
        aliOSS: _Optional[_Union[AliOSSUpload, _Mapping]] = ...,
    ) -> None: ...

class EgressInfo(_message.Message):
    __slots__ = [
        "egress_id",
        "ended_at",
        "error",
        "file",
        "file_results",
        "room_composite",
        "room_id",
        "room_name",
        "segment_results",
        "segments",
        "started_at",
        "status",
        "stream",
        "stream_results",
        "track",
        "track_composite",
        "web",
    ]
    EGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ROOM_COMPOSITE_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_RESULTS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    STREAM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRACK_COMPOSITE_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    WEB_FIELD_NUMBER: _ClassVar[int]
    egress_id: str
    ended_at: int
    error: str
    file: FileInfo
    file_results: _containers.RepeatedCompositeFieldContainer[FileInfo]
    room_composite: RoomCompositeEgressRequest
    room_id: str
    room_name: str
    segment_results: _containers.RepeatedCompositeFieldContainer[SegmentsInfo]
    segments: SegmentsInfo
    started_at: int
    status: EgressStatus
    stream: StreamInfoList
    stream_results: _containers.RepeatedCompositeFieldContainer[StreamInfo]
    track: TrackEgressRequest
    track_composite: TrackCompositeEgressRequest
    web: WebEgressRequest
    def __init__(
        self,
        egress_id: _Optional[str] = ...,
        room_id: _Optional[str] = ...,
        room_name: _Optional[str] = ...,
        status: _Optional[_Union[EgressStatus, str]] = ...,
        started_at: _Optional[int] = ...,
        ended_at: _Optional[int] = ...,
        error: _Optional[str] = ...,
        room_composite: _Optional[_Union[RoomCompositeEgressRequest, _Mapping]] = ...,
        track_composite: _Optional[_Union[TrackCompositeEgressRequest, _Mapping]] = ...,
        track: _Optional[_Union[TrackEgressRequest, _Mapping]] = ...,
        web: _Optional[_Union[WebEgressRequest, _Mapping]] = ...,
        stream: _Optional[_Union[StreamInfoList, _Mapping]] = ...,
        file: _Optional[_Union[FileInfo, _Mapping]] = ...,
        segments: _Optional[_Union[SegmentsInfo, _Mapping]] = ...,
        stream_results: _Optional[_Iterable[_Union[StreamInfo, _Mapping]]] = ...,
        file_results: _Optional[_Iterable[_Union[FileInfo, _Mapping]]] = ...,
        segment_results: _Optional[_Iterable[_Union[SegmentsInfo, _Mapping]]] = ...,
    ) -> None: ...

class EncodedFileOutput(_message.Message):
    __slots__ = [
        "aliOSS",
        "azure",
        "disable_manifest",
        "file_type",
        "filepath",
        "gcp",
        "s3",
    ]
    ALIOSS_FIELD_NUMBER: _ClassVar[int]
    AZURE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GCP_FIELD_NUMBER: _ClassVar[int]
    S3_FIELD_NUMBER: _ClassVar[int]
    aliOSS: AliOSSUpload
    azure: AzureBlobUpload
    disable_manifest: bool
    file_type: EncodedFileType
    filepath: str
    gcp: GCPUpload
    s3: S3Upload
    def __init__(
        self,
        file_type: _Optional[_Union[EncodedFileType, str]] = ...,
        filepath: _Optional[str] = ...,
        disable_manifest: bool = ...,
        s3: _Optional[_Union[S3Upload, _Mapping]] = ...,
        gcp: _Optional[_Union[GCPUpload, _Mapping]] = ...,
        azure: _Optional[_Union[AzureBlobUpload, _Mapping]] = ...,
        aliOSS: _Optional[_Union[AliOSSUpload, _Mapping]] = ...,
    ) -> None: ...

class EncodingOptions(_message.Message):
    __slots__ = [
        "audio_bitrate",
        "audio_codec",
        "audio_frequency",
        "depth",
        "framerate",
        "height",
        "key_frame_interval",
        "video_bitrate",
        "video_codec",
        "width",
    ]
    AUDIO_BITRATE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CODEC_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    FRAMERATE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    KEY_FRAME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_BITRATE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CODEC_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    audio_bitrate: int
    audio_codec: _livekit_models_pb2.AudioCodec
    audio_frequency: int
    depth: int
    framerate: int
    height: int
    key_frame_interval: float
    video_bitrate: int
    video_codec: _livekit_models_pb2.VideoCodec
    width: int
    def __init__(
        self,
        width: _Optional[int] = ...,
        height: _Optional[int] = ...,
        depth: _Optional[int] = ...,
        framerate: _Optional[int] = ...,
        audio_codec: _Optional[_Union[_livekit_models_pb2.AudioCodec, str]] = ...,
        audio_bitrate: _Optional[int] = ...,
        audio_frequency: _Optional[int] = ...,
        video_codec: _Optional[_Union[_livekit_models_pb2.VideoCodec, str]] = ...,
        video_bitrate: _Optional[int] = ...,
        key_frame_interval: _Optional[float] = ...,
    ) -> None: ...

class FileInfo(_message.Message):
    __slots__ = ["duration", "ended_at", "filename", "location", "size", "started_at"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    duration: int
    ended_at: int
    filename: str
    location: str
    size: int
    started_at: int
    def __init__(
        self,
        filename: _Optional[str] = ...,
        started_at: _Optional[int] = ...,
        ended_at: _Optional[int] = ...,
        duration: _Optional[int] = ...,
        size: _Optional[int] = ...,
        location: _Optional[str] = ...,
    ) -> None: ...

class GCPUpload(_message.Message):
    __slots__ = ["bucket", "credentials"]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    credentials: str
    def __init__(
        self, credentials: _Optional[str] = ..., bucket: _Optional[str] = ...
    ) -> None: ...

class ListEgressRequest(_message.Message):
    __slots__ = ["active", "egress_id", "room_name"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    active: bool
    egress_id: str
    room_name: str
    def __init__(
        self,
        room_name: _Optional[str] = ...,
        egress_id: _Optional[str] = ...,
        active: bool = ...,
    ) -> None: ...

class ListEgressResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[EgressInfo]
    def __init__(
        self, items: _Optional[_Iterable[_Union[EgressInfo, _Mapping]]] = ...
    ) -> None: ...

class RoomCompositeEgressRequest(_message.Message):
    __slots__ = [
        "advanced",
        "audio_only",
        "custom_base_url",
        "file",
        "file_outputs",
        "layout",
        "preset",
        "room_name",
        "segment_outputs",
        "segments",
        "stream",
        "stream_outputs",
        "video_only",
    ]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ONLY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_BASE_URL_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    PRESET_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    STREAM_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ONLY_FIELD_NUMBER: _ClassVar[int]
    advanced: EncodingOptions
    audio_only: bool
    custom_base_url: str
    file: EncodedFileOutput
    file_outputs: _containers.RepeatedCompositeFieldContainer[EncodedFileOutput]
    layout: str
    preset: EncodingOptionsPreset
    room_name: str
    segment_outputs: _containers.RepeatedCompositeFieldContainer[SegmentedFileOutput]
    segments: SegmentedFileOutput
    stream: StreamOutput
    stream_outputs: _containers.RepeatedCompositeFieldContainer[StreamOutput]
    video_only: bool
    def __init__(
        self,
        room_name: _Optional[str] = ...,
        layout: _Optional[str] = ...,
        audio_only: bool = ...,
        video_only: bool = ...,
        custom_base_url: _Optional[str] = ...,
        file: _Optional[_Union[EncodedFileOutput, _Mapping]] = ...,
        stream: _Optional[_Union[StreamOutput, _Mapping]] = ...,
        segments: _Optional[_Union[SegmentedFileOutput, _Mapping]] = ...,
        preset: _Optional[_Union[EncodingOptionsPreset, str]] = ...,
        advanced: _Optional[_Union[EncodingOptions, _Mapping]] = ...,
        file_outputs: _Optional[_Iterable[_Union[EncodedFileOutput, _Mapping]]] = ...,
        stream_outputs: _Optional[_Iterable[_Union[StreamOutput, _Mapping]]] = ...,
        segment_outputs: _Optional[
            _Iterable[_Union[SegmentedFileOutput, _Mapping]]
        ] = ...,
    ) -> None: ...

class S3Upload(_message.Message):
    __slots__ = [
        "access_key",
        "bucket",
        "endpoint",
        "force_path_style",
        "metadata",
        "region",
        "secret",
        "tagging",
    ]

    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    FORCE_PATH_STYLE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TAGGING_FIELD_NUMBER: _ClassVar[int]
    access_key: str
    bucket: str
    endpoint: str
    force_path_style: bool
    metadata: _containers.ScalarMap[str, str]
    region: str
    secret: str
    tagging: str
    def __init__(
        self,
        access_key: _Optional[str] = ...,
        secret: _Optional[str] = ...,
        region: _Optional[str] = ...,
        endpoint: _Optional[str] = ...,
        bucket: _Optional[str] = ...,
        force_path_style: bool = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
        tagging: _Optional[str] = ...,
    ) -> None: ...

class SegmentedFileOutput(_message.Message):
    __slots__ = [
        "aliOSS",
        "azure",
        "disable_manifest",
        "filename_prefix",
        "filename_suffix",
        "gcp",
        "playlist_name",
        "protocol",
        "s3",
        "segment_duration",
    ]
    ALIOSS_FIELD_NUMBER: _ClassVar[int]
    AZURE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    FILENAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    FILENAME_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    GCP_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_NAME_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    S3_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_DURATION_FIELD_NUMBER: _ClassVar[int]
    aliOSS: AliOSSUpload
    azure: AzureBlobUpload
    disable_manifest: bool
    filename_prefix: str
    filename_suffix: SegmentedFileSuffix
    gcp: GCPUpload
    playlist_name: str
    protocol: SegmentedFileProtocol
    s3: S3Upload
    segment_duration: int
    def __init__(
        self,
        protocol: _Optional[_Union[SegmentedFileProtocol, str]] = ...,
        filename_prefix: _Optional[str] = ...,
        playlist_name: _Optional[str] = ...,
        segment_duration: _Optional[int] = ...,
        filename_suffix: _Optional[_Union[SegmentedFileSuffix, str]] = ...,
        disable_manifest: bool = ...,
        s3: _Optional[_Union[S3Upload, _Mapping]] = ...,
        gcp: _Optional[_Union[GCPUpload, _Mapping]] = ...,
        azure: _Optional[_Union[AzureBlobUpload, _Mapping]] = ...,
        aliOSS: _Optional[_Union[AliOSSUpload, _Mapping]] = ...,
    ) -> None: ...

class SegmentsInfo(_message.Message):
    __slots__ = [
        "duration",
        "ended_at",
        "playlist_location",
        "playlist_name",
        "segment_count",
        "size",
        "started_at",
    ]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    duration: int
    ended_at: int
    playlist_location: str
    playlist_name: str
    segment_count: int
    size: int
    started_at: int
    def __init__(
        self,
        playlist_name: _Optional[str] = ...,
        duration: _Optional[int] = ...,
        size: _Optional[int] = ...,
        playlist_location: _Optional[str] = ...,
        segment_count: _Optional[int] = ...,
        started_at: _Optional[int] = ...,
        ended_at: _Optional[int] = ...,
    ) -> None: ...

class StopEgressRequest(_message.Message):
    __slots__ = ["egress_id"]
    EGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    egress_id: str
    def __init__(self, egress_id: _Optional[str] = ...) -> None: ...

class StreamInfo(_message.Message):
    __slots__ = ["duration", "ended_at", "error", "started_at", "status", "url"]

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: StreamInfo.Status
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FAILED: StreamInfo.Status
    FINISHED: StreamInfo.Status
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    duration: int
    ended_at: int
    error: str
    started_at: int
    status: StreamInfo.Status
    url: str
    def __init__(
        self,
        url: _Optional[str] = ...,
        started_at: _Optional[int] = ...,
        ended_at: _Optional[int] = ...,
        duration: _Optional[int] = ...,
        status: _Optional[_Union[StreamInfo.Status, str]] = ...,
        error: _Optional[str] = ...,
    ) -> None: ...

class StreamInfoList(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _containers.RepeatedCompositeFieldContainer[StreamInfo]
    def __init__(
        self, info: _Optional[_Iterable[_Union[StreamInfo, _Mapping]]] = ...
    ) -> None: ...

class StreamOutput(_message.Message):
    __slots__ = ["protocol", "urls"]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    protocol: StreamProtocol
    urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        protocol: _Optional[_Union[StreamProtocol, str]] = ...,
        urls: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class TrackCompositeEgressRequest(_message.Message):
    __slots__ = [
        "advanced",
        "audio_track_id",
        "file",
        "file_outputs",
        "preset",
        "room_name",
        "segment_outputs",
        "segments",
        "stream",
        "stream_outputs",
        "video_track_id",
    ]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    PRESET_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    STREAM_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    advanced: EncodingOptions
    audio_track_id: str
    file: EncodedFileOutput
    file_outputs: _containers.RepeatedCompositeFieldContainer[EncodedFileOutput]
    preset: EncodingOptionsPreset
    room_name: str
    segment_outputs: _containers.RepeatedCompositeFieldContainer[SegmentedFileOutput]
    segments: SegmentedFileOutput
    stream: StreamOutput
    stream_outputs: _containers.RepeatedCompositeFieldContainer[StreamOutput]
    video_track_id: str
    def __init__(
        self,
        room_name: _Optional[str] = ...,
        audio_track_id: _Optional[str] = ...,
        video_track_id: _Optional[str] = ...,
        file: _Optional[_Union[EncodedFileOutput, _Mapping]] = ...,
        stream: _Optional[_Union[StreamOutput, _Mapping]] = ...,
        segments: _Optional[_Union[SegmentedFileOutput, _Mapping]] = ...,
        preset: _Optional[_Union[EncodingOptionsPreset, str]] = ...,
        advanced: _Optional[_Union[EncodingOptions, _Mapping]] = ...,
        file_outputs: _Optional[_Iterable[_Union[EncodedFileOutput, _Mapping]]] = ...,
        stream_outputs: _Optional[_Iterable[_Union[StreamOutput, _Mapping]]] = ...,
        segment_outputs: _Optional[
            _Iterable[_Union[SegmentedFileOutput, _Mapping]]
        ] = ...,
    ) -> None: ...

class TrackEgressRequest(_message.Message):
    __slots__ = ["file", "room_name", "track_id", "websocket_url"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    WEBSOCKET_URL_FIELD_NUMBER: _ClassVar[int]
    file: DirectFileOutput
    room_name: str
    track_id: str
    websocket_url: str
    def __init__(
        self,
        room_name: _Optional[str] = ...,
        track_id: _Optional[str] = ...,
        file: _Optional[_Union[DirectFileOutput, _Mapping]] = ...,
        websocket_url: _Optional[str] = ...,
    ) -> None: ...

class UpdateLayoutRequest(_message.Message):
    __slots__ = ["egress_id", "layout"]
    EGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    egress_id: str
    layout: str
    def __init__(
        self, egress_id: _Optional[str] = ..., layout: _Optional[str] = ...
    ) -> None: ...

class UpdateStreamRequest(_message.Message):
    __slots__ = ["add_output_urls", "egress_id", "remove_output_urls"]
    ADD_OUTPUT_URLS_FIELD_NUMBER: _ClassVar[int]
    EGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVE_OUTPUT_URLS_FIELD_NUMBER: _ClassVar[int]
    add_output_urls: _containers.RepeatedScalarFieldContainer[str]
    egress_id: str
    remove_output_urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        egress_id: _Optional[str] = ...,
        add_output_urls: _Optional[_Iterable[str]] = ...,
        remove_output_urls: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class WebEgressRequest(_message.Message):
    __slots__ = [
        "advanced",
        "audio_only",
        "file",
        "file_outputs",
        "preset",
        "segment_outputs",
        "segments",
        "stream",
        "stream_outputs",
        "url",
        "video_only",
    ]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ONLY_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    PRESET_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    STREAM_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ONLY_FIELD_NUMBER: _ClassVar[int]
    advanced: EncodingOptions
    audio_only: bool
    file: EncodedFileOutput
    file_outputs: _containers.RepeatedCompositeFieldContainer[EncodedFileOutput]
    preset: EncodingOptionsPreset
    segment_outputs: _containers.RepeatedCompositeFieldContainer[SegmentedFileOutput]
    segments: SegmentedFileOutput
    stream: StreamOutput
    stream_outputs: _containers.RepeatedCompositeFieldContainer[StreamOutput]
    url: str
    video_only: bool
    def __init__(
        self,
        url: _Optional[str] = ...,
        audio_only: bool = ...,
        video_only: bool = ...,
        file: _Optional[_Union[EncodedFileOutput, _Mapping]] = ...,
        stream: _Optional[_Union[StreamOutput, _Mapping]] = ...,
        segments: _Optional[_Union[SegmentedFileOutput, _Mapping]] = ...,
        preset: _Optional[_Union[EncodingOptionsPreset, str]] = ...,
        advanced: _Optional[_Union[EncodingOptions, _Mapping]] = ...,
        file_outputs: _Optional[_Iterable[_Union[EncodedFileOutput, _Mapping]]] = ...,
        stream_outputs: _Optional[_Iterable[_Union[StreamOutput, _Mapping]]] = ...,
        segment_outputs: _Optional[
            _Iterable[_Union[SegmentedFileOutput, _Mapping]]
        ] = ...,
    ) -> None: ...

class EncodedFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SegmentedFileProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SegmentedFileSuffix(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class StreamProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EncodingOptionsPreset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EgressStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
