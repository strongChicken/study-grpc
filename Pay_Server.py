import time
from datetime import datetime
import grpc
import pymysql
import random
import hmac
import re

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

        with self.conn.cursor() as c:
            try:
                ini_sta = "UPDATE mem_info SET status=0"
                c.execute(ini_sta)
                self.conn.commit()
                print("初始化登录状态成功")
            except Exception as e:
                print("初始化登录状态失败：", e)

    # order(not pay) api
    def order(self, request, context):
        resp = exercise_pb2.OrderResp()
        req = exercise_pb2.OrderReq()

    # 1. check the Account Online
        user_id = request.user_id
        c = self.conn.cursor()
        status = "select status from men_info where id= %s"
        c.execute(status, user_id)
        login_status = c.fetchone()[0]

        if login_status == 0:
            resp.result = "请先登录"
            return resp

    # 2. check item AmountAndPrice
        if req.amount <= 0:
            resp.result = "购买数量有误"
            return resp
        self.conn.begin()
        with self.conn.cursor() as c:
            item_amount = "select NUM from item_info where ITEM_ID= %s and PRICE"
            c.execute(item_amount, req.item_id)
            amount = c.fetchone()[0]
            price = c.fetchone()[1]
            c.close()
            self.conn.commit()
            print("check was over")
        if amount == 0:
            resp.result = "库存不足"
            self.conn.close()
            return resp

    # 3. cut the item amount
        elif amount != 0:
            with self.conn.cursor() as c:
                cut_amount = "update item_info set NUM= NUM-1 where ITEM_ID= %s"
                c.execute(cut_amount, req.item_id)
                c.close()

    # 4. write in user_order table
        locatime = time.localtime((time.time()))
        order_id = '%s%d' % (time.strftime('%Y%m%d%H%M%S', locatime), random.randint(1, 1000000))

        payamount = amount*price

        order_time = datetime.now()

        self.conn.begin()
        with self.conn.cursor() as c:
            writeorder = "INSERT INTO ORDER_INFO(order_id, item_id, item_amount, item_money, order_time) " \
                        "VALUES(%s, %s, %s, %s, %s)"
            c.execute(writeorder, (order_id, req.item_id, item_amount, payamount, order_time))
            c.close()
        self.conn.commit()

    # pay api
        # 1. check order alive
        # 2. check user_account money
        # 3. check item_info if get enough or not
        # 4. if pay enough or not
        # 5. write pay_order in table
        # 6. update item_info table

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
        user_id = request.user_id

        print('request:', request)
        # 输入数量不能小于0
        if request.item_num <= 0:
            return gen_error_resp(errors.ERR_INPUT_INVALID)

        c = self.conn.cursor()
        print("检查登录状态")
        status = "select status from mem_info where id= %s"
        c.execute(status, user_id)
        login_status = c.fetchone()[0]

        if login_status == 0:
            resp.message = "请先登录"
            return resp

        description = request.description
        if description is None or description == "":
            description = "NULL"
            print("description:", description)

        # 验证商品id
        # 如果商品id不存在
        print("item_id:", request.item_id)
        item_id = request.item_id
        if item_id == 0:
            return gen_error_resp(errors.ERR_INPUT_INVALID)

        # 对比购买数量和库存
        sele_num = "SELECT num FROM item_info WHERE item_id= %s"
        c.execute(sele_num, item_id)
        warehouse = c.fetchone()[0]
        if request.item_num > warehouse:
            resp.result = "库存不足"
            c.close()
            return resp

        # 事务 --> 查询、判断余额、扣减余额
        # 查询余额
        self.conn.begin()
        global balance
        try:
            money = "SELECT accou_bal FROM MEM_INFO WHERE id= %s"
            c.execute(money, user_id)
            balance = c.fetchone()[0]
            print("查询余额成功")
        except Exception as e:
            print("查询余额出错:", e)

        try:
            price = "SELECT PRICE FROM ITEM_INFO WHERE ITEM_ID= %s"
            c.execute(price, item_id)
            item_price = c.fetchone()[0]
            print("查询单价成功")
        except Exception as e:
            resp.message = "付费失败"
            print("查询单价失败：", e)

        item_num = request.item_num
        print("item_price:", item_price)
        cost = item_price * item_num

        # 判断余额是否足够
        if balance == 0 or balance < cost:
            resp.message = "余额不足，请充值"
            return resp

        # 扣减余额
        try:
            update_bal = "UPDATE MEM_INFO SET accou_bal=accou_bal - %s WHERE id= %s"
            c.execute(update_bal, (cost, user_id))
            update_times = "UPDATE mem_info SET times_consu=times_consu +1 WHERE id= %s"
            c.execute(update_times, user_id)
            self.conn.commit()
            print("扣费成功")
            resp.message = "付款成功"
        except Exception as e:
            self.conn.rollback()
            resp.message = "扣费失败"
            print("扣费失败：", e)
            return resp

        # 查询库存
        print('query item_info')
        c.execute('''SELECT num FROM item_info WHERE item_id= %d''' % item_id)
        num = c.fetchone()[0]
        print("num:", num)

        # 3 生成order id
        print('generating order_id')
        localtime = time.localtime((time.time()))
        order_id = '%s%d' % (time.strftime('%Y%m%d%H%M%S', localtime), random.randint(1, 10000000))

        # 4 写入 order
        order_time = datetime.now()
        print("order_time:", order_time)
        try:
            print("start to insert order")
            order_insert = "INSERT INTO order_info(order_id, item_id, description, item_num, pay_money, control_id, time) " \
                           "VALUES(%s, %s, %s, %s, %s, %s, %s)"
            c.execute(order_insert, (order_id, item_id, description, item_num, cost, 0, order_time))

        # 5 UPDATE item_info-->num
            print("update_num")
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
        item_id = request.item_id
        c = self.conn.cursor()

        # 通过商品id 查询 库存
        try:
            c.execute('''SELECT NUM FROM ITEM_INFO WHERE ITEM_ID= %s''' % item_id)
            print("SELECT NUM FROM ITEM_INFO WHERE ITEM_ID")
            num = c.fetchone()[0]
            print("num:", num)
            if num is None:
                resp.description = "商品id存在"
            else:
                resp.description = ("商品库存: %d" % num)
                print("库存:", num)
            self.conn.close()
            return resp
        except Exception as e:
            print("query item_info error: ", e)
            resp.description = "the num was error"
            return resp

    # 退单接口
    def Return(self, request, context):
        start = time.clock()
        resp = exercise_pb2.ReturnResp()
        order_id = request.order_id
        user_id = request.user_id
        # print("type_order_id:", type(order_id))
        print("order_id: ", order_id)
        c = self.conn.cursor()

        print("检查登录状态")
        status = "select status from mem_info where id= %s"
        c.execute(status, user_id)
        login_status = c.fetchone()[0]

        if login_status == 0:
            resp.result = "请先登录"
            return resp

        try:
            self.conn.begin()

            # 通过order_id查找item_id
            # item_id_ret = "SELECT 'item_id' FROM order_info WHERE 'order_id'= %s "    为什么这个读不出正确的数据
            # c.execute(item_id_ret, order_id)
            # resu = c.fetchone()

            c.execute('''select item_id, control_id from order_info where order_id= %s lock in share mode''', order_id)
            resu = c.fetchone()
            item_id_ret = resu[0]
            print("item_id_ret:", item_id_ret)
            control_id = resu[1]
            if item_id_ret is None:
                resp.result = "订单错误"
                print("查询商品id成功")
                self.conn.rollback()
                return resp
            elif control_id == 1:
                resp.result = "订单不能退款"
                print("查询退单状态成功")
                return resp
            else:
                print("退款查询商品id 成功：", item_id_ret)

            c.execute('''SELECT item_num FROM order_info WHERE order_id=%s''', order_id)
            return_num = c.fetchone()[0]
            print("查询退单数量成功")

            # 生成退款order_id_ret
            localtime = time.localtime(time.time())
            order_id_ret = '%s%d' % (time.strftime('%Y%m%d%H%M%S', localtime), random.randint(1, 10000000))
            resp.order_id_ret = order_id_ret
            print("生成退款订单号:", order_id_ret)

            # 写入退单操作
            order_time = datetime.now()
            order_ret = "INSERT INTO order_info(order_id, item_id, item_num, time, description, pay_money, control_id) " \
                        "VALUES(%s, %s, %s, %s, %s, %s, %s)"
            c.execute(order_ret, (order_id_ret, item_id_ret, return_num, order_time, 'return', 0, 1))
            print("写入退单信息成功：INSERT INTO order_info")

            # 修改原订单状态
            try:
                update_control_id = "UPDATE order_info SET control_id= 1 WHERE order_id= %s"
                c.execute(update_control_id, order_id)
                print("修改订单状态成功")
            except Exception as e:
                print("修改订单状态失败：", e)

            # 修改库存
            print("item_id_ret:", item_id_ret)
            item_num = "UPDATE ITEM_INFO SET NUM= NUM + %s WHERE ITEM_ID = %s"
            c.execute(item_num, (return_num, item_id_ret))
            print("修改库存完成")
            resp.result = '退单完成'

            # 金额沿路退还-->计算退款金额-->修改余额
            item_price = "SELECT price FROM item_info WHERE item_id= %s"
            c.execute(item_price, item_id_ret)
            price = c.fetchone()[0]
            money_re = return_num * price

            # 修改余额
            try:
                update_bal = "UPDATE MEM_INFO SET accou_bal= accou_bal + %s"
                c.execute(update_bal, money_re)
                resp.result = "退款成功"
                print("更新余额成功")
            except Exception as e:
                print("更新余额失败:", e)
                self.conn.rollback()
                resp.result = "退款失败"
                return resp

            end = time.clock()
            diff_time = end - start

            try:
                insert_cus = "INSERT INTO customer_order(user_id, done, money, time, diff_time) VALUES(%s, %s, %s, %s, %s)"
                c.execute(insert_cus, (user_id, 'return', money_re, order_time, diff_time))
            except Exception as e:
                print("记录退单信息失败：", e)
            self.conn.commit()
            return resp
        except Exception as e:
            self.conn.rollback()
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
        birthday = request.birthday

        if re.match(r'(^1|2[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])', birthday) is None:
            resp.result = "生日日期填写有误"
            print("生日有误")
            return resp

        if re.match(r'^\w[0-9a-zA-Z]{6,10}', keyword) is None:
            resp.result = "密码长度太短"
            print("密码错误")
            return resp

        # 电话-限制格式和类型
        if re.match(r'^1[0-9]{1,11}', call_num) is None:
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
                insert_register = "INSERT INTO MEM_INFO(name, keyword, call_num, gender, birthday) VALUES( %s, %s, %s, %s, %s)"
                c.execute(insert_register, (name, key, call_num, gender, birthday))
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
            try:
                find_user_id = "SELECT id FROM mem_info WHERE name=%s AND keyword=%s"
                c.execute(find_user_id, (name, key))
                user_id = c.fetchone()[0]
                change_sta = "UPDATE mem_info SET status=1 WHERE id=%s"
                c.execute(change_sta, user_id)
                resp.result = "登录成功"
                self.conn.commit()
                print("存在用户信息")
                c.close()
                return resp
            except Exception as c:
                print("验证出错:", c)
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

        if money <= 0 or money == " " or money is None:
            resp.result = "充值金额输入错误"
            print("充值金额输入错误")
            return resp

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
                c.close()
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
                resp.result = "查询余额出错"
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
