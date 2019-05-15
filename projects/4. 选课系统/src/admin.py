#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import os, sys

    PATH = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(PATH)

    from bin import view_course, course, creat_course, creat_student, view_select, view_student, pwd_modified
    from lib import logger


    class Admini(object):

        def __call__(self, *args, **kwargs):

            while True:
                print("""
                       1. 创建课程
                       2. 创建学生账号
                       3. 查看所有课程 
                       4. 查看所有学生
                       5. 查看所有学生选课情况
                       6. 修改管理员密码
                       7. 退出程序
                       
                       """)
                choice = input('请输入功能序号：')
                funcs = {'1': Admini.creat_course, '2': Admini.creat_student, '3': Admini.view_course,
                         '4': Admini.view_student, '5': Admini.view_select, '6': Admini.modified, '7': Admini.end_pro}
                if not funcs.get(choice):
                    print('输入有误，请重新输入')
                    continue
                funcs.get(choice)()

        @staticmethod
        def creat_course():
            creat_course.creat_course()

        @staticmethod
        def creat_student():
            creat_student.creat_student()

        @staticmethod
        def view_course():
            view_course.view_course()

        @staticmethod
        def view_student():
            view_student.view_student()

        @staticmethod
        def view_select():
            view_select.view_select()

        @staticmethod
        def modified():
            pwd_modified.pwd_modified()

        @staticmethod
        def end_pro():
            exit(0)


    if __name__ == '__main__':
        Admini()()

except Exception as e:
    logger.logger(e)
