#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', database='test', charset='utf8')
cur = db.cursor(pymysql.cursors.DictCursor)

sql = 'select count(*) from test1'
sql1 = 'desc test1'
i_li = []
try:
    cur.execute(sql1)
    res = cur.fetchall()
    # print(res)
    for i in res:
        # print(i['Field'])
        i_li.append(i['Field'])

except:
    # db.rollback()
    pass

print(i_li)
cur.close()








