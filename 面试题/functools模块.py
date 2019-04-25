# __all__ = ['update_wrapper', 'wraps', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES',
#            'total_ordering', 'cmp_to_key', 'lru_cache', 'reduce', 'partial',
#            'partialmethod', 'singledispatch']

# 总共11个

"""
1. functools.partial
"""
"""
作用:
functools.partial 通过包装手法，允许我们 "重新定义" 函数签名
用一些默认参数包装一个可调用对象,返回结果是可调用对象，并且可以像原始对象一样对待
冻结部分函数位置函数或关键字参数，简化函数,更少更灵活的函数参数调用
"""
from functools import partial


def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2)
test = square(5)
print(test)


"""
2. functools.reduce
"""

# functools.reduce(function, iterable[, initializer])等同于内置函数reduce()用这个的原因是使代码更兼容(python3)


"""
3. 
"""


