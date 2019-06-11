#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
from socket import SOL_SOCKET, SO_REUSEADDR
sk = socket.socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8000))
sk.listen(5)


def home(url):
    s = '这是页面{}'.format(url)
    print(s)
    return s.encode('utf-8')


def index(url):
    s = '这是页面{}'.format(url)
    print(s)
    return bytes(s, encoding='utf-8')


url_li = {'/index': index, '/home':home}


while True:
    con, addr = sk.accept()
    data = con.recv(1024).decode('utf-8')
    url = data.split()[1]
    con.send(b'HTTP/1.1 200 ok\r\n\r\n')
    # if url == '/index':
    #     data = index(url)
    # elif url == '/home':
    #     data = home(url)
    # else:data = b'404 not found'
    if url_li.get(url):
        data = url_li[url](url)
    else:data = b'404 not found'
    con.send(data)
    con.close()
sk.close()
