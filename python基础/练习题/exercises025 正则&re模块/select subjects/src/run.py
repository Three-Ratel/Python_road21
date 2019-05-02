#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys
PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PATH)
from bin import login
from src import admin, student
from config import settings


def run():
    if not settings.USER:
        login.login()

    if settings.USER == 'admin':
        admin.Admini()()

    else:
        student.Student()()


if __name__ == '__main__':
    run()








