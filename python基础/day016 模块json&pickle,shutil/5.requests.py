#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

content = requests.get('http://www.baidu.com')
print(content.text, type(content.text))
