# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Pay.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Pay.proto',
  package='Pay',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tPay.proto\x12\x03Pay\"e\n\nConsumeReq\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\x12\r\n\x05price\x18\x02 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08item_num\x18\x04 \x01(\x03\x12\x10\n\x08order_id\x18\x05 \x01(\x05\".\n\x0b\x43onsumeResp\x12\x0e\n\x06result\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t20\n\x04Save\x12(\n\x03Pay\x12\x0f.Pay.ConsumeReq\x1a\x10.Pay.ConsumeRespb\x06proto3')
)




_CONSUMEREQ = _descriptor.Descriptor(
  name='ConsumeReq',
  full_name='Pay.ConsumeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='Pay.ConsumeReq.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='Pay.ConsumeReq.price', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Pay.ConsumeReq.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_num', full_name='Pay.ConsumeReq.item_num', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='Pay.ConsumeReq.order_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=18,
  serialized_end=119,
)


_CONSUMERESP = _descriptor.Descriptor(
  name='ConsumeResp',
  full_name='Pay.ConsumeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='Pay.ConsumeResp.result', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='Pay.ConsumeResp.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=121,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['ConsumeReq'] = _CONSUMEREQ
DESCRIPTOR.message_types_by_name['ConsumeResp'] = _CONSUMERESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConsumeReq = _reflection.GeneratedProtocolMessageType('ConsumeReq', (_message.Message,), {
  'DESCRIPTOR' : _CONSUMEREQ,
  '__module__' : 'Pay_pb2'
  # @@protoc_insertion_point(class_scope:Pay.ConsumeReq)
  })
_sym_db.RegisterMessage(ConsumeReq)

ConsumeResp = _reflection.GeneratedProtocolMessageType('ConsumeResp', (_message.Message,), {
  'DESCRIPTOR' : _CONSUMERESP,
  '__module__' : 'Pay_pb2'
  # @@protoc_insertion_point(class_scope:Pay.ConsumeResp)
  })
_sym_db.RegisterMessage(ConsumeResp)



_SAVE = _descriptor.ServiceDescriptor(
  name='Save',
  full_name='Pay.Save',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=169,
  serialized_end=217,
  methods=[
  _descriptor.MethodDescriptor(
    name='Pay',
    full_name='Pay.Save.Pay',
    index=0,
    containing_service=None,
    input_type=_CONSUMEREQ,
    output_type=_CONSUMERESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SAVE)

DESCRIPTOR.services_by_name['Save'] = _SAVE

# @@protoc_insertion_point(module_scope)
