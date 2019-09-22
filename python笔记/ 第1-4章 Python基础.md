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
eg.u'henry'        <--> 'henry'
str               <--> bytes
eg.henryx'         <--> henryex
```

### Note

- bytes类型一般用于文件存储和网络传输

2. 其他不同

|      |                                   | Py2                              | Py3                                                          |
| ---- | --------------------------------- | -------------------------------- | ------------------------------------------------------------ |
| 1    | 字符串类型不同                    |                                  |                                                              |
| 2    | **py2py3默认解释器编码**          | ASCII                            | UTF-8                                                        |
| 3    | 输入输出                          | raw_input() ; print              | input() ; print()                                            |
| 4    | int / long                        | int 和 long，除法只保留整数      | 只用int，除法保留小数                                        |
| 5    | range/xrange                      | range/xrange                     | 只有range，相当于py2的xrange                                 |
| 6    | info.keys,info.values,info .items | 数据类型是list                   | 数据类型是<class 'dict_keys'>                                |
| 7    | map/filter                        | 数据类型是list                   | 返回的是iterator，可以list()查看<map object at 0x108bfc668>  |
| 8    | reduce                            | 内置                             | 移到functools                                                |
| 9    | 模块和包                          | 需要_\_init__.py                 | —                                                            |
| 10   | 经典类和新式类                    | 同时拥有                         | 只有新式类                                                   |
| 11   | yield from                        | 没有                             | 有                                                           |
|      | 进程池和线程池                    | from multiprocessing import Pool | form concurremnt.furtures.thread import ThreadPoolExecutor              orm concurremnt.furtures.process import ProcessPoolExecutor |
| 13   | **字符串类型**                    | unicode，str                     | str，bytes                                                   |



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

#### 1. s.upper() / s.lower()

```python
# 大小写转换
s = 'Henry'
print(s.upper(), s.lower())
```

#### 2. s.isdigit() / **s.isdecimal()**

```python
# 判断是否是数字
s1 = '123'
s2 = '12.3'
print(s1.isdigit(), s2.isdigit())		# True Flase

# isdecimal只判断是否是整数
```

#### 3. s.strip()

```python
# 默认去除两边空格+ \n + \t

s = '  asdfgh,      '
print('-->', s.strip(), '<--')
print('-->', s.strip().strip(','), '<--')
```

#### 4. s.replace('a', 'b', n)

```python
# repalce 中的 a 和 b 必须是str类型， n 必须是int类型
s = 'adsafga'
print(s.replace('a', '666'))
print(s.replace('a', '666', 1))
```

#### 5. s.split('_')

```python
# str的分割
s = 'henry_echo_elaine_'
li = s.split('_')
print(li)  # 分割后的元素永远比分隔符号多一个
```

#### 6. s.startswith() / s.endswith()

```python
# 判断开始/结束位置是否是指定元素
s = 'abghjkdc'
print(s.startswith('ab'), s.endswith('cd'))
# True  Flase
```

#### 7. str 的格式化输出(2种)

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

#### 8. encode

```python
# 指定编码类型
s = '你好'
print(s.encode('utf-8'))   # 6个字节
print( s.encode('gbk'))		 # 4个字节
```

#### 9. '_'.join(s)

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

1.   s.find('a') / s.rfind()
    -   返回第一个 a 的索引值，没有则返回 -1 
2.   s.index('a') / s.rindex() /s.lindex()
    -   返回第一个 a 的索引值，没有报错
3.  s.isupper() / s.islower()
4.  s.capitalize()
5.   s.casefold()
6.  s.center(20, "*")
    -   可以为空
7.  s.ljust(20, "*")/s.rjust()
8.  s.zfill()
    -    用0填充
9.  s.count('a', [start], [end]) 
    -   查找'a' 的个数
10.  s.isalnum()
11.  s.isalpha()
12.  s.isnumeric()
13.  s.isprintable()
14.  s.istitle()
15.  s.partition('a')  / s.rpartition()
     -   分成三部分，a左边，a右边
16.  s.swapcase()

____

____

### 3. 公共方法

#### 1. len(s)

```python
# 返回s长度
s = '1234567890'
print(len(s))     # 10
```

#### 2. s[index]

```python
# 索引取值
s = '123456789'
print(s[3])   # 4
```

#### 3. 切片

```python
s = '123456789'
print(s[3:5])   # 45
```

#### 4. setp

```python 
# 根据step进行切片
s = '123456789'
print(s[3::2])   # 468
```

#### 5. for循环

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

#### 1. li.append('666')

```python
# 任意类型数据，li操作不能直接放在print()中
li = [1, 2, 3, 4, 5, 6]
li.append('666')
print(li)
li.append(['henry'])
print(li)
```

#### 2. li.insert(2, 'henry')

```python
# 按照index位置插入指定内容
li = [1, 2, 3, 4, 5, 6]
li.insert(3, 'henry')
print(li)
```

#### 3. li.remove('aa')

```python
# 删除指定list中的元素
li = ['aa', 'a', 'aacde']
li.remove('aa')
print(li)
li.remove('bb')
print(li)  # 会报错
```

#### 4. li.pop(index)

```python
# 按index删除list中的元素
li = [1, 2, 3, 4, 5, 6]
li.pop()
print(li)
li.pop(3)
print(li)
```

#### 5. li.clear()

```python
# 清空list中的所有元素
li = [1, 2, 3, 4, 5, 6]
li.clear()
print(li)
```

#### 6. li.reverse()

```python
# 反转list中的元素
li = [1, 2, 3, 4, 5, 6]
li.reverse()
print(li)
```

#### 7. li.sort(reveres = True)

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

#### 8. li.extend(s)

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

### 2. 其他

1.  li.count('a')
2.   li.copy()
    -   浅拷贝
3.   li.count()
    -   只计算第一层，不考虑嵌套
4.   li.index('val')

___

___

### 3. 公共方法

#### 1. len(s)

```python
li = [1, 2, 3, 4, 5, 6]
print(len(li))

```

#### 2. index 取值

```python
li = [1, 2, 3, 4, 5, 6]
print(li[2])

```

#### 3. 切片

```python
li = [1, 2, 3, 4, 5, 6]
print(li[2:5])

```

#### 4. step

```python
li = [1, 2, 3, 4, 5, 6]
print(li[2::2])

```

#### 5. for循环

```python
li = [1, 2, 3, 4, 5, 6]
for i in li:
  print(i)

```

#### 6. 修改

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

#### 7. 删除del li[]

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

#### 1. len()

```python
t = (1, 2, 3,)
print(len(t))
```

#### 2. index

```python
t = (1, 2, 3,)
print(t[2])
```

#### 3. 切片

```python
t = (1, 2, 3,)
print(t[1:])
```

#### 4. step

```python
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(t[1::2])
```

#### 5. for 循环

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
# {key1: value1, k2:value2}
# key不能重复
```

#### 1. info/ info.keys()

- 类似 list ，但不是list，例如：dict_keys(['name', 'age', 'gender'])

```python
# 取所有key
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
for key i info:
  print(key)
```

#### 2. Info.values()

```python
# 取所有value
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
for v in info.values():
    print(v)
```

#### 3. info.items()

```python
# 取所有key值对
# 取出的是 tuple 类型
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
for pair in info.items():
    print(pair)
```

#### 4. Info.get(key, 666)

```python
# 有key则取出， 没有则返回指定 值
# 如果没有指定值，则返回 None
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
print(info.get(1, 666))
print(info.get(4, 666))
```

#### 5. info.pop(key)

```python
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
print(info.pop(1))
print(info.pop(4))
```

#### 6. info.update(info1)

```python
# 只能用dict类型更新
info = {}
info1 = {1: 'henry', 2: 'echo', 3: 'eliane'}
info.update(info1)
print(info)
```

#### 7. info.setdefalut(key, value)

```python
# 查询key，有则取出，没有则添加
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
info.setdefault(4, 'hello')
print(info)
# 取出需要赋值给其他变量
val = info.setdefault(4, 'i hate you')
print(val)
```

#### 8. info.popitem()

```python
# 不能加参数，删除最后一个key值对
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
v = info.popitem()
print(v,info)   # v是tuple
```

#### 9. info.clear()

```python
# 清空所有元素
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
info.clear()
print(info)
```

### 2. 其他

1.  info.copy()  # 浅拷贝
2.   info.fromkeys()

```python
li = [1, 2, 3, 4, 5]
info = {'a': 1, 'b': 2}
v = info.fromkeys(li, 'hello')
print(v, info)
```



___

___

### 3. 公共方法

#### 1. len(info)

```python
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
print(len(info))
```

#### 2. Index 取值

```python
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
print(info[1])
```

#### 3. for 循环

```python
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
for i in info:
  print(i)
for v in info.values():
  print(v)
for pair in info.items():
  print(pair)
```

#### 4. 修改

```python
# key一样则修改，不一样则追加
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
info[1] = 'hello'
print(info)
info[4] = 'you are smart'
print(info)
```

#### 5. 删除

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

#### 1. s.add('a')

```python
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.add(5)
print(s)
```

#### 2. s.update(s1)

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

#### 3. s.pop()

```python
# 随机删除，此时pop中不能有任何参数
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.pop()  # 默认删除第一个元素/随机
print(s)
```

#### 4. s.discard()

```python
# 必须有一个参数，没有不报错, 不会返回值
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
val = s.discard(3)
print(s)
print(val)
```

#### 5. s.remove('a')

```python
# 必须有一个参数，没有会报错
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.remove(3)
print(s)
```

#### 6. s.clear()

```python
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
s.clear()
print(s)
```

#### 7. s.intersection(s1)

```python
# 取v1 和v2 的交集
v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
v2 = {1, 3, 5, 7}
v = v1.intersection(v2)
print(v)
```

#### 8. v.union(v1)

```python
# 取并集
v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
v2 = {1, 3, 5, 7}
v = v1.union(v2)
print(v)
```

#### 9. v.difference(v1)

```python
v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
v2 = {1, 3, 5, 7}
v = v1.difference(v2)
print(v)
```

#### 10. v.symmetric_difference(v1)

```python
v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
v2 = {1, 3, 5, 7}
v = v1.symmetric_difference(v2)
print(v)
```

```python
# 集合的运算
	方法
    运算法
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

### 3. 公共方法

#### 1. len(v)

```python
v = {1, 'henry', 2, 'echo', 3, 'eliane'}
print(len(v))
```

#### 2. for 循环

```python
# 无序输出
v = {1, 'henry', 2, 'echo', 3, 'eliane'}
for i in v:
    print(i)
```

## 3.8 公共方法

|                       | int  | bool | str  | list | tuple | dict | set  |
| :-------------------: | :--: | :--: | :--: | :--: | :---: | :--: | :--: |
|        **len**        |  —   |  —   |  ✓   |  ✓   |   ✓   |  ✓   |  ✓   |
|       **index**       |  —   |  —   |  ✓   |  ✓   |   ✓   |  ✓   |  —   |
|       **切片**        |  —   |  —   |  ✓   |  ✓   |   ✓   |  —   |  —   |
|       **step**        |  —   |  —   |  ✓   |  ✓   |   ✓   |  —   |  —   |
| **for循环/ iterable** |  —   |  —   |  ✓   |  ✓   |   ✓   |  ✓   |  ✓   |
|       **修改**        |  —   |  —   |  —   |  ✓   |   —   |  ✓   |  ✓   |
|       **删除**        |  —   |  —   |  —   |  ✓   |   —   |  ✓   |  ✓   |



## 3.9 内存相关&深浅拷贝

### 0. 可嵌套的数据类型

-   所有的容器类例如：list，tuple， dict，set 都可以嵌套，但set(), 只能嵌套可**hash**（int, bool, str, tuple 4种）的数据类型。

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