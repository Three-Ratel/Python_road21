#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

con = pymysql.connect('localhost', 'root', 'root', 'test')

cur = con.cursor()

sql = 'insert into lock_test(money) values(30000)'

try:
    cur.execute(sql)
    con.commit()
except:
    con.rollback()

cur.close()
con.close()


