import time
import datetime
import grpc
import pymysql
import random
import hmac

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

    # 付款接口
        # 验证商品id
        # 根据user_id 查询账户余额
        # 判断 余额是否足够
        # 根据user_id 减少 余额
        # 判断 库存是否足够
        # 生成 订单id
        # 写入 订单信息 -- update 订单信息
        # 扣除 库存 -- update 库存
    def Pay(self, request, context):
        def gen_error_resp(code) -> exercise_pb2.ConsumeResp:
            _resp = exercise_pb2.ConsumeResp()
            _resp.result = code
            _resp.message = errors.error_map[code]
            print('server rpc Pay error:', _resp)
            return _resp

        resp = exercise_pb2.ConsumeResp()

        # user_id == MEM_INFO.id
        user_id = request.user_id

        print('request:', request)
        if request.item_id < 0:
            return gen_error_resp(errors.ERR_INPUT_INVALID)

        # 创建 cursor
        c = self.conn.cursor()

        description = request.description
        if description is None or description == "":
            description = "NULL"
            print("description:", description)

        # 验证商品id
        print("item_id:", request.item_id)
        item_id = request.item_id
        if item_id == 0:
            return gen_error_resp(errors.ERR_INPUT_INVALID)

        # 事务 --> 查询、判断余额、扣减余额
        # 查询余额
        self.conn.begin()
        global balance
        try:
            money = "SELECT accou_bal FROM MEM_INFO user_id= %s"
            c.execute(money, user_id)
            balance = c.fetchone()[0]
        except Exception as e:
            print("查询余额出错:", e)

        price = "SELECT PRICE FROM ITEM_INFO WHERE ITEM_ID= %d"
        c.execute(price, item_id)
        item_price = c.fetchone()[0]
        print("查询单价成功")

        item_num = request.item_num
        cost = item_price * item_num

        # 判断余额是否足够
        if balance == 0 or balance < cost:
            resp.message = "余额不足，请充值"
            return resp

        # 扣减余额
        try:
            update_bal = "UPDATE MEM_INFO SET accou_bal=accou_bal - %d WHERE id= %d"
            c.execute(update_bal, cost, user_id)
            print("扣费成功")
            resp.message = "付款成功"
        except Exception as e:
            self.conn.rollback()
            print("扣费失败：", e)

        # 查询库存
        print('query item_info')
        c.execute('''SELECT num FROM item_info WHERE item_id= %d''' % item_id)
        num = c.fetchone()

        # 判断库存
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
            c.execute('''INSERT INTO order_info(id order_id, item_id, description, item_num) VALUES(NULL, '%s', %d, '%s', %d);''' %
                     (order_id, item_id, description, request.item_num))

        # 5 UPDATE item_info-->num
            item_id = request.item_id
            item_num = request.item_num
            update_num = "UPDATE item_info SET NUM= NUM- %s where item_id= %s"
            c.execute(update_num, (item_num, item_id))
            print("修改库存成功")
        except Exception as e:
            self.conn.rollback()
            print("insert_error:", e)
            return gen_error_resp(errors.ERR_INPUT_INVALID)

        # 6 commit
        print('transaction commit')
        self.conn.commit()

        # 7 return resp
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
        resp = exercise_pb2.ReturnResp()
        order_id = request.order_id
        user_id = request.user_id
        # print("type_order_id:", type(order_id))
        print("order_id: ", order_id)
        c = self.conn.cursor()

        try:
            self.conn.begin()

            # 通过order_id查找item_id
            # item_id_ret = "SELECT 'item_id' FROM order_info WHERE 'order_id'= %s "    为什么这个读不出正确的数据
            # c.execute(item_id_ret, order_id)
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

            # 写入退单操作
            order_ret = "INSERT INTO order_info(order_id, item_id, item_num, control_id) VALUES(%s, %s, %s, %s)"
            c.execute(order_ret, (order_id_ret, item_id_ret, request.return_num, 1))
            print("写入退单信息成功：INSERT INTO order_info")

            # 修改库存
            print("item_id_ret:", item_id_ret)
            item_num = "UPDATE ITEM_INFO SET NUM= NUM + %s WHERE ITEM_ID = %s"
            c.execute(item_num, (request.return_num, item_id_ret))
            print("修改库存完成")
            resp.result = '退单完成'

            # 金额沿路退还-->查询余额-->修改余额
            try:
                # 查询余额
                sele_bal = "SELECT accou_bal FROM MEM_INFO WHERE id= %d FOR UPDATE"
                c.execute(sele_bal, user_id)
                user_bal = c.fetchone()
                print("返回余额")
            except Exception as e:
                print("退款余额失败:", e)
                self.conn.rollback()
                self.conn.commit()
                resp.result = "退款失败"
                return resp

            # 修改余额
            try:
                update_bal = "UPDATE MEM_INFO SET accou_bal= accou_bal + %d"
                c.execute(update_bal, user_bal)
                resp.result = "退款成功"
                print("更新余额成功")
            except Exception as e:
                print("更新余额失败:", e)
                self.conn.rollback()
                resp.result = "退款失败"
                return resp
            self.conn.commit()
            return resp
        except Exception as e:
            self.conn.rollback()
            self.conn.commit()
            print("余额写入出错，原因：", e)
            resp.result = "退单失败"
            return resp

    # 注册接口
    def Register(self, request, context):
        resp = exercise_pb2.RegisteredResp()
        name = request.name
        keyword = request.keyword
        call_num = request.call_num
        gender = request.gender

        # TODO
        # birthday = request.birthday
        if len(keyword) < 6:
            resp.result = "密码长度太短"
            print("密码错误")
            return resp
        # 电话-限制格式和类型
        if len(call_num) < 11 or len(call_num) > 11:
            resp.result = "电话号码格式不正确"
            print("电话号码错误")
            return resp

        salt = "66666"
        message = bytes(keyword, encoding='utf-8')
        salt = bytes(salt, encoding='utf-8')

        key_md5 = hmac.new(salt, message, digestmod='MD5')
        print("完成加密")

        key = key_md5.hexdigest()
        print("hexdigest of key:", key)

        with self.conn.cursor() as c:
            try:
                insert_register = "INSERT INTO MEM_INFO(name, keyword, call_num, gender) VALUES( %s, %s, %s, %s)"
                c.execute(insert_register, (name, key, call_num, gender))
                print("写入注册信息成功")
                resp.result = "注册成功"
                self.conn.commit()
                return resp
            except Exception as e:
                print("注册出错，原因：", e)
                resp.result = "注册失败"
                return resp

    # 登录接口
    def Login(self, request, context):
        resp = exercise_pb2.LoginResp()
        name = request.name
        keyword = request.keyword

        salt = "66666"
        message = bytes(keyword, encoding='utf-8')
        salt = bytes(salt, encoding='utf-8')

        key_md5 = hmac.new(salt, message, digestmod='MD5')
        key = key_md5.hexdigest()
        print("hexdigest of key:", key)

        # 验证账号是否存在

        print("验证账号信息")
        with self.conn.cursor() as c:
            try:
                name_sql = "SELECT name FROM MEM_INFO"
                c.execute(name_sql)
                name_tuple = c.fetchall()[0][0]
                print("name:", name_tuple)
                c.close()
            except Exception as e:
                print("验证账号出错:", e)

        if name_tuple is None:
            request.result = "账号密码错误"
            print("账号错误")
            return resp

        # 验证密码
        print("验证密码")
        with self.conn.cursor() as c:
            key_sql = "SELECT keyword FROM MEM_INFO WHERE name=%s"
            c.execute(key_sql, name)
            key_tuple = c.fetchall()[0][0]
            print("key_tuple:", key_tuple)

        print("验证完成")
        if key in key_tuple:
            resp.result = "登录成功"
            print("存在用户信息")
            return resp
        else:
            resp.result = "账号或密码错误"
            return resp

    # 充值接口
    def Recharge(self, request, context):
        resp = exercise_pb2.RechargeResp()
        money = request.money
        name = request.name
        keyword = request.keyword

        salt = "66666"
        salt = bytes(salt, encoding='utf-8')
        message = bytes(keyword, encoding='utf-8')

        key_md5 = hmac.new(salt, message, digestmod='MD5')
        key = key_md5.hexdigest()

        # 验证账号是否存在
        print("验证账号")
        with self.conn.cursor() as c:
            name_sql = "SELECT name FROM MEM_INFO"
            c.execute(name_sql)
            name_tuple = c.fetchall()[0]
            c.close()

        if name not in name_tuple:
            resp.result = "账号不存在"
            print("账号不存在")
            return resp

        # 验证密码
        print("验证密码")
        with self.conn.cursor() as c:
            key_sql = "SELECT keyword FROM MEM_INFO WHERE name=%s"
            c.execute(key_sql, name)
            key_tuple = c.fetchall()[0]
            c.close()

        if key in key_tuple:
            resp.result = "登录成功"
            print("登录成功")
            with self.conn.cursor() as c:
                accu_name = "SELECT id FROM MEM_INFO WHERE keyword=%s"
                c.execute(accu_name, key)
                user_id = c.fetchone()[0]
                print("获取对应用户信息")
        else:
            resp.result = "账号或密码错误"
            return resp

        self.conn.begin()
        with self.conn.cursor() as c:
            try:
                check_bal = "SELECT accou_bal FROM MEM_INFO WHERE id=%s for update"
                c.execute(check_bal, user_id)
            except Exception as e:
                print("查询余额失败：", e)
                resp.result = "查询余额有误"
                self.conn.commit()
                c.close()
                return resp

            try:
                add_bal = "UPDATE MEM_INFO SET accou_bal=accou_bal + %s"
                c.execute(add_bal, money)
            except Exception as e:
                print("修改余额失败：", e)
                resp.result = "充值失败"
                self.conn.rollback()
                c.close()
                return resp
            finally:
                self.conn.commit()
                c.close()
        resp.result = "充值成功"
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
