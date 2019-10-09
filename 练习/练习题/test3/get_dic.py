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
        "grp1": {"fld19": {"fld6": 11, "fld7": 7, "fld46": 8}}}

fields = 'fld6|fld3|fld7|fld19'
fields = fields.split('|')
new_data = {}


def select(data, fields):
    global new_data
    for i in data.keys():
        if i in fields: new_data[i] = data[i]
        if type(data[i]) is not dict:
            continue
        new_data = select(data[i], fields)
    return new_data


print(select(data, fields))
