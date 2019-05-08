#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
response = requests.get('url')
data = response.content
print(data)


