#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

HOST, PORT = "127.0.0.1", 9999
data = "hello"

# 创建一个socket链接，SOCK_STREAM代表使用TCP协议
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))          # 链接到客户端
    sock.sendall(bytes(data + "\n", "utf-8")) # 向服务端发送数据
    received = str(sock.recv(1024), "utf-8")# 从服务端接收数据

print("Sent:     {}".format(data))
print("Received: {}".format(received))


