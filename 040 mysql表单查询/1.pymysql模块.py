#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import pymysql
#
# con = pymysql.connect(host='localhost', user='root', password='root', database='day40')
# """默认为tuple类型，指定为dict类型"""
# cur = con.cursor(pymysql.cursors.DictCursor)
# """插入"""
# # cur.execute("insert into employee(emp_name, sex, age, hire_date) values('echo', 'male', 19, 20190808)")
# """删除"""
# # cur.execute("delete from employee where emp_name = 'echo'")
# """修改"""
# # cur.execute("update employee set age=20 where emp_name = 'henry'")
# """查询"""
# cur.execute("select emp_name,age from employee where age > 20")
# ret = cur.fetchall()
# print(ret)
#
# con.commit()
# con.close()



import pymysql

# con = pymysql.connect(host='localhost', user='root', password='root', database='day39')
# cur = con.cursor(pymysql.cursors.DictCursor)
# cur.execute('select emp_name from employee where age > 30')
# ret = cur.fetchall()
# print(ret)
# con.commit()
# con.close()