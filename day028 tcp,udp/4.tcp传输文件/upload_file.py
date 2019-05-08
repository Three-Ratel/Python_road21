#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, os
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
file_name = '肖申克的救赎.rmvb'
path = os.path.join('/Users/henry/Movies/Movies', file_name)
size = os.path.getsize(path)
send_size = 0
f = open(path, mode='rb')
sk.send(file_name.encode('utf-8'))
sk.recv(1)
while True:
    percent = round(send_size/size * 100, 3)
    print('文件传输中，已传输%s%% \r' % (percent,), end='')
    chunk = f.read(1024)
    if not chunk: break
    sk.send(chunk)
    send_size += 1024

print('文件传输完成')
sk.close()




