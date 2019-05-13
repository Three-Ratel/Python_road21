#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle


def pickle_write():
    f = open('books_info', mode='ab')
    while True:
        book_name = input('请输入书名(Q/q): ').strip()
        if book_name.upper() == 'Q': break
        while True:
            book_num = input('请输入数量: ').strip()
            if book_num.isdecimal(): break
        dic = {'book_name': book_name, 'book_num': book_num}
        pickle.dump(dic, f)
    f.close()

# pickle_write()

def pickle_read():
    f = open('books_info', mode='rb')
    try:
        while True:
            dic = pickle.load(f)
            print(dic['book_name'], dic['book_num'])
    except:pass
    f.close()

pickle_read()