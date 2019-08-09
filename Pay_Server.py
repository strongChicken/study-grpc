import time
import grpc
import pymysql

from concurrent import futures
from make_gRPC_by_myself import Pay_pb2
from make_gRPC_by_myself import Pay_pb2_grpc


class SaveInfo(Pay_pb2_grpc.SaveServicer):
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "284927463", "order_sql")

    def Pay(self, request, context):
        print('request:', request)
        resp = Pay_pb2.ConsumeResp()

        if request.price < 0:
            print("Input_price is error")
            resp.result = -1
            resp.message = "the price can not less than 0"
            return resp

        if request.item_id < 0:
            print("Input_id is error")
            resp.result = -2
            resp.message = "the item_id can not less than 0"
            return resp

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
            resp.message = "item_id can not be null or zero"
            print("insert failed")
            return resp
        else:
            try:
                self.conn.begin()
                c.execute('''INSERT INTO Consume(cid, description, ID) VALUES(NULL,'%s', %d)''' % (
                            description, item_id))
                c.execute('''UPDATE item_info set num=num+1 where item_id = %d''' % request.item_id)
                self.conn.commit()
                c.close()
                print("save db")
                resp.message = "insert successful"
                return resp
            except Exception as e:
                self.conn.rollback()
                resp.result = -3
                print("Error ", e)
        resp.result = 0
        resp.message = "success"
        return resp

    def Query(self, request, context):
        c = self.conn.cursor()
        resp = Pay_pb2.ConsumeResp()
        if request.order_id == 1:
            db = "consume"
        if request.order_id == 2:
            db = "ITEM_ID"
        if request.order_id < 0:
            resp.message = "order_id can not smaller than 0"
            return resp

        self.conn.begin()
        try:
            result = c.execute('''SELECT * FROM %s FOR UPDATE''' % db)
            self.conn.commit()
            c.close()
            return result
        except Exception as e:
            self.conn.rollback()
            print("check error: ", e)


def main():
    print("start")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Pay_pb2_grpc.add_SaveServicer_to_server(SaveInfo(), server)
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
