# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: livekit_models.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x14livekit_models.proto\x12\x07livekit"\xee\x01\n\x04Room\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rempty_timeout\x18\x03 \x01(\r\x12\x18\n\x10max_participants\x18\x04 \x01(\r\x12\x15\n\rcreation_time\x18\x05 \x01(\x03\x12\x15\n\rturn_password\x18\x06 \x01(\t\x12&\n\x0e\x65nabled_codecs\x18\x07 \x03(\x0b\x32\x0e.livekit.Codec\x12\x10\n\x08metadata\x18\x08 \x01(\t\x12\x18\n\x10num_participants\x18\t \x01(\r\x12\x18\n\x10\x61\x63tive_recording\x18\n \x01(\x08"(\n\x05\x43odec\x12\x0c\n\x04mime\x18\x01 \x01(\t\x12\x11\n\tfmtp_line\x18\x02 \x01(\t"\xa9\x02\n\x0fParticipantInfo\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12-\n\x05state\x18\x03 \x01(\x0e\x32\x1e.livekit.ParticipantInfo.State\x12"\n\x06tracks\x18\x04 \x03(\x0b\x32\x12.livekit.TrackInfo\x12\x10\n\x08metadata\x18\x05 \x01(\t\x12\x11\n\tjoined_at\x18\x06 \x01(\x03\x12\x0e\n\x06hidden\x18\x07 \x01(\x08\x12\x10\n\x08recorder\x18\x08 \x01(\x08\x12\x0c\n\x04name\x18\t \x01(\t\x12\x0f\n\x07version\x18\n \x01(\r">\n\x05State\x12\x0b\n\x07JOINING\x10\x00\x12\n\n\x06JOINED\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x10\n\x0c\x44ISCONNECTED\x10\x03"\x89\x02\n\tTrackInfo\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.livekit.TrackType\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05muted\x18\x04 \x01(\x08\x12\r\n\x05width\x18\x05 \x01(\r\x12\x0e\n\x06height\x18\x06 \x01(\r\x12\x11\n\tsimulcast\x18\x07 \x01(\x08\x12\x13\n\x0b\x64isable_dtx\x18\x08 \x01(\x08\x12$\n\x06source\x18\t \x01(\x0e\x32\x14.livekit.TrackSource\x12#\n\x06layers\x18\n \x03(\x0b\x32\x13.livekit.VideoLayer\x12\x11\n\tmime_type\x18\x0b \x01(\t\x12\x0b\n\x03mid\x18\x0c \x01(\t"r\n\nVideoLayer\x12&\n\x07quality\x18\x01 \x01(\x0e\x32\x15.livekit.VideoQuality\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\x0f\n\x07\x62itrate\x18\x04 \x01(\r\x12\x0c\n\x04ssrc\x18\x05 \x01(\r"\xb4\x01\n\nDataPacket\x12&\n\x04kind\x18\x01 \x01(\x0e\x32\x18.livekit.DataPacket.Kind\x12#\n\x04user\x18\x02 \x01(\x0b\x32\x13.livekit.UserPacketH\x00\x12/\n\x07speaker\x18\x03 \x01(\x0b\x32\x1c.livekit.ActiveSpeakerUpdateH\x00"\x1f\n\x04Kind\x12\x0c\n\x08RELIABLE\x10\x00\x12\t\n\x05LOSSY\x10\x01\x42\x07\n\x05value"=\n\x13\x41\x63tiveSpeakerUpdate\x12&\n\x08speakers\x18\x01 \x03(\x0b\x32\x14.livekit.SpeakerInfo"9\n\x0bSpeakerInfo\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\x02\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08"P\n\nUserPacket\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x18\n\x10\x64\x65stination_sids\x18\x03 \x03(\t"@\n\x11ParticipantTracks\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x12\n\ntrack_sids\x18\x02 \x03(\t"\x9a\x02\n\nClientInfo\x12$\n\x03sdk\x18\x01 \x01(\x0e\x32\x17.livekit.ClientInfo.SDK\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08protocol\x18\x03 \x01(\x05\x12\n\n\x02os\x18\x04 \x01(\t\x12\x12\n\nos_version\x18\x05 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x06 \x01(\t\x12\x0f\n\x07\x62rowser\x18\x07 \x01(\t\x12\x17\n\x0f\x62rowser_version\x18\x08 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\t \x01(\t"R\n\x03SDK\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02JS\x10\x01\x12\t\n\x05SWIFT\x10\x02\x12\x0b\n\x07\x41NDROID\x10\x03\x12\x0b\n\x07\x46LUTTER\x10\x04\x12\x06\n\x02GO\x10\x05\x12\t\n\x05UNITY\x10\x06*+\n\tTrackType\x12\t\n\x05\x41UDIO\x10\x00\x12\t\n\x05VIDEO\x10\x01\x12\x08\n\x04\x44\x41TA\x10\x02*`\n\x0bTrackSource\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43\x41MERA\x10\x01\x12\x0e\n\nMICROPHONE\x10\x02\x12\x10\n\x0cSCREEN_SHARE\x10\x03\x12\x16\n\x12SCREEN_SHARE_AUDIO\x10\x04*6\n\x0cVideoQuality\x12\x07\n\x03LOW\x10\x00\x12\n\n\x06MEDIUM\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\x07\n\x03OFF\x10\x03*6\n\x11\x43onnectionQuality\x12\x08\n\x04POOR\x10\x00\x12\x08\n\x04GOOD\x10\x01\x12\r\n\tEXCELLENT\x10\x02\x42\x46Z#github.com/livekit/protocol/livekit\xaa\x02\rLiveKit.Proto\xea\x02\x0eLiveKit::Protob\x06proto3'
)

_TRACKTYPE = DESCRIPTOR.enum_types_by_name["TrackType"]
TrackType = enum_type_wrapper.EnumTypeWrapper(_TRACKTYPE)
_TRACKSOURCE = DESCRIPTOR.enum_types_by_name["TrackSource"]
TrackSource = enum_type_wrapper.EnumTypeWrapper(_TRACKSOURCE)
_VIDEOQUALITY = DESCRIPTOR.enum_types_by_name["VideoQuality"]
VideoQuality = enum_type_wrapper.EnumTypeWrapper(_VIDEOQUALITY)
_CONNECTIONQUALITY = DESCRIPTOR.enum_types_by_name["ConnectionQuality"]
ConnectionQuality = enum_type_wrapper.EnumTypeWrapper(_CONNECTIONQUALITY)
AUDIO = 0
VIDEO = 1
DATA = 2
UNKNOWN = 0
CAMERA = 1
MICROPHONE = 2
SCREEN_SHARE = 3
SCREEN_SHARE_AUDIO = 4
LOW = 0
MEDIUM = 1
HIGH = 2
OFF = 3
POOR = 0
GOOD = 1
EXCELLENT = 2


_ROOM = DESCRIPTOR.message_types_by_name["Room"]
_CODEC = DESCRIPTOR.message_types_by_name["Codec"]
_PARTICIPANTINFO = DESCRIPTOR.message_types_by_name["ParticipantInfo"]
_TRACKINFO = DESCRIPTOR.message_types_by_name["TrackInfo"]
_VIDEOLAYER = DESCRIPTOR.message_types_by_name["VideoLayer"]
_DATAPACKET = DESCRIPTOR.message_types_by_name["DataPacket"]
_ACTIVESPEAKERUPDATE = DESCRIPTOR.message_types_by_name["ActiveSpeakerUpdate"]
_SPEAKERINFO = DESCRIPTOR.message_types_by_name["SpeakerInfo"]
_USERPACKET = DESCRIPTOR.message_types_by_name["UserPacket"]
_PARTICIPANTTRACKS = DESCRIPTOR.message_types_by_name["ParticipantTracks"]
_CLIENTINFO = DESCRIPTOR.message_types_by_name["ClientInfo"]
_PARTICIPANTINFO_STATE = _PARTICIPANTINFO.enum_types_by_name["State"]
_DATAPACKET_KIND = _DATAPACKET.enum_types_by_name["Kind"]
_CLIENTINFO_SDK = _CLIENTINFO.enum_types_by_name["SDK"]
Room = _reflection.GeneratedProtocolMessageType(
    "Room",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROOM,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.Room)
    },
)
_sym_db.RegisterMessage(Room)

Codec = _reflection.GeneratedProtocolMessageType(
    "Codec",
    (_message.Message,),
    {
        "DESCRIPTOR": _CODEC,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.Codec)
    },
)
_sym_db.RegisterMessage(Codec)

ParticipantInfo = _reflection.GeneratedProtocolMessageType(
    "ParticipantInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARTICIPANTINFO,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.ParticipantInfo)
    },
)
_sym_db.RegisterMessage(ParticipantInfo)

TrackInfo = _reflection.GeneratedProtocolMessageType(
    "TrackInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACKINFO,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.TrackInfo)
    },
)
_sym_db.RegisterMessage(TrackInfo)

VideoLayer = _reflection.GeneratedProtocolMessageType(
    "VideoLayer",
    (_message.Message,),
    {
        "DESCRIPTOR": _VIDEOLAYER,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.VideoLayer)
    },
)
_sym_db.RegisterMessage(VideoLayer)

DataPacket = _reflection.GeneratedProtocolMessageType(
    "DataPacket",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATAPACKET,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.DataPacket)
    },
)
_sym_db.RegisterMessage(DataPacket)

ActiveSpeakerUpdate = _reflection.GeneratedProtocolMessageType(
    "ActiveSpeakerUpdate",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACTIVESPEAKERUPDATE,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.ActiveSpeakerUpdate)
    },
)
_sym_db.RegisterMessage(ActiveSpeakerUpdate)

SpeakerInfo = _reflection.GeneratedProtocolMessageType(
    "SpeakerInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _SPEAKERINFO,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.SpeakerInfo)
    },
)
_sym_db.RegisterMessage(SpeakerInfo)

UserPacket = _reflection.GeneratedProtocolMessageType(
    "UserPacket",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERPACKET,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.UserPacket)
    },
)
_sym_db.RegisterMessage(UserPacket)

ParticipantTracks = _reflection.GeneratedProtocolMessageType(
    "ParticipantTracks",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARTICIPANTTRACKS,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.ParticipantTracks)
    },
)
_sym_db.RegisterMessage(ParticipantTracks)

ClientInfo = _reflection.GeneratedProtocolMessageType(
    "ClientInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLIENTINFO,
        "__module__": "livekit_models_pb2"
        # @@protoc_insertion_point(class_scope:livekit.ClientInfo)
    },
)
_sym_db.RegisterMessage(ClientInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z#github.com/livekit/protocol/livekit\252\002\rLiveKit.Proto\352\002\016LiveKit::Proto"
    _TRACKTYPE._serialized_start = 1738
    _TRACKTYPE._serialized_end = 1781
    _TRACKSOURCE._serialized_start = 1783
    _TRACKSOURCE._serialized_end = 1879
    _VIDEOQUALITY._serialized_start = 1881
    _VIDEOQUALITY._serialized_end = 1935
    _CONNECTIONQUALITY._serialized_start = 1937
    _CONNECTIONQUALITY._serialized_end = 1991
    _ROOM._serialized_start = 34
    _ROOM._serialized_end = 272
    _CODEC._serialized_start = 274
    _CODEC._serialized_end = 314
    _PARTICIPANTINFO._serialized_start = 317
    _PARTICIPANTINFO._serialized_end = 614
    _PARTICIPANTINFO_STATE._serialized_start = 552
    _PARTICIPANTINFO_STATE._serialized_end = 614
    _TRACKINFO._serialized_start = 617
    _TRACKINFO._serialized_end = 882
    _VIDEOLAYER._serialized_start = 884
    _VIDEOLAYER._serialized_end = 998
    _DATAPACKET._serialized_start = 1001
    _DATAPACKET._serialized_end = 1181
    _DATAPACKET_KIND._serialized_start = 1141
    _DATAPACKET_KIND._serialized_end = 1172
    _ACTIVESPEAKERUPDATE._serialized_start = 1183
    _ACTIVESPEAKERUPDATE._serialized_end = 1244
    _SPEAKERINFO._serialized_start = 1246
    _SPEAKERINFO._serialized_end = 1303
    _USERPACKET._serialized_start = 1305
    _USERPACKET._serialized_end = 1385
    _PARTICIPANTTRACKS._serialized_start = 1387
    _PARTICIPANTTRACKS._serialized_end = 1451
    _CLIENTINFO._serialized_start = 1454
    _CLIENTINFO._serialized_end = 1736
    _CLIENTINFO_SDK._serialized_start = 1654
    _CLIENTINFO_SDK._serialized_end = 1736
# @@protoc_insertion_point(module_scope)
