#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server


def home(url):
    s = '这是页面{}'.format(url)
    print(s)
    return s.encode('utf-8')


def index(url):
    s = '这是页面{}'.format(url)
    print(s)
    return bytes(s, encoding='utf-8')


url_li = {'/index/': index, '/home': home}


def run(environ, start_response):
    # 设置http响应头
    start_response('200 ok', [('Content-Type', 'text/html;charset=utf8'), ])
    url = environ['PATH_INFO']
    # print(url, )
    if url_li.get(url):
        response = url_li[url](url)
    else:
        response = b'404 not found'
    return [response, ]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, run)
    print("我在8090等你哦...")
    httpd.serve_forever()
