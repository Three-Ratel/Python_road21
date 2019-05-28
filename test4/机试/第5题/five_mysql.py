#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

con = pymysql.connect(host='localhost', user='root', password='root', database='day42')
cur = con.cursor(pymysql.cursors.DictCursor)
"""插入user数据"""
# with open('user', mode='r', encoding='utf-8') as f:
#     for i in f:
#         a, b, c = i.strip().split(',')
#         sql = "insert into user(user_name, password) value(%s, %s)"
#         cur.execute(sql, (b, c))
#         con.commit()

"""插入orders数据"""
# with open('orders', mode='r', encoding='utf-8') as f:
#     for i in f:
#         a, b, c, d = i.strip().split(',')
#         sql = "insert into orders(order_time,payment,uid) values(%s, %s, %s)"
#         print(sql)
#         cur.execute(sql, (b, c, d))
#         con.commit()


"""插入goods数据"""
# with open('goods', mode='r', encoding='utf-8') as f:
#     for i in f:
#         a, b, c, d= i.strip().split(',')
#         sql = "insert into goods(gname,price,g_num) values(%s, %s, %s)"
#         cur.execute(sql, (b, c, d))
#         con.commit()

"""插入goods_orders数据"""
# with open('goods_orders', mode='r', encoding='utf-8') as f:
#     for i in f:
#         a, b, c, d = i.strip().split(',')
#         sql = "insert into goods_orders(g_id,o_id,buy_num) values(%s, %s, %s)"
#         cur.execute(sql, (b, c, d))
#         con.commit()

"""2. 查询加个最贵的商品id及其价格"""
# sql = 'select goods_id,price  max_price from goods where price=(select max(price) from goods)'
# cur.execute(sql)
# ret = cur.fetchall()
# print(ret)

"""3. 求’taibai’购买的所有订单，并按照订单总额从⾼到低排序"""
# sql = "select user_name,payment from (select user_id,user_name from user where user_name='taibai') as u1 inner join orders on u1.user_id=orders.uid order by payment desc;"
# cur.execute(sql)
# ret = cur.fetchall()
# print(ret)


"""4. 求出销量量最⾼高的商品名"""
# sql = "select gname from goods where goods_id = (select g_id from goods_orders group by g_id order by buy_num desc limit 1)"
# cur.execute(sql)
# ret = cur.fetchall()
# print(ret)

"""5. 求出每个⽉月下单的⽤用户⼈人数(执⾏行行select month(time) from orders 来学习month的⽤用法，并完成本题)"""
# sql = "select month(order_time) month, count(uid) people_num from orders group by month(order_time)"
# cur.execute(sql)
# ret = cur.fetchall()
# print(ret)

"""6. 求出本⽉月各商品的销售总⾦金金额和个数，按照个数排序"""

# sql = "select buy_num,price*buy_num total_money from (select * from (select * from orders inner join goods_orders on order_id=o_id) og1 inner join goods on og1.g_id=goods_id) t group by t.g_id order by buy_num"
# cur.execute(sql)
# ret = cur.fetchall()
# print(ret)

cur.close()
con.close()
