# 今日内容

##1.练习题的变换(6)

####1.1 list： li.extend('a') :拆分a，逐个追加到list中

- 遍历a中的每个元素，追加到list中
- li += s
  - li1 + li2   #list.\_add\_
- extend():是list特有功能

####1.2 del li[2]  # 仅仅是删除，不可返回删除值

- li.pop[2] # 可以把删除值，赋值新变量
- remove # 当找不到目标值时，会报错

####1.3 range(start, end, step) 

- step 可以为负，类似切片

####1.4 insert(3, 'abc')

- 只能用一层索引

#### 1.5 ','.join(li)

- 只要可以循环就可以
- str , list , tuple
- **join操作对象只能是'str'类型**

#### 1.6 s.isdigit()

- 如果有空格则会认为不是数字
  - s.split() :分割后的结果是列表，元素为字符串

####小结：

#####1.extend

#####2.pop和del 区别

1. 删除li[1:4]
2. 变量类型 & 书写规范 % (a ,)
   - v1 = 1	# int
   - v2 = (1)      # int
   - v3 = (1,).    # tuple
   - v4 = ()       # tuple
3. 强制转化
   1. str(999)       # '999'
   2. str(True)      # 'True'
   3. str(['henry', 'echo'] )  # '['henry', 'echo']'
      - ''.join([li]) 
      - str([li])
   4. list('abcdef') 
   5. **list((11, 22, 33, 44))**   # tuple 转换为list
   6. **tuple([11, 22, 33])**     # list转换为tuple
   7. tuple('asdfghjkl')   
   8. **常见的类型转换**
      - str —> int
      - int —> str
      - list —>tuple
      - tuple —> list
      - 其他转bool

## 2.dict（字典）

### 2.1 字典（无序，py3.6之后已经有序）

​	帮助用户表示某一事物的信息（事物属性较多）。

```python
# 基本格式
date = {'key1':'value1','key2':'value2','key3':'value3'}
```

> 表示个人信息，姓名、年龄、性别、爱好

```python
# key值对
info = {'name': 'henry', 'age': 18, 'gender':'male'}  
info['name']
info['age']
...
```

```python
# excise 校验用户登陆
userinfo = {'username': 'alex', 'password': '123'}
user = input('please input your name: ')
pwd = input('please input your pwd: ')
if userinfo['username'] == user and userinfo[password] == pwd:
  print('success')
else:
  print('user or pwd is wrong')
```

### 2.1 字典的操作（3+5）

####1. 获取dic中所有的key

```python
info = {'name': 'henry', 'age': 18, 'gender':'male'}  
info.keys()     # 类似list，但不是
```

####2. 获取dic中所有的value

```python
info = {'name': 'henry', 'age': 18, 'gender':'male'}  
info.values() 
```

####3. 获取dic中所有的 items值

```python
info = {'name': 'henry', 'age': 18, 'gender':'male'}  
info.items() 
for v1，v2 in info.items():
  print(v1, v2)
```



------

#### 4. len

```python
info = {'name': 'henry', 'age': 18, 'gender':'male'}  
print(len(info))
```

#### 5. 索引（key值的索引）

```python
# 利用key取值，key 就是index
info = {'name': 'henry', 'age': 18, 'gender':'male'}  
info['name']
```

#### 6. for循环

```python
info = {'name': 'henry', 'age': 18, 'gender':'male'} 
# 输出keys
for item in info.keys():
  print(item)
#  输出values
for item in info.values():
  print(item)
#  分别输出keys 和 values
for k,v in info.items():
  print(k, v)
#  输出的是tuple
for i in info.items():
  print(i)
```

#### 7. 修改

```python
# 修改值
info = {'name': 'henry', 'age': 18, 'gender':'male'}
age = info['age'] = 19
print(info)
# 改健
# 删除后在增加
del info['name']
info['name'] = 'echo'   # 没有key值默认添加
print(info)
```

#### 8. 删除

```python
# key值对是整体
info = {'name': 'henry', 'age': 18, 'gender':'male'}
del info['name']
print(info)
```

####练习（8）

```python
# 示例1
v = '1 + 3'
# 赋值    
# 此时，是str类型
a, b = v.split('+')
print('-->', a, '<--', '-->', b, '<--')
# 赋值
a, b = (1, 3,)
print('-->', a, '<--', '-->', b, '<--')
# 赋值
a, b = (1, 3,)
print('-->', a, '<--', '-->', b, '<--')
```

```python
# 示例2  输出所有keys
info = {'name': 'henry', 'age': 18, 'gender': 'male'}
for item in info.keys():
  print(item)
```

```python
# 示例3 
# 先打印info，用户输入key值，返回value值
info = {'name': 'henry', 'age': 18, 'gender': 'male'}
for k, v in info.items():
    print(k, v)
user_input = input('please input key: ')
print(info[user_input])
```

```python
# 示例4
# 在字典中添加数据，k1: 1 ，k2: 2， k3: 3
info = {}
info['k1'] = 1

```

```python
# 示例5
# 在空字典中，用户输入：key 和 value，并加入
info = {}
k = input('请输入key：')
v = input('请输入value：')
info[k] = v
print(info)
```

```python
# 示例6
# 在空字典中，用户输入：key 和 value，并加入,一直输入，除非用户输入‘n’
info = {}
while 1:
    k = input('please input a key: ')
    if k == 'n':
        break
    v = input('please input a value: ')
    info[k] = v
 print(info)
```

```python
# 示例7
message = 'k1|v1,k2|v2,k3|123'
# info = {'k1':'v1', 'k2':'v2', 'k3':'123'}

# 方式1
mag = message.split(',')
info = {}
for i in range(len(mag)):
    mag2 = mag[i].split('|')
    mag2[0] = mag2[0].strip()  # 去除空格
    mag2[1] = mag2[1].strip()
    info[mag2[0]] = mag2[1]
print(info)
```

```python
# 方式2
message = 'k1|v1,k2|v2,k3|123'
# info = {'k1':'v1', 'k2':'v2', 'k3':'123'}
new_m = message.split(',')
info = {}
for item in new_m:
    u, v = item.split('|')
    info[u] = v
print(info)
```

```python
# 示例8
li = [11,22,33,True,[11,2],(11,2,[11,22],33,),{'k1':'v1','k2':(11,22,3)}]
info = {k}
```

```python
# 示例9
# 创建一个用户列表，让用户输入，用户名和密码进行登录user_list = [{'user':'用户输入'},{'user':'用户输入'},{'user':'用户输入'}...]
# 输入'n'结束输入

# 构建用户列表
user_list = []
while True:
    u = input('请录入用户名：')
    if u == 'n':
        break
    v = input('请录入密码：')
    info = {}
    info[user] = u
    info[password] = v
    user_list.append(info)
# 校验
name = input('用户名：')
pwd = input('密码：')
for i in range(len(user_list)):
    if name in user_list[i][users] and pwd == user_list[i][password]:
        print('登陆成功')
        break
    if i == len(user_list) - 1:
        print('登陆失败')
        break
```

```python
# 方法二   
# message 标志变量，可进行是、否判断，并输出一次
user_list = []
while True:
    u = input('请录入用户名：')
    if u == 'n':
        break
    v = input('请录入密码：')
    info = {'user': u, 'password': v}
    user_list.append(info)
# 校验
username = input('please input your name: ')
pwd = input('please input your pwd: ')
message = '登陆失败'
for items in user_list:
    if items['user'] == username and items['password'] == pwd:
        message = '登陆成功'
        break
print(message)
```

Note：list 和 dict 不可hash







  











