#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hmac

h = hmac.new(bytes('898oaFs09f', encoding="utf-8"))
h.update(bytes('admin', encoding="utf-8"))
print(h.hexdigest())



