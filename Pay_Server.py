import time
import datetime
import grpc
import pymysql
import random

from concurrent import futures
from make_gRPC_by_myself import exercise_pb2
from make_gRPC_by_myself import exercise_pb2_grpc

from make_gRPC_by_myself import errors


class SaveInfo(exercise_pb2_grpc.SaveServicer):
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",
                                    user="root",
                                    password="284927463",
                                    database="order_sql")

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

        # 创建 cursor
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
            c.execute('''SELECT num FROM item_info where item_id= %d''' % item_id)
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

            try:
                # insert_order = "INSERT INTO order_info(id, order_id, item_id, description, item_num) VALUES(NULL, %s, %d, %s, %d)"
                # c.execute(insert_order, (order_id, item_id, description, request.item_num))
                c.execute('''INSERT INTO order_info(id, order_id, item_id, description, item_num) VALUES(NULL, '%s', %d, '%s', %d);''' % (order_id, item_id, description, request.item_num))
                print("save db")

            # 5 UPDATE item_info(num)
                print('update item_info')
                # sql = "UPDATE item_info SET NUM= NUM - %d where (item_id= %d, version= version+1)"
                # c.execute(sql, (request.item_num, request.item_id))
                print("item_id: ", request.item_id, "\n", "item_num:", request.item_num)

                # 无法修改库存
                c.execute('''UPDATE ITEM_INFO SET NUM= NUM - %d WHERE ITEM_ID= %d and version= version+1''' % (request.item_num, request.item_id))
            except Exception as e_order:
                self.conn.rollback()
                print("insert_error:", e_order)
                return gen_error_resp(errors.ERR_INPUT_INVALID)

            # 6 commit事务
            print('transaction commit')
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print("Error ", e)
            return gen_error_resp(errors.ERR_INPUT_INVALID)

        # 7 return resp
        resp = exercise_pb2.ConsumeResp()
        resp.result = 0
        resp.message = "insert successful"
        resp.order_id = order_id
        return resp

    # 查询接口
    def Query(self, request, context):
        resp = exercise_pb2.QueryResp()
        order_id = request.order_id
        c = self.conn.cursor()

        # 通过订单id 查找 商品id
        try:
            item_id = "SELECT item_id FROM order_info WHERE order_id= %s"
            c.execute(item_id, order_id)
            print("try to SELECT item_id FROM ITEM_info WHERE order_id")
            print("item_id：", item_id)
            resp.ID = item_id
        except Exception as e:
            print("Error:", e)
            resp.description = "the order_id was invalid"
            return resp

        # 通过商品id 查询 库存
        try:
            c.execute('''SELECT NUM FROM ITEM_INFO WHERE ITEM_ID= %d''' % item_id)
            print("SELECT NUM FROM ITEM_INFO WHERE ITEM_ID")
            num = c.fetchone()
            print("num:", num)
            if num is None:
                resp.description = "商品id存在"
            else:
                resp.description = ("商品库存: %d" % num)
                print("库存:", num)
            return resp
        except Exception as e:
            print("query item_info error: ", e)
            resp.description = "the num was error"
            return resp

    # 退单接口
    def Return(self, request, context):
        resp = exercise_pb2.ReturnResp
        order_id = request.order_id
        # print("type_order_id:", type(order_id))
        print("order_id: ", order_id)
        c = self.conn.cursor()

        try:
            self.conn.begin()
            # 通过order_id查找item_id
            # item_id_ret = "SELECT 'item_id' FROM order_info WHERE 'order_id'= %s "    为什么这个读不出正确的数据
            # c.execute(item_id_ret, order_id,)
            # resu = c.fetchone()
            c.execute('''select item_id from order_info where order_id= %s lock in share mode''', order_id)
            resu = c.fetchone()
            item_id_ret = resu[0]
            if item_id_ret is None or (request.return_num is None):
                resp.result = "订单错误"
                self.conn.rollback()
                return resp
            else:
                print("退款查询商品id 成功：", item_id_ret)

            # 生成退款order_id_ret
            localtime = time.localtime(time.time())
            order_id_ret = '%s%d' % (time.strftime('%Y%m%d%H%M%S', localtime), random.randint(1, 10000000))
            resp.order_id_ret = order_id_ret
            print("生成退款订单号:", order_id_ret)
            print("退款订单类型：", type(order_id_ret))

            # 写入退单操作
            print("return_num:", request.return_num)
            order_ret = "INSERT INTO order_info(order_id, item_id, item_num, control_id) VALUES(%s, %s, %s, %s)"
            c.execute(order_ret, (order_id_ret, item_id_ret, request.return_num, 1))
            print("写入退单信息成功：INSERT INTO order_info")

            # 修改库存
            print("item_id_ret:", item_id_ret)
            item_num = "UPDATE ITEM_INFO SET NUM= NUM + %s WHERE ITEM_ID = %s"
            c.execute(item_num, (request.return_num, item_id_ret))
            # c.execute('''UPDATE ITEM_INFO SET NUM= NUM - %s WHERE ITEM_ID = %s lock in share mode''' % (request.return_num, item_id_ret))
            print("修改库存完成")
            resp.result = '退单完成'
            self.conn.commit()
            return resp
        except Exception as e:
            self.conn.rollback()
            print("写入出错，原因：", e)
            resp.result = "退单失败"
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
