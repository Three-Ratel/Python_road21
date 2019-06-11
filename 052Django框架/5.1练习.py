#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jinja2 import Template
from wsgiref.simple_server import make_server


def index(url):
    with open('html/index2.html', mode='r', encoding='utf8') as f:
        data = f.read()
        data = Template(data)
        data = data.render({'name':'henry', 'hobby': ['reading',]})
    return bytes(data, encoding='utf8')


info = {'/index/': index}


def run(environ, start_response):
    start_response('200 ok', [('Content-type', 'text/html; charset=utf8'), ])
    url = environ['PATH_INFO']
    if info.get(url):
        data = info[url](url)
    else:data = b'404 not found'
    return [data, ]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, run)
    httpd.serve_forever()









