#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

fields:由”|”连接的以"fld"开头的字符串,如:fld2|fld3|fld7|fld19 提示:请考虑字典的嵌套层数不是固定的
"""
"""
"fld1":1, "fld2":2},
"fld3":0, "fld5":0.4},
"""
data = {"time": "2016-08-05T13:13:05",
        "some_id": "ID1234",
        "grp1": {"xxx2": {"fld6": 11, "fld7": 7, "fld46": 8}}}

fields = 'fld2|fld3|fld7|fld19'


def select(data, fields):
    for i in data.keys():
        print(i, data[i])
        # if type(data[i]) is dict:


    # return result


select(data, fields)
