# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pymarketstore/proto/marketstore.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pymarketstore/proto/marketstore.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n%pymarketstore/proto/marketstore.proto\x12\x05proto\"8\n\tDataShape\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x04type\x18\x02 \x01(\x0e\x32\x0f.proto.DataType\"\x90\x02\n\x11NumpyMultiDataset\x12!\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x13.proto.NumpyDataset\x12=\n\x0bstart_index\x18\x02 \x03(\x0b\x32(.proto.NumpyMultiDataset.StartIndexEntry\x12\x36\n\x07lengths\x18\x03 \x03(\x0b\x32%.proto.NumpyMultiDataset.LengthsEntry\x1a\x31\n\x0fStartIndexEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a.\n\x0cLengthsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x86\x01\n\x0cNumpyDataset\x12\x14\n\x0c\x63olumn_types\x18\x01 \x03(\t\x12\x14\n\x0c\x63olumn_names\x18\x02 \x03(\t\x12\x13\n\x0b\x63olumn_data\x18\x03 \x03(\x0c\x12\x0e\n\x06length\x18\x04 \x01(\x05\x12%\n\x0b\x64\x61ta_shapes\x18\x05 \x03(\x0b\x32\x10.proto.DataShape\":\n\x11MultiQueryRequest\x12%\n\x08requests\x18\x01 \x03(\x0b\x32\x13.proto.QueryRequest\"\xa0\x02\n\x0cQueryRequest\x12\x18\n\x10is_sql_statement\x18\x01 \x01(\x08\x12\x15\n\rsql_statement\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x03 \x01(\t\x12\x14\n\x0ckey_category\x18\x04 \x01(\t\x12\x13\n\x0b\x65poch_start\x18\x05 \x01(\x03\x12\x19\n\x11\x65poch_start_nanos\x18\x06 \x01(\x03\x12\x11\n\tepoch_end\x18\x07 \x01(\x03\x12\x17\n\x0f\x65poch_end_nanos\x18\x08 \x01(\x03\x12\x1a\n\x12limit_record_count\x18\t \x01(\x05\x12\x18\n\x10limit_from_start\x18\n \x01(\x08\x12\x0f\n\x07\x63olumns\x18\x0b \x03(\t\x12\x11\n\tfunctions\x18\x0c \x03(\t\"`\n\x12MultiQueryResponse\x12\'\n\tresponses\x18\x01 \x03(\x0b\x32\x14.proto.QueryResponse\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08timezone\x18\x03 \x01(\t\"9\n\rQueryResponse\x12(\n\x06result\x18\x01 \x01(\x0b\x32\x18.proto.NumpyMultiDataset\":\n\x11MultiWriteRequest\x12%\n\x08requests\x18\x01 \x03(\x0b\x32\x13.proto.WriteRequest\"R\n\x0cWriteRequest\x12&\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x18.proto.NumpyMultiDataset\x12\x1a\n\x12is_variable_length\x18\x02 \x01(\x08\"?\n\x13MultiServerResponse\x12(\n\tresponses\x18\x01 \x03(\x0b\x32\x15.proto.ServerResponse\"0\n\x0eServerResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"6\n\x0fMultiKeyRequest\x12#\n\x08requests\x18\x01 \x03(\x0b\x32\x11.proto.KeyRequest\"\x19\n\nKeyRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"%\n\x12ListSymbolsRequest\x12\x0f\n\x07results\x18\x01 \x03(\t\"&\n\x13ListSymbolsResponse\x12\x0f\n\x07results\x18\x01 \x03(\t\"\x16\n\x14ServerVersionRequest\"(\n\x15ServerVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t*\xb6\x01\n\x08\x44\x61taType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x46LOAT32\x10\x01\x12\t\n\x05INT32\x10\x02\x12\x0b\n\x07\x46LOAT64\x10\x03\x12\t\n\x05INT64\x10\x04\x12\t\n\x05\x45POCH\x10\x05\x12\x08\n\x04\x42YTE\x10\x06\x12\x08\n\x04\x42OOL\x10\x07\x12\x08\n\x04NONE\x10\x08\x12\n\n\x06STRING\x10\t\x12\t\n\x05INT16\x10\n\x12\t\n\x05UINT8\x10\x0b\x12\n\n\x06UINT16\x10\x0c\x12\n\n\x06UINT32\x10\r\x12\n\n\x06UINT64\x10\x0e\x32\xdb\x02\n\x0bMarketstore\x12<\n\x05Query\x12\x18.proto.MultiQueryRequest\x1a\x19.proto.MultiQueryResponse\x12=\n\x05Write\x12\x18.proto.MultiWriteRequest\x1a\x1a.proto.MultiServerResponse\x12=\n\x07\x44\x65stroy\x12\x16.proto.MultiKeyRequest\x1a\x1a.proto.MultiServerResponse\x12\x44\n\x0bListSymbols\x12\x19.proto.ListSymbolsRequest\x1a\x1a.proto.ListSymbolsResponse\x12J\n\rServerVersion\x12\x1b.proto.ServerVersionRequest\x1a\x1c.proto.ServerVersionResponseb\x06proto3'
)

_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='proto.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT32', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT64', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EPOCH', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BYTE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT16', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT8', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT16', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT32', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT64', index=14, number=14,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1514,
  serialized_end=1696,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
UNKNOWN = 0
FLOAT32 = 1
INT32 = 2
FLOAT64 = 3
INT64 = 4
EPOCH = 5
BYTE = 6
BOOL = 7
NONE = 8
STRING = 9
INT16 = 10
UINT8 = 11
UINT16 = 12
UINT32 = 13
UINT64 = 14



_DATASHAPE = _descriptor.Descriptor(
  name='DataShape',
  full_name='proto.DataShape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.DataShape.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='proto.DataShape.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=48,
  serialized_end=104,
)


_NUMPYMULTIDATASET_STARTINDEXENTRY = _descriptor.Descriptor(
  name='StartIndexEntry',
  full_name='proto.NumpyMultiDataset.StartIndexEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.NumpyMultiDataset.StartIndexEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.NumpyMultiDataset.StartIndexEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=331,
)

_NUMPYMULTIDATASET_LENGTHSENTRY = _descriptor.Descriptor(
  name='LengthsEntry',
  full_name='proto.NumpyMultiDataset.LengthsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.NumpyMultiDataset.LengthsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.NumpyMultiDataset.LengthsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=379,
)

_NUMPYMULTIDATASET = _descriptor.Descriptor(
  name='NumpyMultiDataset',
  full_name='proto.NumpyMultiDataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='proto.NumpyMultiDataset.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_index', full_name='proto.NumpyMultiDataset.start_index', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lengths', full_name='proto.NumpyMultiDataset.lengths', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NUMPYMULTIDATASET_STARTINDEXENTRY, _NUMPYMULTIDATASET_LENGTHSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=379,
)


_NUMPYDATASET = _descriptor.Descriptor(
  name='NumpyDataset',
  full_name='proto.NumpyDataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column_types', full_name='proto.NumpyDataset.column_types', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column_names', full_name='proto.NumpyDataset.column_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column_data', full_name='proto.NumpyDataset.column_data', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='proto.NumpyDataset.length', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_shapes', full_name='proto.NumpyDataset.data_shapes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=382,
  serialized_end=516,
)


_MULTIQUERYREQUEST = _descriptor.Descriptor(
  name='MultiQueryRequest',
  full_name='proto.MultiQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests', full_name='proto.MultiQueryRequest.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=518,
  serialized_end=576,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='proto.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_sql_statement', full_name='proto.QueryRequest.is_sql_statement', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sql_statement', full_name='proto.QueryRequest.sql_statement', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='proto.QueryRequest.destination', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_category', full_name='proto.QueryRequest.key_category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch_start', full_name='proto.QueryRequest.epoch_start', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch_start_nanos', full_name='proto.QueryRequest.epoch_start_nanos', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch_end', full_name='proto.QueryRequest.epoch_end', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch_end_nanos', full_name='proto.QueryRequest.epoch_end_nanos', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit_record_count', full_name='proto.QueryRequest.limit_record_count', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit_from_start', full_name='proto.QueryRequest.limit_from_start', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='proto.QueryRequest.columns', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functions', full_name='proto.QueryRequest.functions', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=579,
  serialized_end=867,
)


_MULTIQUERYRESPONSE = _descriptor.Descriptor(
  name='MultiQueryResponse',
  full_name='proto.MultiQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='proto.MultiQueryResponse.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='proto.MultiQueryResponse.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='proto.MultiQueryResponse.timezone', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=869,
  serialized_end=965,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='proto.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='proto.QueryResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=967,
  serialized_end=1024,
)


_MULTIWRITEREQUEST = _descriptor.Descriptor(
  name='MultiWriteRequest',
  full_name='proto.MultiWriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests', full_name='proto.MultiWriteRequest.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1026,
  serialized_end=1084,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='proto.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='proto.WriteRequest.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_variable_length', full_name='proto.WriteRequest.is_variable_length', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1086,
  serialized_end=1168,
)


_MULTISERVERRESPONSE = _descriptor.Descriptor(
  name='MultiServerResponse',
  full_name='proto.MultiServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='proto.MultiServerResponse.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1170,
  serialized_end=1233,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='proto.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.ServerResponse.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='proto.ServerResponse.version', index=1,
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
  serialized_start=1235,
  serialized_end=1283,
)


_MULTIKEYREQUEST = _descriptor.Descriptor(
  name='MultiKeyRequest',
  full_name='proto.MultiKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests', full_name='proto.MultiKeyRequest.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1285,
  serialized_end=1339,
)


_KEYREQUEST = _descriptor.Descriptor(
  name='KeyRequest',
  full_name='proto.KeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.KeyRequest.key', index=0,
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
  serialized_start=1341,
  serialized_end=1366,
)


_LISTSYMBOLSREQUEST = _descriptor.Descriptor(
  name='ListSymbolsRequest',
  full_name='proto.ListSymbolsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='proto.ListSymbolsRequest.results', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1368,
  serialized_end=1405,
)


_LISTSYMBOLSRESPONSE = _descriptor.Descriptor(
  name='ListSymbolsResponse',
  full_name='proto.ListSymbolsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='proto.ListSymbolsResponse.results', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1407,
  serialized_end=1445,
)


_SERVERVERSIONREQUEST = _descriptor.Descriptor(
  name='ServerVersionRequest',
  full_name='proto.ServerVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=1447,
  serialized_end=1469,
)


_SERVERVERSIONRESPONSE = _descriptor.Descriptor(
  name='ServerVersionResponse',
  full_name='proto.ServerVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='proto.ServerVersionResponse.version', index=0,
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
  serialized_start=1471,
  serialized_end=1511,
)

_DATASHAPE.fields_by_name['type'].enum_type = _DATATYPE
_NUMPYMULTIDATASET_STARTINDEXENTRY.containing_type = _NUMPYMULTIDATASET
_NUMPYMULTIDATASET_LENGTHSENTRY.containing_type = _NUMPYMULTIDATASET
_NUMPYMULTIDATASET.fields_by_name['data'].message_type = _NUMPYDATASET
_NUMPYMULTIDATASET.fields_by_name['start_index'].message_type = _NUMPYMULTIDATASET_STARTINDEXENTRY
_NUMPYMULTIDATASET.fields_by_name['lengths'].message_type = _NUMPYMULTIDATASET_LENGTHSENTRY
_NUMPYDATASET.fields_by_name['data_shapes'].message_type = _DATASHAPE
_MULTIQUERYREQUEST.fields_by_name['requests'].message_type = _QUERYREQUEST
_MULTIQUERYRESPONSE.fields_by_name['responses'].message_type = _QUERYRESPONSE
_QUERYRESPONSE.fields_by_name['result'].message_type = _NUMPYMULTIDATASET
_MULTIWRITEREQUEST.fields_by_name['requests'].message_type = _WRITEREQUEST
_WRITEREQUEST.fields_by_name['data'].message_type = _NUMPYMULTIDATASET
_MULTISERVERRESPONSE.fields_by_name['responses'].message_type = _SERVERRESPONSE
_MULTIKEYREQUEST.fields_by_name['requests'].message_type = _KEYREQUEST
DESCRIPTOR.message_types_by_name['DataShape'] = _DATASHAPE
DESCRIPTOR.message_types_by_name['NumpyMultiDataset'] = _NUMPYMULTIDATASET
DESCRIPTOR.message_types_by_name['NumpyDataset'] = _NUMPYDATASET
DESCRIPTOR.message_types_by_name['MultiQueryRequest'] = _MULTIQUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['MultiQueryResponse'] = _MULTIQUERYRESPONSE
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['MultiWriteRequest'] = _MULTIWRITEREQUEST
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['MultiServerResponse'] = _MULTISERVERRESPONSE
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
DESCRIPTOR.message_types_by_name['MultiKeyRequest'] = _MULTIKEYREQUEST
DESCRIPTOR.message_types_by_name['KeyRequest'] = _KEYREQUEST
DESCRIPTOR.message_types_by_name['ListSymbolsRequest'] = _LISTSYMBOLSREQUEST
DESCRIPTOR.message_types_by_name['ListSymbolsResponse'] = _LISTSYMBOLSRESPONSE
DESCRIPTOR.message_types_by_name['ServerVersionRequest'] = _SERVERVERSIONREQUEST
DESCRIPTOR.message_types_by_name['ServerVersionResponse'] = _SERVERVERSIONRESPONSE
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataShape = _reflection.GeneratedProtocolMessageType('DataShape', (_message.Message,), {
  'DESCRIPTOR' : _DATASHAPE,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.DataShape)
  })
_sym_db.RegisterMessage(DataShape)

NumpyMultiDataset = _reflection.GeneratedProtocolMessageType('NumpyMultiDataset', (_message.Message,), {

  'StartIndexEntry' : _reflection.GeneratedProtocolMessageType('StartIndexEntry', (_message.Message,), {
    'DESCRIPTOR' : _NUMPYMULTIDATASET_STARTINDEXENTRY,
    '__module__' : 'pymarketstore.proto.marketstore_pb2'
    # @@protoc_insertion_point(class_scope:proto.NumpyMultiDataset.StartIndexEntry)
    })
  ,

  'LengthsEntry' : _reflection.GeneratedProtocolMessageType('LengthsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NUMPYMULTIDATASET_LENGTHSENTRY,
    '__module__' : 'pymarketstore.proto.marketstore_pb2'
    # @@protoc_insertion_point(class_scope:proto.NumpyMultiDataset.LengthsEntry)
    })
  ,
  'DESCRIPTOR' : _NUMPYMULTIDATASET,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.NumpyMultiDataset)
  })
_sym_db.RegisterMessage(NumpyMultiDataset)
_sym_db.RegisterMessage(NumpyMultiDataset.StartIndexEntry)
_sym_db.RegisterMessage(NumpyMultiDataset.LengthsEntry)

NumpyDataset = _reflection.GeneratedProtocolMessageType('NumpyDataset', (_message.Message,), {
  'DESCRIPTOR' : _NUMPYDATASET,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.NumpyDataset)
  })
_sym_db.RegisterMessage(NumpyDataset)

MultiQueryRequest = _reflection.GeneratedProtocolMessageType('MultiQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _MULTIQUERYREQUEST,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.MultiQueryRequest)
  })
_sym_db.RegisterMessage(MultiQueryRequest)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

MultiQueryResponse = _reflection.GeneratedProtocolMessageType('MultiQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _MULTIQUERYRESPONSE,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.MultiQueryResponse)
  })
_sym_db.RegisterMessage(MultiQueryResponse)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSE,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.QueryResponse)
  })
_sym_db.RegisterMessage(QueryResponse)

MultiWriteRequest = _reflection.GeneratedProtocolMessageType('MultiWriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _MULTIWRITEREQUEST,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.MultiWriteRequest)
  })
_sym_db.RegisterMessage(MultiWriteRequest)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

MultiServerResponse = _reflection.GeneratedProtocolMessageType('MultiServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _MULTISERVERRESPONSE,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.MultiServerResponse)
  })
_sym_db.RegisterMessage(MultiServerResponse)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESPONSE,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.ServerResponse)
  })
_sym_db.RegisterMessage(ServerResponse)

MultiKeyRequest = _reflection.GeneratedProtocolMessageType('MultiKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _MULTIKEYREQUEST,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.MultiKeyRequest)
  })
_sym_db.RegisterMessage(MultiKeyRequest)

KeyRequest = _reflection.GeneratedProtocolMessageType('KeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _KEYREQUEST,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.KeyRequest)
  })
_sym_db.RegisterMessage(KeyRequest)

ListSymbolsRequest = _reflection.GeneratedProtocolMessageType('ListSymbolsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSYMBOLSREQUEST,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.ListSymbolsRequest)
  })
_sym_db.RegisterMessage(ListSymbolsRequest)

ListSymbolsResponse = _reflection.GeneratedProtocolMessageType('ListSymbolsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSYMBOLSRESPONSE,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.ListSymbolsResponse)
  })
_sym_db.RegisterMessage(ListSymbolsResponse)

ServerVersionRequest = _reflection.GeneratedProtocolMessageType('ServerVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERVERSIONREQUEST,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.ServerVersionRequest)
  })
_sym_db.RegisterMessage(ServerVersionRequest)

ServerVersionResponse = _reflection.GeneratedProtocolMessageType('ServerVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERVERSIONRESPONSE,
  '__module__' : 'pymarketstore.proto.marketstore_pb2'
  # @@protoc_insertion_point(class_scope:proto.ServerVersionResponse)
  })
_sym_db.RegisterMessage(ServerVersionResponse)


_NUMPYMULTIDATASET_STARTINDEXENTRY._options = None
_NUMPYMULTIDATASET_LENGTHSENTRY._options = None

_MARKETSTORE = _descriptor.ServiceDescriptor(
  name='Marketstore',
  full_name='proto.Marketstore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1699,
  serialized_end=2046,
  methods=[
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='proto.Marketstore.Query',
    index=0,
    containing_service=None,
    input_type=_MULTIQUERYREQUEST,
    output_type=_MULTIQUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='proto.Marketstore.Write',
    index=1,
    containing_service=None,
    input_type=_MULTIWRITEREQUEST,
    output_type=_MULTISERVERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='proto.Marketstore.Destroy',
    index=2,
    containing_service=None,
    input_type=_MULTIKEYREQUEST,
    output_type=_MULTISERVERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListSymbols',
    full_name='proto.Marketstore.ListSymbols',
    index=3,
    containing_service=None,
    input_type=_LISTSYMBOLSREQUEST,
    output_type=_LISTSYMBOLSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ServerVersion',
    full_name='proto.Marketstore.ServerVersion',
    index=4,
    containing_service=None,
    input_type=_SERVERVERSIONREQUEST,
    output_type=_SERVERVERSIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MARKETSTORE)

DESCRIPTOR.services_by_name['Marketstore'] = _MARKETSTORE

# @@protoc_insertion_point(module_scope)
