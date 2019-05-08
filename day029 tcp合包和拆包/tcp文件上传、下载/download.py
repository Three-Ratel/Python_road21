#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, os, json, struct


file = '肖申克的救赎.rmvb'


def download(file_name):
    sk = socket.socket()
    sk.connect(('127.0.0.1', 9000))
    """
    给服务器端发送需要下载的文件名
    """
    file_name = file_name.encode('utf-8')
    len_info = struct.pack('i', len(file_name))
    sk.send(len_info)
    sk.send(file_name)

    s_first = sk.recv(2)
    if s_first != b'ok':
        print('文件不存在')
        sk.close()
        return


    s_first = sk.recv(4)
    s_first = struct.unpack('i', s_first)[0]
    str_info = sk.recv(s_first).decode('utf-8')
    info = json.loads(str_info)
    file_name = info['file_name']
    file_size = info['file_size']
    file_path = os.path.join('/Users/henry/Desktop',file_name)
    f = open(file_path, mode='wb')
    receive_size = 0
    while True:
        print('文件接收中，已接收%s%%\r' % round(receive_size / file_size * 100, 3), end='')
        content = sk.recv(1024)
        if not content: break
        f.write(content)
        receive_size += 1024
    print('文件接收完毕')
    f.close()
    sk.close()


if __name__ == '__main__':
    download(file)
