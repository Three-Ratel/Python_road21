# 第一章 计算机基础

## 1. 计算机概览

## 1.1 计算机硬件

计算机的主要组成部分时主板、CPU、硬盘、内存及一些外设设备组成。

##  1.2 常见的操作系统

​	操作系统（OS），是最接近物理硬件的系统软件。主要用来协调、控制、分配计算机硬件资源，使计算机各组件可以发挥最优性能。

- windows
  - Win7，win vista，win10，win server（用于服务器）
- linux（开源）
  - CentOs(免费，开源多用于中小企业)
  - RedHat(商业版，收费)
- macos
  - 主要用于办公



## 1.3 软件（解释器/编译器）

​	软件是运行于操作系统之上的应用程序。

​	计算机语言主要是有解释器/编译器/虚拟机，再加上语法规则构成用来开发其他软件的工具。**解释型语言**，通常是由解释器边解释边执行的计算机语言，例如：python、ruby、PHP、perl。**编译型语言**，通常是由编译器编译整个代码文件，生成计算机可以识别的文件，交由计算机处理。



## 1.4 进制

- 二进制. 0b
- 八进制  0o（计算机内部使用）
- 十进制 int(str, base=2/8/16)
- 十六进制(表示).  \x （一般用于计算机显示）



# 第二章 python入门

## 2.1 环境的安装

​	首先，在官网下载py2与py3，2，3版本有很多不兼容所有会存在两个版本共存的问题。目前，mac、ubuntu等一些系统已经内置了python2版本。

​	为了开发需要，我们需要下载并安装python3。用于开发的软件，通常安装版本一般是找**次新**版本进行安装。安装pycharm IDE 开发工具。

​	环境变量的功能，及其配置。环境变量分为，**用户环境变量**（只对当前用户生效）和**系统环境变量**（所有用户均有效）。主要用于终端使用，不需要输入python解释器的完整路径，只要输入pythonx 就可使用。

​	**PATH**：方便用户在终端执行程序。即，将可执行程序所在的目录添加到环境变量，以后直接调用即可。

​	mac的环境变量在**～/.bash_profile**文件中。通常在安装的时候python会自动生成环境变量，无需手动配置。

## 2.2 编码

​	当前，比较通用的编码有ASCII、Unicode、UTF-8、GB2312、GBK。由于计算机最初使用的是ASCII编码，所以其他编码必须兼容ASCII码。

1. ASCII

   ASCII码，**7bits**表示一个字符,最高位用0表示，后来IBM进行扩展，形成8bit扩展的ASCII码。包含所有英文字母和常用的字符，最多可以表示127或256种。

2. Unicode

   Unicode（万国码），随着计算机的普及，计算机需要兼容多国语言，Unicode编码应运而生。**32bits**表示一个字符，总共可以表示**2\*\*32**种不同的符号，远远超出目前所有文字及字符，迄今使用**21bits**。通用的特点换来的是存储空间的浪费，一般只用于计算机内部处理计算。

3. utf-8

   为弥补unicode的不足，utf-8针对unicode进行压缩和优化，去掉前面多余的0，只保留有效部分。完整保留ASCII码，欧洲文字一般用**2bytes**表示，中文一般用**3bytes**表示。

4. GBK

   全称是GB2312-80《信息交换用汉字编码字符集 基本集》，1980年发布，是中文信息处理的国家标准，在大陆及海外使用简体中文的地区（如新加坡等）是强制使用的唯一中文编码。

   中文使用**2bytes**表示。GBK，是对GB2312的扩展，又称GBK**大字符集**，简而言之就是所有亚洲文字的双字节字符。

```python
# IDE:统一使用UTF-8， 全局和项目均如此
```

## 2.3 变量

​	变量的主要作用是为了多次重复使用方便。

```python
# 查看python关键字
import keyword
keyword.kwlist
```

​	**常量**：不允许修改的值，python中只是约定

## 2.4 python基础语法

### 1. **多行显示**

Python语句中一般以新行作为语句的结束符。

但是我们可以使用斜杠**（ \）**将一行的语句分为多行显示，如下所示：

```python
total = item_one + \
        item_two + \
        item_three
```

### 2. 实现换行

```python
input("按下 enter 键退出，其他任意键显示...\n")

# 不换行输出
print(x, end='')
print(y, end='')
```

### 3. 多个变量赋值

```python
a = b = c = 1
a, b, c = 1, 2, "john"
```

### 4. 成员运算符

```python
in						# 如果在指定的序列中找到值返回 True，否则返回 False
not in				# 如果在指定的序列中找到值返回 False，否则返回 True
```

### 5. 身份运算符

```python
is	
# is 是判断两个标识符是不是引用自一个对象	x is y 
类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	
# is not 是判断两个标识符是不是引用自不同对象	x is not y 
类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
```

### 6.  不换行输出

- print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 **end=""**：

### 7.  pyc 文件

​	执行Python代码时，如果导入了其他的 .py 文件，那么，执行过程中会自动生成一个与其同名的 .pyc 文件，该文件就是Python解释器**编译之后产生的字节码**。

**ps**：代码经过编译可以产生字节码；字节码通过反编译也可以得到代码。

## 2.5 py2与py3的区别

1. 字符串类型不同

```python
v = u'henry'
print(v, type(v))  # unicode类型
# py2                  py3 数据类型对应关系
unicode<class>    <--> str
eg.u'alex'        <--> 'alex'
str               <--> bytes
eg.'alex'         <--> b'alex
```

### Note

- bytes类型一般用于文件存储和网络传输

2. 其他不同

|      |                                   | Py2                         | Py3                                                         |
| ---- | --------------------------------- | --------------------------- | ----------------------------------------------------------- |
| 1    | 字符串类型不同                    |                             |                                                             |
| 2    | py2py3默认解释器编码              | ASCII                       | UTF-8                                                       |
| 3    | 输入输出                          | raw_input() ; print         | input() ; print()                                           |
| 4    | int / long                        | int 和 long，除法只保留整数 | 只用int，除法保留小数                                       |
| 5    | range/xrange                      | range/xrange                | 只有range，相当于py2的xrange                                |
| 6    | info.keys,info.values,info .items | 数据类型是list              | 数据类型是<class 'dict_keys'>                               |
| 7    | map/filter                        | 数据类型是list              | 返回的是iterator，可以list()查看<map object at 0x108bfc668> |
| 8    | reduce                            | 内置                        | 移到functools                                               |
| 9    | 模块和包                          | 需要_\_init__.py            | —                                                           |
| 10   | 经典类和新式类                    | 同时拥有                    | 只有新式类                                                  |



# 第三章 数据类型

## 3.1 int

```python
# None 无操作
# bytes 类
```

```python
# 只有str 可以强转
s = '99'
print(type(int(s)))
```



## 3.2 bool

```python
# bool 布尔，主要用于条件判断。 
# None, 0 , '', [], {}, set() 
# 以上都是False
```



## 3.3 str " "

### 1. 常用操作

```python
str操作常用的 14 (9+5) 种
1.upper/lower 2.isdigit/isdecimal 3.strip 4.replace 5.split 6.startswith/endswith 7.encode 8.format 9.join
```

1. s.upper() / s.lower()

```python
# 大小写转换
s = 'Henry'
print(s.upper(), s.lower())
```

2. s.isdigit() / **s.isdecimal()**

```python
# 判断是否是数字
s1 = '123'
s2 = '12.3'
print(s1.isdigit(), s2.isdigit())		# True Flase

# isdecimal只判断是否是整数
```

3. s.strip()

```python
# 默认去除两边空格+ \n + \t

s = '  asdfgh,      '
print('-->', s.strip(), '<--')
print('-->', s.strip().strip(','), '<--')
```

4. s.replace('a', 'b', n)

```python
# repalce 中的 a 和 b 必须是str类型， n 必须是int类型
s = 'adsafga'
print(s.replace('a', '666'))
print(s.replace('a', '666', 1))
```

5. s.split('_')

```python
# str的分割
s = 'henry_echo_elaine_'
li = s.split('_')
print(li)  # 分割后的元素永远比分隔符号多一个
```

6. s.startswith() / s.endswith()

```python
# 判断开始/结束位置是否是指定元素
s = 'abghjkdc'
print(s.startswith('ab'), s.endswith('cd'))
# True  Flase
```

7. str 的格式化输出(2种)

```python
# 如果使用格式化输入，打印%需要使用 %%
# %s，%d  ：表示占位符

# way1 通常用于函数
"***{0}***{1}**".format(a, b)
# % (a, )  :这里表示tuple，建议加逗号 

# way2 
"***%s, ***%s***" % (a, b,)   
```

```python
# 示例
# way1 '{0} ***{1}'.format(a, b)
a = 'abcd'
b = '666'
s = '{0} ***{1}'.format(a, b)
print(s)
# way2 
s1 = '%s***%s' % (a, b,)
print(s1)
```

**扩展使用示例：**

```python
# %s ，只能是tuple
msg = '我是%s, 年龄%s' % ('alex', 19)
msg = '我是%(name)s, 年龄%(age)s' % {'name': 'alex', 'age': 19}
# format格式化
v1 = '我是{name}, 年龄{age}'.format(name = 'alex', age = 18)
v1 = '我是{name}, 年龄{age}'.format(** {'name': 'alex', 'age': 19})
v2 = '我是{0}, 年龄{1}'.format('alex', 18) 
v2 = '我是{0}, 年龄{1}'.format(*('alex', 18) )
```

8. encode

```python
# 指定编码类型
s = '你好'
print(s.encode('utf-8'))   # 6个字节
print( s.encode('gbk'))		 # 4个字节
```

9. '_'.join(s)

```python
# 用于循环加入指定字符
# s 必须是iterable
# s 可是str，list，tuple，dict，set（str + 容器类）
# s 中元素值必须是str类型
'_'.join(s)
```

```python
# 示例
# 指定元素循环连接str中的元素
s = 'henry'
print('_'.join(s))    # 下划线连接个字符
```



### 2. 其他操作

1. s.find('a') / s.rfind()

```python
# 返回第一个 a 的索引值，没有则返回 -1 
s = 'aaasdfgsh'
index = s.find('a')
print(index)
```

2. s.index('a') / s.rindex() /s.lindex()

```python
# 返回第一个 a 的索引值，没有报错
s = 'aaasdfgsh'
index = s.find('a')
print(index)
```

3. s.isupper() / s.islower()
4. s.capitalize()
5. s.casefold()
6. s.center(20, "*").  # 可以为空
7. s.ljust(20, "*")/s.rjust()
8. s.zfill()  # 用0填充
9. s.count('a', [start], [end])  # 查找'a' 的个数
10. s.isalnum()
11. s.isalpha()
12. s.isnumeric()
13. s.isprintable()
14. s.istitle()
15. s.partition('a')  / s.rpartition()# 分成三部分，a左边，a右边
16. s.swapcase()

____

____

### 3. 公共功能

1. len(s)

```python
# 返回s长度
s = '1234567890'
print(len(s))     # 10
```

2. s[index]

```python
# 索引取值
s = '123456789'
print(s[3])   # 4
```

3. 切片

```python
s = '123456789'
print(s[3:5])   # 45
```

4. setp

```python 
# 根据step进行切片
s = '123456789'
print(s[3::2])   # 468
```

5. for循环

```python
s = '123456789'
for i in s:
    print(i)
```



## 3.4 list  []

### 1. 常用操作

```python
list操作目前一共有15(8+7)种， 1.append 2.insert 3.remove 4.pop 5.clear 6.reverse 7.sort 8.extend
```

1. li.append('666')

```python
# 任意类型数据，li操作不能直接放在print()中
li = [1, 2, 3, 4, 5, 6]
li.append('666')
print(li)
li.append(['henry'])
print(li)
```

2. li.insert(2, 'henry')

```python
# 按照index位置插入指定内容
li = [1, 2, 3, 4, 5, 6]
li.insert(3, 'henry')
print(li)
```

3. li.remove('aa')

```python
# 删除指定list中的元素
li = ['aa', 'a', 'aacde']
li.remove('aa')
print(li)
li.remove('bb')
print(li)  # 会报错
```

4. li.pop(index)

```python
# 按index删除list中的元素
li = [1, 2, 3, 4, 5, 6]
li.pop()
print(li)
li.pop(3)
print(li)
```

5. li.clear()

```python
# 清空list中的所有元素
li = [1, 2, 3, 4, 5, 6]
li.clear()
print(li)
```

6. li.reverse()

```python
# 反转list中的元素
li = [1, 2, 3, 4, 5, 6]
li.reverse()
print(li)
```

7. li.sort(reveres = True)

```python
# reverse = True 从大到小
# 只能是同一类型的元素
# dict，tuple不支持排序
li = [6, 2, 3, 1, 5, 4]
li.sort()
print(li)
li = ['ba', 'ab', 'c', 'd']
li.sort(reverse=True)
print(li)

li = [[6], [2, 3], [1, 5, 4]]
li.sort()
print(li)

li = [(6, 2, 3, 1, 5, 4)]
li.sort()
print(li)
```

8. li.extend(s)

```python
# 把s中的元素，循环取出，逐个追加到list中
# s可以是str， list， tuple， dict， set
# dict只取keys 追加到list中
s = 'henry'
li = [1, 2, 3, 4, 5, 6]
li.extend(s)
print(li)
s = ['a', 'b', 'c', 'd']
li.extend(s)
print(li)
```

### 2. 其他：

1. li.count('a')
2. li.copy(). # 浅拷贝
3. li.count() # 只计算第一层，不考虑嵌套
4. li.index('val')

___

___

### 3. 公共功能

1. len(s)

```python
li = [1, 2, 3, 4, 5, 6]
print(len(li))

```

2. index 取值

```python
li = [1, 2, 3, 4, 5, 6]
print(li[2])

```

3. 切片

```python
li = [1, 2, 3, 4, 5, 6]
print(li[2:5])

```

4. step

```python
li = [1, 2, 3, 4, 5, 6]
print(li[2::2])

```

5. for循环

```python
li = [1, 2, 3, 4, 5, 6]
for i in li:
  print(i)

```

6. **修改**

```python
# 使用index修改，如果只是一个值，则正常修改
li = [1, 2, 3, 4, 5, 6]
li[2] = 'henry'
print(li)
# 使用index修改，如果是多个值，认为是一个tuple
li[2] = 'a', 'b', 'c'
print(li)
# 使用切片[]修改，则循环取值加入
li[2:3] = 'a', 'b', 'c'
print(li)
```

7. 删除del li[]

```python
# del 也不能放在print()里面
li = [1, 2, 3, 4, 5, 6]
del li[2]
print(li)
del li[2:]
print(li
```



## 3.5 tuple ()

```python
# 没有独有操作，目前只有5种
# tuple里，最后一个值最好加一个 逗号 ，以区别于运算符
```

### 1. 常用操作

1. len()

```python
t = (1, 2, 3,)
print(len(t))
```

2. index

```python
t = (1, 2, 3,)
print(t[2])
```

3. 切片

```python
t = (1, 2, 3,)
print(t[1:])
```

4. step

```python
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(t[1::2])
```

5. for 循环

```python
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
for i int t:
  print(i)
```

### 2. 内置函数

- max(tup).   # 返回最大值
- min(tup).   # 返回最小值
- tuple(li).    # list 转tuple 

## 3.6 dict {}

### 1. 常用操作

```python
dict 目前一共有 14(9 + 5) 种操作, 1.keys 2.values 3.items 4.get 5.pop 6.update 7.setdefault 8.popitem 9.clear
# {key1: value1, k2: value2}
# key不能重复
```

1. info/ info.keys()
   - 类似 list ，但不是list，例如：dict_keys(['name', 'age', 'gender'])

```python
# 取所有key
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
for key i info:
  print(key)
```

2. Info.values()

```python
# 取所有value
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
for v in info.values():
    print(v)
```

3. info.items()

```python
# 取所有key值对
# 取出的是 tuple 类型
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
for pair in info.items():
    print(pair)
```

4. Info.get(key, 666)

```python
# 有key则取出， 没有则返回指定 值
# 如果没有指定值，则返回 None
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
print(info.get(1, 666))
print(info.get(4, 666))
```

5. info.pop(key)

```python
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
print(info.pop(1))
print(info.pop(4))
```

6. info.update(info1)

```python
# 只能用dict类型更新
info = {}
info1 = {1: 'henry', 2: 'echo', 3: 'eliane'}
info.update(info1)
print(info)
```

7. info.setdefalut(key, value)

```python
# 查询key，有则取出，没有则添加
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
info.setdefault(4, 'hello')
print(info)
# 取出需要赋值给其他变量
val = info.setdefault(4, 'i hate you')
print(val)
```

8. info.popitem()

```python
# 不能加参数，删除最后一个key值对
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
v = info.popitem()
print(v,info)   # v是tuple
```

9. info.clear()

```python
# 清空所有元素
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
info.clear()
print(info)
```

### 2. 其他

1. info.copy()  # 浅拷贝
2. info.fromkeys()

```python
li = [1, 2, 3, 4, 5]
info = {'a': 1, 'b': 2}
v = info.fromkeys(li, 'hello')
print(v, info)
```



___

___

### 3. 公共功能

1. len(info)

```python
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
print(len(info))
```

2. Index 取值

```python
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
print(info[1])
```

3. for 循环

```python
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
for i in info:
  print(i)
for v in info.values():
  print(v)
for pair in info.items():
  print(pair)
```

4. 修改

```python
# key一样则修改，不一样则追加
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
info[1] = 'hello'
print(info)
info[4] = 'you are smart'
print(info)
```

5. 删除

```python
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
del info[1]
print(info)
```

### 4. 有序字典

```python
# __getitem__ set, del 
from collections import OrderdDict

info = OrderedDict()
info['k1'] = 123
info['k2'] = 456
```



## 3.7 set() /{}

### 1. 常用操作

```python
set 目前一共有11(10 + 2)种操作，空集合用set()表示。 
1.add 2.update 3.pop 4.discard 5.remove 6. clear 7.intersection 8.union 9.difference 10.symmetric_difference
# 无序，不重复
```

1. s.add('a')

```python
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.add(5)
print(s)
```

2. s.update(s1)

```python
# 可以用str ， list， tuple， dict， set， 也可以混合多种类型放入update中
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s1 = {5, 6, 7, 8, 1, 2, 3}
s2 = [5, 6, 7, 8, 1, 2, 3]
s3 = (5, 6, 7, 8, 1, 2, 3)
s4 = {5: 6, 7: 8, 1: 2}
s.update(s1)
print(s)

s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.update(s2)
print(s)

s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.update(s3)
print(s)

s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.update(s4)
print(s)
```

3. s.pop()

```python
# 随机删除，此时pop中不能有任何参数
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.pop()  # 默认删除第一个元素/随机
print(s)
```

4. s.discard()

```python
# 必须有一个参数，没有不报错, 不会返回值
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
val = s.discard(3)
print(s)
print(val)
```

5. s.remove('a')

```python
# 必须有一个参数，没有会报错
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.remove(3)
print(s)
```

6. s.clear()

```python
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.clear()
print(s)
```

7. s.intersection(s1)

```python
# 取v1 和v2 的交集
v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
v2 = {1, 3, 5, 7}
v = v1.intersection(v2)
print(v)
```

8. v.union(v1)

```python
# 取并集
v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
v2 = {1, 3, 5, 7}
v = v1.union(v2)
print(v)
```

9. v.difference(v1)

```python
v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
v2 = {1, 3, 5, 7}
v = v1.difference(v2)
print(v)
```

10. v.symmetric_difference(v1)

```python
v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
v2 = {1, 3, 5, 7}
v = v1.symmetric_difference(v2)
print(v)
```

### 2. 其他

1. v.copy()
2. v.difference_update(v2)
3. v.symmetric_difference_update(v2)
4. v.intersection.update(v2)
5. v.isdisjoint(v2)  # 返回 bool值
6. v.issubset(v2)/ v.issuperset(v2)

___

___

### 3. 公共功能

1. len(v)

```python
v = {1, 'henry', 2, 'echo', 3, 'eliane'}
print(len(v))
```

2. for 循环

```python
# 无序输出
v = {1, 'henry', 2, 'echo', 3, 'eliane'}
for i in v:
    print(i)
```



## 3.8 公共功能



|                       | int  | bool | str  | list | tuple | dict | set  |
| :-------------------: | :--: | :--: | :--: | :--: | :---: | :--: | :--: |
|        **len**        |  —   |  —   |  ✓   |  ✓   |   ✓   |  ✓   |  ✓   |
|       **index**       |  —   |  —   |  ✓   |  ✓   |   ✓   |  ✓   |  —   |
|       **切片**        |  —   |  —   |  ✓   |  ✓   |   ✓   |  —   |  —   |
|       **step**        |  —   |  —   |  ✓   |  ✓   |   ✓   |  —   |  —   |
| **for循环/ iterable** |  —   |  —   |  ✓   |  ✓   |   ✓   |  ✓   |  ✓   |
|       **修改**        |  —   |  —   |  —   |  ✓   |   —   |  ✓   |  ✓   |
|       **删除**        |  —   |  —   |  —   |  ✓   |   —   |  ✓   |  ✓   |



## 3.9 嵌套&深浅copy

### 1. 可嵌套的数据类型

​	所有的容器类例如：list，tuple， dict，set 都可以嵌套，但set(), 只能嵌套可**hash**（int, bool, str, tuple 4种）的数据类型。



## 3.10 内存相关&深浅拷贝

### 1. 内存相关

**小数据池**

- **==**判断值
- **is**判断内存地址
- python中默认会对int，str，bool进行缓存

**缓存规则：**

- int型-5 — 256之间会被缓存
- str：空和单个字符默认缓存;只包含字母、数字、下划线，也缓存; 乘数>1时，str只包含Num、ALp、_时缓存（最终长度不能超过20）
- str：手动指定缓存
- bool

### 2. 深浅拷贝

1. 使用格式import copy（模块）
2. **4 个结论**
   - 浅拷贝只是拷贝第一层可变类型
   - 深拷贝拷贝所有可变类型的数据
   - 只要 copy ，一定会为**数据**开辟新的内存空间
   - tuple 浅copy地址一样， 有嵌套的可变类型，deepcopy也会拷贝tuple数据

# 第四章 文件操作

​	文件操作主要用来读取、修改、和创建指定文件。

## 4.1 文件基本操作

### 1. 文件打开格式

```python
f = open('文件路径'，mode='r/w/a...'，encoding='utf-8')    # 不写会默认
```

### 2. 文件写入格式

- file.write(str)将字符串写入文件，返回的是写入的**字符长度**。

```python
# mode= 'w'
# 打开文件时，会先清空历史文件，没有则创建
f.write('a')
```

### 3. 文件读取格式

```python
# mode= 'r'
# way1 整个文件直接读取到RAM
f.read()
f.read(1) # 如果指定编码格式，会读出 1 个字符
					# 如果是 mode= rb 会读出 1 个字节

# way2 按行读取文件
# 一般用于for循环中，可用来读取 GB 级别的文件
f.readline() 只读取一行
f.readlines()  # 一次性加载所有内容到内存，并根据行分割成字符串
# 读取一行时也可以使用
for line in v:
  	line = line.strip('\n')
```

### 4. 文件的关闭

```python
# 当对文件操作完成后必须关闭，否则不会存储到本地磁盘
f.colse()
# 刷新缓冲区里任何还没写入的信息
```



## 4.2 打开模式

### 1. mode 分类

​	mode常见的有**r/w/a**（只读/写/追加），**r+/w+/a+**（读写/写读/追加读），**rb/wb/ab**（以二进制方式进行读/写/追加），**r+b/w+b/a+b**。

|    模式    |  r   |  r+  |  w   |  w+  |  a   |  a+  |
| :--------: | :--: | :--: | :--: | :--: | :--: | :--: |
|     读     |  +   |  +   |      |  +   |      |  +   |
|     写     |      |  +   |  +   |  +   |  +   |  +   |
|    创建    |      |      |  +   |  +   |  +   |  +   |
|    覆盖    |      |      |  +   |  +   |      |      |
| 指针在开始 |  +   |  +   |  +   |  +   |      |      |
| 指针在结尾 |      |      |      |      |  +   |  +   |



## 4.3 其他操作

​	断点续传，通过终端与服务器之间的交互，找到文件断点位置，从而实现文件的单次传输。此种操作可以使用file.seek(n）实现，n表示字节数。

### 1. 文件定位

​	**seek（offset [,from]）**方法改变当前文件的位置。**Offset**变量表示要移动的字节数。**From**变量指定开始移动字节的参考位置。如果from被设为**0**，这意味着将文件的**开头**作为移动字节的参考位置。如果设为**1**，则使用**当前的位置**作为参考位置。如果它被设为**2**，那么该文件的**末尾**将作为参考位置。

-  file.seek(n)
  - 光标移动到指定**字节**位置。**注意**

- file.tell()
  - 返回当前光标位置。可以用于断点续传技术。

### 2. 重命名和删除文件

- rename()方法需要两个参数，当前的文件名和新文件名。

```python
# 示例
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
# 重命名文件test1.txt到test2.txt。
os.rename( "test1.txt", "test2.txt" )
```

- 你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
# 删除一个已经存在的文件test2.txt
os.remove("test2.txt")
```

### 3. f.flush()

- 强制把内存中的数据，刷到硬盘中。主要用于操作文件时间过长，无法自动保存的问题。

```python
v = open('a.txt',mode='a',encoding='utf-8')
while True:
  	val = input('请输入：')
  	v.write(val)
 	 	v.flush()		# 强制把内存中的数据，刷到硬盘中
v.close()
```



## 4.4 一次性操作文件

```python
v = open('a.txt', mode='a', encoding='utf-8')
v1 = v.read()
v.close()
```

```python
# 缩进中的代码执行完毕后，自动关闭文件
with open('a.txt', mode='a', encoding='utf-8') as v:
	data = v.read()
```



## 4.5 文件修改(示例)

**Note： **

1. **文件在存储的时候，是连续存储的。文件较大时可以按行读取，修改。**
2. **按行读取时，一定要注意一行结束位置有 \n** 

```python
# 示例1 
# 文件的修改，需要先把内容读到内存，修改后再存储
with open('a.txt', mode='r', encoding='utf-8') as v:
	data = v.read()
print(data)

new_data = data.replace('a', 666)
with open('a.txt', mode='w', encoding='utf-8') as v:
	data = v.wirte(new_data)
```

```python
# 示例2  修改指定字符
# 大文件的修改
f1 = open('a.txt', mode='r', encoding='utf-8')
f2 = open('b.txt', mode='r', encoding='utf-8')
for line in f1:
  	line = line.replace('a', 'b')
    f2.write(line)
f1.close
f2.close
```

```python
# 一次性打开修改和关闭
with open('a.txt', mode='r', encoding='utf-8') as f1,open('b.txt', mode='r', encoding='utf-8') as f2:
	for line in f1.readlines():
# 或者如下写法
	for line in f1:   # 这种写法，也会一行行读取，包括 \n 也会单独一行读出
  	line = line.replace('a', 'b')
    f2.write(line)
```



# 第五章 函数

​	以双下划线开头的 **__foo** 代表类的私有成员，以双下划线开头和结尾的 **\__foo__** 代表 Python 里特殊方法专用的标识，如 **__init__()** 代表类的构造函数。

## 5.1 三元运算

又称为三目运算

**和预算符相关**

```python
val = v if v else 666
val = v or 666 # 源码中会见到
```

**Note：为了赋值**

```python
# 简单条件赋值时使用
v = 前面 if 条件 else 后面
```

```python
# 用户输入，如果是整数，则转换，否则赋值为None
data = input('>>>')
value = int(data) if data.isdecimal() else None
```



## 5.2 函数基础

面向过程【可读性差、可重用性差】—> 函数式编程—>面向对象

```python
# 如果给其他人发送邮件，可以把发送程序进行封装起来，可缩减代码长度和提高重复利用性。
```

 **函数式编程**

- 将n行代码放在别处，并取别名，以后可以调用
- 场景：
  - 代码重复执行
  - 代码量特别多，超过一屏，可以选择函数编程（**一般控制在一屏以内**）

### 1. 定义函数

**可以定义一个由自己想要功能的函数，以下是简单的规则：（5）**

- 函数代码块以 **def** 关键词开头，后接**函数标识符名称**和圆括号**()**。
- 任何传入参数和自变量必须放在**圆括号**中间。圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用**文档字符串**—用于存放函数说明。
- 函数内容以**冒号起始**，**并且缩进**。
- **return [表达式]** 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

```python
def functionname( parameters ):   
  "函数_文档字符串"
  function_suite  # 函数体  
	return [expression]
# 默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
```

```python
# 函数定义
# way1
def 函数名():
  	# 函数体
    pass
# 函数的执行
函数名()    # 会自动执行

# way2 
# 形参可以是多个
def 函数名(形参):
  	# 函数体
    pass
函数名(实参)
```

#### **Note1**（1)

- None方法类似函数，但不是（方法操作是s.upper(),方式，而函数是直接调用，len（），open（））

### 2. 两种参数（示例）

​	**形参**（形式参数）与**实参**（实际参数）的位置关系。

```python
def 函数名(形参):
  	# 函数体
    pass
函数名(实参)
```

```python
# 无形参示例
def get_sum_list()
	sum = 0
  for i in li:
    sum += i
print(get_sum_list())
```

```python
# 有形参示例
# 请写一个函数，函数计算列表 info = [11,22,33,44,55] 中所有元素的和。
info = [11, 22, 33, 44]
def get_list_sum(li):
    sum = 0
    for i in li:
        sum += i
    print(sum)
get_list_sum(info)
```



### 3. 函数的返回值

#### Note2(4)

1. **return [表达式]** 结束函数，选择性地返回一个值给调用方(func()为返回值)。
2. return 1， 2 ，3   会返回tuple：(1, 2, 3)
3. 函数默认返回值是 None ，有时可以使用其作为**flag**
4. 可变类型（list）的基本上都是None, 不可变（str）基本上会返回新值

```python
def func(arg):
  	return 9 # 返回值为9，默认为None,可以返回任何类型的数据
val = def func(v)
```

```python
# 示例2
# 让用户输入一段字符串，计算字符串中有多少A，就在文件中写入多少‘echo’
def get_char_count(arg):
  	count = 0
    for i in arg:
      	count += 1

def write_file(data):
  	open('a.txt', mode='w', encoding='utf-8') as v:
        if len(data) == 0:或者 if not bool(data):
            return '写入失败'
				v.write(data)
        return '写入成功'
  	
print(count)
content = input()
```

### 4.  函数的四种方式

```python
# way1 无形参，无return
def fun1():
  	pass
fun()
# way2 有形参，无return
def fun2(arg):
  	pass
fun2(v)
# way3 无形参，有return（指定值）
def fun3():
  	pass
  	return 9
val = fun3(v)
# way4 有形参，有return（变量）
def fun4(arg1, arg2):
  	pass
  	return arg1 + arg2
val = fun4(v1 + v2)
```

### 5.  练习(3)

```python
# 1. 写函数，计算一个list中有多少个数字，打印，有%s个数字
# 判断数字：type(a) == int
# 2. 写函数，计算一个列表中偶数索引位置的数据构造成另外一个列表，并返回。
# 3. 读取文件，将文件的内容构造成指定格式的数据，并返回。
a.log文件
    alex|123|18
    eric|uiuf|19
    ...
目标结构：
a. ["alex|123|18","eric|uiuf|19"] 并返回。
b. [['alex','123','18'],['eric','uiuf','19']]
c. [
	{'name':'alex','pwd':'123','age':'18'},
	{'name':'eric','pwd':'uiuf','age':'19'},
]
```





## 5.3 变量作用域&嵌套

### 1. 函数传参方式(2+1)

​	参数传递方式分为**位置**传参、**关键字**传参、**函数作为参数进行传递**。

- **位置传参**
  - 严格按照位置进行传参

```python
# 示例
def func(a1, a2):
  pass

func(1, 3)
func(1, [1, 2, 3])
```

- **关键字传参**

```python
# 示例
def func(a1, a2)：
	pass

func(a1 = 1, a2 = [1, 2, 3])

func(a1 = 1, 2 )     # 此时会报顺序错误
```

#### **Note3**（1）

1. 关键字传参可以和位置传参混合使用，但 **位置参数** 必须在 关键字传参**前**。

### 2. 函数定义参数(3)

​	函数定义中，def func() 括号中可以**省略**、**默认参数**和 ***args/\*\*kwargs。**

1. **省略参数**

```python
# 示例
def func()：
	pass
```

2. **默认参数**
   - 注意默认参数一定要在位置参数之后
   - 在定义默认参数时，**慎用**可变类型变量

```python
# 示例 
def func(a1, a2=2)：
	pass
# 调用方法，有默认参数时，可以不用省略，采取默认值，也可以重新赋值
func(1)
func(1, 3)
# 默认形参时，如果默认是可变类型的需要谨慎使用
```

```python
# 如果想要给values设置默认是空list
def func(data, value=[]):
  pass
# 推荐
def func(data, value=None):
  if not value:    
    valu=[]
```

3. ***args/\*\*kwargs（万能参数）**

- *args 表示接收所有由**实参**通过**位置传参**方式，传递过来的数据，可以和位置参数一起使用。
  - 接收到的参数值，会通过循环加入**tuple**中

```python
# 示例 : 可以传递任意类型数据
def func(*args)：
	pass

# [1, 2, 3]会被当成整体变成tuple中的一个元素
func(1, 2, 3, [1, 2 ,3])
# 直接赋值, [1, 2, 3]也会循环取出追加到tuple中
func(4, 5 ,6 ,*[1, 2 ,3])
```

- **kwargs 表示接收所有关键字传参的数据，也可以通过\*\*{'k1': 1, 'k2':2}，循环取出keys对，加入形参dict中

```python
# 示例 ：只能通过关键字传参，或者dict赋值
def func(**kwargs):
    print(kwargs)

# [1, 2, 3]会被当成整体变成dict中 'd': [1, 2, 3]
func(a=1, b=2, c=3, d=[1, 2 ,3])
# 直接赋值, {'k1': 4, 'k2': 5}也会循环取出追加到形参的dict中
func(a=1, b=2, c=3, d=[1, 2, 3], **{'k1': 4, 'k2': 5})
```

#### Note4(4)

1. 形参中的**默认参数**，也可以使用**位置传参方式**
2. 传参时，有*（**）时，会直接赋值 (循环加入) 给形参
3. 不带* / **的实参，会转换为tuple / dict
4. 传入的数据都是循环加入tuple / dict中

### 3.  作用域&函数嵌套

​	变量作用域时是变量的有效作用范围，在python中函数就是一个局部作用域。由于作用域的不同，变量的有效范围也不同，根据作用范围可以把变量分为，全局变量和局部变量。

​	**全局变量**：可供任何函数进行使用，修改，在python文件第一层的变量。在python中一般把全局变量命名为全部大写（**规范**），例如：USRE_NAME = 'henry'。

​	**局部变量**：可以把函数中的变量视为局部变量。函数体中变量为函数所私有（只能被其子函数进行使用）。

```python
# 示例1
a	= 'henry'
def func():
  print(a)
a = 123
func()   # 此时使用的是全局变量, 结果是 123

# 示例2
a = 'henry'
def func1():
    def func2():
     		a = 'echo'
        print(a)
    func2()
    print(a)

a = 123
func1()
print(a)
# echo 123 123
```

#### **Note5**（4）

1. **python文件**就是一个全局作用域
2. **函数**是一个 (局部) 作用域
3. 局部作用域中的数据归自己**私有**
4. 作用域中**查找数据规则**
   - 优先查找自己作用域，自己没有，去父籍作用域查找直到找到全局作用域
   - 查找不到会报错，默认只能使用父籍作用域中的变量值不能赋值（**可变类型可以修改**）

```python
# 示例
# 对于可变变量可以进行修改
a = [1, 3, 5, 7]
def fun1():
  	a.append('henry')
fun1()
print(a)     # 此时a会被修改
```

```python
# 两种赋值的方法
# 可以使用 global 关键字对全局变量进行重新赋值
global name
name = 'alex'  # 给全局变量重新赋值

# 可以使用 nolocal 关键字对父籍变量进行重新赋值, 在父籍找不到时，会报错
nonlocal name 
name = 'alex'  # 给父籍变量重新赋值
```

#### Note6(3)

1. 对于可变变量可以进行**修改**
2. global 关键字对全局变量进行**重新赋值**
3. nolocal 关键字对父籍变量进行重新赋值, 在**父籍找不到**会报错



## 5.4 函数进阶

- **高阶函数**(3)
  1. 对函数**赋值**
  2. 函数当作**参数传递**
  3. 把函数当作**返回值**

```python
# <class 'function'>
def func ():
  pass
print(type(func))
# 函数可以认为是一变量
```

### 1. 函数赋值

```python
def func():
  print(123)
v = fun # 指向相同的地址
v()
```

```python
# 示例
def func():
  print(123)
v1 = [func, func, func]
v2 = [func(), func(), func()]
print(v1)
print(v2)
```

### 2. 函数传参

```python
def func(arg):
  print(arg)
def show():
  return 999

func(show)   # 999 None
```

### 3. 函数作为返回值

```python
def func():
  print(1,2,3)
def bar():
  return func
v = bar()  # func
v()
```

#### Note7(3)

1. 注意**func** 和 **func()** 的区别
2. 函数(**实际是内存地址**)可以放入set()中(不常用)， 或dict中（一般用于values，也可以放在key中但不常用）
3. 函数一旦定义，只要进行加载，就是不可变，可 **hash** 

```python
# 10 个函数， 一般是建立字典
def func():
  print('话费查询')
def bar():
  print('***')
def base():
  print('***')

info = {
    'f1': func,
    'f2': bar,
    'f3': base
  }
choice = input('please input your choice: ')
name = info.get('choice')
 if not name：
  	print('输入不存在')
 else：
		name()
```

### 3. lambda表达式

```python
# 三目运算，为了解决简单的if...esle的情况
# lambda，为了解决简单函数的情况
eg:
def func(a1, a2):
  return a1 + a2
# 可以改写为，a1 + 100 即为return 值
func = lambda a1, a2: a1 + 100
```

```python
# way1 直接使用
func = lambda : 100
func = lambda a: a*10
func = lambda *args, **kwargs: len(args) + len(kwargs)
# way2 使用全局变量
DATA = 100
func = lambda a: a + DATA
func(1)
# way3 使用父籍变量
DATA = 100
def func():
  DATA = 1000
  func1 = lambda a: a + DATA
  v = func1(1)
  print(v)
func()
# way4 使用条件判断 ########
func = lambda n1, n2: n1 if n1 > n2 else n2
```

```python
# 练习1
USER_LIST = []
func1 = lambda x: USER_LIST.append(x)
v1 = func1('alex')
print(v1)			# None
print(USER_LIST) # ['alex']

# 练习2
func1 = lambda x: x.strip()
v1 = func1('   alex')
print(v1)			# 'alex'

# 练习3
func_list = [lambda x: x.strip(), lambda y: y+100, lambda x,y: x+y]
v1 = func_list[0]('   alex')
print(v1)			# 'alex'
```

#### Note8(2)

1. 用于表示简单函数（一行解决的函数）。
2. lambda 表达式会默认返回**冒号：**之后的值

### 4. 内置函数（30）

- 自定义函数

- **内置函数**（31）

  1. 强制转换(7)：int()，str,  bool,  list，dict，tuple，set
  2. 输入输出(2)：print, input
  3. 其他(5)：type, id, range, open, len
  4. 数学(7)
     - abs，round，float（int(55.5)保留整数部分）
     - max，min，sum，
     - **divmod**（两数相除，得商和余数, 两个值）
5. 面向对象相关(4)：dir，super，issubclass，isinstance
  
  ```python
  # divmod. 练习
  USER_LIST = []
  for i in range(1, 836):
    tem = {name':'hello-%s' % i, 'email':'XXXX%s@qq.com' %s}
    USER_LIST.append(tem)
  """
  	要求：
  		每页展示10条
  		根据用户输入的页码，查看
  """
  ```
```
  
6. 进制转换(3)：**bin**（0b，int<—>bin），**oct**（0o，int<—>oct），int(其他进制转int)，**hex**（0x，int<—>hex）
  
  ```python
  # base 默认为 10
  v1 = '0b1101'
  result = int(v1, base = 2)
  # 转8进制
  v1 = '0o1101'
  result = int(v1, base = 8)
  # 转16进制
  v1 = '0x1101'
  result = int(v1, base = 16)
```

  ```python
  # ip 点分二进制，将十进制转为二进制并通过 . 连接ip = '192.168.12.79'
  ip = '192.168.12.79'
  li = ip.split('.')
  l = []
  for i in li:
      i = int(i)
      i = bin(i)
      i = str(i).replace('0b', '')
      i = i.rjust(8, '0')
      l.append(i)
  s = '.'.join(l)
  print(s)
  ```

  7. 编码相关

- chr() ：把int型数据，转换为unicode编码
  - ord()：把unicode转换为**字符**
  
  ```python
  # 生成验证码
  import random	# 导入一个模块
  def get_random_data(length=6):
    data = []
    for i in range(length):
        v = random.randint(65,90) # 得到一个随机数
        data.append(v)
  	return ' '.join(data)
    
  code = get_random_data()
print(code)
  ```
  
8. map / filter / reduce（py2）/zip
  
  - **map**，循环每个元素（第二个参数），然后让元素执行函数（第一个参数），将每个函数结果保存到新的list中，并返回。（批量修改数据）
  
  ```python
  # map操作的 func 是一个函数 v 必须是可迭代，
  v = [11, 22, 33]
  def func(arg):
    return arg + 100 
  result = map(func, v) # 将函数的返回值添加到空list中[111, 122, 133]
  print(list(result))
  # 使用lambda 改写
  result = map(lambda x: x+100, v)
	print(result)		# py2直接返回
  print(list(resutl)) # py3会返回一个object，可用list()查看
  ```
```
  
  - **filter**
  
  ```python
  # 结果为True的时候，才返回数据
v = [1, 2, 3, 'welcome', 4, 'hello']
  result = filter(lambda x: type(x) == int, v) # 生成新list
print(list(result))
```

  - **reduce**

  ```python
  import functools
v = [1, 2, 3, 4]
  result = functools.reduce(lambda x,y: x*y, v)
print(result)
  ```

  - **zip**

  ```python
  a = [1,2,3]
  b = [4,5,6]
  c = [4,5,6,7,8]
  zipped = zip(a,b)     # 打包为元组的列表
  [(1, 4), (2, 5), (3, 6)]
  zip(a,c)             
  # 元素个数与最短的列表一致
  [(1, 4), (2, 5), (3, 6)]
  zip(*zipped)          
  # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
  [(1, 2, 3), (4, 5, 6)]
  ```

  

## 5.5 函数闭包

### 1. 函数闭包

```python
def func(name):
  def inner():
    print(name)
  return inner

v1 = func('henry')
v1()
v2 = func('echo')
v2()
```

```python
# 不是闭包
def func(name):
  def inner():
    return 123
  return inner

# 闭包:封装值 + 内层函数需要使用
def func(name):
  def inner():
    print(name)
    return 123
  return inner 
```

#### Note9(5)

1. **闭包**，为函数创建一块区域（内部变量供自己使用），为以后执行提供数据；
2. 函数内部数据不会混乱
3. **执行完毕**+**内部数据不被**其他程序使用会被销毁
4. **应用**：装饰器，SQLAlchemy源码
5. 由函数及其相关的引用环境组合而成的实体(即：**闭包=函数+引用环境**)

### 2. 递归(效率较低)

- 递归限制为1000次

```python
def func(i):
  print(i)
  func(i+1)
```

```python
# 斐波那契数列
def func(a, b):
  print(b)
  func(a, a+b)
```

```python
# 递归
def fun(a):
  if a == 5:
    return 100
  result = func(a+1) + 10
  return result
v = func(1)

# 注意
def fun(a):
  	if a == 5:
    		return 100
  	result = func(a+1) + 10

v = func(1)
```



## 5.6 装饰器和推导式

### 1. 装饰器（重点）

```python
def func():
  def inner():
    pass 
 	return inner

v = func()
print(v)   # inner 函数
# ##############################
def func(arg):
  def inner():
    print(arg) 
 	return inner

v1 = func(1)   # 1
v2 = func(2)   # 2
# ##############################
def func(arg):
  def inner():
    arg()
 	return inner

def f1():
  print(123)
  
v = fucn(f1)
v()		# 123
# ##############################
def func(arg):
    def inner():
        arg()
return inner
def f1():
    print(123)
return 666
v1 = func(f1)
result = v1() 
# 执行inner函数 / f1含函数 -> 123 print(result) 	
# None

# ##############################
def func(arg):
    def inner():
        return arg()
return inner
def f1():
    print(123)
return 666
v1 = func(f1)
result = v1()   # 123 666
```

- **装饰器示例**

```python
def func(arg):
  def inner():
		print('before')
    v = arg()
    print('after')
    return v
  return inner

def index():
  print('123')
  return 666

# 示例
v1 = index()   # 123

v2 = func(index)  # before 123 after
v3 = v2()

v4 = func(index)   # before 123 after
index = v4
index()

index = func(index)  # before 123 after
index()
```

```python
# 第一步，执行func函数，并将下面的函数当作函数传递，相当于func(index)
# 第二部，将func返回值，重新赋值为下面的函数名，index = func(index)
def func(arg):
    def inner():
        return arg()
    return inner

@func
def index():
    print(123)
    return 666

print(index)  # <function func.<locals>.inner at 0x1054a16a8>
```

**应用示例**：

```python
# 计算函数执行时间
def wrapper(func):
  	def inner():
      	start_time = time.time()
				func()
				end_time = time.time()
				print(end_time - start_time)
        return func()
      return inner

import time
 @ warpper   
def func():
    time.sleep(2)
  	print(123)
  
 @ warpper   
def func():
    time.sleep(1.5)
  	print(123)

# 判断用户是否登陆
```

#### Note10(2)

1. **目的**：在在不改变原函数的基础上，在执行函数前后自定义一些操作
2. **场景**：想要为函数扩展功能时

- 编写装饰器

```python
# 装饰器的编写（示例）
def wrapper(func):		# 必须有一个参数
  def inner():
    ret = func()
    return ret
 	return inner
# 应用 index = wrapper(index)
@wapper
def index():
  pass
@wapper
def manage():
  pass 
# 在执行函数，自动触发装饰器
v = index()
print(v)
```

```python
# 导入本目录下的其他py文件
import a
a.f1()
a.f2()
a.f3()
```

- **编写格式**

```python
def wrapper(func):
  	def inner(*args, **kwargs):
				return func(*args, **kwargs)
  	return inner
```

为什么要加*args，**kwargs？

### 2.  关于参数

```python
# 让参数统一的目的：为装饰的函数传参
def x(func):
  def inner(a, b):
    return func()
  return inner

@x
def index():
  pass

index(1, 2)
```

-  返回值

```python
# 装饰器建议写法
def wrapper(function):
  	def inner(*args, **kwargs):
    		v = funtion(*args, **kwargs)
    		return v
  	return inner

@wrapper
def func():
		pass
```

- 带参数的装饰器

```python
# 第一步：v = wrapper(9)
# 第二步：ret = v(index)
# 第三步：index = ret
def x(counter):
    def wrapper(function):
      	def inner(*args, **kwargs):
        		v = funtion(*args, **kwargs)
        		return v
      	return inner
     return wrapper

@x(9)
def index():
  	pass		
```

```python
# 示例：
# 写一个带参数的装饰器，实现，参数是多少，被装饰器就要执行多少次，最终返回一个list
def x(*args):
  def wrapper():
    def inner():
      li = [index() for i in range(args[0])]
      return li
    return inner
  return wrapper

@x(9)
def index():
  return 8

v = index()
print(v)
```

- 元数据
- 多个装饰器：@x1 @x2

### 3. 推导式

1. list推导式(生成式)

   - 格式（生成一个list）

   ```python
   vals = [i for i in 'henry']
   v = [i for i in 可迭代对象 if 条件]  # 满足条件生成list
   v = [i if i > 5 else i+1 for i in 可迭代对象 if 条件]  
   # 满足条件生成list
   ```

   ```python
   # 新浪
   def num():
     	return [lambda x: x * i for i in range(4)]
   print([m(2) for m in num()])
   ```

2. set推导式

   - 格式

   ```python
   # 满足条件生成set,会去重,条件判断可以省略
   v = {i for i in 可迭代对象 if 条件} 
   ```

3. dict推导式

   - 格式

   ```python
   # 满足条件生成dict，但需要key值和冒号：,条件判断可以省略
   v = { 'k' + str(i): i for i in 可迭代对象 if 条件}
   ```



## 5.7迭代器&生成器

**类**：int ,str, list….  / bytes(**b**'xxx'), datetime

**对象**：由**类**创建的数据

> 类和对象

### 1. 迭代器(class:iterator)

- 展示list中所有数据

  1. 迭代器：对某种(str/list/tuple/dict/set) (**序列**)对象中的元素，进行逐个获取。表象：具有**_\_next__()**方法，

  - list —> 迭代器：
    - v = iter([1, 2, 3, 4])
    - val = [1, 2, 3, 4]._\_iter__()
  - 迭代器获取每一个元素：v.next
  - 直到报错：StopIteration，表示迭代终止

  ```python
  v = [1, 2, 3, 4]
  val = iter(v)
  value = val.__next__()
  print(value)
  ```

  2. **甄别**：数据中是否包含**_\_next__()**方法

  3. for循环的内部，首先把数据转化为iter，反复执行iter._\_next__(),取完不报错

### 2. 可迭代对象

- 具有**_\_iter__()**方法，必须返回一个**迭代器（生成器）**
- for循环

### 3. 生成器（函数的变异）（class:generator）

1. 生成器基础

```python
def func():
  pass 
func()
```

```python
# 生成器函数（内部是否包含yield）
def func(arg):
  arg = arg + 1
  yield 1
  yield 2
  yield 100
# 函数内部代码不执行，返回一个生成器
val = func(100) 

# 生成器：可以被for循环的，一旦开始循环，函数内部代码就开始执行
for i in val:
  print(i)
# 遇到第一个yield会把后面的值赋值给 i
# 如果yield已经执行完毕，则意味着for循环结束
```

```python
# 边使用边执行
def func():
  count = 1 
  while True:
  	yield count
    count += 1

# v 只取yield值，是一个生成器对象
v = func()
for i in v:
  print(i)
  
# 查看v中有哪些方法
dir(v）
```

#### Note11(4)

1. 函数中如果存在**yield**，则该函数为**生成器函数**，调用生成器函数会返回一个**生成器**
2. 只有被for循环时，生成器内部代码才会执行，每次循环都会获取yield的返回值
3. 即使函数内部的yield函数**永远执行不到**，也**是生成器**
4. **生成器**也是一种**特殊的迭代器**，也是一个可迭代对象

```python
class Foo(object):
  def __iter__(self):
    return iter([1, 2, 3])
  	yield 1 
    yield 2
    
obj = Foo(object)
```

2. **生成器中send**

#### Note12(2)

1. **send方法，会触发一次next操作，yiled结果为其返回值**
2. 总的来说，send方法和next方法唯一的区别是在执行send方法会首先把上一次挂起的yield语句的返回值通过参数设定，从而实现与生成器方法的交互。
3. **需要注意**，在一个生成器对象没有执行next方法之前，由于没有yield语句被挂起，所以执行send方法会报错

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

3. 生成器示例

```python
# 示例：读取文件
def func():
    curse = 0
    while True:
        f = open('db','r','utf-8')
        f.seek(curse)
        data_list = []
      	for i in range(10):
        		line = f.readline()
            if not line:
              	return
            data_list.append(line)
        curse = f.tell()
        f.close
        for row in data_list:
          	yield row
```

```python
# redis 示例
import redis
coon = redis.Redis(host='192.168.12.12')
```

4. yield from 关键字

```python
# yield from (py3.3之后)
def base():
  yield 88
  yield 99
 
def bar():
  return 123

def func():
  yield 1
  yield from base()
  yield from bar()   # 报错，int 不可迭代，如果可迭代，则循环取出
  yield 2
  yield 
```

5. 生成器推导式

```python
v1 = [i for i in range(10)] # list推导式，立即产生数据
def func():
  for i in range(10):
    yield i
v2 = func()  # 与下面v2相同
v2 = (i for i in range(10)) # 生成器推导式，不会立即产生数据
```



## 5.8 异常处理

### 1. 示例

```python
# 示例1
try:
  val = input('请输入数字：')
  num = int(val)
except Exception as e:
  print('操作异常')
```

```python
# 示例2
import requests
try:
  ret = requests.get('http://www.baidu.com')
	print(ret.text)
except Exception as e:
  print('请求异常')
```

```python
# 示例3
def func(a):
  try:
    return a.strip()
  except Exception as e:
    pass
  return False

v = func([1, 2, 3])
print(v)
```

```python
# 练习1，函数接收一个list将list中的元素每个都加100
def func(arg):
    li = []
    for items in arg:
        if items.isdecimal():
            li.append(int(items) + 100)
     return li
```

```python
# 写函数，接收一个list， 中全是url 访问地址，并获取结果
import requests
def	func(url_list):
  li = []
  try:
    for i in url_list:
      reponse = requests.get(i)
      li.append(reponse.text)
  except Exception as e:
    pass
  return li

func(['http://www.baidu.com', 'http://www.google.com', 'http://www.bing.com'])
```

```python
# 比较异常 try 的位置不同，效果也不同
import requests
def	func(url_list):
  li = []
  for i in url_list:
      try:
          reponse = requests.get(i)
          li.append(reponse.text)
  		except Exception as e:
    			pass
  return li

func(['http://www.baidu.com', 'http://www.google.com', 'http://www.bing.com'])


# 得到的结果是text格式的文本文档
reponse = requests.get('url', useragent:xxxxxx)
```

### 2. 基本格式

```python
try:
  pass
except ValueError as e:
  pass
except IndexErro as e:
  pass
except Exception as e:
  print(e)
finally: 
  print('final')  # 无论对错都要执行的代码
# e 代表异常信息，是Exception类的对象，有一个错误信息
try:
  int('asdf')
except Exception as e:
  print(e)

try:
  int('asdf')
except ValueError as e:
  print(e)
  
try:
  int('asdf')
except IndexError as e:
  print(e)
  
# 即使遇到return 也会执行finally 
def func():
  try:
    int('1')
    return
  except Exception as e:
    print(e)
  finally:
    print('final')
```

### 3. 主动触发异常

```python
try:
  int('123')
  raise Exception('错误信息')   # 主动抛出异常
except Exception as e:
  print(1)
```

```python
# 打开一个文件，
def func():
  resutl = True
  try:
      with open('x.log', mode='r', encoding='utf-8') as f:
        	data = f.read()
      if 'henry' not in data:
        	raise Exception()
   except Exception as e:
     	result = False 
   return result
```

### 4. 自定义异常

```python
# 示例1
class MyException(Exception):
  pass
try:
  raise MyException('haha,错了吧')
except MyException as e:
  print(e)
```

```python
class MyException(Exception):
  def __init__(self, message):
      self.message = message
try:
  raise MyExceptoin('123')
except MyException as e:
  print(e.message)
```
# 第六章 模块



**基本概念模块和包**

1. 什么是模块

   - py文件，写好了的对程序员直接提供某方面功能
   - import / from xxx import xx
   - **包**：存储了多个py文件的文件夹，pickle，json，urlib
   - 如果导入一个包，**包里默认模块是不能使用的**
   - 导入一个包相当于执行**_\_init__.py**文件内容

   ```python
   # 在__init__.py中使用
   from pack import policy
   ```

## 6.1 模块的导入

1. **模块**：可以是py文件也可以是文件夹
2. **定义模块时**，可以把一个py文件或一个包当作一个模块，以便于以后其他py文件使用。
3. **_\_ init__.py** 在文件夹中创建此py文件， **python packages**
   - py2：**文件夹**中必须有_\_ init__.py 
   - py3：不需要，推荐加上
4. **导入模块**（只能导入模块，不能导入函数）
   1. 导入模快—>调用模块中的函数（import 文件名）
   2. import 会把**模块中的文件**优先加载到内存
   3. **from py文件名 import func，show… (*)**：只导入指定函数，也会把模块中的内容加载一遍
      - 模块中的函数名可能和本地函数重名
      - from 模块 import func as f（模块中的函数重命名） f()

```python
# test为文件夹，在当前工作目录中，jd为py文件，f1为jd中的函数
import test.jd
test.jd.f1()
# test为文件夹，在当前工作目录中，jd为py文件，f1为jd中的函数
from test import jd
jd.f1()
```

```python
# 导入(绝对导入、相对. /..导入:相对导入必须有父籍包
# import
# from 模块.模块 import 模块
# from 模块.模块.模块 import 函数
# 调用：模块.函数()，函数()
# 主文件：运行的文件（print(__name__)). 
if __name__ == '__main__
```

### Note1（4）

- 模块在和要执行的py文件在同一路径且需要很多功能时，推荐使用import 模块
- 其他推荐：from 模块 import 模块
- from 模块1.模块2 import 函数     执行：函数()
- 文件(夹)命名不可与模块相同，否则就会用当前目录中的文件(夹)

```python
# __file__ python命令行中获取的参数
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
```



## 6.2 模块的基本知识

1. **分类**：

   - **内置模块**（py内部提供的功能）

   - **第三方模块**

   ```python
   # pip 安装模块
   pip install module_name
   # 安装成功，如果导入不成功，需要重启pycharm 
   ```

   - **自定义模块**

   ```python
   # a.py
   def f1():
     pass
   def f2():
     pass 
   ```

   ```python
   # 调用自定义模块中的功能
   import a
   a.f1()
   ```

## 6.3 内置模块(10)

​	内置模块目前有**random**，**hashlib**， **getpass** ，**sys**相关，**os**相关，**shutil** ，**json**，**time&datetime**, **import lib**, **logging**等 **10**个。

### **1. random**

```python
# random.randint(a, b)
import random
def get_random_data(length=6):
    data = []
    for i in range(length):
        v = chr(random.randint(65, 90)).lower()  # 得到一个随机数
        data.append(v)
    return ' '.join(data)
```

- random.choice([1, 2, 3])：随机选择一个：验证码，抽奖
- random.sample([1, 2, 3, 4, 5], 3)：随机选3个不重复，抽奖多个人
- random.uniform(1, 5)：随机1-5中的随机小数
- random.shuffle([1,2,3,4])：洗牌，算法

### **2. hashlib / getpass**

摘要算法模块，**密文验证**/**校验文件独立性**

#### note

1. md5 / sha
2. 摘要文件内容一样，无论怎么分割，md5摘要后一致（大文件一致性校验）
3. 一般在服务端进行加盐，给每个用户使用不同的salt，**可以借助用户名**

```python
# 将指定的**str**摘要，可以使用sha1/md5
# md5常用来文件完整性校验
# hashlib.md5()/ .update() /.hexdigest()
import hashlib
def get_md5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    return obj.hexdigest()
val = get_md5('123')
print(val)
```

**加盐**：

```python
import hashlib
def get_md5(data):
    obj = hashlib.md5('adsfg12fsg'.encode('utf-8'))
    obj.update(data.encode('utf-8'))
    return obj.hexdigest()
val = get_md5('123')
print(val）
```

**密码不显示**：

```python
import getpass
pwd = getpass.getpass('please input pwd: ')
print(pwd)
```

### **3. time**

```python
import time
v = time.time() # 获取从1970年开始到目前的时间，单位为秒
time.sleep(2)  	# 休眠时间，2秒
```

### 4. sys (5 + 1)

- 解释器相关

1. sys.getrefcount(a)
2. sys.recursionlimit() / sys.setrecursionlimit()
3. sys.stdout.write(). print—>进度条
4. **sys.argv**：获取命令行参数
   - shutil(shutil.rmtree(path)
5. **sys.path**：模块导入路径
6. sys.modules：存储当前程序中用到的所有模块

```python
# 引用计数器
import sys  
a = [1, 2, 3]
print(sys.getrefcount(a))

# python默认支持的递归数量
v = sys.getrecrusionlimit()

# 输入输出，默认换行
sys.stdout.write('hello')
# \n \t 
# \r: 回到当前行的起始位置，一般于end=‘’连用
print('123\r', end='')
print('hello', end='')   
# 在输出的时候，回到123前，重新打印
# 应用：进度条
```

- **sys.argv** / shutil

```python
# sys.argv  shutil
# 删除 目录 的脚本, 只能是directory
import sys
import shutil

path = sys.argv[1]
shutil.rmtree(path)
print('remove the %s' % path)
```

- **sys.path**（是个list）
  - paython解释器会按sys.pathon的路径查找

```python
# sys包含python 和 工作目录
# 当前py文件所在路径会加载到 sys.path中
# pycharm也会 自动添加工作目录 和 项目路径加入
# python导入模块时默认查找路径
# 只能导入目录下的第一层文件

sys.path.append('module_path')
```

### 5. os(操作系统相关)

1. **os.path.exist(file_name)**
2. os.stat(file_name).st_size
3. os.path.abspath(file_name)
4. os.path.dirname(file_name) # 获取上级目录
5. **os.path.join()** # 路径拼接
6. os.listdir()  # 指定目录下的第一层文件，默认path = '.'
7. os.walk(r'path')
8. os.mkdir() / os.makedirs()
9. os.rename(a, b)
10. os.remove(a)
11. os.path.isdir()
12. os.path.isfile()
13. os.path.isabs()
14. os.path.basename()：**获取绝对路径下的文件名**

```python
import os
1. 获取文件大小
fiel_size = os.stat('filename').st_size   # 单位为字节
2. 读取文件
chunk_size = 1024
with open('filename', mode='rb') as f1:
  
v = r'path'  # r 表示转义，包括所有
os.path.dirname(v)
```

```python
转义
v = 'al\\nex'
v = r'al\nex'  # 推荐
```

```python
import os
v = 'test.txt'
path = 'user/henry/desktop'
new_path = os.path.join(path, v)
```

```python
# 当前目录下第一层文件
import os
result = os.listdir(r'path')
print(result)

# 当前目录下的所有文件
import os
result = os.walk(r'path')   # 生成器
for a, b, c in result: 
  for i in c:  # a 是目录;b 是目录下的文件夹;c 是目录下的文件
    path = os.path.join(a, i)
      print(path)
```

### 6. shutil

1. shutil.make_archive()
2. shutil.unpack_archive()
3. shutil.rmtree()
4. shutil.move()

```python
import shutil
shutil.rmtree(r'path')
```

```python
import shutil
 # 没有返回值
shutil.rmtree('dir_name')
# 重命名，可以是文件/目录
shutil.move('file_name1', 'new_file_name')
# 压缩文件(c_file_name.zip), 如果只给定文件名，压缩到py脚本所在目录
shutil.make_archive('c_file_name', 'zip', 'dir_name')
# 解压文件,默认是当前路径， 指定目录不存在会创建文件目录
shutil.unpack_archive('c_file_name.zip', extra=r'dir_paths', format='zip', )
```

```python
from datetime import datetime
# 当前时间
ctime = datetim.now().strftime('%Y-%m-%d %H:%M:%S')
# 1.压缩test文件夹
# 2.放到code目录（默认不存在）
# 3.将文件解压到/User/henry/Desktop/t中
```



## 6.4  json

- **json**， 所有语言通用，**只能**序列化指定的基本数据类型
  - dumps/loads/ dump/load
  - 所有字符串必须都是双引号
  - 最外层只能是dict/list
  - 不能支持load多次
  - dict中key只能是str
- **pickle**，几乎支持所有python东西（socket对象），序列化的内容只能用python
  - dumps/loads/ dump/load
  - 支持连续load多次

### **1. json**

```python
# 只能包含，int，bool，str，list，dict
# 最外层必须是list/dict
# json 中如果包含str，必须是 双引号
# 如果是tuple类型数据，则会转换为list
- 特殊的字符串（list和dict嵌套的string）
- 不同语言间的数据交互
- 序列化/反序列化：把其语言的数据转化成json格式/ 相反
```

```python
import json
v = [12, 3, 4, {'k1': 1}, True, 'adsf']
# 序列化
v = json.dumps(v)
# 反序列化
json.loads(v)
```

```python
# 可转为json的数据中包含中文，让中文完全显示
v = {'k1': 'alex', 'k2': '你好'}
val = json.dumps(v, ensure_ascii=False)
print(val, type(val))

val = json.dumps(v)
print(val, type(val))
```

### **2. pickle**

```python
# 使用pickle序列化后，结果是编码后的二进制
import pickle
v = {1, 2, 3}
val = pickle.dumps(v)
print(val, typ(val))
val = pickle.loads(v)
print(val, typ(val))
# json dump 得到的是str， pickle得到的是bytes
```

**Note**

- 字符串
- 经过编码过后的数据，通常称为 **字节类型**/bytes，格式为：b‘XXXXXXXX'
- 压缩后的0101

## 6.5 time&datetime

### 1. time

> **UTC/GMT**：世界协调时间
>
> **本地时间**：本地时区的时间

- time.time()   # 获取时间戳 1970.1.1 00:00-至今  的秒数
- time.sleep(10)  # 等待的秒数
- time.timezone  # 和标准时间的差距，和电脑的设置有关

### **2. datetime**

```python
# 获取datetime格式时间
from datetime import datetime, timezone, timedelta
v1 = datetime.now()
v2 = datetime.utcnow()
tz = timezone(timedelta(hours = 7))  # 东7区
v3 = datetime.now(tz)  # 当前东7区时间

<class 'datetime.datetime'>
```

```python
# 将datetime格式时间转化为str
v1 = datetime.now()
v1.strftime('%Y-%m-%d') # 连接不能使用汉字（Mac，linux没问题），可以使用.format()方法
```

```python
# str转datetime，时间加减
val = datetime.strptime('2019-04-18', '%Y-%m-%d')
v = val +/- timedelta(days=40)  # 当前时间加/减40天
```

```python
# 时间戳和datetime关系
import time, datetime
ctime = time.time()
datetime.fromtimestamp(ctime，tz)   # 当前时间,tz和上述相同
```

```python
v = datetime.now()
val = v.timestamp()
print(val)
```



## 6.6 模块importlib

**作用**：根据字符串形式导入模块

**开放封闭原则**：配置文件开放，代码封闭

1. 使用str导入模块
2. _\_import__(和importlib.import_module('模块名'))
3. os = _\_import__('os')和2等价

```python
# 用字符串形式，去对象中找到其成员
import importlib
redis = importlib.import_module('utils.redis')
getattr(redis, 'func')()
```

```python
import importlib
path = 'utils.redis.func'
module_path, func_name = path.rsplit('.', 1)
getattr(module_path, func_name)()
```

```python
# 导入模块
import importlib
middleware_classes = [
    'utils.redis.Redis',
    'utils.mysql.MySQL',
    'utils.mongo.Mongo'
]
for path in middleware_classes:
    module_path,class_name = path.rsplit('.',maxsplit=1)
    module_object = importlib.import_module(module_path)    # from utils import redis
    cls = getattr(module_object,class_name)
    obj = cls()
    obj.connect()

# 用字符串的形式导入模块。
# redis = importlib.import_module('utils.redis')
# 用字符串的形式去对象（模块）找到他的成员。
# getattr(redis,'func')()
```



## 6.7 日志（模块logging）

| 日志等级（level） | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| DEBUG             | 最详细的日志信息，典型应用场景是 问题诊断                    |
| INFO              | 信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作 |
| WARNING           | 当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的 |
| ERROR             | 由于一个更严重的问题导致某些功能不能正常运行时记录的信息     |
| CRITICAL          | 当发生严重错误，导致应用程序不能继续运行时记录的信息         |

### 1. 日志示例

##### Note(2)

- 多次配置logging模块，只有第一次配置有效
- 在应用日志时，**保留堆栈**信息需加上**exc_info=True**
- **用户**：记录日志（银行流水）
- **程序员**：统计、故障排除的 debug、错误完成代码优化

```python
# 方法1, 
# basicConfig 不能实现中文编码，不能同时向文件和屏幕输出
import logging
# logging.Error 默认级别
logging.basicConfig(fielname='cmdb.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s'
                    datefmt = '%Y-%m-%d-%H-%M-%S'
                    level=logging.WARNING)
logging.log(10, '日志内容')           # 不写
logging.debug('asdfgh')
logging.log(30, 'asdfgh')            # 写
logging.warning('asdfgh')
```

**应用场景**：对于异常处理捕获的内容，使用日志模块将其保存到日志

```python
try:
  requests.get('http://www.google.com')
except Exception as e:
  msg = str(e)  # 调用e.__str__方法
  logging.error(msg, exc_info=True)   # 线程安全，支持并发
```

### 2. logging本质

```python
# 方法2
import logging
# 对象1：文件 + 格式
file_handler = logging.FileHandler('xxxxx', 'a', encoding='utf-8')
fmt = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s')
file_handler.setFormatter(fmt)

# 对象2：写（封装了对象1 ）
logger = logging.Logger('xxx(在log中会显示)', level=logging.ERROR)
logger.addHandler(file_handler)

logger.error('你好')
```

### 3. 示例

```python
# 推荐
import logging

file_handler = logging.FileHandler(filename='x1.log', mode='a', encoding='utf-8',)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[file_handler,],
    level=logging.ERROR
)

logging.error('你好')
```

**logger对像**

1. 创建一个**logger**对象、**文件操作符**、**屏幕操作符**、**格式**
2. 给logger**绑定****文件**操作和**屏幕**操作
3. 给屏幕操作符和文件操作符**设置格式**
4. 用logger对象**操作**

```python
# warning和error写入不同文件，需要创建不同对象
import logging
# 需要加入name参数
logger = logging.getLogger() 
fh = logging.FileHandler('log.log') # 写入文件
sh = logging.StreamHander()  # 不需要参数，输出到屏幕
logger.addHander(fh)
logger.addHander(sh)
# asctime:日志写入时间， name：logger对象名称， levelname：日志级别， module：模块名称
fmt=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s')
fh.Setformatter(fmt)
logger.waring('message')
```

### 4. 日志切割

```python
import time
import logging
from logging import handlers
# file_handler = logging.FileHandler(filename='x1.log', mode='a', encoding='utf-8',)
file_handler = handlers.TimedRotatingFileHandler(filename='x3.log', when='s', interval=5, encoding='utf-8')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[file_handler,],
    level=logging.ERROR
)

for i in range(1,100000):
    time.sleep(1)
    logging.error(str(i))
# 在应用日志时，如果想要保留异常的堆栈信息,exc_info=True
    msg = str(e)  # 调用e.__str__方法
    logging.error(msg,exc_info=True)
```

## 6.8 collections(python核心模块)

- OrideredDict()

```python
# dict创建过程
info = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
```

- defaultDict
- deque：双端队列
- namedtuple：默认dict，可以给dict的value设置一个默认值

```python
from collections import namedtuple
# 可命名tuple（time 结构化时间）
# 创建了一个Course类，这个类没有方法，所有属性值不能修改
Course = namedtuple('Course', ['name',  'price', 'teacher'])
python = Course('python', 999, 'alex')

print(python)
print(python.name)
print(python.price)
```

## 6.9 struct模块

- unpack的结果是**元组**
- 第一参数是数据类型

```python
# 把数据转换为四个字节
import struct
a = struct.pack('i', 1000)
b = struct.pack('i', 78)

a1 = struct.unpack('i', a)
b1 = struct.unpack('i', b)
```

# 第七章 面向对象

面向对象编程（Object Oriented Programming，**OOP**，面向对象程序设计）

1. 基础概念

   1. **类**：具有相同方法和属性的一类事物
   2. 对象、实例：一个拥有具体属性值和动作的具体个体
   3. 实例化：从一个类得到一个具体对象的过程

2. 组合

   1. 一个类的对像作为另一类对象的实例变量
   2. Foo().name

3. 三大特性

   1. **继承**:所有的查找名字(调用方法和属性)。如果自己和父类都有，希望自己和父类都调用，super()指定类名直接调

      1. 父类、基类、超类
      2. 派生类、子类
      3. 多继承、单继承
      4. 查找顺序
      5. **多态**：一个类变现出来的多种状态—>多个类表现出相似的状态
      6. 鸭子类型：list，tuple，python的多态是通过鸭子类型实现的

   2. 封装

      1. 广义封装：类中成员

      2. 狭义封装：私有成员

         1. 只能在类的内部使用，类的外部不能调用，也不能在子类中使用
         2. _类名__名字：命名

         ![私有方法的访问](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/%E7%A7%81%E6%9C%89%E6%96%B9%E6%B3%95%E7%9A%84%E8%AE%BF%E9%97%AE.png)

4. 类成员

   1. _\_call__：源码中
   2. _\_enter__ (with open 连用)
   3. _\_dict__

5. 特殊方法/魔术方法/内置方法/双下方法

6. 相关内置函数

   1. isinstance
   2. issubclass
   3. type
   4. super（新式类支持，遵循**mro**顺序）

7. 新式类和经典类

   1. 新式类：继承object，super，多继承（**广度优先c3**），具有mro方法
   2. 经典类：py2不继承object，**无super/mro** ， 深度优先

   

## 7.1 面向对象基础

**优点和应用场景**：

1. 业务功能较多时，通过面向对象归类
2. 数据封装（创建字典存储数据）
3. 游戏示例：创建一些角色，并根据角色需要再创建任务

- **封装思想**：将同一类的函数封装到同一个py文件中，以后方便使用
- **面向对象**：将同一类的函数封装到同一个class中，以后方便使用
- **对象名**：命名首字母大写

#### Note1(1)

- 函数式的应用场景 --> 各个函数之间是独立且无共用的数据

### 1. 基本格式

```python
# 定义一个类，Account
class Account:
  	# 方法, 哪个对象调用方法，其就是self
  	def login(self，name):
    		print(123)
        return 666
    def logout(self):
    		pass
# 调用类中的方法 
x = Account()                
# 实例化(创建)Account类的对象，开辟一块内存
val = x.login('henry')        # 使用对象调用class中的方法
print(val)
```

#### Note2(2)

- **应用场景**：用于很多函数，需要对函数进行归类和划分（封装）
- **self**：哪个对象操作，self代表类的**实例**，而非类

### 2. 对象的封装

**作用**：存储一些值，将数据封装到对象，方便使用

**属性调用**：**对象.属性名**进行数据的调用

```python
class File:
  def read(self):
    with open(self.path, mode='r', encoding='utf-8') as f:
      data = f.read()
  def write(self, content):
    with open(self.path, mode='a', encoding='utf-8') as f:
      data = f.write()

obj = File()  					 # 创建对象，并使用   
obj.path = 'test.txt'    # 往obj对象中写入一个私有对象
obj.write(content)
# 定义私有属性,私有属性在类外部无法直接进行访问
obj2 = File('info.txt')
obj2.write(content)
```

```python
class Person:
# __init__初始化方法（构造方法），给对象内部做初始化
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
      	temp = 'i am %s, age:%s, gender:%s ' % (self.name, self.age, self.gender)
      print(temp)
# 类()，会执行__init__         
obj = Person('henry', 19, 'male') 
obj.show()

obj2 = Person('echo', 19, 'female')
obj2.show()
```

#### Note3（3）

1. 函数和数据的封装
   - 如果写代码时，函数较多，可以将**函数归类**，并放入同一类中。（函数的封装）
   - 函数如果有一个反复使用的**公共值**，则可以封装到类中（数据的封装)
2. 面向对象**三大特性**：封装、继承、多态
3. 执行类中的方法时，需要通过**self间接调用**被封装的内容

#### 2.1 查看对象的类

```python
# 类有一个名为 __init__() 的构造方法，该方法在类实例化时会自动调用，一般通过object类进行格式化
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
```

````python
# self.__class__:查看实例所在的类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()
````

#### 2.2 类的方法

​		在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 **self**，且为第一个参数，**self** 代表的是类的实例。**self** 的名字并不是规定死的，也可以使用 **this**，但是最好还是按照约定是用 **self**。

​		类的私有方法**__private_method**：两个下划线开头，声明该方法为**私有方法**，只能在类的内部调用 ，不能在类的外部调用。**self.__private_methods**。

#### 2.3 示例

```python
# 循环让用户输入：用户名，密码，邮箱，输入完成后在打印
class Person():
  def __init__(self, user, pwd, email):
    self.username = user
    self.password = pwd
    self.email = email
  def info(self):
    return  temp = 'i am %s, pwd:%s, email:%s ' % (self.username, self.password, self.email,)

USER_LIST = []
while 1:
  user = input('please input user name: ')
  pwd = input('please input user pwd: ')
  email = input('please input user email: ')
  p = Person(user, pwd, email)
  USER_LIST.append(p)

for i in USER_LIST:
 	data = i.info()
  print(i)
```

### 3.  继承

**场景**：多个类中，如果有公共的方法可以放到基类中，增加代码的重用性。

**继承**：可以对基类中的方法进行覆写

#### 3.1 继承的查找方法

```python
# 父类（基类）
class Base:
  def f1(self):
    pass
  
# 单继承，子类，Foo类继承Base类 （派生类）
class Foo(Base):
  def f2(self):
    pass
# 创建了一个子类对象
obj = Foo()
# 执行对象.方法时，优先在自己类中找，没有则找其父类
obj.f2()    
obj.f1()

# 创建了一个父类对象
obj = Base()
obj.f1()
obj.f2()   # 会报错
```

继承关系中的**查找方法**：

1. self 指的是哪个对象
2. 当类是经典类时，多继承情况下，会按照**深度优先**方式查找
3. 当类是新式类时，多继承情况下，会按照**广度优先**方式查找

#### 3.2 经典类和新式类

​		从字面上可以看出一个老一个新，新的必然包含了跟多的功能，也是之后推荐的写法，从写法上区分的话，如果当前类或者父类继承了object类，那么该类便是新式类，否则便是经典类。

```python
class D(object):
    def bar(self):
        print 'D.bar'
        
class C(D):
    def bar(self):
        print 'C.bar'

class B(D):

    def bar(self):
        print 'B.bar'

class A(B, C):

    def bar(self):
        print 'A.bar'
        
a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> C --> D
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()
```



### 4. 多态（多种形态/类型）

 Pyhon不支持Java和C#这一类强类型语言中多态的写法，但是**原生多态**，Python崇尚“**鸭子类型**”。

```python
# 多态，鸭子模型
def func(arg):  # 多种类型，很多事物
  v = arg[-1]		# 必须具有此方法，呱呱叫
  print(v)
```

```python
# 对于一个函数，python对参数类型不会限制，传入参数时可以是各种类型，在函数中如果有例如：arg.append方法，就会对传入类型进行限制。
# 这就是鸭子模型，类似于上述的函数，我们认为只要能呱呱叫的就是鸭子，只要有append方法，就是我们想要的类型
```

### 5. 类的专有方法

- **_\_init__ :** 初始化，在生成对象时调用
- **_\_del__ :** 析构函数，释放对象时使用
- **_\_repr__ :** 打印，转换
- **_\_setitem__ :** 按照索引赋值
- **_\_getitem__:** 按照索引获取值
- **_\_len__:** 获得长度
- **_\_cmp__:** 比较运算
- **_\_call__:** 函数调用
- **_\_add__:** 加运算
- **_\_sub__:** 减运算
- **_\_mul__:** 乘运算
- **_\_truediv__:** 除运算
- **_\_mod__:** 求余运算
- **_\_pow__:** 乘方

### 6. 运算符重载

Python同样支持**运算符重载**，我们可以对类的专有方法进行重载

```python
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
```



## 7.2 类成员(6)

- 实例化对象时，对在对象中**存储类对象指针**，指向其类

### 1. 类变量（静态字段/属性）

- 写在类的下一级，和方法同级
- 访问：类.变量名/ 对象.变量名
- **继承关系中，自己类中没有的变量可以去基类中找**
- **只能赋值、修改自己的变量**

**对象成员**：**实例变量**（字段）

**Note**：属于谁的只允许谁去取，python允许对象去其类中取变量

### 2. 方法

### 2.1 绑定/普通方法

1. 定义：必须有self参数
2. 执行：先创建对象，由 **对象.方法** 调用

### 2.2 静态方法

1. 定义：@staticmethod， 参数无限制
2. 执行：类.静态方法名() / python对象也可以调用

```python
class Foo:
  	def __init__(self):
    		self.name = 123
    
    def func(self, a, b):
      	print(self.name, a, b)
# python内部装饰器
    @staticmethod
    def f():
      	print(1,2)

Foo.f()
obj = Foo()
obj.func(1, 2)
obj.f()
```

### 2.3 类方法

1. 定义：@classmethod， 必须有cls参数，当前类
2. 执行：类.类方法() / python对象也可以调用

```python
class Foo:
  	def __init__(self):
    		self.name = 123
    
    def func(self, a, b):
      	print(self.name, a, b)
# python内部装饰器
    @classmethod
    def f(cls, a, b):
      	print(a, b)

Foo.f(1, 2)
obj.f(1, 2)   # 不推荐
```

### 3. 属性

1. 定义：@property **只能有一个参数self**
2. **执行**：对象.属性名（ 无括号）

```python
class Foo:
  	@property
  	def func(self):
        print(123)
        print(666)
       
obj = Foo()
ret = obj.func
print(ret)
```

```python
# 示例:属性
class Page：
		def __init__(self, total_count, current_page, per_page = 10):
        self.total_count = total_count
        self.current_page = current_page
        self.per_page = per_page
    
    @proporty
    def start_index(self):
      	return(self.current_page -1 ) * self.per_page
    @property
    def end_index(self):
      	returno self.current_page * self.per_page_count
         
USER_LIST = []
for i in range(321):
  	USER_LIST.append('henry-%s' % (i,))

# 请实现分页
current_page = int(input('请输入要查看的页码：'))
p = Page(321, current_page)
data_list = USER_LIST[p.start_index:p.end_index]
for i in data_list:
  	print(i)
```

### 4. 成员修饰符

- **公有**：所有位置都能访问
- **私有**：_\_开头（只有自己才能访问）

```python
class Foo:
  	def __init__(self, name):
      	self.__name = name    
    def func(self):
      	print(self.name)        
obj = Foo('alex')
print(obj.__name)		# 会报错
obj.func()          # 可以访问
```

```python
class Foo:
  	__x = 1 
    @staticmethod
    def func():
      	print(Foo.__x)
obj = Foo()  
print(Foo.__x)       # 会报错
print(obj._Foo__x)   # 强制访问私有成员
```

## 7.3 特殊方法

- 嵌套
- 特殊成员（方法）_\_init__
- type / isinstance / issubclass / super
- 异常处理

1. **类和对象的关系**：对象是类的一个实例
2. **self**：本质就是一个形式参数，对象调用方法时，python内部会将该对象传给这个参数
3. **类/方法/对像**都可以当作变量或嵌套到其他类中

```python
class School(object):
  	def __init__(self,title):
      self.title = title
    def rename(self):
      pass
   
class Course(object):
  	def __init__(self, name, school_obj):
      self.name = name
      self.school = school_obj
    def reset_price(self):
      pass
      
class Classes(object):
  	def __init__(self,cname, course_obj):
      self.cname = cname
      self.course = course_obj
    def sk(self):
      pass

s1 = School('北京')
c1 = Course('Python', s1)
cl1 = Classes('全栈1期'， c1)
```

### 1. 嵌套

- **函数**：参数可以是任意类型
- **dict**：函数、类和对像都可以作为字典的key， 即都是可hash的
- 继承的查找关系

```python
# 示例1
class StarkConfig(object):
  pass

class AdminSite(object):
  def __init__(self):
    self.data_list = []
  def register(self, arg):
    self.data_list.append(arg)
  
site = AdminSite()
obj = StarkConfig()
site.regisetr(obj)
```

```python
# 示例2
class StarkConfig(object):
  def __init__(self, name, age):
    self.name = name
    self.age = aeg
    
class AdminSite(object):
  def __init__(self):
    self.data_list = []
    self.sk = None
    
  def set_sk(self, arg=StarkConfig):
    self.sk =arg
     
site = AdminSite()
site.set_sk(StarkConfig)
site.sk('henry', 19)
```

```python
# 示例3
class StarkConfig(object):
  list_display = 'henry'
  
  def changelist(self):
    print(self.list_display)
    
class UserConfig(StarkConfig):
  list_display = 'echo'
  
  
class AdminSite(object):
  def __init__(self):
    self._register = {}
    
  def registry(self, key, arg=StarkConfig):
    self._register[key] = arg
  
  def run(self):
    for key, val in self._register.items():
      obj = val()
      obj.changelist()
    
site = AdminSite()
site.registry(1)
site.registry(2, StackConfig)
site.registry(3, UserConfig)     # 易错点 echo
site.run()
```

### 2. 特殊成员

**特殊成员**：为了能够给快速实现某些方法而生。

#### 2.1 _\_init__(初始化方法)

```python
# 填充数据，一般称为初始化
class Foo:
  """
  此类的作用
  """
  def __init__(self):
  """
  初始化方法
  """
    pass
```

#### 2.2 _\_new__(构造方法)

**Note**

1. new方法是静态方法，在使用__new__方法时，构造的对象值为  new 方法的**返回值**
2. 创建的是一块内存和指针

```python
#  __new__ 创建一个空对象
# 通过 __init__ 初始化对像
class Foo(object):
  def __new__(cls, *args, **kwargs):   # 在 __init__ 之前
    return 'henry'/ object.__new__(cls)
  
  obj = Foo()
  print(obj)
```

#### 2.3 _\_call__

```python
# 对象() 会执行类中的 __call__ 方法
class Foo:
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        print('哈哈，你变成我了吧')

Foo()()
# 第三方模块。写一个网站，用户只要来访问，就自动找到第三个参数并执行
make_server('ip', port, Foo())
```

#### 2.4 _\_getitem__   _\_setitem__  _\_delitem__

```python
obj = dict()
obj['k1'] = 123
class Foo(object):
  def __setitem__(self, key, values):
    print(key, value)
  def __getitem__(self, item):
    return item + 'uuu'
  def __delitem__(self, key):
   	print(key)
 
obj1 = Foo()
obj1['k1'] = 123  # 内部会自动调用__setitem__方法
obj1['xxx']       # 内部会自动调用__getitem__方法
del obj1['ttt']   # 内部会自动调用__delitem__方法
```

#### 2.5 _\_str__

```python
# 只有在打印时，会自动调用此方法，并将返回值显示出来
# type 查看
class Foo:
    def __str__(self):
        print('变样是不是不认识我了')
        return 'henry'
      
obj = Foo()
print(obj)
```

#### 2.6 _\_dict__

**作用**： 查看对象中有哪些变量

```python
class Foo(object):
  def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = emial

obj = Foo('henry', 19, '123@qq.com')
val = obj.__dict__ 			   # 去对象中找到所有变量并将其转换为字典
print(val) 
```

#### 2.7 _\_enter__（**上下文管理**）

**作用**：使用with语法时，需要

```python
class Foo(object):
	def __enter__(self):
    self.x = open('a.txt', mode='a', encoding='utf-8')
    return self.x
  def __exit__(self, exe_type, exc_val, exc_tb):
    self.x.close()
  
with Foo() as f:   					# 需要 __enter__ 和 __exit__ 方法
  f.write('henry')
  f.write('echo')
```

#### 2.8 _\_add__ 两个对像相加

```python
class Foo(object):
  def __init__(self, v):
    self.v = v
    
	def __add__(self, other):
    return self.v + other.v

obj1 = Foo()
obj2 = Foo()
val = obj1 + obj2    # obj1触发，把obj1传给self
```

#### 2.9 **_\_iter__**

```python
# 可迭代对象
class Foo:
  	def __iter__(self):
    		return iter([1, 2, 3, 4])
  
obj = Foo()
# 示例2
class Foo:
  	def __iter__(self):
        yield 1
        yield 2
        ...
 
obj = Foo()
```



### 3. 内置函数

#### 3.1 type(对象)

```python
class Foo(object):
  pass

obj = Foo()
print('obj是Foo的对象，开心吧') if type(obj) == Foo else print('哪凉快呆哪去')
```

#### 3.2 issubclass(子类，基类)

```python
# 可以多级继承
class Base(object):
    pass
class Bar(Base):
    pass
class Foo(Bar):
    pass
print(issubclass(Foo, Base))
```

#### 3.3 isinstance(obj, Foo)

```python
# 判断某个对象是否时 某个类 或 基类 的实例(对象)
class Base(object):
    pass
class Foo(Base):
    pass
obj = Foo()
print(isinstance(obj, Foo))
print(isinstance(obj, Base))
```

### 4. super()

```python
# super().func(),根据 self所属类的继承关系进行查找，默认找到第一个就停止
class Bar(object):
  def func(self):
      print('bar.func')
      return 123
class Base(Bar):
 	 def func(self):
      super().func()
      print('bar.func')
      return 123
  
class Foo(Base):
  def func(self):
    v = super().func()
    print('foo.func', v)
  
obj = Foo()
obj.func()
```



## 7.4 接口类和抽象类(约束)&反射

### 1. 扩展

```python
# 会打印 hello
# 类里的成员会加载，代码会执行
# 函数只有在调用时执行
class Foo(object):
  print('hello')
  def func(self):
    pass
```

```python
# 类的嵌套
class Foo(object):
    x = 1
    def func(self):
      	pass

    class Meta(object):
        y = 123
        print('hello')
        def show(self):
          	print(y.self)
```

### 2. 可迭代对象

**表象**：可被for循环的对象

**作用**：组合搜索

**可迭代对象**：在类中实现**_\_iter__**方法并返回**迭代器/生成器**

```python
# 可迭代对象示例1
class Foo:
  	def __iter__(self):
    		return iter([1, 2, 3, 4])
  
obj = Foo()
# 示例2
class Foo:
  	def __iter__(self):
        yield 1
        yield 2
        ...
 
obj = Foo()
```

### 3. 抽象类/接口类(约束 源码)

```python
# python的约束，易错点
# 约束子类中必须要有send方法，如果没有则会抛出：NotImplementedError
class Interface(object):
  def send(self):
    raise NotImplementedError()

class Foo(Interface):
  def send(self):
    pass

class Base(Interface): 
  def func(arg):
    arg.send(arg)
```

```python
# 应用场景示例
class BaseMassage(object):
  def send(self):
    raise NotImplementedError('子类中必须有send方法')
    
class Msg(BaseMassage):
  def send(self):
    print('发送短信')
  
class Email(BaseMassage):
  def send(self):
    print('发送邮件')
  
class Wechat(BaseMassage):
	def send(self):
    print('发送微信')
  
class DingDing(BaseMassage):
	def send(self):
		pass

obj = Email()
obj.send()
```

### 4. 反射

**作用**：根据字符串的形式，去某个对象中操作他的成员。

- **getattr**('对象'， 字符串)：根据字符串的形式，去某个对象中获取其成员。
- **hasattr**('对象'， 字符串)：根据字符串的形式，去某个对象中判断是够有该成员。
- **setattr**('对象'， '变量'，值)：根据字符串的形式，去某个对象中设置成员。
- **delatttr**('对象'， '变量')：根据字符串的形式，去某个对象中删除成员。

```python
# getattr示例
class Foo(object):
  def __init__(self, name):
    self.name = name
    
obj = Foo('alex')
obj.name
v1 = getattr(obj, 'name')
# setattr示例
obj.name = 'eric'
setattr(obj, 'name', 'eric')
```

- **getattr**：反射当前文件内容

```python
# 反射当前文件内容
import sys
getattr(sys.modules[__name__], 'ab')
# 通过对象获取、示例变量、绑定方法
# 通过类来获取类变量、类方法、静态方法
# 通过模块名获取模块中的任意变量(普通变量、函数、类)
# 通过本文件反射任意变量
```

```python
# 应用示例
class Foo(object):
   def login(self):
      pass
    
   def regiseter(self):
      pass
  
obj = Foo()
func_name = input('please input method name: ')
# 获取方法
getattr(obj, func_name)()
```

```python
# setattr 示例
class Foo(object):
  pass

obj = Foo()
setattr(obj, 'k1', 123)
print(obj.k1)
```

```python
# delattr 示例
class Foo(object):
  pass

obj = Foo()
obj.k1 = 999
delattr(obj, 'k1')
print(obj.k1)
```

#### Note（2）

- python中一切皆对象（py文件，包，类，对象），可以通过getattr获取
- 通过字符串操作内部成员都可以通过反射的机制实现

```python
import x

v = x.NUM
# 等价于
v = getattr(x, 'NUM')
print(v)

v = getattr(x, 'func')
v()

v = getattr(x, 'Foo')
val = v()
val.x
```

示例：

```python
# 浏览器两类行为
# way1: 输入地址+回车
get....
# way2: 表单（输入框+按键）
post....

# 浏览器都会有get，post，dispatch方法
class View(object):
  def get(self):
    pass 
  def Post(self):
    pass
  def Dispatch(self):  # 请求第一步来这，在进行分发
    pass
```

```python
# 推荐使用性能较好
class Foo(object):
  def post(self):
    pass

# 方式1
if hasattr(obj, 'get'):
  getattr(obj, 'get')
# 方式2：推荐使用
v = getattr(obj, 'get', None)
print(v)
```



## 7.5 单例&项目结构

### 1. 单例模式

#### 1.1 单例

**场景**：**数据库**连接和数据库**连接池**（数据一致时）

**设计模式**：23种设计模式

```python
class Foo(object):
  pass 
# 每实例化一次，就创建一个新对象,内存地址 不一样
obj1 = Foo()
obj2 = Foo()
```

```python
# 单例(Singleton)模式，无论是实例化多少次，都用第一次创建的那个对象，内存地址一样
class Singleton(object):
  instance = None
  def __new__(cls, *args, **kwargs):
    if not cls.instance:
    	cls.instance = object.__new__(cls)
    return cls.instance
 
obj1 = Singleton()      # 内存地址一致
obj2 = Singleton()
```

#### 1.2 标准

```python
# 需要加锁，多线程，并发
```

```python
class FileHelper(object):
  instance = None
	def __init__(self, path):
    self.file_object = open(path, mode='r', encoding='utf-8')
  
  def __new__(cls, *args, **kwargs):
    if not cls.instance:
      cls.instance = object.__new__(cls)
    return cls.instance

obj1 = FileHelper('x')   # 内存地址一致
obj2 = FileHelper('x')
```

### 2. 模块导入

```python
# 导入模块，只是保留模块内存
# 思考角度：函数名不能重复、内存溢出
from jd import n1

# 多次导入，模块只会加载一次，即使模块中包含其他模块
import jd
import jd
print(456)
```

```python
# 多次导入，模块只会加载一次，即使模块中包含其他模块
import importlib
import jd
# 手动加载，会覆盖第一次导入
importlib.reload(jd)  
print(456)
```

- 通过模块导入特性，也可以实现单例模式

```python
# jd.py
class Foo(object):
  pass
obj = Foo()
```

```python
# app.py
import jd                # 加载jd.py,加载最后会实例化一个Foo对象并赋值给obj
print(jd.obj)
```

### 3. 项目开发规范

1. **bin**：**start**
2. **config**：配置文件**settings**
3. **src**：业务逻辑
4. **db**：数据文件
5. **lib**：扩展模块
6. **log**：日志文件

#### 3.1 脚本

```python
import os
import re
import datetime

import xlrd
import requests
```

#### 3.2 单可执行文件

```python
# app(程序入口)/src(业务相关)/lib(公共的类库)/db(文件)/config(配置)
app.py 越简单越好，少于10行
```

#### 3.3 多可执行文件

```python
# app(程序入口)/src(业务相关)/lib(公共的类库)/db(文件)/config(配置)
# bin(多个可执行文件例如：student.py，teacher.py，admin.py)
# log	(存储日志文件)
# seetings(BASE_PATH,LOG_FILE_NAME...)
path = sys.path.os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
```

![项目目录结构](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/%E9%A1%B9%E7%9B%AE%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84.png)

# 番外篇之正则

## 1. 基本概念

1. re模块本身只是用来操作正则表达式的和正则本身无关
2. **正则表达式**：是一种匹配字符串的规则
3. 为什么要有正则：应用**场景**
   - **匹配字符串**
   - **表单验证**：11位，全数字，1开头，第二个数 3-9，绑定银行卡
   - **爬虫**：从网页源码中获取链接，重要数据

## 2. 规则

### 2.1 元字符

- 是哪个一字符就匹配字符串中的哪**一个**字符

2. 字符组（3）
   - [ad] ，匹配a/d，**单字符匹配**
   - [0-9]， [a-z]， [A-Z] (范围是**从小到大)**,遵循ASCII码
   - [a-zA-Z], [0-9x]
3. 转义字符（7 ）
   - [0-9] 等价于  **\d** (\转义符，转义d使得其匹配0-9之间的数)
   - \w：(word,数字，大小写字母，下划线) 
   - \s：(space, 空格，换行，制表符)  (\t(table) \n(next))
   - \D  \W  \S(对以上结果取反)
   - **\b**：匹配**\w**和**\W**之间，即匹配单词边界匹配一个**单词边界**，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
4. 特殊符号的含义（4）
   - **.** 除了换行符之外的任意内容
   - [\d] [0-9] \d 没有区别。 [\d\D] **匹配所有**
   - [^abc]：**非字符组**，[abc] 取反
   - ^：表示一个字符的开始。 $：表示一个字符的结束 (^abc\$)
5. | 和（）eg. abc|edf。  abc|ab 

```python
# 若果规则有重叠，需要长的在前面
www.(baidu|google).com
# () 表示分组，给一部分正则规定为一组，
```

### 2.2 量词（6）

```python
1[3-9]\d{9}     # 量词前面一个重复次数，9次
1[3-9]\d{9,}    # 量词前面一个重复次数，9次以上
1[3-9]\d{n,m}   # 量词前面一个重复次数，n-m次
?               # ? 匹配到0次或1次，没匹配上也算一次，匹配上算2次
								#（可有可无，只能有一个）
+							  # + 匹配1次或多次
*               # * 匹配0次或多次
```

```python
# 匹配任意小数，保留两位
\d+\.\d{2}
# 匹配任意整数或小数
\d+\.?\d*		    # 有bug
\d+(\.\d+)?     # 分组实现
```

### 2.3 贪婪匹配/惰性匹配

```python
\d{7-12}        # 默认是贪婪匹配，尽量多匹配
                # 回溯算法
  
# 非贪婪匹配，惰性匹配，总是匹配符合条件范围内尽量小的字符串
\d{2,3}?			  # 匹配两位数
\d+?3           # 尽量多取，遇到3结束
元字符 量词 ？x   # 按照元字符规则在量词范围内匹配，一旦遇到x停止
.*?x            # 常用，先找x找到匹配结束
```

```python
# 身份证号匹配(正则表达式，断言)
[1-9](\d{16}[\dx]|\d{14})
[1-9]\d{14}(\d{2}[\dx])

^([1-9]\d{16}[0-9x]|[1-9]\d{14})$
```

```python
. 是任意字符
* 是取 0 至 无限长度
? 是非贪婪模式。
.*?x              # 就是取前面任意长度的字符，直到一个x出现
```

### 2.4 示例

```python
# 匹配邮箱
\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}

# url
^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+
```



## 3. re模块

### 3.1 compile()

- 编译正则表达式模式，返回一个对象的模式。（可以把那些常用的正则表达式编译成正则表达式对象，这样可以提高一点效率。）

- 格式：re.compile(pattern,flags=0)，pattern: 编译时用的表达式字符串。flags 编译标志位，用于修改正则表达式的匹配方式，如：是否区分大小写，多行匹配等。常用的flags有：

| 标志               | 含义                                                     |
| ------------------ | -------------------------------------------------------- |
| re.S(DOTALL)       | 使匹配包括换行在内的所有字符                             |
| re.I（IGNORECASE） | 使匹配对大小写不敏感                                     |
| re.L（LOCALE）     | 做本地化识别（locale-aware)匹配，法语等                  |
| re.M (MULTILINE)   | 多行匹配，影响^和$                                       |
| re.X (VERBOSE)     | 该标志通过给予更灵活的格式以便将正则表达式写得更易于理解 |
| re.U               | 根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B       |

```python
import re
tt = "Tina is a good girl, she is cool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))   
# 查找所有包含'oo'的单词
执行结果如下：
['good', 'cool']
```

###3.2 re.match()

   **格式**：re.match(pattern, string, flags=0)

   - 在search前的正则前加了一个：**^**

   - 想要**完全匹配**，可以在表达式末尾加上边界匹配符**$**，没有匹配到，则返回 **None**

   ```python
   # 从字符串开头匹配，匹配上则返回一个match对像，有group()方法
   import re 
   ret = re.match('\d', '8alex83')  
   print(ret)
   ```

###3.3 search()

   **格式**：re.search(pattern, string, flags=0)

   - re.search只要找到**第一个**匹配然后返回，如果字符串没有匹配，则返回**None**。

   ```python
   print(re.search('\dcom','www.4comrunoob.5com').group())
   # 执行结果如下：4com
   ```

   **注**：match和search一旦匹配成功，就是一个**match object对象**，而match object对象有以下方法：

   - start() 返回匹配开始的位置
   - end() 返回匹配结束的位置
   - span() 返回一个元组包含匹配 (开始,结束) 的位置
   - group() 返回re整体匹配的字符串，可以一次输入多个组号，对应组号匹配的字符串。

a. group（）返回re整体匹配的字符串，
   b. group (n,m) 返回组号为n，m所匹配的字符串，如果组号不存在，则返回indexError异常
   c.groups（）groups() 方法返回一个包含正则表达式中所有小组字符串的元组，从 1 到所含的小组号，通常groups()不需要参数，返回一个**元组**，元组中的元就是正则表达式中定义的组。 

```python
   import re
   a = "123abc456"
    print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,返回整体
    print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
    print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
    print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))   #456
   ###group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。###
```

###3.4 findall()

    **格式**：re.findall(pattern, string, flags=0)

   - 可以获取字符串中所有匹配的字符串，**返回一个列表**，没有匹配则为空。

   ```python
   p = re.compile(r'\d+')
   print(p.findall('o1n2m3k4'))
   执行结果如下：
   ['1', '2', '3', '4']
   ```

   ```python
   import re
   tt = "Tina is a good girl, she is cool, clever, and so on..."
   rr = re.compile(r'\w*oo\w*')
   print(rr.findall(tt))
   print(re.findall(r'(\w)*oo(\w)',tt)) # ()表示子表达式 
   执行结果如下：
   ['good', 'cool']
   [('g', 'd'), ('c', 'l')]
   ```

###3.5 finditer()

   **格式**：re.finditer(pattern, string, flags=0)

   - 搜索string，返回一个顺序访问每一个匹配结果（**Match对象**）的迭代器。找到 RE 匹配的所有子串，并把它们作为一个迭代器返回。

   ```python
   # 匹配到结果为 迭代器，每一项都是match对象，通过group取值
   import re
   ret = re.finditer('\d', 'safh123ghakjdsfg234'*2000000)
   for i in ret:
     print(i.group())
   ```

###3.6 split()

    **格式**：re.split(pattern, string[, maxsplit]，maxsplit用于指定最大分割次数，不指定将全部分割。
    
    - 按照能够匹配的子串将string分割后返回列表。
    - 可以使用re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表。
    
    ```python
    import re
    ret = re.split('\d+', 'henry18')
    print(ret)
    # 保留分组中内容
    ret = re.split('(\d+)', 'henry18')
    print(ret)
    ```


###3.7 sub()/ subn()


    **格式**：re.sub(pattern, repl, string, count=0)
       
    **格式**：subn(pattern, repl, string, count=0, flags=0) 

   - 不返回/返回替换次数

     ```python
     
     ```

    import re
    text = "JGood is a handsome boy, he is cool, clever, and so on..."
    print(re.sub(r'\s+', lambda m:'['+m.group(0)+']', text,0))        # flags=0默认参数
    执行结果如下：
    JGood[ ]is[ ]a[ ]handsome[ ]boy,[ ]he[ ]is[ ]cool,[ ]clever,[ ]and[ ]so[ ]on...
     ```
    
    ```python
    # 替换 n 次
    ret = re.sub('\d', 'G', 'henry18',n)
    print(ret)
    # 返回替换次数（tuple类型）
    ret = re.subn('\d', 'G', 'henry18')
    print(ret)  # 返回值为tuple类型
    ```


## 4. 分组

### 4.1 特殊分组用法

| 语法       | 含义                                       | 示例                 |            |
| ---------- | ------------------------------------------ | -------------------- | ---------- |
| (?P<name>) | 分组，除了原有的编号外再指定一个额外的别名 | (?P<id>abc){2}       | abcabc     |
| (?P=name)  | 引用别名为<name>的分组匹配到字符串         | (?P<id>\d)abc(?P=id) | 1abc15abc5 |
| \<number>  | 引用编号为<number>的分组匹配到字符串       | (\d)abc\1            | 1abc15abc5 |
| (?<=….)    | 以…开头，并不包括开头                      |                      |            |
| (?<!….)    | 不以…结尾，并不包括开头                    |                      |            |

#### Note（3）

1. [^] 带有特殊意义的元字符到字符组中大部分会取消它特殊意义
2. [()+*.]：取消特殊含义，恢复原本意义
3. [-]：第一个或最后表示横杠，中间位置表示范围

### 4.2. group()

- 括号中**默认为0**，即取第0个分组

```python
s = '<h1>wahaha</h1>'
ret = re.search('(\w+)>(.*?)</\w+>', s)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
```

### 4.3 分组命名

- **(?P<name>正则表达式)**
- name：不需要加引号，本身就是字符串

```python
ret = re.search('<(?P<tag>\w+)>(?P<content>.*?)</\w+>', s)
print(ret.group('tag'))
print(ret.group('content'))
```

### 4.4 引用分组

- **(?P=name)**

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

### 4.5 取消分组优先

- **(?:)**

```python
# findall 遇到正则中的分组 优先 显示分组中的内容
import re
ret = re.findall('\d(\d)', 'henry18')
print(ret)
# 取消分组优先（?:正则表达式）
ret = re.findall('\d+(?:\.\d+)?', '1.234+2')
print(ret)
```

### 4.6 split，保留分割符

- **()**

```python
# 保留分组中内容
ret = re.split('(\d+)', 'henry18')
print(ret)
```

## 5. 练习

```python
# 示例1：匹配单个数字，findall方法会有屏蔽所有其他匹配项，只显示分组中内容
import re
ret = re.findall(r'\d+\.\d+|(\d)', '2+23*3.42/3.2')
print(ret)
while True:
    if '' not in ret:break
    ret.remove('')
print(ret)
```

```python
# 示例2：匹配以...开头的数据，不包括开头
import re
m = re.findall('(?<=>)\w+', '\<a>wahaha\</a>\<b>banana\</b>\<h1>qqxing\</h1>')
 for i in m:
     print(i)
# 匹配不以...开头的数据，不包括结尾
m = re.findall('(?<!>)\w+', '\<a>wahaha\</a>\<b>banana\</b>\<h1>qqxing\</h1>')
print(m)
```

- | ：或只负责把两个表达式分开，如果是整个表达式中只对一部分内容进行或，需要分组

- ()：限定一组正则的量词约束 (\d\w)?

```python
# 示例3：以a开头，由至少一个字母组成的字
^a[a-zA-Z]+
^a[a-zA-Z]*
```

```python
# 以1开头，中间3-5个数字，如果中间位置超过5个数字，则整个字符串不匹配
^1\d{3,5}$
```

```python
# 示例4：匹配用户输入的身份证号
import re
content = input('用户输入：')
ret = re.match('[1-9]\d{14}(\d{2}[\dx])?$', content)
```

```python
# 示例5：第一个乘除法
import re
ret = re.search('\d+(\.\d+)?[\*]-?\d+(\.\d+)?', s)
```



___

___

# 附录1:  常见报错

1. SyntaxError: invalid syntax；语法错误：无效语法（变量定义不规范）
2. SyntaxError: invalid character in identifier 语法错误；无效字符（中英文字符混乱）
3. ValueError: invalid literal for int() with base 10: 'henry'；(非法类型转换)
4. NameError: name 'D' is not defined ;（一般发生是变量不合法）
5. ValueError: invalid literal for int() with base 10: '3  2'
   - 字符串没有，强制转换为int
6. TypeError: sequence item 0: expected str instance, int found
   - join 只能是str
7. ValueError: too many values to unpack (expected 2)
   - 赋值号两边参数不一致



# 附录2:  错误记录

1. input() 的数据类型永远是 str
2. 当 break在循环里时，有些时候可以省略 else
3. while True的效率会更高
4. 计数可以倒序(用于while循环)
5. 一直要求用户输入，或者死循环需要使用 while True
6. exit() 终止程序
7. range(0, 100) # 此时可以省略0 ,tpye(range(100)).     <class 'range'>
8. message = '登陆失败'。变量标记
9. li.extend(s1) # 遍历 s1 中的每个元素，追加到list中
10. li.pop(index) # 可以获取删除值
11. li.remove('a') # list 删除指定元素，li中没有会报错
12. ','.join(li) # 只要支持循环就支持 join，操作对象必须是 str 否则报错
13. 当使用s.isdigit()时要注意，s 的数据类型,有空格和其他字符都会返回  False
14. list(dic.keys()) # 可以强转为list，如果是items则list元素为tuple
15. 集合之间操作时，如果元素为空，则输出set()
16. 在循环里操作时，注意代码的有效范围
17. info.get('key', '不存在'）  # 可以返回两种不同的结果
18. 判断key是否在dict中只需：if key in info：
19. type(i) is int   # 这里的 int 是类
20. tyep(i) == int  # 可以判断数据类型, 地址和内容都是一样
21. 集合之间操作时，如果元素为空，则输出set()
22. 在循环里操作时，注意代码的有效范围
23. info.get('key', '不存在'）  # 可以返回两种不同的结果
24. 判断key是否在dict中只需：if key in info：
25. type(i) is int   # 这里的 int 是类
26. tyep(i) == int  # 可以判断数据类型, 地址和内容都是一样
27. 集合之间操作时，如果元素为空，则输出set()
28. 在循环里操作时，注意代码的有效范围
29. info.get('key', '不存在'）  # 可以返回两种不同的结果
30. 判断key是否在dict中只需：if key in info：
31. type(i) is int   # 这里的 int 是类
32. tyep(i) == int  # 可以判断数据类型, 地址和内容都是一样
33. 只要是'_'.join 处理过的，都是srt
34. s.split(',') :
    - 默认是空白，实际应用中可以是字符或字符串；
    - 循环去除；
    - 但变量有且仅能是一个。
35. 只要是'_'.join 处理过的，都是srt
36. s.split(',') :
    - 默认是空白，实际应用中可以是字符或字符串；
    - 循环去除；
    - 但变量有且仅能是一个。
37. 程序一行太长显示不全，可以使用 \ 进行换行
38. 函数传输文件名时，需要传输 str 类型
39. line = line.strip('\n').split('|'),从左到右操作
40. 如果需要双重甚至多重循环时， 可以考虑先构造一个子元素利用函数返回值默认时 None 可以实现 flag 标志功能
41. range()是range类
42. return 1， 2， 3 返回的是元组
43. 注意：函数类似于变量，func 代指一块代码的内存地址。
44. a = ('b', 3, 4)*2 ，tuple里面的数据重复2次，list 和 tuple都可以
45. for循环是根据索引进行循环，删除元素后，后面要进行补位
46. socket收发内容必须是**bytes**类型
47. 



