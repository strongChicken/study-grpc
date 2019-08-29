import random

import grpc

import exercise_pb2
import exercise_pb2_grpc

import sys

'''
sys.path.append("/Users/water/waaater/make_gRPC_by_myself")
'''


print("start greet")


def pay(item_id: int, item_num: int, user_id: int):
    port = 50051
    channel = grpc.insecure_channel("127.0.0.1:%d" % port)
    print("link for port")
    stub = exercise_pb2_grpc.SaveStub(channel=channel)
    print("make stub")
    req = exercise_pb2.ConsumeReq()
    req.item_id = item_id
    req.description = "test"
    req.item_num = item_num
    req.user_id = user_id
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


def registered(name: str, keyword: str, tel_ph: str, gender: str, birthday: int):
    port = 50051
    channel = grpc.insecure_channel("127.0.0.1:%d" % port)
    print("link for port to return")
    stub = exercise_pb2_grpc.SaveStub(channel=channel)
    print("made stub")
    req = exercise_pb2.RegisteredReq()
    req.name = name
    req.keyword = keyword
    req.call_num = tel_ph
    req.gender = gender
    req.birthday = birthday
    print("send request:")
    resp = stub.Register(req)
    print("resp: ", resp.result)


def login(name: str, keyword: str):
    port = 50051
    channel = grpc.insecure_channel("127.0.0.1:%d" % port)
    print("link for port to return")
    stub = exercise_pb2_grpc.SaveStub(channel=channel)
    print("made stub")
    req = exercise_pb2.LoginReq()
    req.name = name
    req.keyword = keyword
    print("send request:")
    resp = stub.Login(req)
    print("resp: ", resp.result)


def recharge(name: str, keyword: str, money: int):
    port = 50051
    channel = grpc.insecure_channel("127.0.0.1:%d" % port)
    print("link for port to return")
    stub = exercise_pb2_grpc.SaveStub(channel=channel)
    print("made stub")
    req = exercise_pb2.RechargeReq()
    req.name = name
    req.keyword = keyword
    req.money = money
    print("send request:")
    resp = stub.Recharge(req)
    print("resp: ", resp.result)
    

if __name__ == '__main__':
    if sys.argv[1] == 'query':
        query_data(sys.argv[2])
    elif sys.argv[1] == 'return':
        return_(sys.argv[2], int(sys.argv[3]))
    elif sys.argv[1] == 'pay':
        pay(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif sys.argv[1] == 'registered':
        registered(sys.argv[2], sys.argv[3], str(sys.argv[4]), sys.argv[5], int(sys.argv[6]))
    elif sys.argv[1] == 'login':
        login(sys.argv[2], str(sys.argv[3]))
    elif sys.argv[1] == 'recharge':
        recharge(sys.argv[2], sys.argv[3], int(sys.argv[4]))


'''
mysql -uroot -p284927463 order_sql

SELECT * FROM ITEM_INFO;

python3 Pay_Client.py pay 3 1

INSERT INTO ITEM_INFO (ITEM_ID, PRICE, NUM) VALUES (2, 18, 5);

CREATE DATABASE order_sql;

CREATE TABLE ORDER_INFO(id int NOT NULL auto_increment, 
                         order_id varchar(255) NOT NULL, 
                         item_id int NOT NULL, 
                         item_num int NOT NULL,
                         pay_money int NOT NULL,
                         description varchar(255) NOT NULL, 
                         control_id int NOT NULL,
                         time datetime NOT NULL, 
                         PRIMARY KEY(id));
                         
CREATE TABLE ITEM_INFO(ITEM_ID int NOT NULL auto_increment,
                        PRICE int NOT NULL,
                        NUM int NOT NULL,
                        PRIMARY KEY(ITEM_ID));
                        
CREATE TABLE MEM_INFO(id int NOT NULL auto_increment,
                      name varchar(255) NOT NULL,
                      keyword varchar(255) NOT NULL,
                      call_num varchar(255) NOT NULL,
                      gender varchar(255) NOT NULL,
                      birthday date,
                      accou_bal int NOT NULL DEFAULT 0,
                      times_consu int NOT NULL DEFAULT 0,
                      money_consu int NOT NULL DEFAULT 0,
                      PRIMARY KEY(id));
                      
                        
ALTER TABLE 
'''
