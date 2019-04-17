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
- 八进制  （计算机内部使用）
- 十进制
- 十六进制(表示).  \x （一般用于计算机显示）



# 第二章 python入门

## 2.1 环境的安装

​	首先，在官网下载py2与py3，2，3版本有很多不兼容所有会存在两个版本共存的问题。目前，mac、ubuntu等一些系统已经内置了python2版本。

​	为了开发需要，我们需要下载并安装python3。用于开发的软件，通常安装版本一般是找次新版本进行安装。安装pycharm IDE 开发工具。

​	环境变量的功能，及其配置。环境变量分为，用户环境变量（只对当前用户生效）和系统环境变量（所有用户均有效）。主要用于终端使用，不需要输入python解释器的完整路径，只要输入python* 就可使用。

​	mac的环境变量在～/.bash_profile文件中。通常在安装的时候python会自动生成环境变量，无需手动配置。

## 2.2 编码

​	当前，比较通用的编码有ASCII、Unicode、UTF-8、GB2312、GBK。由于计算机最初使用的是ASCII编码，所以掐他编码必须兼容ASCII码。

1. ASCII

   ASCII码，**8bits**表示一个字符。包含所有英文字母和常用的字符，最多可以表示256种。

2. Unicode

   Unicode（万国码），随着计算机的普及，计算机需要兼容多国语言，Unicode编码应运而生。**32bits**表示一个字符，总共可以表示**2\*\*32**种不同的符号，远远超出目前所有文字及字符，迄今使用**21bits**。通用的特点换来的是存储空间的浪费，一般只用于计算机内部处理计算。

3. utf-8

   为弥补unicode的不足，utf-8针对unicode进行压缩和优化，去掉前面多余的0，只保留有效部分。完整保留ASCII码，欧洲文字一般用**2bytes**表示，中文一般用**3bytes**表示。

4. GBK

   全称是GB2312-80《信息交换用汉字编码字符集 基本集》，1980年发布，是中文信息处理的国家标准，在大陆及海外使用简体中文的地区（如新加坡等）是强制使用的唯一中文编码。

   中文使用**2bytes**表示。GBK，是对GB2312的扩展，又称GBK大字符集，简而言之就是将所有亚洲文字的双字节字符。

   

## 2.3 变量

​	变量的主要作用是为了多次重复使用方便。

```python
# 查看python关键字
import keyword
keyword.kwlist
```

## 2.4 python基础语法

### 1. **多行显示**

Python语句中一般以新行作为语句的结束符。

但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：

```python
total = item_one + \
        item_two + \
        item_three
```

### 2. 实现换行

```python
input("按下 enter 键退出，其他任意键显示...\n")

# 不换行输出
print x,
print y,
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

​	执行Python代码时，如果导入了其他的 .py 文件，那么，执行过程中会自动生成一个与其同名的 .pyc 文件，该文件就是Python解释器编译之后产生的字节码。

**ps**：代码经过编译可以产生字节码；字节码通过反编译也可以得到代码。

# 第三章 数据类型

## 3.1 int

```python
# None 无操作
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
# 去除两边空格+ \n + \t

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
7. s.counter('a', [start], [end])
8. s.count('a')     # 查找'a' 的个数
9. s.isalnum()
10. s.isalpha()
11. s.isnumeric()
12. s.isprintable()
13. s.istitle()
14. s.ljust()
15. s.rjust()
16. s.partition('a')  / s.rpartition()# 分成三部分，a左边，a，a右边
17. s.swapcase()
18. s.zfill()  # 用0填充
19. s.copy()   # li = li1.copy()



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

___

___

### 2. 公共功能

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
print(li)
```

### 3. 内置函数

- list中python 内置的函数有， len，max，min，list(强转)
- list.copy()    是浅copy

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

**Note：可以转tuple 的是 list，dict(keys)，tuple(强转)**

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
info.popitem()
print(info)
```

9. info.clear()

```python
# 清空所有元素
info = {1: 'henry', 2: 'echo', 3: 'eliane'}
info.clear()
print(info)
```

___

___

### 2. 公共功能

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
del infop[1]
print(info)
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
s.pop()
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

___

___

### 2. 公共功能

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

​	所有的容器类例如：list，tuple， dict，set 都可以嵌套，但set(), 只能嵌套可hash（int, bool, str, tuple 4种）的数据类型。



## 3.10 内存相关&深浅拷贝

### 1. 内存相关

**小数据池**

- ==判断值
- is判断内存地址
- python中默认会对int，str，bool进行缓存

**缓存规则：**

- int型-5 — 256之间会被缓存
- str：空和单个字符默认缓存;只包含字母、数字、下划线，也缓存; 乘数>1时，str只包含Num、ALp、_时缓存（最终长度不能超过20）
- str：手动指定缓存
- bool

### 2. 深浅拷贝

1. 使用格式import copy
2. **4 个结论**
   - 浅拷贝只是拷贝第一层
   - 深拷贝会拷贝所有可变类型的数据
   - 只要 copy ，一定会开辟新的内存空间
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
f.readline()  # 一次性加载所有内容到内存，并根据行分割成字符串
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



### 3. file.flush()

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

#### **Note1**（2）

- 函数默认返回值是 None ，有时可以使用其作为**flag**
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

#### **Note2**（2）

- **return [表达式]** 结束函数，选择性地返回一个值给调用方(func()为返回值)。
- return 1， 2 ，3   会返回tuple：(1, 2, 3)

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

#### **Note4**（4）

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
4. 作用域中查找数据规则
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

#### **Note6**（3）

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

#### **Note7**（3）

1. 注意**func** 和 **func()** 的区别
2. 函数可以放入set()中(不常用)， 或dict中（一般用于values，也可以放在key中但不常用）
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
# way4 使用条件判断
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

#### **Note8**（3）

1. 用于表示简单函数（一行解决的函数）。
2. lambda 表达式会默认返回**冒号：**之后的值
3. 可变类型（list）的基本上都是None, 不可变（str）基本上会返回新值

### 4. 内置函数（28）

- 自定义函数

- **内置函数**（28）

  1. 强制转换(7)：int()，str,  bool,  list，dict，tuple，set
  2. 输入输出(2)：print, input
  3. 其他(5)：type, id, range, open, len
  4. 数学(6)
     - abs，float（int(55.5)保留整数部分）
     - max，min，sum，
     - **divmod**（两数相除，得商和余数, 两个值）

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

  5. 进制转换(3)：**bin**（0b，int<—>bin），**oct**（0o，int<—>oct），int(其他进制转int)，**hex**（0x，int<—>hex）

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

  6. 编码相关
     - chr() ：把int型数据，转换为unicode编码
     - ord()：把字符转换为unicode

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

  7. map / filter / reduce（py2）/zip
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
  print(list(result))
  ```

  - **reduce**

  ```python
  import functools
  v = [1, 2, 3, 4]
  result = functools.reduce(lambda x,y: x*y, v)
  print(result)
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

#### Note9（4） 

1. **闭包**，为函数创建一块区域（内部变量供自己使用），为以后执行提供数据；
2. 函数内部数据不会混乱
3. **执行完毕**+**内部数据不被**其他程序使用会被销毁
4. **应用**：装饰器，SQLAlchemy源码

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

**装饰器**：在不改变原函数的基础上，在函数执行之前、之后可以执行操作

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

#### **Note10**

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





# 第六章 模块



## 6.1 模块的基本知识

1. **分类**：

   - **内置模块**（py内部提供的功能）

   - **第三方模块**

   ```python
   # pip 安装模块
   pip install moudle_name
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

## 6.2 内置模块

​	内置模块目前有**random**，**hashlib**， **getpass** ，**time**，**sys**相关，**os**相关，**shutil** 等 **7** 个。

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

### **2. hashlib / getpass**

```python
# 将指定的**str**加密
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
4. **sys.argv**
   - shutil(shutil.rmtree(path)
5. **sys.path**

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
# pycharm也会自动添加工作目录和pycharm的目录
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

#### 6. shutil

```python
import shutil
shutil.rmtree(r'path')
```

## 6.3  json

- 特殊的字符串（list和dict嵌套的string）
- 不同语言间的数据交互
- 序列化/反序列化：把其语言的数据转化成**json**格式/ 相反
- **格式**

```python
# 只能包含，int，str，list，dict，bool
# 最外层必须是list/dict
# json 中如果包含str，必须是 双引号
# 如果是tuple类型数据，则会转换为list
```

```python
import json
v = [12, 3, 4, {'k1': 1}, True, 'adsf']
# 序列化
v = json.dumps(v)
# 反序列化
json.loads(v)
```





































# 第七章 面向对象

# 第八章 网络编程

# 第九章 并发编程

# 第十章 数据库

# 第十一章 前端开发

# 第十二章 Django框架









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

## Day01 - 10

1. day001

   - input() 的数据类型永远是 str
   - 当 break在循环里时，有些时候可以省略 else

2. day002

   - while True的效率会更高
   - 计数可以倒序(用于while循环)
   - 一直要求用户输入，或者死循环需要使用 while True
   - exit() 终止程序

3. day003

   - range(0, 100) # 此时可以省略0 ,tpye(range(100)).     <class 'range'>
   - message = '登陆失败'。变量标记

4. day004

   - li.extend(s1) # 遍历 s1 中的每个元素，追加到list中
   - li.pop(index) # 可以获取删除值
   - li.remove('a') # list 删除指定元素，li中没有会报错
   - ','.join(li) # 只要支持循环就支持 join，操作对象必须是 str 否则报错

5. day005

   - 当使用s.isdigit()时要注意，s 的数据类型,有空格和其他字符都会返回  False
   - list(dic.keys()) # 可以强转为list，如果是items则list元素为tuple

6. day06

   -  集合之间操作时，如果元素为空，则输出set()
   - 在循环里操作时，注意代码的有效范围
   - info.get('key', '不存在'）  # 可以返回两种不同的结果
   - 判断key是否在dict中只需：if key in info：
   - type(i) is int   # 这里的 int 是类
   - tyep(i) == int  # 可以判断数据类型, 地址和内容都是一样

7. day007

   -  只要是'_'.join 处理过的，都是srt
   - s.split(',') :
     - 默认是空白，实际应用中可以是字符或字符串；
     - 循环去除；
     - 但变量有且仅能是一个。

8. day008

   - 按行读取

   ```python
   # way1
   with open(***) as v:
      for line in v:
         line.strip('\n')
   # way2
      for line in v.readlines():
         line.strip('\n')
   ```

   - 程序一行太长显示不全，可以使用 \ 进行换行

9. day009

   -  函数传输文件名时，需要传输 str 类型
   - line = line.strip('\n').split('|'),从左到右操作
   - 如果需要双重甚至多重循环时， 可以考虑先构造一个子元素利用函数返回值默认时 None 可以实现 flag 标志功能

10. day10

   - range()是range类
   - return 1， 2， 3 返回的是元组
   - 注意：函数类似于变量，func 代指一块代码的内存地址。
   - a = ('b', 3, 4)*2 ，tuple里面的数据重复2次，list 和 tuple都可以

## Day11-20



