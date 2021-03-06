# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc.proto',
  package='grpc_defs',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ngrpc.proto\x12\tgrpc_defs\"\x1b\n\rLockDataRefId\x12\n\n\x02id\x18\x01 \x01(\x04\"\x07\n\x05\x45mpty\"A\n\x0bReadRequest\x12%\n\x03txn\x18\x01 \x01(\x0b\x32\x18.grpc_defs.LockDataRefId\x12\x0b\n\x03key\x18\x02 \x01(\t\" \n\x02KV\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"P\n\x0cWriteRequest\x12%\n\x03txn\x18\x01 \x01(\x0b\x32\x18.grpc_defs.LockDataRefId\x12\x19\n\x02kv\x18\x02 \x01(\x0b\x32\r.grpc_defs.KV\".\n\x05Value\x12\r\n\x03val\x18\x01 \x01(\tH\x00\x12\x0f\n\x05\x65rror\x18\x02 \x01(\tH\x00\x42\x05\n\x03res\"2\n\nWriteError\x12\x0f\n\x05\x65rror\x18\x01 \x01(\tH\x00\x12\x0c\n\x02ok\x18\x02 \x01(\tH\x00\x42\x05\n\x03res\"*\n\x0cKVCollection\x12\x1a\n\x03val\x18\x01 \x03(\x0b\x32\r.grpc_defs.KV\"M\n\x0bValueRanged\x12&\n\x03val\x18\x01 \x01(\x0b\x32\x17.grpc_defs.KVCollectionH\x00\x12\x0f\n\x05\x65rror\x18\x02 \x01(\tH\x00\x42\x05\n\x03res\"\x15\n\x04Json\x12\r\n\x05inner\x18\x01 \x01(\t\"g\n\x10JsonWriteRequest\x12%\n\x03txn\x18\x01 \x01(\x0b\x32\x18.grpc_defs.LockDataRefId\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x1e\n\x05value\x18\x03 \x01(\x0b\x32\x0f.grpc_defs.Json2\xef\x02\n\nReplicator\x12;\n\rnew_with_time\x12\x18.grpc_defs.LockDataRefId\x1a\x10.grpc_defs.Empty\x12\x36\n\nserve_read\x12\x16.grpc_defs.ReadRequest\x1a\x10.grpc_defs.Value\x12\x42\n\x10serve_range_read\x12\x16.grpc_defs.ReadRequest\x1a\x16.grpc_defs.ValueRanged\x12=\n\x0bserve_write\x12\x17.grpc_defs.WriteRequest\x1a\x15.grpc_defs.WriteError\x12\x34\n\x06\x63ommit\x12\x18.grpc_defs.LockDataRefId\x1a\x10.grpc_defs.Empty\x12\x33\n\x05\x61\x62ort\x12\x18.grpc_defs.LockDataRefId\x1a\x10.grpc_defs.Empty2\xa5\x02\n\x0eMainReplicator\x12@\n\x12\x63reate_transaction\x12\x10.grpc_defs.Empty\x1a\x18.grpc_defs.LockDataRefId\x12/\n\x04read\x12\x16.grpc_defs.ReadRequest\x1a\x0f.grpc_defs.Json\x12\x35\n\x05write\x12\x1b.grpc_defs.JsonWriteRequest\x1a\x0f.grpc_defs.Json\x12\x33\n\x05\x61\x62ort\x12\x18.grpc_defs.LockDataRefId\x1a\x10.grpc_defs.Empty\x12\x34\n\x06\x63ommit\x12\x18.grpc_defs.LockDataRefId\x1a\x10.grpc_defs.Emptyb\x06proto3'
)




_LOCKDATAREFID = _descriptor.Descriptor(
  name='LockDataRefId',
  full_name='grpc_defs.LockDataRefId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc_defs.LockDataRefId.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=52,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='grpc_defs.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=61,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='grpc_defs.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='txn', full_name='grpc_defs.ReadRequest.txn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='grpc_defs.ReadRequest.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=128,
)


_KV = _descriptor.Descriptor(
  name='KV',
  full_name='grpc_defs.KV',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='grpc_defs.KV.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='grpc_defs.KV.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=162,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='grpc_defs.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='txn', full_name='grpc_defs.WriteRequest.txn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kv', full_name='grpc_defs.WriteRequest.kv', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=244,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='grpc_defs.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='grpc_defs.Value.val', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='grpc_defs.Value.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='res', full_name='grpc_defs.Value.res',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=246,
  serialized_end=292,
)


_WRITEERROR = _descriptor.Descriptor(
  name='WriteError',
  full_name='grpc_defs.WriteError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='grpc_defs.WriteError.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ok', full_name='grpc_defs.WriteError.ok', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='res', full_name='grpc_defs.WriteError.res',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=294,
  serialized_end=344,
)


_KVCOLLECTION = _descriptor.Descriptor(
  name='KVCollection',
  full_name='grpc_defs.KVCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='grpc_defs.KVCollection.val', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=388,
)


_VALUERANGED = _descriptor.Descriptor(
  name='ValueRanged',
  full_name='grpc_defs.ValueRanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='grpc_defs.ValueRanged.val', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='grpc_defs.ValueRanged.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='res', full_name='grpc_defs.ValueRanged.res',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=390,
  serialized_end=467,
)


_JSON = _descriptor.Descriptor(
  name='Json',
  full_name='grpc_defs.Json',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inner', full_name='grpc_defs.Json.inner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=469,
  serialized_end=490,
)


_JSONWRITEREQUEST = _descriptor.Descriptor(
  name='JsonWriteRequest',
  full_name='grpc_defs.JsonWriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='txn', full_name='grpc_defs.JsonWriteRequest.txn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='grpc_defs.JsonWriteRequest.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='grpc_defs.JsonWriteRequest.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=595,
)

_READREQUEST.fields_by_name['txn'].message_type = _LOCKDATAREFID
_WRITEREQUEST.fields_by_name['txn'].message_type = _LOCKDATAREFID
_WRITEREQUEST.fields_by_name['kv'].message_type = _KV
_VALUE.oneofs_by_name['res'].fields.append(
  _VALUE.fields_by_name['val'])
_VALUE.fields_by_name['val'].containing_oneof = _VALUE.oneofs_by_name['res']
_VALUE.oneofs_by_name['res'].fields.append(
  _VALUE.fields_by_name['error'])
_VALUE.fields_by_name['error'].containing_oneof = _VALUE.oneofs_by_name['res']
_WRITEERROR.oneofs_by_name['res'].fields.append(
  _WRITEERROR.fields_by_name['error'])
_WRITEERROR.fields_by_name['error'].containing_oneof = _WRITEERROR.oneofs_by_name['res']
_WRITEERROR.oneofs_by_name['res'].fields.append(
  _WRITEERROR.fields_by_name['ok'])
_WRITEERROR.fields_by_name['ok'].containing_oneof = _WRITEERROR.oneofs_by_name['res']
_KVCOLLECTION.fields_by_name['val'].message_type = _KV
_VALUERANGED.fields_by_name['val'].message_type = _KVCOLLECTION
_VALUERANGED.oneofs_by_name['res'].fields.append(
  _VALUERANGED.fields_by_name['val'])
_VALUERANGED.fields_by_name['val'].containing_oneof = _VALUERANGED.oneofs_by_name['res']
_VALUERANGED.oneofs_by_name['res'].fields.append(
  _VALUERANGED.fields_by_name['error'])
_VALUERANGED.fields_by_name['error'].containing_oneof = _VALUERANGED.oneofs_by_name['res']
_JSONWRITEREQUEST.fields_by_name['txn'].message_type = _LOCKDATAREFID
_JSONWRITEREQUEST.fields_by_name['value'].message_type = _JSON
DESCRIPTOR.message_types_by_name['LockDataRefId'] = _LOCKDATAREFID
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['KV'] = _KV
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['WriteError'] = _WRITEERROR
DESCRIPTOR.message_types_by_name['KVCollection'] = _KVCOLLECTION
DESCRIPTOR.message_types_by_name['ValueRanged'] = _VALUERANGED
DESCRIPTOR.message_types_by_name['Json'] = _JSON
DESCRIPTOR.message_types_by_name['JsonWriteRequest'] = _JSONWRITEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LockDataRefId = _reflection.GeneratedProtocolMessageType('LockDataRefId', (_message.Message,), {
  'DESCRIPTOR' : _LOCKDATAREFID,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.LockDataRefId)
  })
_sym_db.RegisterMessage(LockDataRefId)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.Empty)
  })
_sym_db.RegisterMessage(Empty)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

KV = _reflection.GeneratedProtocolMessageType('KV', (_message.Message,), {
  'DESCRIPTOR' : _KV,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.KV)
  })
_sym_db.RegisterMessage(KV)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.Value)
  })
_sym_db.RegisterMessage(Value)

WriteError = _reflection.GeneratedProtocolMessageType('WriteError', (_message.Message,), {
  'DESCRIPTOR' : _WRITEERROR,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.WriteError)
  })
_sym_db.RegisterMessage(WriteError)

KVCollection = _reflection.GeneratedProtocolMessageType('KVCollection', (_message.Message,), {
  'DESCRIPTOR' : _KVCOLLECTION,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.KVCollection)
  })
_sym_db.RegisterMessage(KVCollection)

ValueRanged = _reflection.GeneratedProtocolMessageType('ValueRanged', (_message.Message,), {
  'DESCRIPTOR' : _VALUERANGED,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.ValueRanged)
  })
_sym_db.RegisterMessage(ValueRanged)

Json = _reflection.GeneratedProtocolMessageType('Json', (_message.Message,), {
  'DESCRIPTOR' : _JSON,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.Json)
  })
_sym_db.RegisterMessage(Json)

JsonWriteRequest = _reflection.GeneratedProtocolMessageType('JsonWriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _JSONWRITEREQUEST,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc_defs.JsonWriteRequest)
  })
_sym_db.RegisterMessage(JsonWriteRequest)



_REPLICATOR = _descriptor.ServiceDescriptor(
  name='Replicator',
  full_name='grpc_defs.Replicator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=598,
  serialized_end=965,
  methods=[
  _descriptor.MethodDescriptor(
    name='new_with_time',
    full_name='grpc_defs.Replicator.new_with_time',
    index=0,
    containing_service=None,
    input_type=_LOCKDATAREFID,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='serve_read',
    full_name='grpc_defs.Replicator.serve_read',
    index=1,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_VALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='serve_range_read',
    full_name='grpc_defs.Replicator.serve_range_read',
    index=2,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_VALUERANGED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='serve_write',
    full_name='grpc_defs.Replicator.serve_write',
    index=3,
    containing_service=None,
    input_type=_WRITEREQUEST,
    output_type=_WRITEERROR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='commit',
    full_name='grpc_defs.Replicator.commit',
    index=4,
    containing_service=None,
    input_type=_LOCKDATAREFID,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='abort',
    full_name='grpc_defs.Replicator.abort',
    index=5,
    containing_service=None,
    input_type=_LOCKDATAREFID,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPLICATOR)

DESCRIPTOR.services_by_name['Replicator'] = _REPLICATOR


_MAINREPLICATOR = _descriptor.ServiceDescriptor(
  name='MainReplicator',
  full_name='grpc_defs.MainReplicator',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=968,
  serialized_end=1261,
  methods=[
  _descriptor.MethodDescriptor(
    name='create_transaction',
    full_name='grpc_defs.MainReplicator.create_transaction',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_LOCKDATAREFID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='read',
    full_name='grpc_defs.MainReplicator.read',
    index=1,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_JSON,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='write',
    full_name='grpc_defs.MainReplicator.write',
    index=2,
    containing_service=None,
    input_type=_JSONWRITEREQUEST,
    output_type=_JSON,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='abort',
    full_name='grpc_defs.MainReplicator.abort',
    index=3,
    containing_service=None,
    input_type=_LOCKDATAREFID,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='commit',
    full_name='grpc_defs.MainReplicator.commit',
    index=4,
    containing_service=None,
    input_type=_LOCKDATAREFID,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAINREPLICATOR)

DESCRIPTOR.services_by_name['MainReplicator'] = _MAINREPLICATOR

# @@protoc_insertion_point(module_scope)
