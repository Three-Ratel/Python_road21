#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, json, struct, os

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
while True:
    con, addr = sk.accept()

    def send():
        """
        解析用户即将下载的文件名
        """
        s_first = con.recv(4)
        s_size = struct.unpack('i', s_first)[0]
        file_name = con.recv(s_size).decode('utf-8')

        if not os.path.exists(file_name):
            con.send(b'qq')
            return
        con.send(b'ok')

        file_size = os.path.getsize(file_name)
        send_size = 0
        info = {'file_name': file_name, 'file_size': file_size}
        b_info = json.dumps(info).encode('utf-8')
        s_first = struct.pack('i', len(b_info))
        con.send(s_first)
        con.send(b_info)
        f = open(file_name, mode='rb')
        while True:
            percent = round(send_size / file_size * 100, 3)
            print('文件传输中，已传输%s%% \r' % (percent,), end='')
            chunk = f.read(1024)
            con.send(chunk)
            if not chunk: break
            send_size += 1024
        print('文件传输完成')
        con.close()


    if __name__ == '__main__':
        send()
