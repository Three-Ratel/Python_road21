[TOC]



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

​	**字节码（Bytecode）**是一种包含执行程序、由一序列 op 代码/数据对 组成的**二进制文件**。**字节码是一种中间码**。它比机器码更抽象，需要直译器转译后才能成为机器码的中间代码。

​	**机器码(machine code)**，学名机器语言指令，有时也被称为原生码（Native Code），**是电脑的CPU可直接解读的数据**。**机器码**是电脑CPU直接读取运行的机器指令。

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
value = int(data) if data.isdecimal() else Non
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
  
  - **filter**
  
  ```python
  v = [1, 2, 3, 'welcome', 4, 'hello']
  result = filter(lambda x: type(x) == int, v) # 生成新list
  print(list(result)
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
  
  # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
  [(1, 2, 3), (4, 5, 6)]
  # 两组序列，转字典
  list1 = ['key1','key2','key3']
  list2 = ['1','2','3']
  info = dict(zip(list1,list2))
  print(info)
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

- 使用**func._\_name__**获取被调用的func函数名，func为形参

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

- **yiled**可以保存状态，yield的状态保存与操作系统的保存线程状态很像，但是yield是代码级别控制的，更轻量级
- **send**可以把一个函数的结果传给另外一个函数，以此实现单线程内程序之间的切换

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

6. 酸爽生成器

   - 所有生成器取一次就没有了

   - 不取不会执行，**惰性运算**

```python
# 示例1
ret = filter(lambda n: n%3==0, range(10))
print(len(list(ret)))                    # 4
print(len(list(ret)))										 # 0
```

```python
# 示例2
def add(n, i):
  return n + i

def test():
  for i in range(4):
    yield i
    
g = test()
for n in [1, 10]:
  g = (add(n, i) for i in g)
  
print(list(g))
# [20 21 22 23 24]
```

```python
# 示例3
def add(n, i):
  return n + i

def test():
  for i in range(4):
    yield i
    
g = test()
for n in [1, 10, 5]:
  g = (add(n, i) for i in g)
  
print(list(g))
# [15, 16, 17, 18]
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

## 6.1 模块的导入

1. **模块**：可以是py文件也可以是文件夹
   - py文件，写好了的对程序员直接提供某方面功能
   - import / from xxx import xx
   - **包**：存储了多个py文件的文件夹，pickle，json，urlib
   - 如果导入一个包，**包里默认模块是不能使用的**
     - 导入一个包相当于执行**_\_init__.py**文件内容
2. **定义模块时**，可以把一个py文件或一个包当作一个模块，以便于以后其他py文件使用。
3. **_\_ init__.py** 在文件夹中创建此py文件， **python packages**
   - py2：**文件夹**中必须有_\_ init__.py 
   - py3：不需要，推荐加上
4. **导入模块**
   1. 导入模块—>调用模块中的函数（import 文件名）
   2. import 会把**模块中的文件**加载到内存
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

### 1. random(7)

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

1. random.randint(1,5)
2. random.choice([1, 2, 3])：随机选择一个：验证码，抽奖≥
3. random.sample([1, 2, 3, 4, 5], 3)：随机选3个不重复，抽奖多个人
4. random.uniform(1, 5)：随机1-5中的随机小数
5. random.shuffle([1,2,3,4])：洗牌，算法
6. random.random()：随机生成**[0-1)**之间的数
7. random.randrange(1,5)：**randint基于randrange**

### 2. hashlib(1) / getpass

摘要算法模块，**密文验证**/**校验文件独立性**

#### note1(3)

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

### 3. time(2)

```python
import time
v = time.time() # 获取从1970年开始到目前的时间，单位为秒
time.sleep(2)  	# 休眠时间，2秒
```

### 4. sys (5)

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

### 5. os(操作系统相关)(16)

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
15. os.getpid()：获取进程的id
16. os.getppid()：获取其父进程的id

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

### 6. shutil(4)

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

**序列化**：将原本的字典、列表等内容转换成一个字符串的过程就叫做**序列化**。

**目的**：

1. 以某种存储形式使自定义**对象持久化**
   - 对象持久化是指将内存中的对象保存到**可永久保存**的存储设备中（如磁盘）的一种技术。
2. 将对象从一个地方传递到另一个地方。
3. 使程序更具维护性。

![序列化](/Users/henry/Documents/截图/Py截图/序列化.png)

- **json**， 所有语言通用，**只能**序列化指定的基本数据类型
  - dumps/loads/ dump/load
  - 所有字符串必须都是**双引号**
  - **最外层**只能是**dict/list**
  - 不能支持load多次
  - dict中**key**只能是**str**
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

#### Note(2)

1. 经过编码过后的数据，通常称为 **字节类型**/bytes，字符串，格式为：b‘XXXXXXXX'
2. 压缩后的0101

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
tz = timezone(timedelta(hours = 7))    # 东7区
v3 = datetime.now(tz)                  # 当前东7区时间

<class 'datetime.datetime'>
```

```python
# 将datetime格式时间转化为str
v1 = datetime.now()
v1.strftime('%Y-%m-%d')                # 连接不能使用汉字（Mac，linux没问题），可以使用.format()方法
```

```python
# str转datetime，时间加减
val = datetime.strptime('2019-04-18', '%Y-%m-%d')
v = val +/- timedelta(days=40)         # 当前时间加/减40天
```

```python
# 时间戳和datetime关系
import time, datetime
ctime = time.time()
datetime.fromtimestamp(ctime，tz)      # 当前时间,tz和上述相同
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

## 7.1 面向对象基础

**面向对象编程**（Object Oriented Programming，**OOP**，面向对象程序设计）

**优点和应用场景**：

1. 业务功能较多时，通过面向对象归类
2. 数据封装（创建字典存储数据）
3. 游戏示例：创建一些角色，并根据角色需要再创建任务

- **封装思想**：将同一类的函数封装到同一个py文件中，以后方便使用
- **面向对象**：将同一类的函数封装到同一个class中，以后方便使用
- **对象名**：命名首字母大写

#### Note1(1)

- 函数式的应用场景 --> 各个函数之间是独立且无共用的数据

### 1. 基础概念

- **类**：具有相同方法和属性的一类事物
- **对象**、**实例**：一个拥有具体属性值和动作的具体个体
- **实例化**：从一个类得到一个具体对象的过程

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

- **作用**：存储一些值，将数据封装到对象，方便使用
- **属性调用**：**对象.属性名**进行数据的调用
- **广义封装**：类中成员
- **狭义封装**：私有成员：_类名__名字：命名

```python
class File:
  def read(self):
    with open(self.path, mode='r', encoding='utf-8') as f:
      data = f.read()
  def write(self, content):
    with open(self.path, mode='a', encoding='utf-8') as f:
      data = f.write()

obj = File()  					                        # 创建对象，并使用   
obj.path = 'test.txt'                           # 往obj对象中写入一个私有对象
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

#### Note3(3)

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

- **新式类**：继承object，super，多继承（**广度优先c3**），具有mro方法
  - super（新式类支持，遵循**mro**顺序）
- **经典类**：py2不继承object，**无super/mro** ， 深度优先

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

**多态**：一个类变现出来的多种状态—>多个类表现出相似的状态。

 Pyhon不支持Java和C#这一类强类型语言中多态的写法，但是**原生多态**，Python崇尚“**鸭子类型**”。list，tuple，python的多态是通过鸭子类型实现的

```python
# 多态，鸭子模型
def func(arg):                   # 多种类型，很多事物
  v = arg[-1]		                 # 必须具有此方法，呱呱叫
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

1. **定义**：必须有self参数
2. **执行**：先创建对象，由 **对象.方法** 调用

### 2.2 静态方法

1. **定义**：@staticmethod， 参数无限制
2. **执行**：类.静态方法名() / python对象也可以调用

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

1. **定义**：@classmethod， 必须有cls参数，当前类
2. **执行**：类.类方法() / python对象也可以调用

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

1. **定义**：@property **只能有一个参数self**
2. **执行**：对象.属性名（ **无括号**）

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

- 特殊方法/魔术方法/内置方法/双下方法
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

#### 2.9 _\_iter__

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

- **表象**：可被for循环的对象
- **作用**：组合搜索
- **可迭代对象**：在类中实现**_\_iter__**方法并返回**迭代器/生成器**

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
        ...''
 
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

反射的概念是由Smith在1982年首次提出的，**主要是指程序可以访问、检测和修改它本身状态或行为的一种能力（自省）**。这一概念的提出很快引发了计算机科学领域关于应用反射性的研究。它首先被程序语言的设计领域所采用,并在Lisp和面向对象方面取得了成绩。

**反射**：通过字符串的形式操作对象相关的属性。python中的一切事物都是对象（都可以使用反射）

- **getattr**('对象'， 字符串)：根据字符串的形式，去某个对象中获取其成员。
- **hasattr**('对象'， 字符串)：根据字符串的形式，去某个对象中判断是否有该成员。
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
- 通过**字符串操作内部成员**都可以通过反射的机制实现

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





# 第八章 网络编程

1. 网络基础
2. 基于tcp协议和udp协议的**socket**
3. 解决tcp协议的**粘包问题**
4. **并发**

## 8.1 网络基础

### 1. 基本概念(2)

1. 两个运行中的程序传递信息？
  
   - 通过**文件**，通过**网络**
3. 网络应用开发架构
   - C/S：client/server（需要安装对应的客户端）
   
   ![c:s架构](/Users/henry/Documents/截图/Py截图/c:s架构.png)
   
   - B/S：browser/server（不需要任何客户端）
     - 统一程序的入口
   - B/S是特殊的C/S

### 2. 网络中的概念(7)

1. **网卡(3)**
   - mac地址：48位, 6位冒分十六进制
   - head中包含的源和目标地址由来
     - ethernet规定接入internet的设备都必须具备网卡，发送端和接收端的地址便是指网卡的地址，即mac地址。
   - mac地址：每块网卡出厂时都被烧制上一个世界唯一的mac地址，长度为48位2进制，通常由12位16进制数表示（**前六位是厂商编号**，后六位是流水线号）
2. **交换机(4)**
   - **功能**：负责局域网通信（只认识mac地址，通过arp/ rarp协议）
   - **通信方式**：广播、单播、组播(交换机只使用前面的**两种**)
   - **ARP**协议：地址解析协议，通过ip地址，获取其mac地址
   - **保留网段（私有IP）**：192.168.0.0-92.168.255.255 /172.16.0.0-172.31.255.255 /10.0.0.0-10.255.255.255
   - **广播限制**在二层交换机的局域网范围内，**禁止广播数据穿过路由器**，防止广播数据影响大面积的主机
3. **路由器(2)**
   - 负责局域网间通信
   - **网关ip**：**局域网的网络出口**，访问局域网之外的区域都需要经过gateway
   - 路由器（Router）又称**网关设备**（Gateway）是用于连接多个逻辑上分开的网络
4. **协议**
   - server和client得到的内容都是二进制，双发预先约定好的一套语法规则 
   - 语法、语义、时序
5. **IP地址**
   - Ipv6:冒分16进制，0:0:0:0:0:0:0:0- FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF(128bits, 16x8)
   - 每一个ip地址要想被所有人访问到，那么这个ip地址必须是申请的
6. **port 端口(4)**
   - 端口号0 - 65535

   - 一个端口同一时刻只能被一个服务占用
   - ip+port：可以确认一台机器上的一个应用
   - 1024以内只能是root才能启用



## 8.2 OSI&TCP/IP

### 1. TCP协议(6)

1. **TCP**（Transmission Control Protocol）可靠的、面向连接的协议（eg:打电话）、传输效率低全双工通信（发送缓存&接收缓存）、**面向字节流**。
2. **应用场景**：文件上传下载（邮件、网盘、缓存电影）、Web浏览器；电子邮件、文件传输程序。
3. **特点**（3）：面向连接、可靠、流式传输的全双工通信
4. **三次握手**：请求(SYN)—> 确认(ACK)+请求—>确认
   - **server端** **accept** 接收过程中等待客户端的连接
   - **connect** 会发送一个**syn**连接请求
     - 如果收到了server响应**ack**和由server端发来的**syn**连接请求
     - client端进行回复ack信息后，建立了一个tcp连接
   - 三次握手过程在代码过程中是由**accept**和**connect**共同完成，具体细节在socket没有体现
5. **四次挥手**：请求(FIN)—> 确认—>请求—>确认
   - server 端和clinet端在代码中都有**close**方法，每一端发起的close操作都是断开**fin**请求，得到断开确认**ack**之后，就可以结束一端的数据发送
   - 如果两端发起close请求，那么就是**两次请求**和**两次确认**，一共是四次操作
   - 可以结束数据发送，表示连接断开
6. **长连接**：会一直占用双方port
7. I/O：相对于**内存**来说
   - write 是 send
   - read 是 recv
   - i input 向内存中输入 input，read，recv， recvfrom， accept， connect， close
   - output 从内存中输出 print，write，send，sendto， accept， connect， close

![TCP](/Users/henry/Documents/截图/Py截图/TCP.png)

### 2. UDP协议

1. **UDP**（User Datagram Protocol）不可靠的、无连接的服务，传输效率高（发送前时延小），一对一、一对多、多对一、多对多、面向报文，尽最大努力服务，无拥塞控制。
2. 场景**：即时通讯（qq，wechat），域名系统 (DNS)；视频流；IP语音(VoIP)。
3. **特点**：面向数据报，不可靠，传输速度快，能完成一对多，多对一，和一对一的高效通信
4. **UDP** 是User Datagram Protocol的简称， 中文名是用户数据报协议

#### Note1(3)

- TCP传输**数据几乎没有限制**，UDP能够传递数据长度是有限的，是根据数据传递设备的设置有关
- Tcp可靠**长**连接，udp不可靠无连接
- 三次握手时，确认信息和请求连接信息合并为一帧，四次挥手，主动断开端，不能确定另一端是否还需要传输信息，所以不能合并。

### 3. OSI(Open System Interconnection)

1. 应用层
2. 表示层
3. 会话层
4. 传输层
5. 网络层
6. 数据链路层
7. 物理层

OSI**五层**协议(简化)

1. 应用层：代码
2. 传输层：tcp/udp **端口号**，**四层路由器、四层交换机**
3. 网络层：ipv4/ipv6，**三层路由器、三层交换机**
4. 数据链路层：mac地址，arp协议，**(二层)交换机**
5. 物理层：二进制流

TCP/IP(**arp在tcp/ip中属于网络层**)

1. 应用层
2. 传输层
3. 网络层
4. 链路层

#### Note2(4)

1. 家用路由器集成了交换功能
2. **网络协议**
   - **网际层**协议:IP协议、ICMP协议、ARP协议、RARP协议。 
   - **传输层**协议:TCP协议、UDP协议。 
   - **应用层**协议:FTP、Telnet、SMTP、HTTP、RIP、NFS、DNS

### 4. socekt(套接字)

1. 工作在**应用层**和**传输层**之间的**抽象层**，帮助我们完成所有信息的**组织**和**拼接**
   - Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是**一组接口**。在**设计模式中**，Socket其实就是一个门面模式，它把复杂的**TCP/IP协议族隐藏在Socket接口后**面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。
2. socket历史
   1. 套接字起源于 20 世纪 70 年代加利福尼亚大学伯克利分校版本的 Unix,即人们所说的 **BSD Unix**。 因此,有时人们也把套接字称为“伯克利套接字”或“BSD 套接字”。一开始,套接字被设计用在同 一台主机上多个应用程序之间的通讯。这也被称**进程间通讯**,或 **IPC**。**套接字有两种**（或者称为有两个种族）,分别是**基于文件**型的和**基于网络**型的。 
   2. **基于文件类型的套接字家族**
      - 套接字家族的名字：**AF_UNIX**，unix一切皆文件，基于文件的套接字**调用**的就是**底层的文件系统**来取数据，两个套接字进程运行在同一机器，可以通过访问同一个文件系统间接完成通信
   3. **基于网络类型的套接字家族**
      - 套接字家族的名字：**AF_INET**，(还有**AF_INET6**被用于ipv6，还有一些其他的地址家族，不过，他们要么是只用于某个平台，要么就是已经被废弃，或者是很少被使用，或者是根本没有实现，所有地址家族中，AF_INET是使用最广泛的一个，python支持很多种地址家族，但是由于我们只关心网络编程，所以大部分时候我么只使用AF_INET)
3. 同一机器上的两个服务之间的通信(基于文件)
   - **基于网络**的多台机器之间的多个服务通信

![socket](/Users/henry/Documents/截图/Py截图/socket.png)

4. **其实站在你的角度上看，socket就是一个模块**。我们通过调用模块中已经实现的方法建立两个进程之间的连接和通信。也有人将**socke**t说成**ip+port**，因为ip是用来标识互联网中的一台主机的位置，而port是用来标识这台机器上的一个应用程序。所以我们只要确立了ip和port就能找到一个应用程序，并且使用**socket**模块来与之通信。

## 8.3 Socket模块

![socket使用](/Users/henry/Documents/截图/Py截图/socket使用.jpg)

### 1. socket参数的详解

```python
import socket
socket.socket(family=AF_INET,type=SOCK_STREAM,proto=0,fileno=None)
# 创建socket对象的参数说明：
```

| 参数       | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| **family** | 地址系列应为**AF_INET**(默认值),AF_INET6,AF_UNIX,AF_CAN或AF_RDS。 （AF_UNIX 域实际上是使用本地 socket 文件来通信） |
| **type**   | 套接字类型应为**SOCK_STREAM**(默认值),SOCK_DGRAM,SOCK_RAW或其他SOCK_常量之一。 **SOCK_STREAM** 是基于**TCP**的，有保障的（即能保证数据正确传送到对方）面向连接的SOCKET，多用于资料传送。  **SOCK_DGRAM** 是基于UDP的，无保障的面向消息的socket，多用于在网络上发广播信息。 |
| **proto**  | 协议号通常为零,可以省略,或者在地址族为AF_CAN的情况下,协议应为CAN_RAW或CAN_BCM之一。 |
| **fileno** | 如果指定了**fileno**,则其他参数将被忽略,导致带有指定文件描述符的套接字返回。 与socket.fromfd()不同,fileno将返回相同的套接字,而不是重复的。 这可能有助于使用socket.close()关闭一个独立的插座。 |

### 2. TCP信息传输

```python
type = socket.SOCK_STREAM  # 表示tcp协议
# server 端
import socket 
sk = socket.socket()
sk.bind(('127.0.0.1'), port号)
sk.listen(n)               # 监听链接，n 表示允许多少个客户端等待，3.7之后无限制可省略
con,cli_addr = sk.accept() # 接受客户端链接，阻塞,服务端需要一直监听，不能关闭
con.recv(size)    				 # 接收字节数
con.send('content'.encode('utf-8')) 
# socket 发送接收都是字节流，即二进制
con.close()           		 #关闭客户端套接字
sk.close()								 #关闭服务器套接字(可选)

# client 端
import socket
sk = socket.socket()
sk.connet(('ip', port号))
sk.send('content'.encode('utf-8'))
sk.recv(size)
sk.close()
```

```python
# ip和端口占用解决方法，针对macos
import socket
from socket import SOL_SOCKET,SO_REUSEADDR # 加入一条socket配置，重用ip和端口
sk = socket.socket()
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 		# 就是它，在bind前加
sk.bind(('127.0.0.1',8898))  						 		# 把地址绑定到套接字
```

### 3. TCP黏包问题

#### 1. 黏包现象

- **提高效率**：为了减少tcp协议中的**确认收到**的网络延迟时间 
- **发送端**：由于两个数据的发送**时间间隔短**+**数据长度小**，tcp协议的优化机制将两条信息作为一条信息发送出去
- **接收端**：由于tcp协议中所传输的**数据无边界**，来不及接收的**多条数据**会在接收端**内核的缓存端黏在一起**
- **本质**：接收信息的边界不清晰，主要是接收方不知道消息之间的界限，不知道一次性提取多少字节的数据所造成的

#### 2. 成因机制

1. **tcp协议的拆包机制**
   - 当发送端缓冲区的长度大于网卡的MTU时，tcp会将这次发送的数据拆成几个数据包发送出去。 
   - MTU是Maximum Transmission Unit的缩写。意思是网络上传送的最大数据包。**MTU**的单位是**字节**。 **大部分网络设备的MTU都是1500**。
   - 如果**本机的MTU比网关的MTU大**，大的数据包就会被拆开来传送，这样会产生很多数据包碎片，增加丢包率，降低网络速度。
2. **面向流的通信特点和Nagle算法**
   - TCP（transport control protocol，**传输控制协议**）是面向连接的，面向流的，提供高可靠性服务。
   - 收发两端（客户端和服务器端）都要有**一一成对的socket**，因此，**发送端为了将多个发往接收端的包，更有效的发到对方，使用了优化方法（Nagle算法）**，将多次间隔较小且数据量小的数据，合并成一个大的数据块，然后进行封包。这样，接收端，就难于分辨出来了，必须提供科学的拆包机制。 **即面向流的通信是无消息保护边界的。**
   - **对于空消息**：**tcp**是基于数据流的，于是收发的**消息不能为空**，这就需要在客户端和服务端都添加空消息的处理机制，防止程序卡住，而**udp**是基于数据报的，即便是你输入的是**空内容(直接回车)，也可以被发送**，udp协议会帮你封装上消息头发送过去。 
   - **可靠黏包的tcp协议**：tcp的协议数据不会丢，没有收完包，下次接收，会继续上次继续接收，己端总是在收到ack时才会清除缓冲区内容。**数据是可靠的，但是会粘包**。

#### 3. Tcp黏包现象

- **自定义协议**：首先发送报头(**4**bytes) ，针对发送数据大小进行提前声明，内容是即将发送**报文字节长度**
  - struct：把所有数字都固定的转换为4bytes
  - 再发送数据信息

```python
# 自定义协议，解决黏包问题
# server端
import struct
import socket
sk = socket.socket()
sk.bind(('ip', port))
sk.listen()
con, cli_addr = sk.accept()
size = con.recv(4)
size = struct.unpack(size)[0]							# unpack,为一tuple类型
content = con.recv(size).decode('utf-8')	# 接收文件内容
con.close()
sk.close()

# client端
import struct
import socket
sk = socket.socket()
sk.connect(('ip', port))
content  = '我是henry'.encode('utf-8')     # 字节流
size = struct.pack('i', len(content))			# 发送内容长度进行struct
sk.send(size)
sk.send(content)
sk.close()
```

### 4. UDP信息传输

```python
# server
import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))

msg, client_addr = sk.recvfrom(1024)
print(msg)
sk.sendto(b'received', client_addr)
sk.close()

# client
import socket
sk = socket.socket(type = socket.SOCK_DGRAM)

sk.sendto(b'hello', ('127.0.0.1', 9000))
ret = sk.recv(1024)
print(ret)
sk.close()
```

#### Note3(2)

1. socket收发的**必须是bytes**类型，经过编码的文件均是bytes类型
2. 网络传输数据一般使用**json**格式

#### 1. UDP不会发生黏包(6)

1. **UDP（user datagram protocol，用户数据报协议）**是无连接的，面向消息的，提供高效率服务。 
2. **不会使用块的合并优化算法**，由于UDP支持的是一对多的模式，所以接收端的skbuff(套接字缓冲区）采用了**链式结构来记录每一个到达的UDP包**，在每个UDP包中就有了消息头（消息来**源地址**，**端口**等信息），这样，对于接收端来说，就容易进行区分处理了。 即**面向消息的通信是有消息保护边界的**。 
3. **对于空消息**：tcp是基于数据流的，于是收发的消息不能为空，这就需要在**客户端**和**服务端**都添加**空消息的处理机制**，防止程序卡住，而udp是基于数据报的，即便是你输入的是空内容（直接回车），也可以被发送，udp协议会帮你封装上消息头发送过去。 
4. **不可靠不黏包的udp**协议：udp的**recvfrom**是**阻塞**的，一个recvfrom(x)必须对唯一一个sendto(y),收完了x个字节的数据就算完成,若是y;x数据就丢失，这意味着udp根本不会粘包，但是会丢数据，不可靠。
5. 用**UDP协议发送**时，用sendto函数最大能发送数据的长度为：**65535- IP头(20) – UDP头(8)＝65507字节**。用sendto函数发送数据时，如果发送数据长度**大于该值，则函数会返回错误**。（丢弃这个包，不进行发送） 
6. 用**TCP协议发送**时**，由于TCP是数据流协议，因此不存在包大小的限制（暂不考虑缓冲区的大小），这是指在用send函数时，**数据长度**参数**不受限制。而实际上，所指定的这段数据并不一定会一次性发送出去，如果这段数据比**较长**，会被**分段发送**，如果比**较短**，可能会等待和下一次数据**一起发送**。

### 5.  socket其他操作

```python
import socket
# 服务端套接字函数
s.bind()    # 绑定(主机,端口号)到套接字
s.listen()  # 开始TCP监听
s.accept()  # 被动接受TCP客户的连接,(阻塞式)等待连接的到来

# 客户端套接字函数
s.connect()     # 主动初始化TCP服务器连接
s.connect_ex()  # connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

# 公共用途的套接字函数
s.recv()            # 接收TCP数据
s.send()            # 发送TCP数据
s.sendall()         # 发送TCP数据

s.recvfrom()        # 接收UDP数据
s.sendto()          # 发送UDP数据

s.getpeername()     # 连接到当前套接字的远端的地址
s.getsockname()     # 当前套接字的地址
s.getsockopt()      # 返回指定套接字的参数
s.setsockopt()      # 设置指定套接字的参数
s.close()           # 关闭套接字

# 面向锁的套接字方法
s.setblocking()     # 设置套接字的阻塞与非阻塞模式
s.settimeout()      # 设置阻塞套接字操作的超时时间
s.gettimeout()      # 得到阻塞套接字操作的超时时间

# 面向文件的套接字的函数
s.fileno()          # 套接字的文件描述符
s.makefile()        # 创建一个与该套接字相关的文件
```

```python
# 官方文档对socket模块下的socket.send()和socket.sendall()解释如下：
socket.send(string[, flags])
Send data to the socket. The socket must be connected to a remote socket. The optional flags argument has the same meaning as for recv() above. Returns the number of bytes sent. Applications are responsible for checking that all data has been sent; if only some of the data was transmitted, the application needs to attempt delivery of the remaining data.
# send()的返回值是发送的字节数量，这个数量值可能小于要发送的string的字节数，也就是说可能无法发送string中所有的数据。如果有错误则会抛出异常。

socket.sendall(string[, flags])
Send data to the socket. The socket must be connected to a remote socket. The optional flags argument has the same meaning as for recv() above. Unlike send(), this method continues to send data from string until either all data has been sent or an error occurs. None is returned on success. On error, an exception is raised, and there is no way to determine how much data, if any, was successfully sent.
# 尝试发送string的所有数据，成功则返回None，失败则抛出异常。

# 故，下面两段代码是等价的：
sock.sendall('Hello world\n')

buffer = 'Hello world\n'
while buffer:
    bytes = sock.send(buffer)
    buffer = buffer[bytes:]        # ？？？？
```

## 8.4 非阻塞模型

- 阻塞io模型，非阻塞io模型，事件驱动io，io多路复用，异步io模型**五种**

### 1. 非阻塞io模型模型

- 利用**tcp**可以实现**并发**
- server端使用setblocking(False)方法进行设置，此时需要使用异常处理
- **客户端下线**时，在**非阻塞**情况下，**msg为空**

```python
# server端
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.setblocking(False)               # 设置为非阻塞状态
sk.listen()

user = []
del_user = []
while True:
    try:
        con, addr = sk.accept()
        user.append(con)
    except BlockingIOError:
        for i in user:
            try:
                content = i.recv(1024).decode('utf-8')
                if not content:
                    del_user.append(i)
                    continue
                i.send(content.upper(). encode('utf-8')) 
                # 发送的bytes类型可以直接解释出(ascii字符)
            except BlockingIOError:pass     # 注意异常，会报错
        for i in del_user:
            user.remove(i)
        del_user.clear()
sk.close()
```

```python
# clinet端
import time
import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
while True:
    sk.send(b'hello')
    msg = sk.recv(1024)
    print(msg)
    time.sleep(0.2)
sk.close()
```

#### Note4(3)

1. socket的非阻塞io模型 + io多路复用实现(**框架实现方式**)
2. 非阻塞提高了cpu利用率，但cpu有效率很低
3. TCP**断开连接**后，只要有数据发送就会**报错**

### 2. 验证客户端的合法性

- 验证客户端的合法性(自动化开发)

```python
# 客户端使用对象是用户，直接登陆验证
	# 可以看到源码,在服务端进行验证登陆
# 客户端使用对象是机器
```

1. **摘要算法：hmac算法**

```python
import hmac
secret_key = b'asdfgh'
random_seq = os.urandom(32)
hmac.new(secret_key, random_seq)
ret = hmac.digest()   # 结果是bytes类型数据
```

2. **使用hmac验证客户端的合法性**

```python
# 使用TCP协议发送数据为空时，默认不会发送
# server端
import os
import hmac
import socket

def chat(con):
    while True:
        msg = con.recv(1024).decode('utf-8')
        print('------>', msg)
        con.send(msg.upper().encode('utf-8'))
        # con.send(''.encode('utf-8'))         # tcp不会发送
        
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

com_key = b'henry'
while True:
    con, addr = sk.accept()
    sec_key = os.urandom(32)
    con.send(sec_key)                 # 第一次发送
    val = hmac.new(com_key, sec_key).digest()
    data = con.recv(32)               # 第一次接收
    if data == val:
        print('客户端合法')
        chat(con)
    else:
        print('客户端不合法')
        con.close()
sk.close()
```

```python
# client 端
import socket
import hmac

def chat(sk):
    while True:
        sk.send('hello'.encode('utf-8'))
        msg = sk.recv(1024).decode('utf-8')
        print('------>', [msg])

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
sec_key = sk.recv(32)      # 第一次接收
com_key = b'henry'
val = hmac.new(com_key, sec_key).digest()
sk.send(val)               # 第一次发送
chat(sk)

sk.close()
```

```python
# 进阶示例
from socket import *
import hmac,os

secret_key=b'henry bang bang bang'
def conn_auth(conn):
    ''' 认证客户端链接'''
    print('开始验证新链接的合法性')
    msg=os.urandom(32)
    conn.sendall(msg)
    h=hmac.new(secret_key,msg)
    digest=h.digest()
    respone=conn.recv(len(digest))
    return hmac.compare_digest(respone,digest)

def data_handler(conn,bufsize=1024):
    if not conn_auth(conn):
        print('该链接不合法,关闭')
        conn.close()
        return
    print('链接合法,开始通信')
    while True:
        data=conn.recv(bufsize)
        if not data:break
        conn.sendall(data.upper())

def server_handler(ip_port,bufsize,backlog=5):
    '''只处理链接'''
    tcp_socket_server=socket(AF_INET,SOCK_STREAM)
    tcp_socket_server.bind(ip_port)
    tcp_socket_server.listen(backlog)
    while True:
        conn,addr=tcp_socket_server.accept()
        print('新连接[%s:%s]' %(addr[0],addr[1]))
        data_handler(conn,bufsize)

if __name__ == '__main__':
    ip_port=('127.0.0.1',9999)
    bufsize=1024
    server_handler(ip_port,bufsize)
```

```python
# 客户端
__author__ = 'Linhaifeng'
from socket import *
import hmac,os

secret_key=b'linhaifeng bang bang bang'
def conn_auth(conn):
    '''验证客户端到服务器的链接'''
    msg=conn.recv(32)
    h=hmac.new(secret_key,msg)
    digest=h.digest()
    conn.sendall(digest)

def client_handler(ip_port,bufsize=1024):
    tcp_socket_client=socket(AF_INET,SOCK_STREAM)
    tcp_socket_client.connect(ip_port)
    conn_auth(tcp_socket_client)
    while True:
        data=input('>>: ').strip()
        if not data:continue					# tcp协议不支持发送数据为空
        if data.lower() == 'q':break

        tcp_socket_client.sendall(data.encode('utf-8'))
        respone=tcp_socket_client.recv(bufsize)
        print(respone.decode('utf-8'))
    tcp_socket_client.close()

if __name__ == '__main__':
    ip_port=('127.0.0.1',9999)
    bufsize=1024
    client_handler(ip_port,bufsize)
```

## 8.5 socketserver模块

### 1. socketserver模块

```python
# server端
import socketserver       # socket是socketserver的底层模块和time，datetime一样
class Myserver(socketserver.BaseRequestHandler):
  def handle(self):				# 自动触发handle方法，self.request == con
    print(self.request)   # con
server = socketsever.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)
server.server_forever()

# client 
import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
```

### 2. socketserver模块进阶

```python 
# 进阶示例
import socketserver
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        # self.client_address
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9999
    # 设置allow_reuse_address允许服务器重用地址
    socketserver.TCPServer.allow_reuse_address = True
    # 创建一个server, 将服务地址绑定到127.0.0.1:9999
    server = socketserver.TCPServer((HOST, PORT),Myserver)
    # 让server永远运行下去，除非强制停止程序
    server.serve_forever()
   
# client端
import socket
HOST, PORT = "127.0.0.1", 9999
data = "hello"
# 创建一个socket链接，SOCK_STREAM代表使用TCP协议
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))                # 链接到客户端
    sock.sendall(bytes(data + "\n", "utf-8")) # 向服务端发送数据
    received = str(sock.recv(1024), "utf-8")  # 从服务端接收数据

print("Sent:     {}".format(data))
print("Received: {}".format(received))
```



# 第九章 并发编程

## 9.1 操作系统基础

- 操作系统发展史
- 并发和并行
- 阻塞和非阻塞
- 同步和异步
- 进程：三状态图，唯一标示，开始和结束
- 线程

### 1. 操作系统发展史

#### 1.1 人机矛盾(cpu利用率低)

—>磁带存储+批处理(降低数据的读取时间,提高cpu的利用率)

—>**多道操作系统**：数据隔离、时空复用(能够遇到**I/O**操作的时候主动把cpu让出来，给其他任务使用，切换需要时间，由OS完成)

—> 短作业优先算法、先来先服务算法

—>**分时OS**：时间分片，CPU轮转，每一个程序分配一个时间片，**降低了cpu利用率**，**提高了用户体验**

—>**分时**OS + **多道**OS：多个程序一起执行，遇到IO切换，时间片到了也要切换

- **多道技术介绍**

1. 产生背景：针对单核，实现并发
2. 现在的主机一般是多核，那么每个核都会利用多道技术有4个cpu，运行于cpu1的某个程序遇到io阻塞，会等到io结束再重新调度，会被调度到4个 cpu中的任意一个，具体由操作系统调度算法决定。
3. 空间上的复用：如内存中同时有多道程序
4. 时间上的复用：复用一个cpu的时间片

**Note**：遇到io切，占用cpu时间过长也切，**核心**在于切之前将进程的状态保存下来，这样
才能保证下次切换回来时，能基于上次切走的位置继续运行。  

#### 2.2 操作系统**分类**(4)

**OS作用**：将应用程序对硬件资源的**竞态请求**变得有序化

- **实时OS**：实时控制，实时信息处理
- **通用OS**：多道、分时、实时处理或其两种以上
- **网络OS**：自带网络相关服务
- **分布式OS**：python中可使用：**celery**模块

### 2. 进程

#### 2.1 进程：运行中的程序

- 程序只是一个文件，进程是程序文件被cpu运行
- 进程是计算机中最小的**资源分配**单位
- 在OS中有唯一标示符**PID**

#### 2.2 OS调度算法(4)

- 短作业优先
- 先来先服务
- 时间片轮转
- **多级反馈算法**：分时+先来先服务+短作业优先

#### 2.3 并行与并发

1. **并发**（concurrency）：把任务在**不同的时间点**交给处理器进行处理。看起来程序同时执行，实际在同一时间点，任务并不会同时运行。
2. **并行**（parallelism）：把每一个任务分配给每一个处理器独立完成。在同一时间点，任务一定是同时运行。
3. **并发的本质**：切换+保存状态

### 3. 同步异步阻塞非阻塞

1. **同步**：调用一个函数/方法，需要**等待**这个函数/方法**结束**
   - **一个功能调用时，没有得到结果之前，就不会返回，可以说是一种操作方式。**
2. **异步**：程序同时运行，没有**依赖**和**等待**关系，调用一个方法，**不等待**这个方法**结束**，不关心这个方法做了什么
3. **阻塞**：cpu不工作
   - **阻塞调用**是指调用结果返回之前，**当前线程**会被挂起。函数只有在得到结果之后才会返回。
4. **非阻塞**：cpu工作
   - 指调用在不能立刻得到结果之前，该**调用不会阻塞当前线程**。
5. **同步阻塞**
   - con.recv()，socket阻塞的tcp协议
6. **同步非阻塞**
   - 没有io操作的func()
   - socket非阻塞tcp协议； 调用自定义函数(不存在io操作)
7. **异步非阻塞**（重点）
   - 没有io操作，把func扔到其他任务里各自执行，cpu一直工作
8. **异步阻塞**
   - 程序中出现io操作

#### Note1(2)

1. 同步和异步关注的是**消息通信机制** (synchronous communication/ asynchronous communication)
2. 阻塞和非阻塞关注的是**程序在等待调用结果（消息，返回值）时的状态**

### 4. 进程的三状态图

#### 1. 进程状态

**进程状态**：运行(runing)  就绪(ready)  阻塞(blocking)

![进程三状态图](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/%E8%BF%9B%E7%A8%8B%E4%B8%89%E7%8A%B6%E6%80%81%E5%9B%BE.png)

#### 2. 进程的创建与结束

- **进程创建**

1. 系统初始化(**ps**)
2. 一个进程开启了一个子进程(os.fork，subprocess.Popen)
3. 用户交互式请求(用户双击app)
4. 批处理作业的初始化(只在大型机的批处理系统中应用)

- **进程结束**

1. 正常退出
2. 出错退出
3. 严重错误
4. 被其他进程杀死(**kill -9 pid**)



## 9.2 进程

### 1. 进程与线程

#### 1.1 分别做多件事

- 如果是两个程序分别做两件事
  - 起两个进程
- 如果是一个程序，要分别做两件事
  - 起线程，视频软件：下载电影1，电影2，电影3

#### 1.2 进程解析

1. **进程**（**Process**）是计算机中的程序关于**某数据集合上**的一次运行活动，是系统进行**资源分配和调度**的**基本单位**，是OS结构的基础。

     

2. 在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；在当代**面向线程设计**的计算机结构中，**进程是线程的容器**。程序是指令、数据及其组织形式的描述，**进程是程序的实体。**

3. 顾名思义，进程即正在执行的一个过程。**进程**是对正在运行程序的一个抽象。

4. 进程的概念起源于操作系统，是操作系统最核心的概念，也是操作系统提供的最古老也是最重要的**抽象概念**之一。操作系统的其他所有内容都是围绕进程的概念展开的。

   **PS**：即使可以利用的cpu只有一个（早期的计算机确实如此），也能保证支持（伪）并发的能力。将一个单独的cpu变成多个虚拟的cpu（多道技术：时间多路复用和空间多路复用+硬件上支持隔离），没有进程的抽象，现代计算机将不复存在。

5. **进程概念**

   - 进程是一个程序实体。每**一个进程**都有它自己的**地址空间**，一般情况下，包括**文本区域**（text region）、**数据区域**（data region）和**堆栈**（stack region）。文本区域存储处理器执行的代码；数据区域存储变量和进程执行期间使用的**动态分配**的内存；堆栈区域存储着活动过程调用的**指令和本地变量**。
   - 进程是一个“执行中的程序”。程序是一个没有生命的实体，只有处理器赋予程序生命时（操作系统执行之），它才能成为一个活动的实体，我们称其为进程。
   - 进程是操作系统中最基本、重要的概念。是多道程序系统出现后，为了刻画系统内部出现的动态情况，描述系统内部各道程序的活动规律引进的一个概念,所有**多道程序设计操作系统**都建立在**进程**的基础上。

6. **特点**

   - 是计算机中最小的**资源分配单位**，**数据隔离**。
   - 创建、销毁、切换进程时间**开销大**
   - 可以利用多核

#### 1.3 线程(5)

1. 线程是进程中的一部分，不能脱离进程存在
2. 任何进程中至少有一个线程，**只**负责执行代码，不负责存储共享的数据，也不负责资源分配
3. 创建、销毁和切换的开销**远远小于**进程
4. **线程**是计算机中能被**cpu调度的最小单位**
   - 爬虫使用需要配合前端
5. 一个进程中的多个线程可以共享这个进程的数据——  **数据共享**

#### 1.4 开销

1. 线程的创建和销毁
   - 需要一些开销(一个**存储局部变量**的数据结构，**记录状态**)
   - 创建、销毁、切换**开销**远**远小于**进程
2. python中的线程比较特殊，所以进程也有可能被用到
3. **进程**：数据隔离、开销大、数据不安全、可以利用多核、os切换
4. **线程**：数据共享、开销小 、数据不安全、不可以利用多核、os切换

### 2. 进程的创建

- 仔细说来，**multiprocess**不是一个模块而是python中一个操作、管理进程的包。 之所以叫multi是取自multiple的多功能的意思,在这个包中几乎包含了和进程有关的所有子模块。由于提供的子模块非常多，为了方便大家归类记忆，我将这部分大致分为四个部分：**创建进程**部分，**进程同步**部分，**进程池**部分，进程之间**数据共享**。

#### 2.1 multiprocessing

- 基于process模块

```python
# 获取进程的pid, 父进程的id及ppid
import os
import time
print('start')
time.sleep(20)
print(os.getpid(),os.getppid(),'end')
```

#### 2.2 子进程和父进程

1. pycharm中启动的所有py程序都是pycharm的子进程

```python
# 把func函数交给子进程执行
import os
import time
from multiprocessing import Process

def func():
  print('start', os.getpid())
  time.sleep(1)
  print('end', os.getpid())

if __name__ == '__main__':	  
  p = Process(target=func)				      # 创建一个即将要执行的进程对象
  p.start()	                            # 开启一个进程，异步非阻塞
  p.join()												      # 同步阻塞，直到子进程执行完毕
  print('main', os.getpid())		      	# 异步的程序，调用开启进程的方法，并不等待这个进程的开启
```

2. **创建子进程注意**

ps：_\_name__ 只有两种情况，**文件名**或**双下划线**main字符串

```python
# windows
通过（模块导入）执行父进程文件中的代码获取父进程中的变量
只要是不希望被子进程执行的代码，就写在if __name__ == '__mian__'下
进入导入时，父进程文件中的 __name__ != '__mian__'
# linux/macos
创建新的子进程是copy父进程内存空间，完成数据导入工作（fork）,正常写就可以

公司开发环境都是linux，无需考虑win中的缺陷
# windows中相当于把主进程中的文件又从头执行了一遍

# linux，macos不执行代码，直接执行调用的函数在Windows操作系统中由于没有fork(linux操作系统中创建进程的机制)，在创建子进程的时候会自动 import 启动它的这个文件，而在 import 的时候又执行了整个文件。因此如果将process() 直接写在文件中就会无限递归创建子进程报错。所以必须把创建子进程的部分使用if __name__ ==‘__main__’ 判断保护起来，import 的时候  ，就不会递归运行了。
```

- 父进程(主进程)存活周期

![父子进程](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/%E7%88%B6%E5%AD%90%E8%BF%9B%E7%A8%8B.png)

#### Note2(5)

1. 进程之间不能共享内存
2. 主进程需要等待子进程结束，主进程负责**创建**和**回收**子进程
3. 子进程执行结束，若父进程没有回收资源，即**僵尸**进程。
4. 主进程结束逻辑：主进程**代码结束**、所有子进程结束、回收子进程资源、主**进程结束**
5. **进程里面无法进行input**
   - 所有print都是向文件里**写**数据
   - 只有主进程支持input操作，子进程不支持，会报错**EOFError: EOF when reading a line**

#### 2.3 join方法

- 把一个进程的结束事件封装成一个join方法
- 执行join方法效果，**阻塞**，直到子进程结束，就结束
- 所有的进程执行的先后是由**OS控制的**

```python
# 在多个子进程中使用join方法
from multiprocessing import Process
def send_mail(i):
    print('邮件已发送', i)
if __name__ == '__main__':
    li = []
    for i in range(10):
        p = Process(target=send_mail, args=(i,))  # args必须是元组，给子进程中的函数传参数
        p.start()
    li.append(p)
    for p in li: p.join()													# 阻塞，知道所有子进程执行完毕
    print('100封邮件已发送')
# 主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程 
```



## 9.3 锁&进程间通信

### 1. Process类

#### 1.1 守护进程

- 生产者消费者模型
- 和守护线程做对比

 **p.daemon**：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，**p不能创建自己的新进程**，必须在p.start()之前设置

```python
import time
from multiprocessing import Process

def son1():
  	while True:
        print('is alive')
        time.sleep(0.5)
    
def son2():
  	for i in range(5):
      print('in son2')
      time.sleep(1)
              
if __name__ == '__main__':
    p = Process(target=son1)
    p.daemon = True                               # 把p子进程设置成了守护进程	 
    p.start()
    p2 = Process(target=son2)
    p2.start()
    time.sleep(2)
# 守护进程是随着主进程‘代码’结束而结束
# 所有子进程都必须在主进程结束之前结束
# 守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
```

#### 1.2 Process的方法

- p.**terminate**(), p.i**s_alive**()，current_process(current_process.ident/ **name**/ pid)
- **异步非阻塞**
  - 使用terminate方法后，再查看进程是否还存活时，会发现进程还存活，并没有等待OS关闭进程，说明terminate方法请求后，程序会继续执行

```python
import time
from multiprocessing import Process

def son1():
  	while True:
        print('is alive')
        time.sleep(0.5)
              
if __name__ == '__main__':
    p = Process(target=son1)
    p.start()                   # 开启了一个进程
  	print(p.is_alive)           # 判断子进程时候存活, Ture和False
    time.sleep(1)
    p.terminate()               # “异步非阻塞”，强制结束一个子进程
    print(p.is_alive)           # True，os还没来得及关闭进程
   	time.sleep(0.01)
    print(p.is_alive)           # False，OS已经响应了关闭进程的需求，再去检测的时候，结果是进程已经结束
```

#### 1.3 面向对象开启进程

- 当创建子进程需要传参时，需要使用**super()._\_init__()**

```python 
import os
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, x, y):                 # 子进程如果不需要参数，可以省略
        self.x = x
        self.y = y
        super().__init__()        
        
    def run(self):
        while True:
            print(self.x, self.y, os.getpid())
            print('in myprocess')

if __name__ == '__main__':
    mp = MyProcess(1, 2)
    mp.daemon = True
    mp.start()                                # 开启一个子进程，会调用run()方法
    time.sleep(1)
    mp.terminate()						              	# 结束进程，异步非阻塞						
    print(mp.is_alive())				              # True
    time.sleep(0.01)				
    print(mp.is_alive())				              # False
```

- p.join() : 同步阻塞
- p.terminate() 和 p.start()：异步非阻
- p.is_alive()：获取当前进程状态
- **daemon = True**：设置为守护进程，守护进程在主进程代码执行结束而结束

### 2. 锁

1. 在并发的场景下，设计某部分的内容
   - 需要修改一些所有进程共享数据资源
   - 需要加锁来维护数据的安全
2. 在数据安全的基础上，才考虑效率问题
   - with lock：内部**有异常处理**
   - 在主进程中进行实例化
   - 把锁传递给子进程
3. 在子进程中对需要加锁的代码进行with lock
   - with lock：相当于lock.acquire()和lock.release()
4. 需要加锁的场景
   - 操作共享的数据资源
   - 对资源进行修改操作
   - 加锁之后能够保证数据的安全性，但会降低程序执行效率

```python 
# 数据操作时，不能同时进行修改
import json
from multiprocessing import Process, Lock             # 导入Lock

def search_ticket(user):
    with open('tickets.txt') as f:
        dic = json.load(f)
        print('%s查询结果：%s张余票' %(user, dic['count']))

def buy_ticket(user, lock):
    # with lock:
    lock.acquire()
    # time.sleep(0.01)
    with open('tickets.txt') as f:
        dic = json.load(f)
    if dic["count"] > 0:
        print('%s已买到票' % user)
        dic["count"] -= 1
    else:
        print('%s没买到票' % user)
    with open('tickets.txt', 'w') as f:
        json.dump(dic, f)
    lock.release()


if __name__ == '__main__':
    lock = Lock()                                      # 实例化一个对象
    for i in range(10):
      	search_ticket('user%s '%(i+1),)
        p = Process(target=buy_ticket, args=('user%s '%(i+1), lock))
        p.start()
```

### 3. 进程间的通信

#### 3.1 进程间数据隔离

```python
from multiprocessing import Process
n = 100
def func():
	global n
  n -= 1
 
li = []
for i in range(10):
  p = Process(target=func)
  p.start()
  li.append(p)
  
 for p in li:p.join()
 print(n)

```

#### 3.2 进程间通信

- 文件或网络只有这两种
- 进程间通信(**IPC**， inter-process communication):**Queue和Pipe**
- **Queue(3)**：先进先出，文件家族的**socket**，写文件基于**pickle**，基于**Lock**
  - 数据安全，**Pipe**管道：天生数据不安全（socket通信）
  - Queue = **Pipe**(socket + picket)**+Lock**
- **第三方提供(5)**：redis，memcache，kafka，rabbitmq（消息中间件(消息转发)）
  - 并发需求
  - 高可用
  - 实现集群的概念
  - 断电保存数据
  - 解耦

```python
from multiprocessing import Process,Queue

def func(exp,q):
    res = eval(exp)
    q.put(res)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=func, args=('1+2+3',q))
    p.start()
    print(q.get())

```

```python
from multiprocessing import Pipe
pip = Pipe()
pip.send()
pip.recv()

```

```python
# Process中的队列
import queue
from multiprocessing import Queue
q = Queue(3)													# 可设置队列长度
q.put(1)
q.put(2)															# 对列为满时，继续放数据会发生阻塞
q.put(3)
print('----------')
try:
	q.put_nowait(4)                     # 对列为满时，继续放数据会报错和丢失
except queue.Full:pass
print('----------')

q.get()
q.get()
q.get()                                # 对列为空时，会发生阻塞
try:
	q.get_nowait()											 # 对列为空时，会报错，阻塞会取消
except queue.Empty:pass

```

```python
q.empty()                              # 有缺陷
q.qsize()
q.full()

```



## 9.4 cp模型&线程

### 1. 生产者消费者模型

#### 1.1 程序的解耦

- 把写在一起的功能分开成多个小的功能处理
  - 修改和复用，增加可读性
  - 计算速度有差异，执行效率最大化，节省进程
- **生产者**：生产数据
- **消费者**：处理数据

![生产者消费者模型](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/%E7%94%9F%E4%BA%A7%E8%80%85%E6%B6%88%E8%B4%B9%E8%80%85%E6%A8%A1%E5%9E%8B.jpg)

#### 1.2 生产者和消费者

1. 一个进程就是一个生产者/消费者
2. 生产者和消费者之间的容器就是队列(**队列有大小，控制内存消耗**)

```python
# 生产者消费者模型示例
import time
import random
from multiprocessing import Process, Queue

def producer(q, name, food):
    for i in range(10):
        time.sleep(random.random())
        fd = '%s%s' % (food, i)
        q.put(fd)
        print('%s生产了一个%s' % (name, food))

def consumer(q, name):
    while True:
        food = q.get()
        if not food:
            q.put(None)
            break
        time.sleep(random.randint(1, 3))
        print('%s吃了%s' % (name, food))

def cp(num1, num2):
    q = Queue(10)
    p_l = []
    for i in range(num1):
        p = Process(target=producer, args=(q, 'henry', 'food'))
        p.start()
        p_l.append(p)
    for i in range(num2):
        c = Process(target=consumer, args=(q, 'echo%s' % (i+1,)))
        c.start()
    for i in p_l:
        i.join()
    q.put(None)

if __name__ == '__main__':
    cp(1, 4)

```

```python
# 生产者消费者模型示例之爬虫
import re
import requests
from multiprocessing import Process, Queue

def producer(q, url):
    response = requests.get(url)
    q.put(response.text)

def consumer(q):
    while True:
        s = q.get()
        if not s:
            q.put(None)
            break
        com = re.compile(
            '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
            '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)
        ret = com.finditer(s)
        for i in ret:
            print({
                "id": i.group("id"),
                "title": i.group("title"),
                "rating_num": i.group("rating_num"),
                "comment_num": i.group("comment_num"),
            })

if __name__ == '__main__':
    count = 0
    q = Queue()
    p_l = []
    for i in range(10):
        count += 25
        p = Process(target=producer, args=(q, 'https://movie.douban.com/top250?start=%s&filter=' % count))
        p.start()
        p_l.append(p)
    for i in range(5):
        c = Process(target=consumer, args=(q,))
        c.start()
    for i in p_l:
        i.join()
    q.put(None)

```

#### 1.3 joinablequeue

1. **q.join()**：阻塞，直到队列中所有内容被取走且**q.task_done**
   - 生产者将使用此方法进行阻塞，直到队列中所有项目均被处理。阻塞将持续到为队列中的每个项目均调用
2. 先设置消费者为守护进程
   - **c.daemon = True**
3. 阻塞生产者
   - 其中的队列阻塞结束后，才会结束
4. 在生产者中使用阻塞队列
   - 阻塞一结束，所有数据都已经消费完
5. 队列阻塞结束代表消费者，把所有生产数据消费完（**jq.taks_done()操作**）
   - 使用者使用此方法发出信号，表示q.get()返回的项目已经被处理。如果调用此方法的次数大于从队列中删除的项目数量，将引发**ValueError**异常。

![joinable_queue](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/joinable_queue.png)

![joinable逻辑](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/joinable%E9%80%BB%E8%BE%91.png)

```python
# joinable实现生产者、消费者模型
import time
import random
from multiprocessing import Process,JoinableQueue

def producer(q, name, food):
  for i in range(10):
    time.sleep(random.random())
    fd = '%s%s'%(food,i)
    print('%s生产了一个%s'%(name, food))
  q.join()

def consumer(q, name, food):
  while True:
    food = q.get()
    if not food:
      q.put(None)
      break
    time.sleep(random.randint(1, 3))
    print('%s吃了%s'%(name, food))
    q.task_done()
 
if __name__ = '__main__':
  jq = JoinableQueue()
  p = Processor(target=producer, args=(jq, 'henry', 'food'))
  p.start()

```

### 2. 进程间数据共享

1. 与数据共享相关：**Manager模块**(Manager().list(), Manager().Queue)
2. multiprocessing 中有一个manager类
3. 封装了所有和进程相关的**数据共享**、**数据传递**
4. 但是对于dict、list这类进行数据操作时，会产生数据不安全
5. m = Manager()也可以使用**with Manager() as m**:

```python
# 进程间数据是独立的，可以借助于队列或管道实现通信，二者都是基于消息传递的
# 虽然进程间数据独立，但可以通过Manager实现数据共享，事实上Manager的功能远不止于此
A manager object returned by Manager() controls a server process which holds Python objects and allows other processes to manipulate them using proxies.

A manager returned by Manager() will support types list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array.

```

```python
from mutliprocessing import Manager,Lock
def func(dic, lock):
  with lock:
		dic['count'] -= 1

if __name__ = '__main__':
  # m = Manager()
  lock = Lock()
  with Manager() as m:
    l = Lock()
    dic = m.dict({'count': 100})    							# 共享的dict,list li = m.list([1,2,3])
    p_l = []
    for i in range(100):
      p = Process(target=func, args=(dic,lock))
      p.start()
      p_l.append(p)
    for p in p_l:p.join()
    print(dic)

```

### 3. 线程

1. **调度和切换**：线程**上下文切换**比进程上下文切换要快得多。
2. **四核八线程**
   - 每个核心被虚拟成两个核心，可以同时执行8个线程。
   - 如果是计算复杂数据，会转换到四核
   - https：加证书，需要购买
3. 在多线程的操作系统中，通常是在一个进程中包括多个线程，**每个线程**都是作为**利用CPU的基本单位**，是花费最小开销的实体。
4. **线程具有以下属性(4)**
   1. 线程中的实体基本上不拥有系统资源，只是**有一点必不可少的、能保证独立运行的资源**。
      - 独立调度和分派的基本单位。
      - 在多线程OS中，线程是能独立运行的基本单位，因而也是独立调度和分派的基本单位。由于线程很“轻”，故线程的切换非常迅速且开销小（在同一进程中的）。
   2. 线程的实体包括**程序**、**数据**和**TCB**。**线程是动态概念**，它的动态特性由线程控制块**TCB**（Thread Control Block）描述。
      - 线程状态。
      - 当线程不运行时，被保存的现场资源。
      - 一组执行堆栈。
      - 存放每个线程的**局部变量主存区**。
      - 访问同一个进程中的主存和其它资源。
      - 用于指示被执行指令序列的**程序计数器**、**保留局部变量**、**少数状态参数**和**返回地址**等的一组寄存器和堆栈。
   3. **共享进程资源**
      - 线程在同一进程中的各个线程，都可以共享该进程所拥有的资源，
      - 这首先表现在：**所有线程**都具有**相同的进程id**，这意味着，线程可以访问该进程的每一个内存资源；
      - 此外，还可以访问进程所拥有的**已打开文件**、**定时器**、**信号量机构**等。由于同一个进程内的线程共享内存和文件，所以线程之间互相通信不必调用内核。
   4. **可并发执行**
      - 在一个进程中的多个线程之间，可以并发执行，甚至允许在一个进程中所有线程都能并发执行；
      - 同样，不同进程中的线程也能并发执行，充分利用和发挥了处理机与外围设备并行工作的能力。

#### 3.1垃圾回收机制

1. **cpython**解释器不能实现多线程利用多核
2. 垃圾回收机制(gc)：**引用计数** + **分代回收**
   - 专门有一条线程完成垃圾回收机制，对每一个在程序中的变量**统计引用计数**

#### 3.2 GIL锁

**GIL**(global interpreter lock)：**全局解释器锁**

1. 保证了整个python程序中，只能有一个线程被CPU执行
   - 导致了py程序不能并行
   - 使用多线程并不影响高IO型操作，只会对高计算型程序有效率的影响
   - 遇到高计算：多进程+多线程，分布式
2. 原因：**cpython**解释器中特殊的垃圾回收机制
3. cpython、pypy，jpython(先翻译为java字节码，在java上执行)、iron python

#### 3.3 遇到IO操作的时候

1. 5-6亿条cpu指令
2. 5-6cpu指令 == 一句python代码
3. 几千万条python代码

#### 3.4 web框架几乎都是多线程

- 利用IO操作，类似多道系统

### 4. python操作线程(重点)

#### 4.1 开启线程

- 使用**Threading**类

```python
# multiprocessing 是完全仿照Threading类的
import os
import time
from threading imoprt Thread
def func():
  print('start son thread')
  time.sleep(1)
  print('end son thread', os.getpid())
  
Thread(target=func).start()                 # 开启一个线程的速度非常快
print('start')
time.sleep(0.5)
print('end', os.getpid())

```

```python
# 开启多个线程
import os
import time
from threading imoprt Thread
def func():
  print('start son thread')
  time.sleep(1)
  print('end son thread', os.getpid())
 
for i in range(10):
  Thread(target=func).start()                 # 开启一个线程的速度非常快
  																					  # 线程的调度由OS决定

```

#### 4.2 join方法

1. join阻塞知道子线程执行结束

- **主线程**如果结束了，**主进程**也就结束了
- **主线程**需要等待**所有子线程结束**才能结束

```python
import os
import time
from threading imoprt Thread
def func():
    print('start son thread')
    time.sleep(1)
    print('end son thread', os.getpid())

t_l = []
for i in range(10):
    t = Thread(target=func)
    t.start()
    t_l.append(t)
for i in t_l:i.join()
print('子线程执行结束')

```

#### 4.3 面向对象启动线程

- self.ident / current_thread：查看线程id
- enumerate / active_count：查看线程存活情况

```python
from threading import Thread

class MyThread(Thread):
    def __init__(self, i):
        self.i = i
        super().__init__()                   # 注意变量名避免与父类init中的变量重名  

    def run(self):
        print(self.i, self.ident)            # 通过self.ident，查看子线程的id

t_l = []
for i in range(100):
    t = MyThread(i)
    t_l.append(t)
    t.start()                                 # start 方法封装了开启线程的方法和run方法

for t in t_l: t.join()
print('主进程结束')       

```

#### 4.4 线程中的其他方法(3大类)

```python
from threading import current_thread, enumerate, active_count

def func():
    print('start son thread', i , current_thread())
    time.sleep(1)
    print('end son thread', os.getpid())

t = Thread(target=func)
t.start()
print(t.ident)
print(current_thread().ident)                 # current_ident()在哪个线程，就得到这个线程id
print(enumerate())					                  # 统计当前进程中多少线程活着，包含主线程
print(active_count())				                  # 统计当前进程中多少线程活着，个数，包含主线程
                                              # 线程中不能从主线程结束一个子线程
  
  
current_thread().name     									  # 当前线程名称
current_thread().ident												# 当前线程id
current_thread().isalive()										# 当前线程是否存活
current_thread().isdaemon()										# 当前线程是否是守护线程

```

#### 4.5 效率差

```python
import time
from threading import Thread
from multiprocessing import Process
def func(a, b):
  	c = a + b
 
if __name__ == '__main__':
    p_l = []
    start = time.time()
    for i in range(100):
        p = Process(target=func, args=(i, i*2))
        p.start()
        p_l.append(p)
     for i in P_l:i.join()
     print(time.time() - start)
    
     t_l = []
     start = time.time()
     for i in range(100):
         t = Thread(target=func, args=(i, i*2))
         t.start()
         t_l.append(t)
     for i in t_l:i.join()
     print(time.time() - start)

```

#### 4.6 数据共享

```python
# 不要在子线程里随便修改全局变量
from threading import Thread
n = 100
def son():
  global n
  n -= 1

t_l = []
for i in range(100):
		t = Thread(target=son)
    t_l.append(t)
    t.start()
    
for t in t_l:t.join()
print(n)

```

#### 4.7 守护线程

- 守护线程会一直等到所有非守护线程结束之后才结束
- 除了**守护主线程**的代码之外，也会**守护子线程**
- 只要有非守护线程存在，主进程就不会结束

```python
import time
from threading imoprt Thread
def son():
  	while True:
      		time.sleep(0.5)

def son2():
  	for i in range(5):
      
t = Thread(target=son)
t.daemon = True
t.start()
time.sleep(3)

```

#### Note3(2)

1. 对**主进程**来说，运行完毕指的是主进程**代码运行完毕**
   - 主进程在其代码结束后就已经运行完毕了（守护进程在此时就被回收），然后主进程会一直等非守护进程都运行完毕后回收子进程资源（否则会产生僵尸进程），才会结束。
2. 对**主线程**来说，运行完毕指的是主线程所在的进程内所有**非守护线程执行完毕**
   - 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收），因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。

## 9.5 锁&池

### 1. 互斥锁

#### 1.1 互斥锁

```python
# 线程数据同样不安全
import dis
a = 0
def func():
  	global a
  	a += 1
dis.dis(func)                                   # 返回cpu指令

```

- 即便是线程，有GIL锁， 也会出现**数据不安全**的问题
- **STORE_GLOBAL**：一旦有这种方法，就会有数据安全问题
- **操作是全局变量**
- **操作以下方法**
  - += , -= , *=, /=（在操作线程全局变量时，注意）
  - li[0] += 1, dic['key'] -= 1
  - 对同一文件进行写操作

```python
# 使用互斥锁解决线程全局变量数据不安全问题
from threading import Thread, Lock
a = 0
def add_f(lock):
    global a
    with lock:
        for i in range(2000000):
            a += 1
def sub_f(lock):
    global a
    with lock:
        for i in range(2000000):
            a -= 1
lock = Lock()
t1 = Thread(target=add_f, args=(lock,))
t1.start()
t2 = Thread(target=sub_f, args=(lock,))
t2.start()
t1.join()
t2.join()
print(a)

```

**互斥锁**：是锁中的一种，在同一线程中，不能连续lock.acquire()多次

```python
from threading import Lock
lock = Lock()
lock.acquire()
print('-------------')
lock.acquite()
print('-------------')

```

#### 1.2 单例模式

```python 
import time
import random
from threading import Thread

class Singleton:
    from threading import Lock                          # 复用性考虑
    __instance = None
    lock = Lock()
    
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(random.random())             # 切换GIL锁
                cls.__instance = super().__new__(cls)
        return cls.__instance

def fun():
    print(Singleton())

li = []
for i in range(10):
    t = Thread(target=fun)
    li.append(t)
    t.start()
for t in li: t.join()

```

### 2. 死锁

#### 2.1 原因(2)

- 有**多把锁**(一把以上)
- 多把锁**交替使用**

```python
from threading import Thread,Lock
noodle_lock = Lock()
fork_lock = Lock()
def eat1(name,noddle_lock, fork_lock):
    noddle_lock.acquire()
    print('%s抢到面了'%name)
    fork_lock.acquire()
    print('%s抢到叉子了'%name)
    print('%s吃了一口面'%name)
    noddle_lock.release()
    print('%s放下面了'%name)
    fork_lock.release()
    print('%s放下叉子了'%name)
 
def eat2(name,noddle_lock, fork_lock):
    fork_lock.acquire()
    print('%s抢到叉子了'%name)
    noddle_lock.acquire()
    print('%s抢到面了'%name)
    print('%s吃了一口面'%name)
    noddle_lock.release()
    print('%s放下面了'%name)
    fork_lock.release()
    print('%s放下叉子了'%name)

```

#### 2.2 解决方案

1. **递归锁**
   - 递归锁在同一线程中，可以连续**acquire多次**不会阻塞
   - **本质**：一把锁
   - acquire和release次数要一致
   - **优点**：在同一线程中多次acquire也不会发生阻塞
   - **缺点**：**占用**了更多的**资源**
2. **多把递归锁**也会产生**死锁**现象
   - 使用递归锁，永远不要使用多把
   - 互斥锁效率更高，递归锁效率较低

```python
import time
from threading import RLock, Thread
noodle_lock = fork_lock = RLock()                      # 将多把互斥锁变成了一把递归锁

def eat1(name, noodle_lock, fork_lock):
    noodle_lock.acquire()
    print('%s抢到面了' % name)
    fork_lock.acquire()
    print('%s抢到叉子了' % name)
    print('%s吃了一口面' % name)
    time.sleep(0.1)
    fork_lock.release()
    print('%s放下叉子了' % name)
    noodle_lock.release()
    print('%s放下面了' % name)

def eat2(name, noodle_lock, fork_lock):
    fork_lock.acquire()
    print('%s抢到叉子了' % name)
    noodle_lock.acquire()
    print('%s抢到面了' % name)
    print('%s吃了一口面' % name)
    time.sleep(0.1)
    noodle_lock.release()
    print('%s放下面了' % name)
    fork_lock.release()
    print('%s放下叉子了' % name)

lst = ['henry', 'echo', 'dean', 'daniel']
Thread(target=eat1, args=(lst[0], noodle_lock, fork_lock)).start()
Thread(target=eat2, args=(lst[1], noodle_lock, fork_lock)).start()
Thread(target=eat1, args=(lst[2], noodle_lock, fork_lock)).start()
Thread(target=eat2, args=(lst[3], noodle_lock, fork_lock)).start()

```

3. **代码优化**

```python
# 使用互斥锁解决问题
import time
from threading import Lock, Thread

lock = Lock()
def eat1(name, lock):
    lock.acquire()
    print('%s抢到面了' % name)
    print('%s抢到叉子了' % name)
    print('%s吃了一口面' % name)
    time.sleep(0.1)
    print('%s放下叉子了' % name)
    print('%s放下面了' % name)
    lock.release()

def eat2(name, lock):
    lock.acquire()
    print('%s抢到叉子了' % name)
    print('%s抢到面了' % name)
    print('%s吃了一口面' % name)
    time.sleep(0.1)
    print('%s放下面了' % name)
    print('%s放下叉子了' % name)
    lock.release()

lst = ['henry', 'echo', 'dean', 'daniel]
Thread(target=eat1, args=(lst[0], lock)).start()
Thread(target=eat2, args=(lst[1], lock)).start()
Thread(target=eat1, args=(lst[2], lock)).start()
Thread(target=eat2, args=(lst[3], lock)).start()

```

### 3. 队列

- 线程之间的通信，线程安全

```python
import queue
# 先进先出队列：服务
from queue import Queue           
q = Queue(5)
q.put(1)
q.get()
# 后进先出队列：算法
from queue import LifoQueue
lfq = LifiQueue(4)
lfq.put(1)
lfq.put(2)
lfq.get()
lfq.get()
# 优先级队列：自动排序、vip用户、告警级别
from queue import PriorityQueue
pq = PriorityQueue()
pq.put((10, 'henry'))
pq.put((6, 'echo'))
pq.put((10, 'dean'))
pq.get()
pq.get()
pq.get()

```

- FIFO：所有的请求放在对列里，先来先服务思想
- LIFO：一般用于算法

### 4. 池

- 进程，线程开启关闭切换需要时间
- 进程池一般和cpu核心说有关，个数一般为cpu核心数或加一
- 节省了进程创建和销毁的时间

#### 4.1 池

- 预先开启固定个数的进程数，当任务来临时，直接提交给开好的进程，让这个进行执行，从而减轻了os调度的负担

#### 4.2 concurrent

- **concurrent.futures模块(3)**
- 3.4版本之后出现
- **进程池**

```python
# 进程池。 p.submit， p.shutdown
import os,time, random
from concurrent.futrures import ProcessPoolExecutor

def func(i):
    print('start', os.getpid())
    time.sleep(random.randint(1,3))
    print('end', os.getpid())
    return '%s * %s' %(i, os.getpid())

if __name__ == '__main__':
    p = ProcessPoolExecutor(5)                    # cpu核心数或多一
    ret_l = []
    for i in range(10):
        ret = p.submit(func, i)			              # 提交进程,参数直接放在其后
        ret_l.append(ret)						              # ret为future对象，ret.result()取值
    # 关闭池，不能提交任务，阻塞，直到已经提交的任务执行完毕
    p.shutdown()
    for ret in ret_l:                             # 会阻塞，相当于q.get()
      	print('------>',ret.result())             # result，同步阻塞
    print('main', os.getpid())

```

- 一个进程池中的任务个数，限制了我们程序的并发个数
- **线程池**

```python
# 线程池。p.submit(), p.shutdown(), ret.result()
from concurrent.futures import ThreadPoolExecutor

def func(i):
    print('start', os.getpid())
    time.sleep(random.randint(1,3))
    print('end', os.getpid())
    return '%s * %s' %(i, os.getpid())

tp = ThreadPoolExecutor(20)                      # 线程个数一般为cpu核心数4-5倍
ret_l = []
for i in range(100):
		ret = tp.submit(func, 1)
    ret_l.append(ret)
for ret in ret_l:
  	print('------->', ret.result())
p.shutdown()
print('main')

```

- tp.map(func, **可迭代对象**)：参数只能传输一个

```python
# 线程池。p.submit(), p.shutdown(), ret.result()
from concurrent.futures import ThreadPoolExecutor

def func(i):
    print('start', os.getpid())
    time.sleep(random.randint(1,3))
    print('end', os.getpid())
    return '%s * %s' %(i, os.getpid())

tp = ThreadPoolExecutor(20)                     # 线程个数一般为cpu核心数4-5倍
ret = tp.map(func, range(20))				          	# tp.map()方法
for i in ret:print(i)														# ret 为生成器对象

```

#### 4.3 回调函数

- ret.add_done_callback：回调函数
- 先来先响应，会提高整体的处理速度
- 会监听obj值：直到obj.result()有值为止

```python
from concurrent.futures import ThreadPoolExecutor
def get_page(url):
  	content = requests.get(url)
    return {'url':url, 'content':content.text}
def parserpage(dic):
  	print(dic.result()['url'])

for url in url_l:
  	ret = get_page(url)
    ret.add_done_callback(parserpage)          # 先执行完，先调用parserpage函数
    																	       	 # ret=add_done_callback(函数名)

```

```python
from concurrent.futures import ProcessPoolExecutor
import requests
import os

def get_page(url):
    print('<进程%s> get %s' % (os.getpid(), url))
    respone = requests.get(url)
    if respone.status_code == 200:
        return {'url': url, 'text': respone.text}

def parse_page(res):
    res = res.result()
    print('<进程%s> parse %s' % (os.getpid(), res['url']))
    parse_res = 'url:<%s> size:[%s]\n' % (res['url'], len(res['text']))
    with open('db.txt', 'a') as f:
        f.write(parse_res)

if __name__ == '__main__':
    urls = ['https://www.baidu.com', 'https://www.openstack.org', 'http://www.sina.com.cn/', 'https://www.tencent.com']
    p = ProcessPoolExecutor(3)
    for url in urls:
        p.submit(get_page, url).add_done_callback(parse_page)  # parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果


```



## 9.6 协程

### 1. 协程概念

1. **协程**：是单线程下的并发，又称**微线程**，**纤程**。英文名**Coroutine**。一句话说明什么是协程：**协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的**，多个任务在一条线程上来回切换。

2. **协程**：用户级别，自己写的py代码；控制切换是OS不可见的

   1. 一个线程中的阻塞都被其他的各种任务占满了
   2. 让OS认为这个线程很忙，尽量减少这个线程进入阻塞状态
   3. 提高了**单线程对cpu的利用率**
      - 多个任务在同一个线程中执行，也达到了一个并发的效果
   4. 规避了每个任务的io操作，减少了线程的个数，减轻了OS负担

3. 在**Cpython**解释器：**协程和线程**都不能利用**多核**

   1. 由于多线程本身不能利用多核
   2. 即便开启了多线程也只能**轮流在一个cpu上执行**
   3. 协程如果把所有**io操作都规避掉**，只剩下需要使用cpu的操作

4. 线程和协程**对比**

   1. **线程**
      - 切换需要OS，开销大，os不可控，给os的压力大
      - os对io操作的感知更加敏感
   2. **协程**

   - 切换需要py代码，开销小，用户操作可控，完全不会增加os压力
     - 用户级别对io操作感知较低
       - 协程切换开销几乎和函数调用一致

5. **协程特点**

   1. 必须在只有一个单线程里实现并发
   2. **修改共享数据**不需加锁
   3. 用户程序里自己保存多个控制流的上下文栈
   4. 附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（**select机制**））

6. 对比OS控制线程的切换，用户在**单线程内**控制协程的切换

   **优点如下**：

   1. 协程的切换开销更小，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级
   2. 单线程内就可以实现并发的效果，最大限度地利用cpu

   **缺点如下**：

   1. 协程的**本质**是单线程下，无法利用多核，可以是一个程序开启多个进程，每个进程内开启多个线程，每个线程内开启协程
   2. **协程指的是单个线程**，因而一旦协程出现阻塞，将会**阻塞整个线程**

### 2. greenlet&gevent

#### 2.1 原生python完成

- asynicio：**使用yield**
- 能够在一个线程下的多个任务之间来回切换，那么每一个任务都是协程

```python
# 切换，协程任务
def func1():
  	1 + 2
    2 + 3
    yield 1 
    sleep(1)
def func2():
  	g = func1()
    next(g)
    next(g)

```

#### 2.2 C语言完成的py模块

- greenlet
- gevent

1. greenlet模块

```python
# 完成切换
import time
from greenlet import greenlet

def func1():
    print(123)
    time.sleep(0.5)
    g2.switch()
    print(123)
  
def func2():
  	print(456)
    time.sleep(0.5)
    print(456)
    g1.switch()
   
g1 = greenlet(func1)
g2 = greenlet(func2)
g1.switch()

```

2. **协程切换原理**
   - **事件循环**：第三者一直在循环所有任务调度所有任务

```python
def sleep(num):
  	t = num + time.time()
    yield t
    print('sleep 结束')
    
g1 = sleep(1)
g2 = sleep(2)
t1 = next(g1) 
t2 = next(g2)
lst = [t1, t2]
min_t = min(lst)
time.sleep(min_t - time.time())
g1.next()

min_t = min(lst)
time.sleep(min_t - time.time())
g2.next()
```

3. gevent模块
   - 基于greenlet
   - gevent.sleep/ gevent.**spawn(func)** / gevent.**joinall(func_li)** / g.**join**()

```python
# gevent不认识time.sleep
import time
import gevent
from gevent import monkey
monkey.patch_all()                        # 可能的阻塞方法

def func1():
    print(123)
    gevent.sleep(1)
    print(123)
  
def func2():
  	print(456)
    gevnet.sleep(1)
    print(456)
  
g1 = gevent.spawn(fun1)
g2 = gevent.spawn(fun2)
# gevent.sleep(2)											  	# 遇到阻塞才会切换
# g1.join()                               # 阻塞直到g1任务完成为止
# g2.join() 
gevent.joinall([g1, g2])

g_l = []
for i in range(10):
  	g = gevent.spawn(func1)
    g_l.append(g)
gevent.joinall(g_l)

```

```python
# 示例大变身
import gevent
from gevent import monkey,time
monkey.patch_all()                          # 对io操作进行重现实现

def func1():
    print(123)
    time.sleep(3)
    print(456)

def func2():
    print('---------')
    time.sleep(1)
    print('=========')

g1 = gevent.spawn(func1)
g2 = gevent.spawn(func2)
gevent.joinall([g1, g2])									  # 阻塞列表中的所有协程
print('main')

```

- 获取返回值

```python
print(g1.value )                            # value是属性，如果没有执行则为None
```

- 协程实现socket

```python
import socket
import gevent
from gevent import monkey
monkey.patch_all()

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

def chat(con):
    while True:
        msg = con.recv(1024).decode('utf-8')
        con.send(msg.upper().encode('utf-8'))

while True:
    con, _ = sk.accept()
    gevent.spawn(chat, con)

```

### 3. asynico

- python原生底层的协程模块
  - 爬虫、webserver框架
  - 提高网编的效率和并发效果

#### 3.1 启动一个任务

```python
import asyncio                          # 只识别自身的方法

# 起一个任务
async def demo():                       # 必须要async修饰，协程方法
    print('start')
		await asyncio.sleep(1)              # 阻塞，await关键字 + 协程函数
    print('end')
    
loop = asyncio.get_event_loop()         # 创建一个事件循环
loop.run_until_complete(demo())         # 阻塞，直到协程执行完毕
																				# 把demo任务丢到事件循环中执行

```

#### 3.2 启动多个任务

1. **没有返回值**
   - 创建一个事件循环
   - 等待
   - 阻塞

```python
import asyncio                          # 只识别自身的方法

async def demo():                       # 必须要async修饰，协程方法
    print('start')
		await asyncio.sleep(1)              # 阻塞，await关键字 + 协程函数
    print('end')

loop = asyncio.get_event_loop()         # 创建一个事件循环
wait_obj = asyncio.wait([demo(), demo(), demo()])
loop.run_until_complete(wait_obj)       # 没有返回值

```

2. **有返回值**
   - 创建一个事件循环
   - loop.creat_task(func(arg1, arg2 …))
   - asyncio.wait([task1, taks2 …])：得到一个任务列表对象
   - loop.run_until)_complete(wait_obj)
   - task列表中即为返回值(**task对象**)

```python
# 同步取返回值
import asyncio
async def demo():
    print('start')
		await asyncio.sleep(1)
    print('end')
    return 123
    
loop = asyncio.get_event_loop()        # 创建一个事件循环
t1 = loop.create_task(demo())
t2 = loop.create_task(demo())
tasks = [t1, t2]                       # 任务列表
wait_obj = asyncio.wait([t1, t2])
loop.run_until_complete(wait_obj)
for task in tasks:
 	 	print(t.result())                   # 获取返回值

```

3. **异步取返回值**
   - task = asyncio.ensure_future(func(arg1, arg2...))
   - asyncio.as_compeleted(task_l)：可迭代对象
   - i await i

```python
import asyncio
async def demo(i):
    print('start')
		await asyncio.sleep(10-i)
    print('end')
    return i, 123

async def main():
  	task_l = []
    for i in range(10):
      	task = asyncio.ensure_future(demo(i))
        task_l.append(task)
    for ret in asyncio.as_compeleted(task_l):
      	res = await ret
        print(res)
        
loop = asyncio.get_event_loop() 
loop.run_until_compeleted(main())

```

#### Note3(2)

1. **await** 阻塞事件，协程函数从这里切换出去，还能保证切回来
   - 必须写在**async**里面，async函数是个协程函数(调用时并不执行)
2. **loop**是事件循环，所有的协程执行、调度、都离不开**loop**

### 4. 协程的上下文切换

1. 在一个基于协程的应用程序中，可能会产生数以千计的协程，所有这些协程，会有一个的**调度器来统一调度**。
2. 另外我们知道，高性能的程序首要注意的就是**避免程序阻塞**。
3. 那么，在以**协程为最小运行单位**的程序中，同样也需要确保这一点，即每一个协程都不能发生阻塞。
4. 因为**只要某一个协程发生了阻塞**，那么整个调度器就阻塞住了，后续等待的协程得不到运行，整个程序此时也将死翘翘了。
5. CPU**只认识线程**，不会像线程一样把**上下文保存在CPU寄存器**，协程是用户控制的。
6. 协程的**优缺点**
   1. **优点**
      - 无需线程上下文切换的开销，用yield的时候，只是在函数之间来回切换
      - 无需原子操作锁定及同步的开销，**没有异步锁**之类的东西，因为协程就是单线程
      - 方便切换控制流，简化编程模型
      - 高并发-高扩展-低成本，一个CPU支持**上万个协程**都不成问题
   2. **缺点**
      - 由于是单线程的无法利用多核资源，协程本质上是单线程
      - 协程需要和进程配合才能运行在多CPU上
      - 协程阻塞时会阻塞整个程序

## 小结

### 1. 协程

1. **概念**：多个任务在一条线程上来回切换
2. **目的**：
   - 在一条线程上最大限度提高CPU的使用率
   - 在一个任务中遇到IO的时候就切换到其他任务
3. **特点**：开销很小，是用户级别(从用户级别能够感知的IO操作)，不能利用多核，数据共享，**协程之间数据安全**
4. **模块**
   1. gevent：基于greenlet切换
      - 导入模块
      - 导入monkey，执行patch_all
      - 写一个函数但做协程要执行的任务
      - 协程对象 = gevent.spawn(函数名, 参数，)
      - 协程对象.join(), gevent.joinall([g1, g2…])
   2. 分辨gevent是否识别了我们写的代码中的io操作
      - patch_all：queue.get()
      - print()：在**patch_all前后打印**io操作的函数地址
   3. asyncio：**基于yield切换**
      - **async**：标识一个协程函数
      - **await**：后面跟着一个asyncio模块提供的io操作的函数
      - **loop**：事件循环，负责在多个任务之间进行切换

### 2. 进程和线程

1. 什么是GIL
   1. 全局解释器锁
   2. 由Cpython解释器提供的
   3. 导致了一个进程中的多个线程同一时刻只能有一个线程访问CPU
2. 进程、线程中都需要用到锁
   1. **互斥锁**：在一个线程中不能连续acquire多次，效率高，产生死锁的几率大
   2. **递归锁**：在一个线程中能连续acquire多次，效率低，一把锁永远不死锁
3. 进程、线程、协程特点（**开销**，**数据隔离/共享**，**能不能利用多核**，**数据安全**，**用户还是os**）
   1. 进程：开销大，数据隔离，可以利用多核，数据不安全，os控制
   2. 线程：开销中，数据共享，cpython解释器中不能利用多核，数据不安全，os控制
   3. 协程：开销小，数据共享，不能利用多核，数据安全，用户控制
4. 在哪些地方用到了线程和协程
   1. 自己用线程、协程完成爬虫任务
   2. 但是，后来有了比较丰富的爬虫框架
      - 了解到爬虫**scrapy**、**beautyful soup**、**aiohttp**爬虫框架，哪些用到了线程、哪些用到了协程
   3. web框架中，并发是如何实现的
      - 传统框架：**django**线程实现，flask(优先选择协程、其次使用线程)
      - socket server：多线程实现
      - 异步框架：**tornado**，**sanic**都是协程实现
5. IPC
   1. 进程间通信机制
   2. 内置模块(基于文件)：queue，pipe
   3. 第三方工具(基于网络)：redis，kafka，memcache，rabbitmq
   4. 第三方：发挥的都是消息中间件的功能
6. 线程相关：
   1. 开启线程时间很短，satrt是一个异步非阻塞方法
   2. 同步数据安全
   3. 列表的操作，无论是同步还是异步都是数据安全的