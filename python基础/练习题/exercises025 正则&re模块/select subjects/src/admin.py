#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle, os, sys

PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PATH)
from src import student
from bin import view_course, course
from lib import get_md5

path = os.path.join(PATH, 'db')
course_list = os.path.join(path, 'course_list.txt')
student_list = os.path.join(path, 'student_list.txt')


class Admini(object):

    def __call__(self, *args, **kwargs):

        while True:
            print("""
                   1. 创建课程
                   2. 创建学生账号
                   3. 查看所有课程
                   4. 查看所有学生
                   5. 查看所有学生选课情况
                   6. 退出程序
                   """)
            choice = input('请输入功能序号(N/n)：')
            if choice.upper() == 'N':
                return
            funcs = {'1': Admini.creat_course, '2': Admini.creat_student, '3': Admini.view_course,
                     '4': Admini.view_student, '5': Admini.view_select, '6': Admini.end_pro}
            if not funcs.get(choice):
                print('输入有误，请重新输入')
                continue
            funcs.get(choice)()

    @staticmethod
    def creat_course():
        while True:
            name = input('please input the course name(N/n): ').ljust(8)
            if name.strip().upper() == 'N':
                break
            price = input('please input the course price: ').ljust(8)
            period = input('please input the course period: ').ljust(8)
            teacher = input('please input the course teacher: ').ljust(8)
            val = course.Course(name, price, period, teacher)
            with open(course_list, mode='ab') as f:
                pickle.dump(val, f)

    @staticmethod
    def creat_student():
        while True:
            name = input('please input the course name(N/n): ')
            if name.upper() == 'N':
                break
            pwd = get_md5.get_md5('123')
            val = student.Student(name, pwd)
            with open(student_list, mode='ab') as f:
                pickle.dump(val, f)

    @staticmethod
    def view_course():
        view_course.view_course()

    @staticmethod
    def view_student():
        if not os.path.exists(student_list):
            print('学生账号信息为空')
            return
        f = open(student_list, mode='rb')
        while True:
            try:
                v = pickle.load(f)
                print(v.name)
            except:
                break
        f.close()

    @staticmethod
    def view_select():
        pass

    @staticmethod
    def end_pro():
        exit(0)


if __name__ == '__main__':
    Admini()()


