#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, time
from socket import SOL_SOCKET, SO_REUSEADDR

sk = socket.socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8000))
sk.listen(5)


# def home(url):
#     with open('./html/home.html', 'rb') as f:
#         data = f.read()
#     return data


def index(url):
    with open('./html/index.html', 'rb') as f:
        data = f.read()
    return data

# 返回动态页面
def home(url):
    with open('./html/home.html', 'r', encoding='utf-8') as f:
        data = f.read().replace('@@time@@', time.strftime('%H:%M:%S')).encode('utf-8')
    return data


url_li = {'/index': index, '/home': home}

while True:
    con, addr = sk.accept()
    data = con.recv(1024).decode('utf-8')
    url = data.split()[1]
    con.send(b'HTTP/1.1 200 ok\r\n\r\n')
    if url_li.get(url):
        data = url_li[url](url)
    else:
        data = b'404 not found'
    con.send(data)
    con.close()
sk.close()
