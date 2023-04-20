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

ACTIVE: StreamState
DESCRIPTOR: _descriptor.FileDescriptor
PAUSED: StreamState
PUBLISHER: SignalTarget
SUBSCRIBER: SignalTarget
TCP: CandidateProtocol
TLS: CandidateProtocol
UDP: CandidateProtocol

class AddTrackRequest(_message.Message):
    __slots__ = [
        "cid",
        "disable_dtx",
        "disable_red",
        "encryption",
        "height",
        "layers",
        "muted",
        "name",
        "sid",
        "simulcast_codecs",
        "source",
        "stereo",
        "type",
        "width",
    ]
    CID_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DTX_FIELD_NUMBER: _ClassVar[int]
    DISABLE_RED_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    SIMULCAST_CODECS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STEREO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    cid: str
    disable_dtx: bool
    disable_red: bool
    encryption: _livekit_models_pb2.Encryption.Type
    height: int
    layers: _containers.RepeatedCompositeFieldContainer[_livekit_models_pb2.VideoLayer]
    muted: bool
    name: str
    sid: str
    simulcast_codecs: _containers.RepeatedCompositeFieldContainer[SimulcastCodec]
    source: _livekit_models_pb2.TrackSource
    stereo: bool
    type: _livekit_models_pb2.TrackType
    width: int
    def __init__(
        self,
        cid: _Optional[str] = ...,
        name: _Optional[str] = ...,
        type: _Optional[_Union[_livekit_models_pb2.TrackType, str]] = ...,
        width: _Optional[int] = ...,
        height: _Optional[int] = ...,
        muted: bool = ...,
        disable_dtx: bool = ...,
        source: _Optional[_Union[_livekit_models_pb2.TrackSource, str]] = ...,
        layers: _Optional[
            _Iterable[_Union[_livekit_models_pb2.VideoLayer, _Mapping]]
        ] = ...,
        simulcast_codecs: _Optional[_Iterable[_Union[SimulcastCodec, _Mapping]]] = ...,
        sid: _Optional[str] = ...,
        stereo: bool = ...,
        disable_red: bool = ...,
        encryption: _Optional[_Union[_livekit_models_pb2.Encryption.Type, str]] = ...,
    ) -> None: ...

class ConnectionQualityInfo(_message.Message):
    __slots__ = ["participant_sid", "quality", "score"]
    PARTICIPANT_SID_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    participant_sid: str
    quality: _livekit_models_pb2.ConnectionQuality
    score: float
    def __init__(
        self,
        participant_sid: _Optional[str] = ...,
        quality: _Optional[_Union[_livekit_models_pb2.ConnectionQuality, str]] = ...,
        score: _Optional[float] = ...,
    ) -> None: ...

class ConnectionQualityUpdate(_message.Message):
    __slots__ = ["updates"]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[ConnectionQualityInfo]
    def __init__(
        self,
        updates: _Optional[_Iterable[_Union[ConnectionQualityInfo, _Mapping]]] = ...,
    ) -> None: ...

class DataChannelInfo(_message.Message):
    __slots__ = ["id", "label", "target"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    id: int
    label: str
    target: SignalTarget
    def __init__(
        self,
        label: _Optional[str] = ...,
        id: _Optional[int] = ...,
        target: _Optional[_Union[SignalTarget, str]] = ...,
    ) -> None: ...

class ICEServer(_message.Message):
    __slots__ = ["credential", "urls", "username"]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    credential: str
    urls: _containers.RepeatedScalarFieldContainer[str]
    username: str
    def __init__(
        self,
        urls: _Optional[_Iterable[str]] = ...,
        username: _Optional[str] = ...,
        credential: _Optional[str] = ...,
    ) -> None: ...

class JoinResponse(_message.Message):
    __slots__ = [
        "alternative_url",
        "client_configuration",
        "ice_servers",
        "other_participants",
        "participant",
        "ping_interval",
        "ping_timeout",
        "room",
        "server_info",
        "server_region",
        "server_version",
        "subscriber_primary",
    ]
    ALTERNATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    ICE_SERVERS_FIELD_NUMBER: _ClassVar[int]
    OTHER_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    PING_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    SERVER_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVER_REGION_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    alternative_url: str
    client_configuration: _livekit_models_pb2.ClientConfiguration
    ice_servers: _containers.RepeatedCompositeFieldContainer[ICEServer]
    other_participants: _containers.RepeatedCompositeFieldContainer[
        _livekit_models_pb2.ParticipantInfo
    ]
    participant: _livekit_models_pb2.ParticipantInfo
    ping_interval: int
    ping_timeout: int
    room: _livekit_models_pb2.Room
    server_info: _livekit_models_pb2.ServerInfo
    server_region: str
    server_version: str
    subscriber_primary: bool
    def __init__(
        self,
        room: _Optional[_Union[_livekit_models_pb2.Room, _Mapping]] = ...,
        participant: _Optional[
            _Union[_livekit_models_pb2.ParticipantInfo, _Mapping]
        ] = ...,
        other_participants: _Optional[
            _Iterable[_Union[_livekit_models_pb2.ParticipantInfo, _Mapping]]
        ] = ...,
        server_version: _Optional[str] = ...,
        ice_servers: _Optional[_Iterable[_Union[ICEServer, _Mapping]]] = ...,
        subscriber_primary: bool = ...,
        alternative_url: _Optional[str] = ...,
        client_configuration: _Optional[
            _Union[_livekit_models_pb2.ClientConfiguration, _Mapping]
        ] = ...,
        server_region: _Optional[str] = ...,
        ping_timeout: _Optional[int] = ...,
        ping_interval: _Optional[int] = ...,
        server_info: _Optional[_Union[_livekit_models_pb2.ServerInfo, _Mapping]] = ...,
    ) -> None: ...

class LeaveRequest(_message.Message):
    __slots__ = ["can_reconnect", "reason"]
    CAN_RECONNECT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    can_reconnect: bool
    reason: _livekit_models_pb2.DisconnectReason
    def __init__(
        self,
        can_reconnect: bool = ...,
        reason: _Optional[_Union[_livekit_models_pb2.DisconnectReason, str]] = ...,
    ) -> None: ...

class MuteTrackRequest(_message.Message):
    __slots__ = ["muted", "sid"]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    muted: bool
    sid: str
    def __init__(self, sid: _Optional[str] = ..., muted: bool = ...) -> None: ...

class ParticipantUpdate(_message.Message):
    __slots__ = ["participants"]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    participants: _containers.RepeatedCompositeFieldContainer[
        _livekit_models_pb2.ParticipantInfo
    ]
    def __init__(
        self,
        participants: _Optional[
            _Iterable[_Union[_livekit_models_pb2.ParticipantInfo, _Mapping]]
        ] = ...,
    ) -> None: ...

class Ping(_message.Message):
    __slots__ = ["rtt", "timestamp"]
    RTT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    rtt: int
    timestamp: int
    def __init__(
        self, timestamp: _Optional[int] = ..., rtt: _Optional[int] = ...
    ) -> None: ...

class Pong(_message.Message):
    __slots__ = ["last_ping_timestamp", "timestamp"]
    LAST_PING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    last_ping_timestamp: int
    timestamp: int
    def __init__(
        self, last_ping_timestamp: _Optional[int] = ..., timestamp: _Optional[int] = ...
    ) -> None: ...

class ReconnectResponse(_message.Message):
    __slots__ = ["client_configuration", "ice_servers"]
    CLIENT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    ICE_SERVERS_FIELD_NUMBER: _ClassVar[int]
    client_configuration: _livekit_models_pb2.ClientConfiguration
    ice_servers: _containers.RepeatedCompositeFieldContainer[ICEServer]
    def __init__(
        self,
        ice_servers: _Optional[_Iterable[_Union[ICEServer, _Mapping]]] = ...,
        client_configuration: _Optional[
            _Union[_livekit_models_pb2.ClientConfiguration, _Mapping]
        ] = ...,
    ) -> None: ...

class RegionInfo(_message.Message):
    __slots__ = ["distance", "region", "url"]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    distance: int
    region: str
    url: str
    def __init__(
        self,
        region: _Optional[str] = ...,
        url: _Optional[str] = ...,
        distance: _Optional[int] = ...,
    ) -> None: ...

class RegionSettings(_message.Message):
    __slots__ = ["regions"]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    regions: _containers.RepeatedCompositeFieldContainer[RegionInfo]
    def __init__(
        self, regions: _Optional[_Iterable[_Union[RegionInfo, _Mapping]]] = ...
    ) -> None: ...

class RoomUpdate(_message.Message):
    __slots__ = ["room"]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    room: _livekit_models_pb2.Room
    def __init__(
        self, room: _Optional[_Union[_livekit_models_pb2.Room, _Mapping]] = ...
    ) -> None: ...

class SessionDescription(_message.Message):
    __slots__ = ["sdp", "type"]
    SDP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    sdp: str
    type: str
    def __init__(
        self, type: _Optional[str] = ..., sdp: _Optional[str] = ...
    ) -> None: ...

class SignalRequest(_message.Message):
    __slots__ = [
        "add_track",
        "answer",
        "leave",
        "mute",
        "offer",
        "ping",
        "ping_req",
        "simulate",
        "subscription",
        "subscription_permission",
        "sync_state",
        "track_setting",
        "trickle",
        "update_layers",
        "update_metadata",
    ]
    ADD_TRACK_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    LEAVE_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    PING_REQ_FIELD_NUMBER: _ClassVar[int]
    SIMULATE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    TRACK_SETTING_FIELD_NUMBER: _ClassVar[int]
    TRICKLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_LAYERS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    add_track: AddTrackRequest
    answer: SessionDescription
    leave: LeaveRequest
    mute: MuteTrackRequest
    offer: SessionDescription
    ping: int
    ping_req: Ping
    simulate: SimulateScenario
    subscription: UpdateSubscription
    subscription_permission: SubscriptionPermission
    sync_state: SyncState
    track_setting: UpdateTrackSettings
    trickle: TrickleRequest
    update_layers: UpdateVideoLayers
    update_metadata: UpdateParticipantMetadata
    def __init__(
        self,
        offer: _Optional[_Union[SessionDescription, _Mapping]] = ...,
        answer: _Optional[_Union[SessionDescription, _Mapping]] = ...,
        trickle: _Optional[_Union[TrickleRequest, _Mapping]] = ...,
        add_track: _Optional[_Union[AddTrackRequest, _Mapping]] = ...,
        mute: _Optional[_Union[MuteTrackRequest, _Mapping]] = ...,
        subscription: _Optional[_Union[UpdateSubscription, _Mapping]] = ...,
        track_setting: _Optional[_Union[UpdateTrackSettings, _Mapping]] = ...,
        leave: _Optional[_Union[LeaveRequest, _Mapping]] = ...,
        update_layers: _Optional[_Union[UpdateVideoLayers, _Mapping]] = ...,
        subscription_permission: _Optional[
            _Union[SubscriptionPermission, _Mapping]
        ] = ...,
        sync_state: _Optional[_Union[SyncState, _Mapping]] = ...,
        simulate: _Optional[_Union[SimulateScenario, _Mapping]] = ...,
        ping: _Optional[int] = ...,
        update_metadata: _Optional[_Union[UpdateParticipantMetadata, _Mapping]] = ...,
        ping_req: _Optional[_Union[Ping, _Mapping]] = ...,
    ) -> None: ...

class SignalResponse(_message.Message):
    __slots__ = [
        "answer",
        "connection_quality",
        "join",
        "leave",
        "mute",
        "offer",
        "pong",
        "pong_resp",
        "reconnect",
        "refresh_token",
        "room_update",
        "speakers_changed",
        "stream_state_update",
        "subscribed_quality_update",
        "subscription_permission_update",
        "track_published",
        "track_unpublished",
        "trickle",
        "update",
    ]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_QUALITY_FIELD_NUMBER: _ClassVar[int]
    JOIN_FIELD_NUMBER: _ClassVar[int]
    LEAVE_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    PONG_FIELD_NUMBER: _ClassVar[int]
    PONG_RESP_FIELD_NUMBER: _ClassVar[int]
    RECONNECT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROOM_UPDATE_FIELD_NUMBER: _ClassVar[int]
    SPEAKERS_CHANGED_FIELD_NUMBER: _ClassVar[int]
    STREAM_STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_QUALITY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_PERMISSION_UPDATE_FIELD_NUMBER: _ClassVar[int]
    TRACK_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    TRACK_UNPUBLISHED_FIELD_NUMBER: _ClassVar[int]
    TRICKLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    answer: SessionDescription
    connection_quality: ConnectionQualityUpdate
    join: JoinResponse
    leave: LeaveRequest
    mute: MuteTrackRequest
    offer: SessionDescription
    pong: int
    pong_resp: Pong
    reconnect: ReconnectResponse
    refresh_token: str
    room_update: RoomUpdate
    speakers_changed: SpeakersChanged
    stream_state_update: StreamStateUpdate
    subscribed_quality_update: SubscribedQualityUpdate
    subscription_permission_update: SubscriptionPermissionUpdate
    track_published: TrackPublishedResponse
    track_unpublished: TrackUnpublishedResponse
    trickle: TrickleRequest
    update: ParticipantUpdate
    def __init__(
        self,
        join: _Optional[_Union[JoinResponse, _Mapping]] = ...,
        answer: _Optional[_Union[SessionDescription, _Mapping]] = ...,
        offer: _Optional[_Union[SessionDescription, _Mapping]] = ...,
        trickle: _Optional[_Union[TrickleRequest, _Mapping]] = ...,
        update: _Optional[_Union[ParticipantUpdate, _Mapping]] = ...,
        track_published: _Optional[_Union[TrackPublishedResponse, _Mapping]] = ...,
        leave: _Optional[_Union[LeaveRequest, _Mapping]] = ...,
        mute: _Optional[_Union[MuteTrackRequest, _Mapping]] = ...,
        speakers_changed: _Optional[_Union[SpeakersChanged, _Mapping]] = ...,
        room_update: _Optional[_Union[RoomUpdate, _Mapping]] = ...,
        connection_quality: _Optional[_Union[ConnectionQualityUpdate, _Mapping]] = ...,
        stream_state_update: _Optional[_Union[StreamStateUpdate, _Mapping]] = ...,
        subscribed_quality_update: _Optional[
            _Union[SubscribedQualityUpdate, _Mapping]
        ] = ...,
        subscription_permission_update: _Optional[
            _Union[SubscriptionPermissionUpdate, _Mapping]
        ] = ...,
        refresh_token: _Optional[str] = ...,
        track_unpublished: _Optional[_Union[TrackUnpublishedResponse, _Mapping]] = ...,
        pong: _Optional[int] = ...,
        reconnect: _Optional[_Union[ReconnectResponse, _Mapping]] = ...,
        pong_resp: _Optional[_Union[Pong, _Mapping]] = ...,
    ) -> None: ...

class SimulateScenario(_message.Message):
    __slots__ = [
        "migration",
        "node_failure",
        "server_leave",
        "speaker_update",
        "subscriber_bandwidth",
        "switch_candidate_protocol",
    ]
    MIGRATION_FIELD_NUMBER: _ClassVar[int]
    NODE_FAILURE_FIELD_NUMBER: _ClassVar[int]
    SERVER_LEAVE_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_UPDATE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    SWITCH_CANDIDATE_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    migration: bool
    node_failure: bool
    server_leave: bool
    speaker_update: int
    subscriber_bandwidth: int
    switch_candidate_protocol: CandidateProtocol
    def __init__(
        self,
        speaker_update: _Optional[int] = ...,
        node_failure: bool = ...,
        migration: bool = ...,
        server_leave: bool = ...,
        switch_candidate_protocol: _Optional[_Union[CandidateProtocol, str]] = ...,
        subscriber_bandwidth: _Optional[int] = ...,
    ) -> None: ...

class SimulcastCodec(_message.Message):
    __slots__ = ["cid", "codec", "enable_simulcast_layers"]
    CID_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SIMULCAST_LAYERS_FIELD_NUMBER: _ClassVar[int]
    cid: str
    codec: str
    enable_simulcast_layers: bool
    def __init__(
        self,
        codec: _Optional[str] = ...,
        cid: _Optional[str] = ...,
        enable_simulcast_layers: bool = ...,
    ) -> None: ...

class SpeakersChanged(_message.Message):
    __slots__ = ["speakers"]
    SPEAKERS_FIELD_NUMBER: _ClassVar[int]
    speakers: _containers.RepeatedCompositeFieldContainer[
        _livekit_models_pb2.SpeakerInfo
    ]
    def __init__(
        self,
        speakers: _Optional[
            _Iterable[_Union[_livekit_models_pb2.SpeakerInfo, _Mapping]]
        ] = ...,
    ) -> None: ...

class StreamStateInfo(_message.Message):
    __slots__ = ["participant_sid", "state", "track_sid"]
    PARTICIPANT_SID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRACK_SID_FIELD_NUMBER: _ClassVar[int]
    participant_sid: str
    state: StreamState
    track_sid: str
    def __init__(
        self,
        participant_sid: _Optional[str] = ...,
        track_sid: _Optional[str] = ...,
        state: _Optional[_Union[StreamState, str]] = ...,
    ) -> None: ...

class StreamStateUpdate(_message.Message):
    __slots__ = ["stream_states"]
    STREAM_STATES_FIELD_NUMBER: _ClassVar[int]
    stream_states: _containers.RepeatedCompositeFieldContainer[StreamStateInfo]
    def __init__(
        self,
        stream_states: _Optional[_Iterable[_Union[StreamStateInfo, _Mapping]]] = ...,
    ) -> None: ...

class SubscribedCodec(_message.Message):
    __slots__ = ["codec", "qualities"]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    QUALITIES_FIELD_NUMBER: _ClassVar[int]
    codec: str
    qualities: _containers.RepeatedCompositeFieldContainer[SubscribedQuality]
    def __init__(
        self,
        codec: _Optional[str] = ...,
        qualities: _Optional[_Iterable[_Union[SubscribedQuality, _Mapping]]] = ...,
    ) -> None: ...

class SubscribedQuality(_message.Message):
    __slots__ = ["enabled", "quality"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    quality: _livekit_models_pb2.VideoQuality
    def __init__(
        self,
        quality: _Optional[_Union[_livekit_models_pb2.VideoQuality, str]] = ...,
        enabled: bool = ...,
    ) -> None: ...

class SubscribedQualityUpdate(_message.Message):
    __slots__ = ["subscribed_codecs", "subscribed_qualities", "track_sid"]
    SUBSCRIBED_CODECS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_QUALITIES_FIELD_NUMBER: _ClassVar[int]
    TRACK_SID_FIELD_NUMBER: _ClassVar[int]
    subscribed_codecs: _containers.RepeatedCompositeFieldContainer[SubscribedCodec]
    subscribed_qualities: _containers.RepeatedCompositeFieldContainer[SubscribedQuality]
    track_sid: str
    def __init__(
        self,
        track_sid: _Optional[str] = ...,
        subscribed_qualities: _Optional[
            _Iterable[_Union[SubscribedQuality, _Mapping]]
        ] = ...,
        subscribed_codecs: _Optional[
            _Iterable[_Union[SubscribedCodec, _Mapping]]
        ] = ...,
    ) -> None: ...

class SubscriptionPermission(_message.Message):
    __slots__ = ["all_participants", "track_permissions"]
    ALL_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    TRACK_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    all_participants: bool
    track_permissions: _containers.RepeatedCompositeFieldContainer[TrackPermission]
    def __init__(
        self,
        all_participants: bool = ...,
        track_permissions: _Optional[
            _Iterable[_Union[TrackPermission, _Mapping]]
        ] = ...,
    ) -> None: ...

class SubscriptionPermissionUpdate(_message.Message):
    __slots__ = ["allowed", "participant_sid", "track_sid"]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_SID_FIELD_NUMBER: _ClassVar[int]
    TRACK_SID_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    participant_sid: str
    track_sid: str
    def __init__(
        self,
        participant_sid: _Optional[str] = ...,
        track_sid: _Optional[str] = ...,
        allowed: bool = ...,
    ) -> None: ...

class SyncState(_message.Message):
    __slots__ = ["answer", "data_channels", "offer", "publish_tracks", "subscription"]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TRACKS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    answer: SessionDescription
    data_channels: _containers.RepeatedCompositeFieldContainer[DataChannelInfo]
    offer: SessionDescription
    publish_tracks: _containers.RepeatedCompositeFieldContainer[TrackPublishedResponse]
    subscription: UpdateSubscription
    def __init__(
        self,
        answer: _Optional[_Union[SessionDescription, _Mapping]] = ...,
        subscription: _Optional[_Union[UpdateSubscription, _Mapping]] = ...,
        publish_tracks: _Optional[
            _Iterable[_Union[TrackPublishedResponse, _Mapping]]
        ] = ...,
        data_channels: _Optional[_Iterable[_Union[DataChannelInfo, _Mapping]]] = ...,
        offer: _Optional[_Union[SessionDescription, _Mapping]] = ...,
    ) -> None: ...

class TrackPermission(_message.Message):
    __slots__ = ["all_tracks", "participant_identity", "participant_sid", "track_sids"]
    ALL_TRACKS_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_SID_FIELD_NUMBER: _ClassVar[int]
    TRACK_SIDS_FIELD_NUMBER: _ClassVar[int]
    all_tracks: bool
    participant_identity: str
    participant_sid: str
    track_sids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        participant_sid: _Optional[str] = ...,
        all_tracks: bool = ...,
        track_sids: _Optional[_Iterable[str]] = ...,
        participant_identity: _Optional[str] = ...,
    ) -> None: ...

class TrackPublishedResponse(_message.Message):
    __slots__ = ["cid", "track"]
    CID_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    cid: str
    track: _livekit_models_pb2.TrackInfo
    def __init__(
        self,
        cid: _Optional[str] = ...,
        track: _Optional[_Union[_livekit_models_pb2.TrackInfo, _Mapping]] = ...,
    ) -> None: ...

class TrackUnpublishedResponse(_message.Message):
    __slots__ = ["track_sid"]
    TRACK_SID_FIELD_NUMBER: _ClassVar[int]
    track_sid: str
    def __init__(self, track_sid: _Optional[str] = ...) -> None: ...

class TrickleRequest(_message.Message):
    __slots__ = ["candidateInit", "target"]
    CANDIDATEINIT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    candidateInit: str
    target: SignalTarget
    def __init__(
        self,
        candidateInit: _Optional[str] = ...,
        target: _Optional[_Union[SignalTarget, str]] = ...,
    ) -> None: ...

class UpdateParticipantMetadata(_message.Message):
    __slots__ = ["metadata", "name"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    metadata: str
    name: str
    def __init__(
        self, metadata: _Optional[str] = ..., name: _Optional[str] = ...
    ) -> None: ...

class UpdateSubscription(_message.Message):
    __slots__ = ["participant_tracks", "subscribe", "track_sids"]
    PARTICIPANT_TRACKS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    TRACK_SIDS_FIELD_NUMBER: _ClassVar[int]
    participant_tracks: _containers.RepeatedCompositeFieldContainer[
        _livekit_models_pb2.ParticipantTracks
    ]
    subscribe: bool
    track_sids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        track_sids: _Optional[_Iterable[str]] = ...,
        subscribe: bool = ...,
        participant_tracks: _Optional[
            _Iterable[_Union[_livekit_models_pb2.ParticipantTracks, _Mapping]]
        ] = ...,
    ) -> None: ...

class UpdateTrackSettings(_message.Message):
    __slots__ = [
        "disabled",
        "fps",
        "height",
        "priority",
        "quality",
        "track_sids",
        "width",
    ]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    TRACK_SIDS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    fps: int
    height: int
    priority: int
    quality: _livekit_models_pb2.VideoQuality
    track_sids: _containers.RepeatedScalarFieldContainer[str]
    width: int
    def __init__(
        self,
        track_sids: _Optional[_Iterable[str]] = ...,
        disabled: bool = ...,
        quality: _Optional[_Union[_livekit_models_pb2.VideoQuality, str]] = ...,
        width: _Optional[int] = ...,
        height: _Optional[int] = ...,
        fps: _Optional[int] = ...,
        priority: _Optional[int] = ...,
    ) -> None: ...

class UpdateVideoLayers(_message.Message):
    __slots__ = ["layers", "track_sid"]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    TRACK_SID_FIELD_NUMBER: _ClassVar[int]
    layers: _containers.RepeatedCompositeFieldContainer[_livekit_models_pb2.VideoLayer]
    track_sid: str
    def __init__(
        self,
        track_sid: _Optional[str] = ...,
        layers: _Optional[
            _Iterable[_Union[_livekit_models_pb2.VideoLayer, _Mapping]]
        ] = ...,
    ) -> None: ...

class SignalTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class StreamState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CandidateProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
