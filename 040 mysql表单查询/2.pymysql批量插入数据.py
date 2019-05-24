#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

con = pymysql.connect(host='localhost', user='root', password='root', database='day40')

cur = con.cursor()
with open('info', encoding='utf-8') as f:
    for i in f:
        a, b, c, d, e = i.strip().split('|')
        com = "insert into book(book_name, author, publisher, price, publish_date) values('%s', '%s', '%s', '%s', '%s' )" % (a, b, c, d, e)
        cur.execute(com)

con.commit()
con.close()
