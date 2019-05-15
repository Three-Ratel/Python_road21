#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import os, pickle
    from config import settings
    from lib import get_md5, logger
    from src import student


    def pwd_modified():
        f = open(settings.STUDENT_LIST, mode='rb')
        f1 = open(settings.STUDENT_LIST1, mode='ab')
        while True:
            pwd = input('请输入旧密码(N/n)：').strip()
            if pwd.upper() == 'N':
                f.close()
                f1.close()
                os.remove(settings.STUDENT_LIST)
                os.rename(settings.STUDENT_LIST1, settings.STUDENT_LIST)
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
                            os.remove(settings.STUDENT_LIST)
                            os.rename(settings.STUDENT_LIST1, settings.STUDENT_LIST)
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
                os.remove(settings.STUDENT_LIST)
                os.rename(settings.STUDENT_LIST1, settings.STUDENT_LIST)
                break

except Exception as e:
    logger.logger(e)

