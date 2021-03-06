# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2



_FILECOVERAGEINFO = descriptor.Descriptor(
  name='FileCoverageInfo',
  full_name='klee.FileCoverageInfo',
  filename='CoverageLogs.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='file_name', full_name='klee.FileCoverageInfo.file_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='covered_lines', full_name='klee.FileCoverageInfo.covered_lines', index=1,
      number=2, type=5, cpp_type=1, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_COVERAGEINFO = descriptor.Descriptor(
  name='CoverageInfo',
  full_name='klee.CoverageInfo',
  filename='CoverageLogs.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='time_stamp', full_name='klee.CoverageInfo.time_stamp', index=0,
      number=2, type=4, cpp_type=4, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='file_coverage', full_name='klee.CoverageInfo.file_coverage', index=1,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_COVERAGEINFO.fields_by_name['file_coverage'].message_type = _FILECOVERAGEINFO

class FileCoverageInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILECOVERAGEINFO

class CoverageInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COVERAGEINFO

