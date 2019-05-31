## 今日内容

1. | ：或只负责把两个表达式分开，如果是整个表达式中只对一部分内容进行或，需要分组

2. ()：限定一组正则的量词约束 (\d\w)?

3. 以a开头，由至少一个字母组成的字符串

```python
^a[a-zA-Z]+
^a[a-zA-Z]*
```

3. 以1开头，中间3-5个数字，如果中间位置超过5个数字，则整个字符串不匹配

```python
^1\d{3,5}$
```



## 内容详情

1. re模块：

   - python中的方法（+正则表达式）：分组写法、分组命名、引用分组

   - 转义符
   - 爬虫例子



## 1. 转义符

1. \：表示转义   匹配 \n :\\\n
   - 需要匹配几个 \ ,需要2倍的 \ 的个数（**工具中**）
   - 正则表达式中的转义符，在python的字符串中也刚好有转义作用
   - 正则表达式中的转义字符和字符串中的转义字符并没有关系
   - 容易有冲突
   - 为了避免：所有正则都以在工具中测试为结果
   - 在正则和待匹配的字符串前加 **r** ( raw string notation)

## 2. re模块

1. re.findall('\d', 'Alex83')

```python
# 没有匹配到，则返回空list
import re
ret = re.findall('\d+', 'alex83')
print(ret)
```

2. **re.search()**

```python
# 匹配到的结果是一个对象
# 匹配不到则返回 None
import re
ret = re.search('\d+', 'alex83')
print(ret)
# 使用group()方法，从头到尾，从待匹配字符串中取出第一个符合条件项
if ret:
		print(ret.group())   # 匹配不到会报错，使用 if 判断
```

3. re.match()：在search前的正则前加了一个：**^**

```python
# 没有匹配到，则返回 None
# 从字符串开头匹配，匹配上则返回一个match对像，有group()方法
import re
ret = re.match('\d', '8alex83')
print(ret)
```

- 时间复杂度(效率)、空间复杂度(内存)、用户体验
- findall时间和空间压力

4. re.finditer()：有效降低内存占有率，在查询结果超过一个的情况

```python
# 匹配到结果为 迭代器，每一项都是match对象，通过group取值
import re
ret = re.finditer('\d', 'safh123ghakjdsfg234'*2000000)
for i in ret:
  print(i.group())
```

5. re.compile()：同一正则表达式，多次使用

```python
# 循环str，找到符合正则的字符
ret = re.compile('正则表达式')
r1 = ret.search('alex83')
print(r1.group())
```

6. re.sub()/ re.subn()

```python
# 替换 n 次
ret = re.sub('\d', 'G', 'henry18'，n)
print(ret)
# 返回替换次数
ret = re.subn('\d', 'G', 'henry18')
print(ret)
```

7. re.split()

```python
import re
ret = re.split('\d+', 'henry18')
print(ret)
# 保留分组中内容
ret = re.split('(\d+)', 'henry18')
print(ret)
```

## 3. 分组

1. group()：括号中默认为0，即取第0个分组

```python
s = '<h1>wahaha</h1>'
ret = re.search('(\w+)>(.*?)</\w+>', s)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
```

2. **分组命名**(?P<name>正则表达式)
   - name：不需要加引号，本身就是字符串

```python
ret = re.search('<(?P<tag>\w+)>(?P<content>.*?)</\w+>', s)
print(ret.group('tag'))
print(ret.group('content'))
```

3. **引用分组**(?P=name)

```python
s = '<h1>wahaha</h1>'
ret = re.search('(?P<tag>\w+)>.*?</(?P=tag)>', s)
print(ret.group())
```

```python
s = '<h1>wahaha</h1>'
# \1 在python中有特殊含义
ret = re.search(r'(\w+)>.*?</\1>', s)
print(ret.group())
```

4. 取消分组优先(?:)

```python
# findall 遇到正则中的分组 优先 显示分组中的内容
import re
ret = re.findall('\d(\d)', 'henry18')
print(ret)
# 取消分组优先（?:正则表达式）
ret = re.findall('\d+(?:\.\d+)?', '1.234+2')
print(ret)
```

5. split，保留分割符()

```python
# 保留分组中内容
ret = re.split('(\d+)', 'henry18')
print(ret)
```

## 4. 练习

```python
import re
ret = re.findall(r'\d+\.\d+|(\d)', '2+23*3.42/3.2')
print(ret)
ret.remove('')
print(ret)
```

**生成器中send**

```python
def func():
    print(123)
    n = yield('aaa')
    print('----->', n)
    yield 'bbb'

data = func()
next(data)
v = data.send('太厉害了，直接传进去了')
print(v)
```

**爬虫示例**

```python
# 
import requests
ret = requests.get('url')
content = ret.text

ret = re.findall(pattern, content)
print(ret)
```

















