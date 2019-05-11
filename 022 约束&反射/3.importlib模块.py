#!/usr/bin/env python
# -*- coding:utf-8 -*-

import importlib
path = 'utils.redis.func'
module_path, func_name = path.rsplit('.', 1)
getattr(module_path, 'func_name')()
