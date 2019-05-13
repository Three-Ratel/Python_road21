#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import pickle


class Library(object):
    # l_li 表示借阅书籍的集合
    l_li = set()

    def __call__(self):
        f = open('borrow_books.txt', mode='rb')
        self.l_li = pickle.load(f)
        f.close()

    def login(self, user_name, user_pwd):
        if user_name == 'alex' and user_pwd == '123':
            print('登陆成功')
            return True
        else:
            print('登陆失败')

    # 把借阅的图书写入文件
    def write(self):
        f = open('borrow_books.txt', mode='wb')
        pickle.dump(self.l_li, f)
        f.close()

    # 1. 查看所有图书列表
    def ls_dir(self):
        with open('books_info.txt', mode='rb') as f:
            try:
                while True:
                    dic = pickle.load(f)
                    print(dic['book_name'], dic['book_num'])
            except:
                pass

    # 2. 将图书添加到借阅列表
    def add_book(self):

        while True:
            book_name = input('请输入借阅书名(Q/q)：').strip()
            if book_name.upper() == 'Q': break
            f = open('books_info.txt', mode='rb')
            try:
                while True:
                    dic = pickle.load(f)
                    if dic['book_name'] == book_name:
                        self.l_li.add(dic['book_name'])
                        print(self.l_li)
            except:
                f.close()

        # 把借阅的图书写入文件
        self.write()


    # 3. 查看已经借阅的图书
    def view_book(self):
        count = 0
        for i in self.l_li:
            count += 1
            print(count, i)

    # 4. 归还图书
    def back_book(self):
        while True:
            book_name = input('请输入要归还书名(Q/q)：').strip()
            if book_name.upper() == 'Q': break
            if book_name in self.l_li:
                self.l_li.discard(book_name)
                print('%s已归还' % book_name)

        # 把借阅的图书写入文件
        self.write()

    # 5. 退出程序
    def exit_func(self):
        return 'q'


def run():
    # 登陆
    while True:
        print('***** 欢迎登陆网络图书馆 *****')
        user_name = input('用户名：')
        user_pwd = input('用户密码：')
        obj = Library()
        obj()
        if obj.login(user_name, user_pwd):break

    # 2）中操作
    while True:
        print("""
                1. 查看所有图书列表
                2. 将图书添加到借阅列表
                3. 查看已经借阅的图书
                4. 归还图书
                5. 退出程序  
               """)
        choice = input('请输入功能选项：')
        funcs_dic = {'1': obj.ls_dir, '2': obj.add_book, '3': obj.view_book,
                     '4': obj.back_book, '5': obj.exit_func}
        if not funcs_dic.get(choice): continue
        val = funcs_dic[choice]()
        if val == 'q': return


if __name__ == '__main__':
    run()
