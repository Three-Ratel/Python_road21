#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "day40")
# 使用cursor()方法获取操作游标
cur = db.cursor()
# SQL 查询语句
sql = "SELECT * FROM employee \
       WHERE salary > %s" % (1000)
try:
    ret = cur.execute(sql)           # 执行SQL语句
    print(ret)                       # ret为数据行数
    results = cur.fetchall()         # 获取所有记录列表
    for row in results:
        id = row[0]
        name = row[1]
        gender = row[2]
        age = row[3]
        hire_date = row[4]
        print("id=%s,name=%s,gender=%s,age=%s,hire_date=%s"%(id, name, gender, age, hire_date))
except:
    print("Error: unable to fetch data")
# 关闭数据库连接
db.close()




