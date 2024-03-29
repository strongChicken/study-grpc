# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exercise.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='exercise.proto',
  package='exercise',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x65xercise.proto\x12\x08\x65xercise\"U\n\nConsumeReq\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08item_num\x18\x03 \x01(\x03\x12\x0f\n\x07user_id\x18\x04 \x01(\x05\"@\n\x0b\x43onsumeResp\x12\x0e\n\x06result\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x10\n\x08order_id\x18\x03 \x01(\t\"\x1b\n\x08QueryReq\x12\x0f\n\x07item_id\x18\x01 \x01(\t\",\n\tQueryResp\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\".\n\tReturnReq\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\"2\n\nReturnResp\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x14\n\x0corder_id_ret\x18\x02 \x01(\t\"b\n\rRegisteredReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07keyword\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61ll_num\x18\x03 \x01(\t\x12\x0e\n\x06gender\x18\x04 \x01(\t\x12\x10\n\x08\x62irthday\x18\x05 \x01(\x05\"Q\n\x0eRegisteredResp\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x02 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61ll_num\x18\x04 \x01(\x05\")\n\x08LoginReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07keyword\x18\x02 \x01(\t\"\x1b\n\tLoginResp\x12\x0e\n\x06result\x18\x01 \x01(\t\";\n\x0bRechargeReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07keyword\x18\x02 \x01(\t\x12\r\n\x05money\x18\x03 \x01(\x05\"\x1e\n\x0cRechargeResp\x12\x0e\n\x06result\x18\x01 \x01(\t\"+\n\x08OrderReq\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\"\x1b\n\tOrderResp\x12\x0e\n\x06result\x18\x01 \x01(\t2\xff\x02\n\x04Save\x12\x32\n\x03Pay\x12\x14.exercise.ConsumeReq\x1a\x15.exercise.ConsumeResp\x12\x30\n\x05Query\x12\x12.exercise.QueryReq\x1a\x13.exercise.QueryResp\x12\x33\n\x06Return\x12\x13.exercise.ReturnReq\x1a\x14.exercise.ReturnResp\x12=\n\x08Register\x12\x17.exercise.RegisteredReq\x1a\x18.exercise.RegisteredResp\x12\x30\n\x05Login\x12\x12.exercise.LoginReq\x1a\x13.exercise.LoginResp\x12\x39\n\x08Recharge\x12\x15.exercise.RechargeReq\x1a\x16.exercise.RechargeResp\x12\x30\n\x05Order\x12\x12.exercise.OrderReq\x1a\x13.exercise.OrderRespb\x06proto3')
)




_CONSUMEREQ = _descriptor.Descriptor(
  name='ConsumeReq',
  full_name='exercise.ConsumeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='exercise.ConsumeReq.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='exercise.ConsumeReq.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_num', full_name='exercise.ConsumeReq.item_num', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='exercise.ConsumeReq.user_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=28,
  serialized_end=113,
)


_CONSUMERESP = _descriptor.Descriptor(
  name='ConsumeResp',
  full_name='exercise.ConsumeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='exercise.ConsumeResp.result', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='exercise.ConsumeResp.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='exercise.ConsumeResp.order_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=115,
  serialized_end=179,
)


_QUERYREQ = _descriptor.Descriptor(
  name='QueryReq',
  full_name='exercise.QueryReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='exercise.QueryReq.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=181,
  serialized_end=208,
)


_QUERYRESP = _descriptor.Descriptor(
  name='QueryResp',
  full_name='exercise.QueryResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='exercise.QueryResp.ID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='exercise.QueryResp.description', index=1,
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
  serialized_start=210,
  serialized_end=254,
)


_RETURNREQ = _descriptor.Descriptor(
  name='ReturnReq',
  full_name='exercise.ReturnReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_id', full_name='exercise.ReturnReq.order_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='exercise.ReturnReq.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=256,
  serialized_end=302,
)


_RETURNRESP = _descriptor.Descriptor(
  name='ReturnResp',
  full_name='exercise.ReturnResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='exercise.ReturnResp.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id_ret', full_name='exercise.ReturnResp.order_id_ret', index=1,
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
  serialized_start=304,
  serialized_end=354,
)


_REGISTEREDREQ = _descriptor.Descriptor(
  name='RegisteredReq',
  full_name='exercise.RegisteredReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='exercise.RegisteredReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='exercise.RegisteredReq.keyword', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_num', full_name='exercise.RegisteredReq.call_num', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='exercise.RegisteredReq.gender', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='birthday', full_name='exercise.RegisteredReq.birthday', index=4,
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
  serialized_start=356,
  serialized_end=454,
)


_REGISTEREDRESP = _descriptor.Descriptor(
  name='RegisteredResp',
  full_name='exercise.RegisteredResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='exercise.RegisteredResp.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account', full_name='exercise.RegisteredResp.account', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='exercise.RegisteredResp.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_num', full_name='exercise.RegisteredResp.call_num', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=456,
  serialized_end=537,
)


_LOGINREQ = _descriptor.Descriptor(
  name='LoginReq',
  full_name='exercise.LoginReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='exercise.LoginReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='exercise.LoginReq.keyword', index=1,
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
  serialized_start=539,
  serialized_end=580,
)


_LOGINRESP = _descriptor.Descriptor(
  name='LoginResp',
  full_name='exercise.LoginResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='exercise.LoginResp.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=582,
  serialized_end=609,
)


_RECHARGEREQ = _descriptor.Descriptor(
  name='RechargeReq',
  full_name='exercise.RechargeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='exercise.RechargeReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='exercise.RechargeReq.keyword', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='money', full_name='exercise.RechargeReq.money', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=611,
  serialized_end=670,
)


_RECHARGERESP = _descriptor.Descriptor(
  name='RechargeResp',
  full_name='exercise.RechargeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='exercise.RechargeResp.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=672,
  serialized_end=702,
)


_ORDERREQ = _descriptor.Descriptor(
  name='OrderReq',
  full_name='exercise.OrderReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='exercise.OrderReq.item_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='exercise.OrderReq.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=704,
  serialized_end=747,
)


_ORDERRESP = _descriptor.Descriptor(
  name='OrderResp',
  full_name='exercise.OrderResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='exercise.OrderResp.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=749,
  serialized_end=776,
)

DESCRIPTOR.message_types_by_name['ConsumeReq'] = _CONSUMEREQ
DESCRIPTOR.message_types_by_name['ConsumeResp'] = _CONSUMERESP
DESCRIPTOR.message_types_by_name['QueryReq'] = _QUERYREQ
DESCRIPTOR.message_types_by_name['QueryResp'] = _QUERYRESP
DESCRIPTOR.message_types_by_name['ReturnReq'] = _RETURNREQ
DESCRIPTOR.message_types_by_name['ReturnResp'] = _RETURNRESP
DESCRIPTOR.message_types_by_name['RegisteredReq'] = _REGISTEREDREQ
DESCRIPTOR.message_types_by_name['RegisteredResp'] = _REGISTEREDRESP
DESCRIPTOR.message_types_by_name['LoginReq'] = _LOGINREQ
DESCRIPTOR.message_types_by_name['LoginResp'] = _LOGINRESP
DESCRIPTOR.message_types_by_name['RechargeReq'] = _RECHARGEREQ
DESCRIPTOR.message_types_by_name['RechargeResp'] = _RECHARGERESP
DESCRIPTOR.message_types_by_name['OrderReq'] = _ORDERREQ
DESCRIPTOR.message_types_by_name['OrderResp'] = _ORDERRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConsumeReq = _reflection.GeneratedProtocolMessageType('ConsumeReq', (_message.Message,), {
  'DESCRIPTOR' : _CONSUMEREQ,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.ConsumeReq)
  })
_sym_db.RegisterMessage(ConsumeReq)

ConsumeResp = _reflection.GeneratedProtocolMessageType('ConsumeResp', (_message.Message,), {
  'DESCRIPTOR' : _CONSUMERESP,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.ConsumeResp)
  })
_sym_db.RegisterMessage(ConsumeResp)

QueryReq = _reflection.GeneratedProtocolMessageType('QueryReq', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQ,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.QueryReq)
  })
_sym_db.RegisterMessage(QueryReq)

QueryResp = _reflection.GeneratedProtocolMessageType('QueryResp', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESP,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.QueryResp)
  })
_sym_db.RegisterMessage(QueryResp)

ReturnReq = _reflection.GeneratedProtocolMessageType('ReturnReq', (_message.Message,), {
  'DESCRIPTOR' : _RETURNREQ,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.ReturnReq)
  })
_sym_db.RegisterMessage(ReturnReq)

ReturnResp = _reflection.GeneratedProtocolMessageType('ReturnResp', (_message.Message,), {
  'DESCRIPTOR' : _RETURNRESP,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.ReturnResp)
  })
_sym_db.RegisterMessage(ReturnResp)

RegisteredReq = _reflection.GeneratedProtocolMessageType('RegisteredReq', (_message.Message,), {
  'DESCRIPTOR' : _REGISTEREDREQ,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.RegisteredReq)
  })
_sym_db.RegisterMessage(RegisteredReq)

RegisteredResp = _reflection.GeneratedProtocolMessageType('RegisteredResp', (_message.Message,), {
  'DESCRIPTOR' : _REGISTEREDRESP,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.RegisteredResp)
  })
_sym_db.RegisterMessage(RegisteredResp)

LoginReq = _reflection.GeneratedProtocolMessageType('LoginReq', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQ,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.LoginReq)
  })
_sym_db.RegisterMessage(LoginReq)

LoginResp = _reflection.GeneratedProtocolMessageType('LoginResp', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESP,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.LoginResp)
  })
_sym_db.RegisterMessage(LoginResp)

RechargeReq = _reflection.GeneratedProtocolMessageType('RechargeReq', (_message.Message,), {
  'DESCRIPTOR' : _RECHARGEREQ,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.RechargeReq)
  })
_sym_db.RegisterMessage(RechargeReq)

RechargeResp = _reflection.GeneratedProtocolMessageType('RechargeResp', (_message.Message,), {
  'DESCRIPTOR' : _RECHARGERESP,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.RechargeResp)
  })
_sym_db.RegisterMessage(RechargeResp)

OrderReq = _reflection.GeneratedProtocolMessageType('OrderReq', (_message.Message,), {
  'DESCRIPTOR' : _ORDERREQ,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.OrderReq)
  })
_sym_db.RegisterMessage(OrderReq)

OrderResp = _reflection.GeneratedProtocolMessageType('OrderResp', (_message.Message,), {
  'DESCRIPTOR' : _ORDERRESP,
  '__module__' : 'exercise_pb2'
  # @@protoc_insertion_point(class_scope:exercise.OrderResp)
  })
_sym_db.RegisterMessage(OrderResp)



_SAVE = _descriptor.ServiceDescriptor(
  name='Save',
  full_name='exercise.Save',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=779,
  serialized_end=1162,
  methods=[
  _descriptor.MethodDescriptor(
    name='Pay',
    full_name='exercise.Save.Pay',
    index=0,
    containing_service=None,
    input_type=_CONSUMEREQ,
    output_type=_CONSUMERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='exercise.Save.Query',
    index=1,
    containing_service=None,
    input_type=_QUERYREQ,
    output_type=_QUERYRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Return',
    full_name='exercise.Save.Return',
    index=2,
    containing_service=None,
    input_type=_RETURNREQ,
    output_type=_RETURNRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='exercise.Save.Register',
    index=3,
    containing_service=None,
    input_type=_REGISTEREDREQ,
    output_type=_REGISTEREDRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='exercise.Save.Login',
    index=4,
    containing_service=None,
    input_type=_LOGINREQ,
    output_type=_LOGINRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Recharge',
    full_name='exercise.Save.Recharge',
    index=5,
    containing_service=None,
    input_type=_RECHARGEREQ,
    output_type=_RECHARGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Order',
    full_name='exercise.Save.Order',
    index=6,
    containing_service=None,
    input_type=_ORDERREQ,
    output_type=_ORDERRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SAVE)

DESCRIPTOR.services_by_name['Save'] = _SAVE

# @@protoc_insertion_point(module_scope)
