#!/usr/bin/env python
# -*- coding:utf-8 -*-
from socket import socket,SOL_SOCKET, SO_REUSEADDR
sk = socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(("127.0.0.1", 9000))
sk.listen()
con, addr = sk.accept()
msg = con.recv(1024)
print(msg)
con.send(b"HTTP/1.1 200 OK \r\n\r\n")
with open('小米商城.htm', mode='r', encoding='utf8') as f:
    data=f.read()
con.send(data.encode("utf-8"))
