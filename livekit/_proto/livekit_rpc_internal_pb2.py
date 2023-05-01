# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: livekit_rpc_internal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import livekit_egress_pb2 as livekit__egress__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1alivekit_rpc_internal.proto\x12\x07livekit\x1a\x14livekit_egress.proto"\xf6\x02\n\x12StartEgressRequest\x12\x11\n\tegress_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x11\n\tsender_id\x18\n \x01(\t\x12\x0f\n\x07sent_at\x18\x04 \x01(\x03\x12=\n\x0eroom_composite\x18\x05 \x01(\x0b\x32#.livekit.RoomCompositeEgressRequestH\x00\x12?\n\x0ftrack_composite\x18\x06 \x01(\x0b\x32$.livekit.TrackCompositeEgressRequestH\x00\x12,\n\x05track\x18\x07 \x01(\x0b\x32\x1b.livekit.TrackEgressRequestH\x00\x12(\n\x03web\x18\x0b \x01(\x0b\x32\x19.livekit.WebEgressRequestH\x00\x12\x0f\n\x07room_id\x18\x03 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0e\n\x06ws_url\x18\t \x01(\t:\x02\x18\x01\x42\t\n\x07request"\xbb\x01\n\rEgressRequest\x12\x11\n\tegress_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x11\n\tsender_id\x18\x05 \x01(\t\x12\x35\n\rupdate_stream\x18\x03 \x01(\x0b\x32\x1c.livekit.UpdateStreamRequestH\x00\x12*\n\x04stop\x18\x04 \x01(\x0b\x32\x1a.livekit.StopEgressRequestH\x00:\x02\x18\x01\x42\t\n\x07request"Z\n\x0e\x45gressResponse\x12!\n\x04info\x18\x01 \x01(\x0b\x32\x13.livekit.EgressInfo\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x12\n\nrequest_id\x18\x03 \x01(\t:\x02\x18\x01\x42\x46Z#github.com/livekit/protocol/livekit\xaa\x02\rLiveKit.Proto\xea\x02\x0eLiveKit::Protob\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "livekit_rpc_internal_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z#github.com/livekit/protocol/livekit\252\002\rLiveKit.Proto\352\002\016LiveKit::Proto"
    _STARTEGRESSREQUEST._options = None
    _STARTEGRESSREQUEST._serialized_options = b"\030\001"
    _EGRESSREQUEST._options = None
    _EGRESSREQUEST._serialized_options = b"\030\001"
    _EGRESSRESPONSE._options = None
    _EGRESSRESPONSE._serialized_options = b"\030\001"
    _STARTEGRESSREQUEST._serialized_start = 62
    _STARTEGRESSREQUEST._serialized_end = 436
    _EGRESSREQUEST._serialized_start = 439
    _EGRESSREQUEST._serialized_end = 626
    _EGRESSRESPONSE._serialized_start = 628
    _EGRESSRESPONSE._serialized_end = 718
# @@protoc_insertion_point(module_scope)