#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, json, struct, os

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
while True:
    con, addr = sk.accept()


    def receive():
        s_first = con.recv(4)
        s_first = struct.unpack('i', s_first)[0]
        str_info = con.recv(s_first).decode('utf-8')
        info = json.loads(str_info)
        file_name = info['file_name']
        file_size = info['file_size']

        f = open(file_name, mode='wb')
        receive_size = 0
        while True:
            print('文件接收中，已接收%s%%\r' % round(receive_size / file_size * 100, 3), end='')
            content = con.recv(1024)
            if not content: break
            f.write(content)
            receive_size += 1024
        print('文件接收完毕')
        f.close()
        con.close()

    if __name__ == '__main__':
        receive()


