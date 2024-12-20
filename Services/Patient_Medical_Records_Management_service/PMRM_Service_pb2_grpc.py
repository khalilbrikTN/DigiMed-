# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import PMRM_Service_pb2 as PMRM__Service__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in PMRM_Service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PMRMServiceStub(object):
    """The main PMRMService handles all CRUD operations for MedicalConditions, MedicalTests, and TreatedBy tables
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateMedicalCondition = channel.unary_unary(
                '/medicalrecords.PMRMService/CreateMedicalCondition',
                request_serializer=PMRM__Service__pb2.CreateMedicalConditionRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.CreateMedicalConditionResponse.FromString,
                _registered_method=True)
        self.UpdateMedicalCondition = channel.unary_unary(
                '/medicalrecords.PMRMService/UpdateMedicalCondition',
                request_serializer=PMRM__Service__pb2.UpdateMedicalConditionRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.UpdateMedicalConditionResponse.FromString,
                _registered_method=True)
        self.RetrieveMedicalCondition = channel.unary_unary(
                '/medicalrecords.PMRMService/RetrieveMedicalCondition',
                request_serializer=PMRM__Service__pb2.RetrieveMedicalConditionRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.RetrieveMedicalConditionResponse.FromString,
                _registered_method=True)
        self.DeleteMedicalCondition = channel.unary_unary(
                '/medicalrecords.PMRMService/DeleteMedicalCondition',
                request_serializer=PMRM__Service__pb2.DeleteMedicalConditionRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.DeleteMedicalConditionResponse.FromString,
                _registered_method=True)
        self.CreateMedicalTest = channel.unary_unary(
                '/medicalrecords.PMRMService/CreateMedicalTest',
                request_serializer=PMRM__Service__pb2.CreateMedicalTestRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.CreateMedicalTestResponse.FromString,
                _registered_method=True)
        self.UpdateMedicalTest = channel.unary_unary(
                '/medicalrecords.PMRMService/UpdateMedicalTest',
                request_serializer=PMRM__Service__pb2.UpdateMedicalTestRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.UpdateMedicalTestResponse.FromString,
                _registered_method=True)
        self.RetrieveMedicalTest = channel.unary_unary(
                '/medicalrecords.PMRMService/RetrieveMedicalTest',
                request_serializer=PMRM__Service__pb2.RetrieveMedicalTestRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.RetrieveMedicalTestResponse.FromString,
                _registered_method=True)
        self.DeleteMedicalTest = channel.unary_unary(
                '/medicalrecords.PMRMService/DeleteMedicalTest',
                request_serializer=PMRM__Service__pb2.DeleteMedicalTestRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.DeleteMedicalTestResponse.FromString,
                _registered_method=True)
        self.CreateTreatedBy = channel.unary_unary(
                '/medicalrecords.PMRMService/CreateTreatedBy',
                request_serializer=PMRM__Service__pb2.CreateTreatedByRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.CreateTreatedByResponse.FromString,
                _registered_method=True)
        self.UpdateTreatedBy = channel.unary_unary(
                '/medicalrecords.PMRMService/UpdateTreatedBy',
                request_serializer=PMRM__Service__pb2.UpdateTreatedByRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.UpdateTreatedByResponse.FromString,
                _registered_method=True)
        self.RetrieveTreatedBy = channel.unary_unary(
                '/medicalrecords.PMRMService/RetrieveTreatedBy',
                request_serializer=PMRM__Service__pb2.RetrieveTreatedByRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.RetrieveTreatedByResponse.FromString,
                _registered_method=True)
        self.DeleteTreatedBy = channel.unary_unary(
                '/medicalrecords.PMRMService/DeleteTreatedBy',
                request_serializer=PMRM__Service__pb2.DeleteTreatedByRequest.SerializeToString,
                response_deserializer=PMRM__Service__pb2.DeleteTreatedByResponse.FromString,
                _registered_method=True)


class PMRMServiceServicer(object):
    """The main PMRMService handles all CRUD operations for MedicalConditions, MedicalTests, and TreatedBy tables
    """

    def CreateMedicalCondition(self, request, context):
        """MedicalConditions table methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMedicalCondition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveMedicalCondition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMedicalCondition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateMedicalTest(self, request, context):
        """MedicalTests table methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMedicalTest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveMedicalTest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMedicalTest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTreatedBy(self, request, context):
        """TreatedBy table methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTreatedBy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveTreatedBy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTreatedBy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PMRMServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateMedicalCondition': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateMedicalCondition,
                    request_deserializer=PMRM__Service__pb2.CreateMedicalConditionRequest.FromString,
                    response_serializer=PMRM__Service__pb2.CreateMedicalConditionResponse.SerializeToString,
            ),
            'UpdateMedicalCondition': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMedicalCondition,
                    request_deserializer=PMRM__Service__pb2.UpdateMedicalConditionRequest.FromString,
                    response_serializer=PMRM__Service__pb2.UpdateMedicalConditionResponse.SerializeToString,
            ),
            'RetrieveMedicalCondition': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveMedicalCondition,
                    request_deserializer=PMRM__Service__pb2.RetrieveMedicalConditionRequest.FromString,
                    response_serializer=PMRM__Service__pb2.RetrieveMedicalConditionResponse.SerializeToString,
            ),
            'DeleteMedicalCondition': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMedicalCondition,
                    request_deserializer=PMRM__Service__pb2.DeleteMedicalConditionRequest.FromString,
                    response_serializer=PMRM__Service__pb2.DeleteMedicalConditionResponse.SerializeToString,
            ),
            'CreateMedicalTest': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateMedicalTest,
                    request_deserializer=PMRM__Service__pb2.CreateMedicalTestRequest.FromString,
                    response_serializer=PMRM__Service__pb2.CreateMedicalTestResponse.SerializeToString,
            ),
            'UpdateMedicalTest': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMedicalTest,
                    request_deserializer=PMRM__Service__pb2.UpdateMedicalTestRequest.FromString,
                    response_serializer=PMRM__Service__pb2.UpdateMedicalTestResponse.SerializeToString,
            ),
            'RetrieveMedicalTest': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveMedicalTest,
                    request_deserializer=PMRM__Service__pb2.RetrieveMedicalTestRequest.FromString,
                    response_serializer=PMRM__Service__pb2.RetrieveMedicalTestResponse.SerializeToString,
            ),
            'DeleteMedicalTest': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMedicalTest,
                    request_deserializer=PMRM__Service__pb2.DeleteMedicalTestRequest.FromString,
                    response_serializer=PMRM__Service__pb2.DeleteMedicalTestResponse.SerializeToString,
            ),
            'CreateTreatedBy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTreatedBy,
                    request_deserializer=PMRM__Service__pb2.CreateTreatedByRequest.FromString,
                    response_serializer=PMRM__Service__pb2.CreateTreatedByResponse.SerializeToString,
            ),
            'UpdateTreatedBy': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTreatedBy,
                    request_deserializer=PMRM__Service__pb2.UpdateTreatedByRequest.FromString,
                    response_serializer=PMRM__Service__pb2.UpdateTreatedByResponse.SerializeToString,
            ),
            'RetrieveTreatedBy': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveTreatedBy,
                    request_deserializer=PMRM__Service__pb2.RetrieveTreatedByRequest.FromString,
                    response_serializer=PMRM__Service__pb2.RetrieveTreatedByResponse.SerializeToString,
            ),
            'DeleteTreatedBy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTreatedBy,
                    request_deserializer=PMRM__Service__pb2.DeleteTreatedByRequest.FromString,
                    response_serializer=PMRM__Service__pb2.DeleteTreatedByResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'medicalrecords.PMRMService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('medicalrecords.PMRMService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PMRMService(object):
    """The main PMRMService handles all CRUD operations for MedicalConditions, MedicalTests, and TreatedBy tables
    """

    @staticmethod
    def CreateMedicalCondition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/CreateMedicalCondition',
            PMRM__Service__pb2.CreateMedicalConditionRequest.SerializeToString,
            PMRM__Service__pb2.CreateMedicalConditionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateMedicalCondition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/UpdateMedicalCondition',
            PMRM__Service__pb2.UpdateMedicalConditionRequest.SerializeToString,
            PMRM__Service__pb2.UpdateMedicalConditionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RetrieveMedicalCondition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/RetrieveMedicalCondition',
            PMRM__Service__pb2.RetrieveMedicalConditionRequest.SerializeToString,
            PMRM__Service__pb2.RetrieveMedicalConditionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteMedicalCondition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/DeleteMedicalCondition',
            PMRM__Service__pb2.DeleteMedicalConditionRequest.SerializeToString,
            PMRM__Service__pb2.DeleteMedicalConditionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateMedicalTest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/CreateMedicalTest',
            PMRM__Service__pb2.CreateMedicalTestRequest.SerializeToString,
            PMRM__Service__pb2.CreateMedicalTestResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateMedicalTest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/UpdateMedicalTest',
            PMRM__Service__pb2.UpdateMedicalTestRequest.SerializeToString,
            PMRM__Service__pb2.UpdateMedicalTestResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RetrieveMedicalTest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/RetrieveMedicalTest',
            PMRM__Service__pb2.RetrieveMedicalTestRequest.SerializeToString,
            PMRM__Service__pb2.RetrieveMedicalTestResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteMedicalTest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/DeleteMedicalTest',
            PMRM__Service__pb2.DeleteMedicalTestRequest.SerializeToString,
            PMRM__Service__pb2.DeleteMedicalTestResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateTreatedBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/CreateTreatedBy',
            PMRM__Service__pb2.CreateTreatedByRequest.SerializeToString,
            PMRM__Service__pb2.CreateTreatedByResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateTreatedBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/UpdateTreatedBy',
            PMRM__Service__pb2.UpdateTreatedByRequest.SerializeToString,
            PMRM__Service__pb2.UpdateTreatedByResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RetrieveTreatedBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/RetrieveTreatedBy',
            PMRM__Service__pb2.RetrieveTreatedByRequest.SerializeToString,
            PMRM__Service__pb2.RetrieveTreatedByResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteTreatedBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/medicalrecords.PMRMService/DeleteTreatedBy',
            PMRM__Service__pb2.DeleteTreatedByRequest.SerializeToString,
            PMRM__Service__pb2.DeleteTreatedByResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
