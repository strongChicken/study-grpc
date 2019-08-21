import random

import grpc

import exercise_pb2
import exercise_pb2_grpc

import sys

'''
sys.path.append("/Users/water/waaater/make_gRPC_by_myself")
'''


print("start greet")


def pay():
    port = 50051
    channel = grpc.insecure_channel("127.0.0.1:%d" % port)
    print("link for port")
    stub = exercise_pb2_grpc.SaveStub(channel=channel)
    print("make stub")
    req = exercise_pb2.ConsumeReq()
    # IO的异常处理 TODO
    req.item_id = 3
    req.description = "test"
    req.item_num = 1
    print("send request")
    resp = stub.Pay(req)
    print('resp', resp)
    if resp.result != 0:
        print(resp.message)
    else:
        print("success")


def query_data(order_id: str):
    port = 50051
    channel = grpc.insecure_channel("127.0.0.1:%d" % port)
    print("link for port to query")
    stub = exercise_pb2_grpc.SaveStub(channel=channel)
    print("made stub")
    req = exercise_pb2.QueryReq()
    req.order_id = order_id
    print("send request order_id:", req.order_id)
    resp = stub.Query(req)
    print("resp: ", resp.description)


def return_(order_id: str, return_num: int):
    port = 50051
    channel = grpc.insecure_channel("127.0.0.1:%d" % port)
    print("link for port to return")
    stub = exercise_pb2_grpc.SaveStub(channel=channel)
    print("made stub")
    req = exercise_pb2.ReturnReq()
    req.order_id = order_id
    req.return_num = return_num
    print("send request:", req.order_id, "& ", req.return_num)
    resp = stub.Return(req)
    print("resp: ", resp.result)
    

if __name__ == '__main__':
    if sys.argv[1] == 'query':
        query_data(sys.argv[2])
    elif sys.argv[1] == 'return':
        return_(sys.argv[2], int(sys.argv[3]))
    elif sys.argv[1] == 'pay':
        pay()

'''
mysql -uroot -p284927463 order_sql

SELECT * FROM ITEM_INFO;

INSERT INTO ITEM_INFO (ITEM_ID, PRICE, NUM) VALUES (2, 18, 5);

python3 Pay_Client.py query 201908212156004018647 

CREATE DATABASE order_sql;

CREATE TABLES order_info(id int NOT NULL auto_increment, 
                         order_id varchar(255) NOT NULL, 
                         item_id int NOT NULL, 
                         description varchar(255) NOT NULL, 
                         item_num int NOT NULL, 
                         control_id int NOT NULL,
                         PRIMARY KEY(id));
                         
CREATE TABLES ITEM_INFO(ITEM_ID NOT NULL auto_increment,
                        PRICE int NOT NULL,
                        NUM int NOT NULL,
                        VERSION int NOT NULL,
                        PRIMARY KEY(ITEM_ID);
'''
