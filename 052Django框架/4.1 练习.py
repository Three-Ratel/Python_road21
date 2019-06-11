#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server


def index(url):
    s =  '{1}{0}'.format(url, '我是').encode('utf-8')
    print(s)
    return s


info = {'/index/': index}


def run(environ, start_response):
    url = environ['PATH_INFO']
    start_response('200 ok', [('Content-Type', 'text/html; charset=utf8'), ])
    if info.get(url):
        data = info[url](url)
    else:
        data = b'404 not found'
    return [data, ]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, run)
    httpd.serve_forever()
