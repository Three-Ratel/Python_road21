#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, os, json, struct


file_name = '肖申克的救赎.rmvb'
path = os.path.join('/Users/henry/Movies/Movies', file_name)


def upload(file_name):
    sk = socket.socket()
    sk.connect(('127.0.0.1', 9000))

    file_size = os.path.getsize(path)
    send_size = 0
    f = open(path, mode='rb')
    info = {'file_name': file_name, 'file_size': file_size}
    b_info = json.dumps(info).encode('utf-8')
    s_first = struct.pack('i', len(b_info))
    sk.send(s_first)
    sk.send(b_info)

    while True:
        percent = round(send_size/file_size * 100, 3)
        print('文件传输中，已传输%s%% \r' % (percent,), end='')
        chunk = f.read(1024)
        sk.send(chunk)
        if not chunk: break
        send_size += 1024

    print('文件传输完成')
    sk.close()


if __name__ == '__main__':
    upload(file_name)
