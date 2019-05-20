#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
2.写一个socket 的udp代码，client端发送一个时间格式，server端按照client的格式返回当前时间
  例如 client发送'%Y-%m-%d'，server端返回'2019-5-20'
"""
import datetime
import socket


sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))
form, addr = sk.recvfrom(1024)
form = form.decode('utf-8')
time = datetime.datetime.now().strftime(form)
sk.sendto(time.encode('utf-8'), addr)

sk.close()






