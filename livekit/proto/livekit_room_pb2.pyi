from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import livekit_egress_pb2 as _livekit_egress_pb2
import livekit_models_pb2 as _livekit_models_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRoomRequest(_message.Message):
    __slots__ = [
        "egress",
        "empty_timeout",
        "max_participants",
        "metadata",
        "name",
        "node_id",
    ]
    EGRESS_FIELD_NUMBER: _ClassVar[int]
    EMPTY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    egress: RoomEgress
    empty_timeout: int
    max_participants: int
    metadata: str
    name: str
    node_id: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        empty_timeout: _Optional[int] = ...,
        max_participants: _Optional[int] = ...,
        node_id: _Optional[str] = ...,
        metadata: _Optional[str] = ...,
        egress: _Optional[_Union[RoomEgress, _Mapping]] = ...,
    ) -> None: ...

class DeleteRoomRequest(_message.Message):
    __slots__ = ["room"]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    room: str
    def __init__(self, room: _Optional[str] = ...) -> None: ...

class DeleteRoomResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListParticipantsRequest(_message.Message):
    __slots__ = ["room"]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    room: str
    def __init__(self, room: _Optional[str] = ...) -> None: ...

class ListParticipantsResponse(_message.Message):
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

class ListRoomsRequest(_message.Message):
    __slots__ = ["names"]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...

class ListRoomsResponse(_message.Message):
    __slots__ = ["rooms"]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    rooms: _containers.RepeatedCompositeFieldContainer[_livekit_models_pb2.Room]
    def __init__(
        self,
        rooms: _Optional[_Iterable[_Union[_livekit_models_pb2.Room, _Mapping]]] = ...,
    ) -> None: ...

class MuteRoomTrackRequest(_message.Message):
    __slots__ = ["identity", "muted", "room", "track_sid"]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    TRACK_SID_FIELD_NUMBER: _ClassVar[int]
    identity: str
    muted: bool
    room: str
    track_sid: str
    def __init__(
        self,
        room: _Optional[str] = ...,
        identity: _Optional[str] = ...,
        track_sid: _Optional[str] = ...,
        muted: bool = ...,
    ) -> None: ...

class MuteRoomTrackResponse(_message.Message):
    __slots__ = ["track"]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    track: _livekit_models_pb2.TrackInfo
    def __init__(
        self, track: _Optional[_Union[_livekit_models_pb2.TrackInfo, _Mapping]] = ...
    ) -> None: ...

class RemoveParticipantResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RoomEgress(_message.Message):
    __slots__ = ["room", "tracks"]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    room: _livekit_egress_pb2.RoomCompositeEgressRequest
    tracks: _livekit_egress_pb2.AutoTrackEgress
    def __init__(
        self,
        room: _Optional[
            _Union[_livekit_egress_pb2.RoomCompositeEgressRequest, _Mapping]
        ] = ...,
        tracks: _Optional[_Union[_livekit_egress_pb2.AutoTrackEgress, _Mapping]] = ...,
    ) -> None: ...

class RoomParticipantIdentity(_message.Message):
    __slots__ = ["identity", "room"]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    identity: str
    room: str
    def __init__(
        self, room: _Optional[str] = ..., identity: _Optional[str] = ...
    ) -> None: ...

class SendDataRequest(_message.Message):
    __slots__ = ["data", "destination_sids", "kind", "room", "topic"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_SIDS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    destination_sids: _containers.RepeatedScalarFieldContainer[str]
    kind: _livekit_models_pb2.DataPacket.Kind
    room: str
    topic: str
    def __init__(
        self,
        room: _Optional[str] = ...,
        data: _Optional[bytes] = ...,
        kind: _Optional[_Union[_livekit_models_pb2.DataPacket.Kind, str]] = ...,
        destination_sids: _Optional[_Iterable[str]] = ...,
        topic: _Optional[str] = ...,
    ) -> None: ...

class SendDataResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateParticipantRequest(_message.Message):
    __slots__ = ["identity", "metadata", "name", "permission", "room"]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    identity: str
    metadata: str
    name: str
    permission: _livekit_models_pb2.ParticipantPermission
    room: str
    def __init__(
        self,
        room: _Optional[str] = ...,
        identity: _Optional[str] = ...,
        metadata: _Optional[str] = ...,
        permission: _Optional[
            _Union[_livekit_models_pb2.ParticipantPermission, _Mapping]
        ] = ...,
        name: _Optional[str] = ...,
    ) -> None: ...

class UpdateRoomMetadataRequest(_message.Message):
    __slots__ = ["metadata", "room"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    metadata: str
    room: str
    def __init__(
        self, room: _Optional[str] = ..., metadata: _Optional[str] = ...
    ) -> None: ...

class UpdateSubscriptionsRequest(_message.Message):
    __slots__ = ["identity", "participant_tracks", "room", "subscribe", "track_sids"]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_TRACKS_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    TRACK_SIDS_FIELD_NUMBER: _ClassVar[int]
    identity: str
    participant_tracks: _containers.RepeatedCompositeFieldContainer[
        _livekit_models_pb2.ParticipantTracks
    ]
    room: str
    subscribe: bool
    track_sids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        room: _Optional[str] = ...,
        identity: _Optional[str] = ...,
        track_sids: _Optional[_Iterable[str]] = ...,
        subscribe: bool = ...,
        participant_tracks: _Optional[
            _Iterable[_Union[_livekit_models_pb2.ParticipantTracks, _Mapping]]
        ] = ...,
    ) -> None: ...

class UpdateSubscriptionsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
