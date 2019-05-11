# 今日内容

1. *计算机初步认识*
2. *解释器的安装*
3. *IDE安装，编辑代码的软件：Pycharm*
4. *python入门*
5. *交作业：bolg/git*

# markdowny语法

1. 标题： #标题内容 ## ###
2. 列表：- 元素1 - 元素2 / 1. 元素1 2.元素2
3. 图片 复制，黏贴
4. 代码块： ```（英文版的～）
5. 表格：段落->表格

# 内容详细

##1. 计算机概览



   	1. 常见的操作系统

     - win：xp、win7、win10、windows server
     - linux：cnetos（GUI稍差）、ubuntu（个人开发，GUI比较好）、redhat（企业级）
     - macos（办公）

  2.  编程语言  —>   解释器+语法

      - 安装解释器/编译器/虚拟机(3者本质相同)
      - 学习语法

      
## 2. 解释器安装 (py不同版本可共存)（3步）

1. 官网下载

   - **尽量选择最新的前一版本**
   - python 2.7.16（2020年官方不再维护） &  python3.6.8

2. 安装python 

3. 检查是否安装成功

   - 在终端中运行python.exe文件

   - **PATH**：系统环境变量（用户环境变量值针对某一用户有效）

   - 环境变量是为了在终端运行程序方便

     1. 任何.exe 文件都可使用path简化操作

     2. 自动添加环境变量是添加到**用户变量**（win安装python解释器时可选择）

        - win10: 计算机->属性->高级->环境变量->系统变量->Path->新建 

        - Win7: Path会放在同一行中，用 **；**隔开

     3. 重新打开**终端**（cmd/terimal）生效

   *Note：*

   - python  解释器路径 （cmd）；

   - code文件可以是任何形式，为区分不同语言，建议固定后缀（.py）

   

## 3. 第一个脚本

- 终端 中输入： 解释器路径 文件 

  ```python
  print('你好’)
  ```




## 4. 编码 （3）

1. 初识编码

   - 万国码unicode 4bytes（迄今占用21位）
     - 用于计算机内存计算
   - uncicode表示ASCII时，前用0补齐
   - UTF-8(**16**)（对unicode压缩，保留8(16)n倍bit）*

2. Python2默认采用ASCII码，python3默认UTF-8 （**区别一**）

   - **# -\*- coding:utf-8 --        添加头件**（解决py2不能解释UTF-8文件问题）*

     ```python
     #-*- coding:utf-8 -*-  
     print('你好’)
     ```

3. 文件编码

   - 建议：编写文件时，保存要用utf-8
     - mac终端默认utf-8
     - win终端默认GBK （chcp 65001）
     - 编解码要一致，否则会乱码



## 5.解释器

文件：a.py

```python
#!/usr/bin/env python		在Linux指定解释器路径
#-*- coding:utf-8 -*-
print('你好')
```

运行：解释器+文件路径

- 给文件赋予一个可执行的权限
- ./a.py 查找文件第一行，认为其为解释器路径
  - 相当于 ：/usr/bin/env/python a.py 

以上环境头只在Linux上生效



##  6.输出

```python
print ('想要输出的内容')		
print ('666')
print (666)
```

Note：（***第二个区别***）

- Py2: print  "你好"
- Py3:print("你好")



## 7.数据类型

```python
'alex'/"alex"/'''alex'''/"""alex""" 一般称为字符串 str
666，一般称为数字/整型 int
True or False，一般称为 bool类型
```

Note: 

- 为解决string里有引号存在，'' 和"" 共存
- """  """ 和 ''' ''' 支持换行

1. 字符串 str
   - 单引号
   - 双引号
   - 三引号""" """较为常见
2. 数字（无引号）str
3. bool 类型



## 8.变量

命名要求：（3+2）

1. 变量名***只***能包含：字母、数字、下划线

2. 数字不能开头

3. 不能时python的关键字（关键字会有特殊颜色）

   - ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

   **2个建议**：

   - 见名知意，
   - 多个单词用 **_** 隔开（在py中常见），或单词首字母大写（驼峰式 java）

## 9.练习 （string的乘法）

```python
#第一题
age = 18
new_age = age + 1
print(new_age)

#第二题
name = 'alex'
new_name = name + 'sb'
print(new_name)

#第三题
age = '666'
new_age = age + '666'
print(new_age)

#第四题 
age = '666'
new_age = age + 666
print(new_age)		#此时会报错TypeError：...

#第五题
age = 6
new_age = age * 2
print(new_age)

#第六题（字符串相乘：重复次数）
name = 'alex'
new_name = name * 2
print(new_name)

#第七题
age = 18
value = age >= 19
print(value)

#第八题
_ = 9
_9 = 9
9name = 9 #数字不能打头
True = 9 #key
print = 666 #key
```



## 10.输入

```python
user_name = input('please input your name: ')
message = user_name + 'sb'
print (message)
```

Note: 

-  **input( ) 用户输入的任何内容都默认为string**
- Py 2与3 的区别三：
  - Py2: name = **raw_input**('please input your name ')
  - Py3: name = **input**('please input your name')

示例：（string的拼接）

```python
user_name = input('please input your name: ')
password = input('please input your pwd: ')
#输出用户名和密码拼接
content = 'your name is: ' + user_name + ';' 'your pwd is: ' + password	
#输出用户名和密码拼接结果
print(content)
```



## 11.注释

```python 
# 单行注释管一行

"""
多行注释
""" 

'''
多行注释
'''
```



## 12.条件判断

1. 初级条件语句

```python
#请实现一个功能：用户输入性别，如果是男，则输出：再见；如果是女：则输出：来呀来呀；
gender = input('please input your gender: ')
"""
如果是boy，打印goodbye
如果是girl，打印come on
"""
if gender == 'boy'：		#同一代码块中，同一级缩进要一致
	print('goodbay')
else:
  print('come on')
  
```

2. elif 条件

```python
gender = input('please input your gender: ')
"""
如果是boy，打印goodbye
如果是girl，打印come on
如果是XXX，打印to find alex
如果是other，打印out
"""
if gender == 'boy'：		#同一代码块中，同一级缩进要一致
	print('goodbay')
elif gender == 'girl':
  print('come on')
elif gender == 'XXX'
	print('to find alex')
 else:
  print('out')
print('end')
```

3. if单语句

```python
gender = input('please input your gender: ')
if gender == 'boy':
	print('goodbay')
```

4. 练习：类型转换 和 == 比较运算符

```python
#用户输入一个数字，如果数字>50,输出：大了；若果数字<=50,输出：小了
num = int(input('please input a num: '))
if num > 50:
  print('bigger')
else:
  print('smaller')
  
#第二题：用户名密码登陆
user_name = input('please input user_name: ')
pwd = input('please input pwd: ')
if user_name == 'alex' and pwd == 'alex':
  print('congratulations')
else:
  print('user_name or paw is fault')
```



## 13.Pycharm 安装

java开发

安装使用：

1. create new project -> pure python -> creat a new dir

![Pycharm1](/Users/henry/Documents/截图/Py截图/Pycharm1.png)



![Pycharm2](/Users/henry/Documents/截图/Py截图/Pycharm3.png)