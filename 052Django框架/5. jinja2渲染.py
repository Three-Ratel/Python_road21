#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jinja2 import Template
from wsgiref.simple_server import make_server


def index(url):
    with open('./html/index2.html', 'r', encoding='utf-8') as f:
        data = f.read()
        # 生成模版文件
        template = Template(data)
        # 把数据填充到模版
        res = template.render({'name': 'henry', 'hobby': ['reading', 'movies', 'musics']})
    return bytes(res, encoding='utf-8')


def home(url):
    with open('.html/home.html', 'rb') as f:
        response = f.read()
    return response


url_li = {'/index': index, '/home': home}


def run_server(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html;charset=utf8'), ])
    url = environ['PATH_INFO']
    if url_li.get(url):
        response = url_li[url](url)
    else:
        response = b'404 not found'
    return [response, ]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, run_server)
    print('here')
    httpd.serve_forever()
