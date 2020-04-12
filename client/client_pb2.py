# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='client.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0c\x63lient.proto\")\n\x07\x44\x61taReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08somethig\x18\x02 \x01(\t\"\x18\n\x07\x44\x61taRes\x12\r\n\x05reply\x18\x01 \x01(\t2+\n\x07Greeter\x12 \n\x08SendData\x12\x08.DataReq\x1a\x08.DataRes\"\x00\x62\x06proto3'
)




_DATAREQ = _descriptor.Descriptor(
  name='DataReq',
  full_name='DataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DataReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='somethig', full_name='DataReq.somethig', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=16,
  serialized_end=57,
)


_DATARES = _descriptor.Descriptor(
  name='DataRes',
  full_name='DataRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='DataRes.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=59,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['DataReq'] = _DATAREQ
DESCRIPTOR.message_types_by_name['DataRes'] = _DATARES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataReq = _reflection.GeneratedProtocolMessageType('DataReq', (_message.Message,), {
  'DESCRIPTOR' : _DATAREQ,
  '__module__' : 'client_pb2'
  # @@protoc_insertion_point(class_scope:DataReq)
  })
_sym_db.RegisterMessage(DataReq)

DataRes = _reflection.GeneratedProtocolMessageType('DataRes', (_message.Message,), {
  'DESCRIPTOR' : _DATARES,
  '__module__' : 'client_pb2'
  # @@protoc_insertion_point(class_scope:DataRes)
  })
_sym_db.RegisterMessage(DataRes)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=85,
  serialized_end=128,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendData',
    full_name='Greeter.SendData',
    index=0,
    containing_service=None,
    input_type=_DATAREQ,
    output_type=_DATARES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
