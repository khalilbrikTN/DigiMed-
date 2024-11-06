# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: PMRM_Service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'PMRM_Service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PMRM_Service.proto\x12\x0emedicalrecords\"n\n\x1d\x43reateMedicalConditionRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x14\n\x0cMedCondition\x18\x03 \x01(\t\x12\r\n\x05Notes\x18\x04 \x01(\t\"0\n\x1e\x43reateMedicalConditionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"n\n\x1dUpdateMedicalConditionRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x14\n\x0cMedCondition\x18\x03 \x01(\t\x12\r\n\x05Notes\x18\x04 \x01(\t\"0\n\x1eUpdateMedicalConditionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"a\n\x1fRetrieveMedicalConditionRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x14\n\x0cMedCondition\x18\x03 \x01(\t\"m\n RetrieveMedicalConditionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x14\n\x0cMedCondition\x18\x03 \x01(\t\x12\r\n\x05Notes\x18\x04 \x01(\t\"_\n\x1d\x44\x65leteMedicalConditionRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x14\n\x0cMedCondition\x18\x03 \x01(\t\"0\n\x1e\x44\x65leteMedicalConditionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\xbe\x01\n\x18\x43reateMedicalTestRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x0e\n\x06TestID\x18\x03 \x01(\x05\x12\x11\n\tTest_Type\x18\x04 \x01(\t\x12\x15\n\rSubjectOfTest\x18\x05 \x01(\t\x12\x0e\n\x06Result\x18\x06 \x01(\t\x12\x13\n\x0bImageOfScan\x18\x07 \x01(\t\x12\x19\n\x11\x44\x61te_TimeOfUpload\x18\x08 \x01(\t\"+\n\x19\x43reateMedicalTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\xbe\x01\n\x18UpdateMedicalTestRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x0e\n\x06TestID\x18\x03 \x01(\x05\x12\x11\n\tTest_Type\x18\x04 \x01(\t\x12\x15\n\rSubjectOfTest\x18\x05 \x01(\t\x12\x0e\n\x06Result\x18\x06 \x01(\t\x12\x13\n\x0bImageOfScan\x18\x07 \x01(\t\x12\x19\n\x11\x44\x61te_TimeOfUpload\x18\x08 \x01(\t\"+\n\x19UpdateMedicalTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"V\n\x1aRetrieveMedicalTestRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x0e\n\x06TestID\x18\x03 \x01(\x05\"\xbd\x01\n\x1bRetrieveMedicalTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x0e\n\x06TestID\x18\x03 \x01(\x05\x12\x11\n\tTest_Type\x18\x04 \x01(\t\x12\x15\n\rSubjectOfTest\x18\x05 \x01(\t\x12\x0e\n\x06Result\x18\x06 \x01(\t\x12\x13\n\x0bImageOfScan\x18\x07 \x01(\t\x12\x19\n\x11\x44\x61te_TimeOfUpload\x18\x08 \x01(\t\"T\n\x18\x44\x65leteMedicalTestRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x0e\n\x06TestID\x18\x03 \x01(\x05\"+\n\x19\x44\x65leteMedicalTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"j\n\x16\x43reateTreatedByRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x13\n\x0b\x44octorNatID\x18\x03 \x01(\t\x12\x11\n\tstartDate\x18\x04 \x01(\t\")\n\x17\x43reateTreatedByResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"j\n\x16UpdateTreatedByRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x13\n\x0b\x44octorNatID\x18\x03 \x01(\t\x12\x11\n\tstartDate\x18\x04 \x01(\t\")\n\x17UpdateTreatedByResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"Y\n\x18RetrieveTreatedByRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x13\n\x0b\x44octorNatID\x18\x03 \x01(\t\"i\n\x19RetrieveTreatedByResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x13\n\x0b\x44octorNatID\x18\x03 \x01(\t\x12\x11\n\tstartDate\x18\x04 \x01(\t\"W\n\x16\x44\x65leteTreatedByRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x0cPatientNatID\x18\x02 \x01(\t\x12\x13\n\x0b\x44octorNatID\x18\x03 \x01(\t\")\n\x17\x44\x65leteTreatedByResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xbb\n\n\x0bPMRMService\x12w\n\x16\x43reateMedicalCondition\x12-.medicalrecords.CreateMedicalConditionRequest\x1a..medicalrecords.CreateMedicalConditionResponse\x12w\n\x16UpdateMedicalCondition\x12-.medicalrecords.UpdateMedicalConditionRequest\x1a..medicalrecords.UpdateMedicalConditionResponse\x12}\n\x18RetrieveMedicalCondition\x12/.medicalrecords.RetrieveMedicalConditionRequest\x1a\x30.medicalrecords.RetrieveMedicalConditionResponse\x12w\n\x16\x44\x65leteMedicalCondition\x12-.medicalrecords.DeleteMedicalConditionRequest\x1a..medicalrecords.DeleteMedicalConditionResponse\x12h\n\x11\x43reateMedicalTest\x12(.medicalrecords.CreateMedicalTestRequest\x1a).medicalrecords.CreateMedicalTestResponse\x12h\n\x11UpdateMedicalTest\x12(.medicalrecords.UpdateMedicalTestRequest\x1a).medicalrecords.UpdateMedicalTestResponse\x12n\n\x13RetrieveMedicalTest\x12*.medicalrecords.RetrieveMedicalTestRequest\x1a+.medicalrecords.RetrieveMedicalTestResponse\x12h\n\x11\x44\x65leteMedicalTest\x12(.medicalrecords.DeleteMedicalTestRequest\x1a).medicalrecords.DeleteMedicalTestResponse\x12\x62\n\x0f\x43reateTreatedBy\x12&.medicalrecords.CreateTreatedByRequest\x1a\'.medicalrecords.CreateTreatedByResponse\x12\x62\n\x0fUpdateTreatedBy\x12&.medicalrecords.UpdateTreatedByRequest\x1a\'.medicalrecords.UpdateTreatedByResponse\x12h\n\x11RetrieveTreatedBy\x12(.medicalrecords.RetrieveTreatedByRequest\x1a).medicalrecords.RetrieveTreatedByResponse\x12\x62\n\x0f\x44\x65leteTreatedBy\x12&.medicalrecords.DeleteTreatedByRequest\x1a\'.medicalrecords.DeleteTreatedByResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PMRM_Service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATEMEDICALCONDITIONREQUEST']._serialized_start=38
  _globals['_CREATEMEDICALCONDITIONREQUEST']._serialized_end=148
  _globals['_CREATEMEDICALCONDITIONRESPONSE']._serialized_start=150
  _globals['_CREATEMEDICALCONDITIONRESPONSE']._serialized_end=198
  _globals['_UPDATEMEDICALCONDITIONREQUEST']._serialized_start=200
  _globals['_UPDATEMEDICALCONDITIONREQUEST']._serialized_end=310
  _globals['_UPDATEMEDICALCONDITIONRESPONSE']._serialized_start=312
  _globals['_UPDATEMEDICALCONDITIONRESPONSE']._serialized_end=360
  _globals['_RETRIEVEMEDICALCONDITIONREQUEST']._serialized_start=362
  _globals['_RETRIEVEMEDICALCONDITIONREQUEST']._serialized_end=459
  _globals['_RETRIEVEMEDICALCONDITIONRESPONSE']._serialized_start=461
  _globals['_RETRIEVEMEDICALCONDITIONRESPONSE']._serialized_end=570
  _globals['_DELETEMEDICALCONDITIONREQUEST']._serialized_start=572
  _globals['_DELETEMEDICALCONDITIONREQUEST']._serialized_end=667
  _globals['_DELETEMEDICALCONDITIONRESPONSE']._serialized_start=669
  _globals['_DELETEMEDICALCONDITIONRESPONSE']._serialized_end=717
  _globals['_CREATEMEDICALTESTREQUEST']._serialized_start=720
  _globals['_CREATEMEDICALTESTREQUEST']._serialized_end=910
  _globals['_CREATEMEDICALTESTRESPONSE']._serialized_start=912
  _globals['_CREATEMEDICALTESTRESPONSE']._serialized_end=955
  _globals['_UPDATEMEDICALTESTREQUEST']._serialized_start=958
  _globals['_UPDATEMEDICALTESTREQUEST']._serialized_end=1148
  _globals['_UPDATEMEDICALTESTRESPONSE']._serialized_start=1150
  _globals['_UPDATEMEDICALTESTRESPONSE']._serialized_end=1193
  _globals['_RETRIEVEMEDICALTESTREQUEST']._serialized_start=1195
  _globals['_RETRIEVEMEDICALTESTREQUEST']._serialized_end=1281
  _globals['_RETRIEVEMEDICALTESTRESPONSE']._serialized_start=1284
  _globals['_RETRIEVEMEDICALTESTRESPONSE']._serialized_end=1473
  _globals['_DELETEMEDICALTESTREQUEST']._serialized_start=1475
  _globals['_DELETEMEDICALTESTREQUEST']._serialized_end=1559
  _globals['_DELETEMEDICALTESTRESPONSE']._serialized_start=1561
  _globals['_DELETEMEDICALTESTRESPONSE']._serialized_end=1604
  _globals['_CREATETREATEDBYREQUEST']._serialized_start=1606
  _globals['_CREATETREATEDBYREQUEST']._serialized_end=1712
  _globals['_CREATETREATEDBYRESPONSE']._serialized_start=1714
  _globals['_CREATETREATEDBYRESPONSE']._serialized_end=1755
  _globals['_UPDATETREATEDBYREQUEST']._serialized_start=1757
  _globals['_UPDATETREATEDBYREQUEST']._serialized_end=1863
  _globals['_UPDATETREATEDBYRESPONSE']._serialized_start=1865
  _globals['_UPDATETREATEDBYRESPONSE']._serialized_end=1906
  _globals['_RETRIEVETREATEDBYREQUEST']._serialized_start=1908
  _globals['_RETRIEVETREATEDBYREQUEST']._serialized_end=1997
  _globals['_RETRIEVETREATEDBYRESPONSE']._serialized_start=1999
  _globals['_RETRIEVETREATEDBYRESPONSE']._serialized_end=2104
  _globals['_DELETETREATEDBYREQUEST']._serialized_start=2106
  _globals['_DELETETREATEDBYREQUEST']._serialized_end=2193
  _globals['_DELETETREATEDBYRESPONSE']._serialized_start=2195
  _globals['_DELETETREATEDBYRESPONSE']._serialized_end=2236
  _globals['_PMRMSERVICE']._serialized_start=2239
  _globals['_PMRMSERVICE']._serialized_end=3578
# @@protoc_insertion_point(module_scope)
