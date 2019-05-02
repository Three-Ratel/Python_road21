#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle, os, sys

PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PATH)
from bin import view_course
from config import settings
from lib import get_md5
from src import student

path = os.path.join(PATH, 'db')
course_list = os.path.join(path, 'course_list.txt')
student_list = os.path.join(path, 'student_list.txt')
student_list1 = os.path.join(path, 'student_list1.txt')
select_info = os.path.join(path, 'select_info.txt')
select_info1 = os.path.join(path, 'select_info1.txt')

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
            choice = input('请输入功能序号(N/n)：')
            if choice.upper() == 'N':
                return
            funcs = {'1': Student.look_course, '2': Student.select_course,
                     '3': Student.look_select, '4': Student.pwd_modified,
                     '5': Student.end_pro}
            if not funcs.get(choice):
                print('输入有误，请重新输入')
                continue
            funcs.get(choice)()

    @staticmethod
    def look_course():
        view_course.view_course()

    @staticmethod
    def select_course():

        info = {}
        info['course'] = set()
        while True:
            course_num = input('请输入要选择课程序号(N/n)：').strip()
            if course_num.upper() == 'N':
                return

            f = open(course_list, mode='rb')
            i = 1
            flag1 = False
            while True:
                try:
                    v = pickle.load(f)
                    print(v)
                    print(('%s' % i).ljust(8), v.name, v.price, v.period, v.teacher)
                    if str(i) == course_num:
                        flag1 = True
                        info['name'] = settings.USER
                        if v.name not in info['course']:
                            info['course'].add(v.name)
                        print(info['name'], info['course'])
                    i += 1
                except:
                    break
            if not flag1:
                print('输入有误，请重新输入')
                continue
            f.close()

            f1 = open(select_info1, mode='ab')
            f = open(select_info, mode='rb')
            flag = False
            while True:
                try:
                    user_info = pickle.load(f)
                    if info['name'] == user_info['name']:
                        print(user_info['name'], '----------------------d')
                        flag = True
                        user_info = user_info['course'].union(info['course'])
                        print(user_info['course'], '哈哈哈哈哈')
                    pickle.dump(user_info, f1)
                except:
                    break

            if not flag:
                print('hahahhahahahhahah')
                pickle.dump(info, f1)
            f.close()
            f1.close()
            os.remove(select_info)
            os.rename(select_info1, select_info)


    @staticmethod
    def look_select():
        flag = False
        f = open(select_info, mode='rb')
        while True:
            try:
                user_info = pickle.load(f)
                if settings.USER == user_info['name']:
                    flag = True
                    print('用户：', settings.USER)
                    print('所选课程：', end='')
                    for i in user_info['course']:
                        print(i.ljust(6), end='')
                    break
            except:
                break
            f.close()
        if not flag:
            print('还没有选择任何课程')

    @staticmethod
    def pwd_modified():
        f = open(student_list, mode='rb')
        f1 = open(student_list1, mode='ab')
        while True:
            pwd = input('请输入旧密码(N/n)：').strip()
            if pwd.upper() == 'N':
                return
            pwd = get_md5.get_md5(pwd)
            if pwd == settings.PWD:
                break
            else:
                print('密码输入有误，请重新输入')
                continue

        while True:
            try:
                v = pickle.load(f)
                if v.name == settings.USER:
                    while True:
                        settings.USER = v.name
                        pwd = input('请输入新密码(N/n)：').strip()
                        if pwd.upper() == 'N':
                            f.close()
                            f1.close()
                            return
                        pwd2 = input('请确认新密码：').strip()
                        if pwd != pwd2:
                            continue
                        pwd = get_md5.get_md5(pwd)
                        val = student.Student(v.name, pwd)
                        pickle.dump(val, f1)
                        print('密码修改成功')
                        break
                else:
                    pickle.dump(v, f1)
            except:
                f.close()
                f1.close()
                os.remove(student_list)
                os.rename(student_list1, student_list)
                break

    @staticmethod
    def end_pro():
        exit()


if __name__ == '__main__':
    Student()()
