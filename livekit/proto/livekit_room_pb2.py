# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: livekit_room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import livekit_models_pb2 as livekit__models__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x12livekit_room.proto\x12\x07livekit\x1a\x14livekit_models.proto"u\n\x11\x43reateRoomRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rempty_timeout\x18\x02 \x01(\r\x12\x18\n\x10max_participants\x18\x03 \x01(\r\x12\x0f\n\x07node_id\x18\x04 \x01(\t\x12\x10\n\x08metadata\x18\x05 \x01(\t"!\n\x10ListRoomsRequest\x12\r\n\x05names\x18\x01 \x03(\t"1\n\x11ListRoomsResponse\x12\x1c\n\x05rooms\x18\x01 \x03(\x0b\x32\r.livekit.Room"!\n\x11\x44\x65leteRoomRequest\x12\x0c\n\x04room\x18\x01 \x01(\t"\x14\n\x12\x44\x65leteRoomResponse"\'\n\x17ListParticipantsRequest\x12\x0c\n\x04room\x18\x01 \x01(\t"J\n\x18ListParticipantsResponse\x12.\n\x0cparticipants\x18\x01 \x03(\x0b\x32\x18.livekit.ParticipantInfo"9\n\x17RoomParticipantIdentity\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t"\x1b\n\x19RemoveParticipantResponse"X\n\x14MuteRoomTrackRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x11\n\ttrack_sid\x18\x03 \x01(\t\x12\r\n\x05muted\x18\x04 \x01(\x08":\n\x15MuteRoomTrackResponse\x12!\n\x05track\x18\x01 \x01(\x0b\x32\x12.livekit.TrackInfo"]\n\x15ParticipantPermission\x12\x15\n\rcan_subscribe\x18\x01 \x01(\x08\x12\x13\n\x0b\x63\x61n_publish\x18\x02 \x01(\x08\x12\x18\n\x10\x63\x61n_publish_data\x18\x03 \x01(\x08"\x80\x01\n\x18UpdateParticipantRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\t\x12\x32\n\npermission\x18\x04 \x01(\x0b\x32\x1e.livekit.ParticipantPermission"\x9b\x01\n\x1aUpdateSubscriptionsRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x12\n\ntrack_sids\x18\x03 \x03(\t\x12\x11\n\tsubscribe\x18\x04 \x01(\x08\x12\x36\n\x12participant_tracks\x18\x05 \x03(\x0b\x32\x1a.livekit.ParticipantTracks"\x1d\n\x1bUpdateSubscriptionsResponse"o\n\x0fSendDataRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12&\n\x04kind\x18\x03 \x01(\x0e\x32\x18.livekit.DataPacket.Kind\x12\x18\n\x10\x64\x65stination_sids\x18\x04 \x03(\t"\x12\n\x10SendDataResponse";\n\x19UpdateRoomMetadataRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08metadata\x18\x02 \x01(\t2\xe6\x06\n\x0bRoomService\x12\x37\n\nCreateRoom\x12\x1a.livekit.CreateRoomRequest\x1a\r.livekit.Room\x12\x42\n\tListRooms\x12\x19.livekit.ListRoomsRequest\x1a\x1a.livekit.ListRoomsResponse\x12\x45\n\nDeleteRoom\x12\x1a.livekit.DeleteRoomRequest\x1a\x1b.livekit.DeleteRoomResponse\x12W\n\x10ListParticipants\x12 .livekit.ListParticipantsRequest\x1a!.livekit.ListParticipantsResponse\x12L\n\x0eGetParticipant\x12 .livekit.RoomParticipantIdentity\x1a\x18.livekit.ParticipantInfo\x12Y\n\x11RemoveParticipant\x12 .livekit.RoomParticipantIdentity\x1a".livekit.RemoveParticipantResponse\x12S\n\x12MutePublishedTrack\x12\x1d.livekit.MuteRoomTrackRequest\x1a\x1e.livekit.MuteRoomTrackResponse\x12P\n\x11UpdateParticipant\x12!.livekit.UpdateParticipantRequest\x1a\x18.livekit.ParticipantInfo\x12`\n\x13UpdateSubscriptions\x12#.livekit.UpdateSubscriptionsRequest\x1a$.livekit.UpdateSubscriptionsResponse\x12?\n\x08SendData\x12\x18.livekit.SendDataRequest\x1a\x19.livekit.SendDataResponse\x12G\n\x12UpdateRoomMetadata\x12".livekit.UpdateRoomMetadataRequest\x1a\r.livekit.RoomBFZ#github.com/livekit/protocol/livekit\xaa\x02\rLiveKit.Proto\xea\x02\x0eLiveKit::Protob\x06proto3'
)


_CREATEROOMREQUEST = DESCRIPTOR.message_types_by_name["CreateRoomRequest"]
_LISTROOMSREQUEST = DESCRIPTOR.message_types_by_name["ListRoomsRequest"]
_LISTROOMSRESPONSE = DESCRIPTOR.message_types_by_name["ListRoomsResponse"]
_DELETEROOMREQUEST = DESCRIPTOR.message_types_by_name["DeleteRoomRequest"]
_DELETEROOMRESPONSE = DESCRIPTOR.message_types_by_name["DeleteRoomResponse"]
_LISTPARTICIPANTSREQUEST = DESCRIPTOR.message_types_by_name["ListParticipantsRequest"]
_LISTPARTICIPANTSRESPONSE = DESCRIPTOR.message_types_by_name["ListParticipantsResponse"]
_ROOMPARTICIPANTIDENTITY = DESCRIPTOR.message_types_by_name["RoomParticipantIdentity"]
_REMOVEPARTICIPANTRESPONSE = DESCRIPTOR.message_types_by_name[
    "RemoveParticipantResponse"
]
_MUTEROOMTRACKREQUEST = DESCRIPTOR.message_types_by_name["MuteRoomTrackRequest"]
_MUTEROOMTRACKRESPONSE = DESCRIPTOR.message_types_by_name["MuteRoomTrackResponse"]
_PARTICIPANTPERMISSION = DESCRIPTOR.message_types_by_name["ParticipantPermission"]
_UPDATEPARTICIPANTREQUEST = DESCRIPTOR.message_types_by_name["UpdateParticipantRequest"]
_UPDATESUBSCRIPTIONSREQUEST = DESCRIPTOR.message_types_by_name[
    "UpdateSubscriptionsRequest"
]
_UPDATESUBSCRIPTIONSRESPONSE = DESCRIPTOR.message_types_by_name[
    "UpdateSubscriptionsResponse"
]
_SENDDATAREQUEST = DESCRIPTOR.message_types_by_name["SendDataRequest"]
_SENDDATARESPONSE = DESCRIPTOR.message_types_by_name["SendDataResponse"]
_UPDATEROOMMETADATAREQUEST = DESCRIPTOR.message_types_by_name[
    "UpdateRoomMetadataRequest"
]
CreateRoomRequest = _reflection.GeneratedProtocolMessageType(
    "CreateRoomRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEROOMREQUEST,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.CreateRoomRequest)
    },
)
_sym_db.RegisterMessage(CreateRoomRequest)

ListRoomsRequest = _reflection.GeneratedProtocolMessageType(
    "ListRoomsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTROOMSREQUEST,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.ListRoomsRequest)
    },
)
_sym_db.RegisterMessage(ListRoomsRequest)

ListRoomsResponse = _reflection.GeneratedProtocolMessageType(
    "ListRoomsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTROOMSRESPONSE,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.ListRoomsResponse)
    },
)
_sym_db.RegisterMessage(ListRoomsResponse)

DeleteRoomRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteRoomRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEROOMREQUEST,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.DeleteRoomRequest)
    },
)
_sym_db.RegisterMessage(DeleteRoomRequest)

DeleteRoomResponse = _reflection.GeneratedProtocolMessageType(
    "DeleteRoomResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEROOMRESPONSE,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.DeleteRoomResponse)
    },
)
_sym_db.RegisterMessage(DeleteRoomResponse)

ListParticipantsRequest = _reflection.GeneratedProtocolMessageType(
    "ListParticipantsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTPARTICIPANTSREQUEST,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.ListParticipantsRequest)
    },
)
_sym_db.RegisterMessage(ListParticipantsRequest)

ListParticipantsResponse = _reflection.GeneratedProtocolMessageType(
    "ListParticipantsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTPARTICIPANTSRESPONSE,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.ListParticipantsResponse)
    },
)
_sym_db.RegisterMessage(ListParticipantsResponse)

RoomParticipantIdentity = _reflection.GeneratedProtocolMessageType(
    "RoomParticipantIdentity",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROOMPARTICIPANTIDENTITY,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.RoomParticipantIdentity)
    },
)
_sym_db.RegisterMessage(RoomParticipantIdentity)

RemoveParticipantResponse = _reflection.GeneratedProtocolMessageType(
    "RemoveParticipantResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _REMOVEPARTICIPANTRESPONSE,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.RemoveParticipantResponse)
    },
)
_sym_db.RegisterMessage(RemoveParticipantResponse)

MuteRoomTrackRequest = _reflection.GeneratedProtocolMessageType(
    "MuteRoomTrackRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _MUTEROOMTRACKREQUEST,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.MuteRoomTrackRequest)
    },
)
_sym_db.RegisterMessage(MuteRoomTrackRequest)

MuteRoomTrackResponse = _reflection.GeneratedProtocolMessageType(
    "MuteRoomTrackResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MUTEROOMTRACKRESPONSE,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.MuteRoomTrackResponse)
    },
)
_sym_db.RegisterMessage(MuteRoomTrackResponse)

ParticipantPermission = _reflection.GeneratedProtocolMessageType(
    "ParticipantPermission",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARTICIPANTPERMISSION,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.ParticipantPermission)
    },
)
_sym_db.RegisterMessage(ParticipantPermission)

UpdateParticipantRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateParticipantRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEPARTICIPANTREQUEST,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.UpdateParticipantRequest)
    },
)
_sym_db.RegisterMessage(UpdateParticipantRequest)

UpdateSubscriptionsRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateSubscriptionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATESUBSCRIPTIONSREQUEST,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.UpdateSubscriptionsRequest)
    },
)
_sym_db.RegisterMessage(UpdateSubscriptionsRequest)

UpdateSubscriptionsResponse = _reflection.GeneratedProtocolMessageType(
    "UpdateSubscriptionsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATESUBSCRIPTIONSRESPONSE,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.UpdateSubscriptionsResponse)
    },
)
_sym_db.RegisterMessage(UpdateSubscriptionsResponse)

SendDataRequest = _reflection.GeneratedProtocolMessageType(
    "SendDataRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SENDDATAREQUEST,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.SendDataRequest)
    },
)
_sym_db.RegisterMessage(SendDataRequest)

SendDataResponse = _reflection.GeneratedProtocolMessageType(
    "SendDataResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SENDDATARESPONSE,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.SendDataResponse)
    },
)
_sym_db.RegisterMessage(SendDataResponse)

UpdateRoomMetadataRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateRoomMetadataRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEROOMMETADATAREQUEST,
        "__module__": "livekit_room_pb2"
        # @@protoc_insertion_point(class_scope:livekit.UpdateRoomMetadataRequest)
    },
)
_sym_db.RegisterMessage(UpdateRoomMetadataRequest)

_ROOMSERVICE = DESCRIPTOR.services_by_name["RoomService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z#github.com/livekit/protocol/livekit\252\002\rLiveKit.Proto\352\002\016LiveKit::Proto"
    _CREATEROOMREQUEST._serialized_start = 53
    _CREATEROOMREQUEST._serialized_end = 170
    _LISTROOMSREQUEST._serialized_start = 172
    _LISTROOMSREQUEST._serialized_end = 205
    _LISTROOMSRESPONSE._serialized_start = 207
    _LISTROOMSRESPONSE._serialized_end = 256
    _DELETEROOMREQUEST._serialized_start = 258
    _DELETEROOMREQUEST._serialized_end = 291
    _DELETEROOMRESPONSE._serialized_start = 293
    _DELETEROOMRESPONSE._serialized_end = 313
    _LISTPARTICIPANTSREQUEST._serialized_start = 315
    _LISTPARTICIPANTSREQUEST._serialized_end = 354
    _LISTPARTICIPANTSRESPONSE._serialized_start = 356
    _LISTPARTICIPANTSRESPONSE._serialized_end = 430
    _ROOMPARTICIPANTIDENTITY._serialized_start = 432
    _ROOMPARTICIPANTIDENTITY._serialized_end = 489
    _REMOVEPARTICIPANTRESPONSE._serialized_start = 491
    _REMOVEPARTICIPANTRESPONSE._serialized_end = 518
    _MUTEROOMTRACKREQUEST._serialized_start = 520
    _MUTEROOMTRACKREQUEST._serialized_end = 608
    _MUTEROOMTRACKRESPONSE._serialized_start = 610
    _MUTEROOMTRACKRESPONSE._serialized_end = 668
    _PARTICIPANTPERMISSION._serialized_start = 670
    _PARTICIPANTPERMISSION._serialized_end = 763
    _UPDATEPARTICIPANTREQUEST._serialized_start = 766
    _UPDATEPARTICIPANTREQUEST._serialized_end = 894
    _UPDATESUBSCRIPTIONSREQUEST._serialized_start = 897
    _UPDATESUBSCRIPTIONSREQUEST._serialized_end = 1052
    _UPDATESUBSCRIPTIONSRESPONSE._serialized_start = 1054
    _UPDATESUBSCRIPTIONSRESPONSE._serialized_end = 1083
    _SENDDATAREQUEST._serialized_start = 1085
    _SENDDATAREQUEST._serialized_end = 1196
    _SENDDATARESPONSE._serialized_start = 1198
    _SENDDATARESPONSE._serialized_end = 1216
    _UPDATEROOMMETADATAREQUEST._serialized_start = 1218
    _UPDATEROOMMETADATAREQUEST._serialized_end = 1277
    _ROOMSERVICE._serialized_start = 1280
    _ROOMSERVICE._serialized_end = 2150
# @@protoc_insertion_point(module_scope)
