#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""socket tcp"""
# from socket import socket, SO_REUSEADDR, SOL_SOCKET
#
# sk = socket()
# sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# sk.bind(('127.0.0.1', 9000))
# sk.listen()
# con, _ = sk.accept()
# while True:
#     msg = con.recv(1024).decode('utf8')
#     con.send(msg.upper().encode('utf8'))

"""socket udp"""
# import socket
#
# sk = socket.socket(type=socket.SOCK_DGRAM)
# sk.bind(('127.0.0.1', 9000))
# while True:
#     msg, addr = sk.recvfrom(1024)
#     msg = msg.decode('utf8')
#     sk.sendto(msg.upper().encode('utf8'), addr)


"""非阻塞io模型"""
# 连接存在，recv会报错，连接不存在接收为空
# import time
# from socket import socket, SOL_SOCKET, SO_REUSEADDR
#
# sk = socket()
# sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# sk.bind(('127.0.0.1', 9000))
# sk.setblocking(False)               # 设置为非阻塞状态
# sk.listen()
#
# user = []
# del_user = []
# while True:
#     try:
#         con, addr = sk.accept()
#         user.append(con)
#     except BlockingIOError:
#         for i in user:
#             try:
#                 content = i.recv(1024).decode('utf-8')
#                 if not content:
#                     del_user.append(i)
#                     continue
#                 i.send(content.upper(). encode('utf-8'))
#             except BlockingIOError: pass
#
#         for i in del_user:
#             user.remove(i)
#         del_user.clear()
#         time.sleep(1)
# sk.close()


"""socketserver模块"""
import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            msg = self.request.recv(1024).decode('utf8')
            self.request.send(msg.upper().encode('utf8'))


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), MyServer)
server.serve_forever()