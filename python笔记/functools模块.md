functools：Higher-order functions and operations on callable objects

functools模块是一个高阶函数，即在函数上(any callable object)进行操作，并返回函数。 
用一些默认参数包装一个可调用对象,返回结果是可调用对象，并且可以像原始对象一样对待

冻结部分函数位置函数或关键字参数，简化函数,更少更灵活的函数参数调用

1. **functors.partial**

```python
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
```

```python
# 示例
def power(base, exponent):
    return base ** exponent

from functools import partial
square = partial(power, exponent=2)
test = square(5)
print(test)

25
```

