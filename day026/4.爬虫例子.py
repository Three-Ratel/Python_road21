#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import re, time


def parser_page(par, content):
    """
    :param par: 编译过的正则表达式
    :param content: 需要匹配的目标
    :return:
    """
    res = par.finditer(content)
    for i in res:
        yield {'id': i.group('id'),
               'title': i.group('title'),
               'score': i.group('score'),
               'com_num': i.group('comment_num')}


def get_page(url):
    ret = requests.get(url)
    return ret.text


pattern = '<div class="item">.*?<em class="">(?P<id>\d+)</em>.*?<span class="title">(?P<title>.*?)</span>.*?\
            <span class="rating_num".*?>(?P<score>.*?)</span>.*?<span>(?P<comment_num>.*?)人评价</span>'
par = re.compile(pattern, flags=re.S)

num = 0

with open('movie_info.txt', mode='w', encoding='utf-8') as f:
    for i in range(10):
        content = get_page('https://movie.douban.com/top250?start=%s&filter=' % num)
        g = parser_page(par, content)

        for dic in g:
            f.write('%s\n' % json.dumps(dic, ensure_ascii=False))
            # json.dump(dic, f, ensure_ascii=False)
            # f.write('\n')
        num += 25

