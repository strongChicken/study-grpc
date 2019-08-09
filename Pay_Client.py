import random

import grpc

from make_gRPC_by_myself import exercise_pb2
from make_gRPC_by_myself import exercise_pb2_grpc

print("start greet")


def pay():
    port = 50051
    channel = grpc.insecure_channel("127.0.0.1:%d" % port)
    print("link for port")
    stub = exercise_pb2_grpc.SaveStub(channel=channel)
    print("make stub")
    req = exercise_pb2.ConsumeReq()
    # IO的异常处理 TODO
    req.item_id = 1
    req.description = "test"
    req.item_num = 1
    print("send request")
    resp = stub.Pay(req)
    print('resp', resp)
    if resp.result != 0:
        print(resp.message)

    print("success")


if __name__ == '__main__':
    pay()
