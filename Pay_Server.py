import time
import datetime
import grpc
import pymysql
import random

from concurrent import futures
from make_gRPC_by_myself import exercise_pb2
from make_gRPC_by_myself import exercise_pb2_grpc

from . import errors


class SaveInfo(exercise_pb2_grpc.SaveServicer):
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "284927463", "order_sql")

    def Pay(self, request, context):
        def gen_error_resp(code) -> exercise_pb2.ConsumeResp:
            _resp = exercise_pb2.ConsumeResp()
            _resp.result = code
            _resp.message = errors.error_map[code]
            print('server rpc Pay error:', _resp)
            return _resp

        print('request:', request)

        if request.item_id < 0:
            return gen_error_resp(errors.ERR_INPUT_INVALID)

        print("ready to connect")
        self.conn = pymysql.connect("localhost", "root", "284927463", "order_sql")      # 为什么又一次尝试连接数据库呢？
        print("Opened order_sql.db successfully")

        c = self.conn.cursor()

        description = request.description
        if description is None or description == "":
            description = "NULL"
            print("description:", description)

        # write into order
        print("item_id:", request.item_id)
        item_id = request.item_id
        # when item_id is null, will be zero
        if item_id == 0:
            return gen_error_resp(errors.ERR_INPUT_INVALID)

        # now = datetime.datetime.now()
        # order_id = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), random.randint(1000000000))
        try:
            # 1 开启事务
            print('begin transaction')
            self.conn.begin()

            # 2 查询库存（num）
            print('query item_info')
            c.execute('''SELECT num FROM item_info where item_id= %d;''' % item_id)
            num = c.fetchone()
            if num is None:
                return gen_error_resp(errors.ERR_ITEM_NOT_FOUND)
            if num[0] <= request.item_num:
                return gen_error_resp(errors.ERR_ITEM_NOT_ENOUGH)

            # 3 生成order id
            print('generating order_id')
            localtime = time.localtime((time.time()))
            order_id = '%s%d' % (time.strftime('%Y%m%d%H%M%S', localtime), random.randint(1, 10000000))

            # 4 写入 order
            print('insert: ', '''INSERT INTO order_info(id, order_id, item_id, description, item_num) VALUES(NULL, '%s', %d, '%s', %d)''' % (order_id, item_id, description, request.item_num))
            c.execute('''INSERT INTO order_info(id, order_id, item_id, description, item_num) VALUES(NULL, '%s', %d, '%s', %d);''' % (order_id, item_id, description, request.item_num))
            print("save db")

            # 5 UPDATE item_info(num)
            print('update item_info')
            c.execute('''UPDATE item_info SET num=num-%d where item_id= %d;''' % (request.item_num, request.item_id))

            # 6 commit事务
            print('transaction commit')
            self.conn.commit()

            # 7 return resp
            print('success')
        except Exception as e:
            self.conn.rollback()
            print("Error ", e)
            return gen_error_resp(errors.ERR_INPUT_INVALID)     # 不知道返回什么

        resp = exercise_pb2.ConsumeResp()
        resp.result = 0
        resp.message = "insert successful"
        resp.order_id = order_id
        return resp

    def Query(self, request, context):
        # check item_info.num by item_id
        # if enough -> return NUM
        # if not enough -> return not enough and NUM
        # ues begin...commit
        order_id = SaveInfo.Pay(request.order_id)
        resp = exercise_pb2.QueryResp()
        self.conn = pymysql.connect("localhost", "order_sql")
        print("Query->connect order_sql success")
        c = self.conn.cursor()
        try:
            print("开启事务A")
            self.conn.begin()
            c.execute('''SELECT item_id FROM order_info WHERE order_id= %d;''' % order_id)
            print("try to SELECT item_id FROM ITEM_info WHERE order_id")
            item_id = c.fetchone()
            self.conn.commit()
            print("item_id：", item_id)
        except Exception as e:
            self.conn.rollback()
            print("Error:", e)
            resp.description = "the order_id was invalid"
            return resp

        try:
            print("开始事务B")
            self.conn.commit()
            c.execute('''SELECT NUM  FROM ITEM_INFO WHERE ITEM_ID= %d''' % item_id)
            print("SELECT NUM FROM ITEM_INFO WHERE ITEM_ID")
            num = c.fetchone()
            print("库存:", num)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("query item_info error: ", e)
            resp.description = "the num was error"
            return resp


def main():
    print("start")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    exercise_pb2_grpc.add_SaveServicer_to_server(SaveInfo(), server)
    print("begin listen")
    port = 50051
    server.add_insecure_port("127.0.0.1:%d" % port)
    server.start()
    print("listen port: %d" % port)

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()
