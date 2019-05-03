#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bin import view_course, select_course , look_select, pwd_modified


class Student(object):
    def __init__(self, name=None, pwd=None):
        self.name = name
        self.pwd = pwd

    def __call__(self, *args, **kwargs):
        while True:
            print("""
                          1. 查看课程
                          2. 选择课程
                          3. 查看所选课程
                          4. 修改密码
                          5. 退出程序
                          """)
            choice = input('请输入功能序号：')
            funcs = {'1': Student.look_course, '2': Student.select,
                     '3': Student.look, '4': Student.modified,
                     '5': Student.end_pro}
            if not funcs.get(choice):
                print('输入有误，请重新输入')
                continue
            funcs.get(choice)()

    @staticmethod
    def look_course():
        view_course.view_course()

    @staticmethod
    def select():
        select_course.select_course()

    @staticmethod
    def look():
        look_select.look_select()

    @staticmethod
    def modified():
        pwd_modified.pwd_modified()

    @staticmethod
    def end_pro():
        exit()


if __name__ == '__main__':
    Student()()
