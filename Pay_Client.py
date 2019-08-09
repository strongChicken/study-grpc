import random

import grpc

from make_gRPC_by_myself import Pay_pb2_grpc
from make_gRPC_by_myself import Pay_pb2

print("start greet")


def pay():
    port = 50051
    channel = grpc.insecure_channel("127.0.0.1:%d" % port)
    print("link for port")
    stub = Pay_pb2_grpc.SaveStub(channel=channel)
    print("make stub")
    req = Pay_pb2.ConsumeReq()
    # IO的异常处理 TODO
    req.item_id = random.randint(1, 10)
    req.price = random.randint(1, 100)
    req.description = "test"
    print("send request")
    resp = stub.Pay(req)
    print('resp', resp)
    if resp.result != 0:
        print(resp.message)

    print("success")


if __name__ == '__main__':
    pay()
