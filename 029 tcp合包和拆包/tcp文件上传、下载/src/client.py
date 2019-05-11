#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, os, json, struct
USER = []

class Client(object):

    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1', 9000))

    def upload(self):
        while True:
            # file_path = input('请输入文件路径(Q)：')
            file_path = '/Users/henry/Documents/文档资料/python文档/正则指引.pdf'
            file_name = os.path.basename(file_path)
            if file_name.upper() == 'Q':
                self.sk.send(b'0')
                return

            if os.path.exists(file_path):
                self.sk.send(b'1')
                break
            print('文件不存在，请重新输入')

        file_size = os.path.getsize(file_path)
        send_size = 0
        f = open(file_path, mode='rb')
        info = {'file_name': file_name, 'file_size': file_size}
        b_info = json.dumps(info).encode('utf-8')
        s_first = struct.pack('i', len(b_info))
        self.sk.send(s_first)
        self.sk.send(b_info)

        while True:
            percent = round(send_size/file_size * 100, 3)
            print('文件传输中，已传输%s%% \r' % (percent,), end='')
            chunk = f.read(1024)
            self.sk.send(chunk)
            if not chunk: break
            send_size += 1024

        print('文件传输完成')

    def download(self):
        # file_name = input('请输入文件名：')
        file_name = '正则指引.pdf'
        """
        给服务器端发送需要下载的文件名
        """
        file_name = file_name.encode('utf-8')
        len_info = struct.pack('i', len(file_name))
        self.sk.send(len_info)
        self.sk.send(file_name)

        s_first = self.sk.recv(2)
        if s_first != b'ok':
            print('文件不存在')
            return

        s_first = self.sk.recv(4)
        s_first = struct.unpack('i', s_first)[0]
        str_info = self.sk.recv(s_first).decode('utf-8')
        info = json.loads(str_info)
        file_name = info['file_name']
        file_size = info['file_size']
        file_path = os.path.join('/Users/henry/Desktop',file_name)
        f = open(file_path, mode='wb')
        receive_size = 0
        while True:
            percent = round(receive_size / file_size * 100, 3)
            print('文件接收中，已接收%s%%\r' % percent, end='')
            if percent == 100.000: break
            content = self.sk.recv(1024)
            f.write(content)
            receive_size += 1024
        print('文件接收完毕')
        f.close()

    def login(self):
        while True:
            user_name = input('请输入用户名(Q/q)：')
            self.sk.send(user_name.encode('utf-8'))
            if user_name.strip().upper() == 'Q':
                return False

            user_pwd = input('请输入密码：')
            self.sk.send(user_pwd.encode('utf-8'))

            msg = self.sk.recv(1024).decode('utf-8')
            if msg == '0':
                print('登陆成功')
                USER.append(user_name)
                return True
            elif msg == '1':
                print('用户名或密码错误，请重新输入\n')
                continue
            elif msg == '2':
                print('网站维护中....\n')
                break

    def run(self):
        while not USER: self.login()
        while True:
            print("""
            1. 文件上传
            2. 文件下载
            
            """)
            choice = input('请输入功能选项(Q)：')
            if choice.upper() == 'Q':
                self.sk.send(choice.encode('utf-8'))
                break
            func_info = {'1': self.upload, '2': self.download}
            if not func_info.get(choice):
                print('选择有误，请重新输入')
                continue
            self.sk.send(choice.encode('utf-8'))
            func_info[choice]()



Client().run()



