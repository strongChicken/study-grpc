# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import exercise_pb2 as exercise__pb2


class SaveStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Pay = channel.unary_unary(
        '/exercise.Save/Pay',
        request_serializer=exercise__pb2.ConsumeReq.SerializeToString,
        response_deserializer=exercise__pb2.ConsumeResp.FromString,
        )
    self.Query = channel.unary_unary(
        '/exercise.Save/Query',
        request_serializer=exercise__pb2.QueryReq.SerializeToString,
        response_deserializer=exercise__pb2.QueryResp.FromString,
        )
    self.Return = channel.unary_unary(
        '/exercise.Save/Return',
        request_serializer=exercise__pb2.ReturnReq.SerializeToString,
        response_deserializer=exercise__pb2.ReturnResp.FromString,
        )


class SaveServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Pay(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Return(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SaveServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Pay': grpc.unary_unary_rpc_method_handler(
          servicer.Pay,
          request_deserializer=exercise__pb2.ConsumeReq.FromString,
          response_serializer=exercise__pb2.ConsumeResp.SerializeToString,
      ),
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=exercise__pb2.QueryReq.FromString,
          response_serializer=exercise__pb2.QueryResp.SerializeToString,
      ),
      'Return': grpc.unary_unary_rpc_method_handler(
          servicer.Return,
          request_deserializer=exercise__pb2.ReturnReq.FromString,
          response_serializer=exercise__pb2.ReturnResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'exercise.Save', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
