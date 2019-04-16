# 今日内容

##1. 集合(无序、不可重复)

##2. 内存(py节约内存)

##3. 深浅拷贝

#  补充

## 1. list

### 1.1 反转

- li.reverse()

### 1.2 排序

- li.sort(reverse = False）   # 从小到大， 默认是False
- li.sort(reverse = True）     # 从大到小

## 2. dict

### 2.1 Info.get('key'，666)     

- key存在则取值，不存在则返回666（默认是none）
- v = None    # 没有功能，bool(None) 是False

```python
info = {'k1':'v1', 'k2':'v2'}
result = info.get('k111')
if result:
  print('value = ')
if not result:
  print('不存在')
```

###2.2 result = Info.pop('k2')	

- 可以返回删除值，del 不可以
- 没有 k2 会报错
- info.popitem()         # 随机删除一个key值对

###2.3 info.update(info1)  

- 没有则添加，存在覆盖

### 2.4 判断一个str 中是否有敏感字符

1. str

```python
v = 'python 全栈'
if '全栈' in v:
  print('含敏感字符')
```

2. list/tuple

```python
v = ['python 全栈', 'alex']
if 'alex' in v:
  print('含敏感字符')
```

3. dict   **v.values()类似list但不是**

```python
v = ['k1':'V1', 'k2':'v2', 'k3':'v3']
# 默认按照key判断，即x是否是dict的 key
if 'x' in v:
  pass
# 判断：k1 是否在其中
if 'k1' in v:
  pass
```

```python
# 判断：v2 是否在其中
# 方式一：循环判断
flag = '不存在'
for v in v.values():
  	if v == 'v2':
   			flag = '存在'
 print（flag）

#方式二：先强转，v.values()类似list但不是
if 'v2' in list(v.values()): # 强制转换为列表
  		pass
```

```python
# 判断：k2:v2 是否在其中
value = v.get('value')
if value == 'v2':
  	print('exsit')
else:
  	print('not exsit')
```



```python
# 练习题
# 让用户输入任意string，判断是否包含指定的敏感字符
chars_list = ['alex', 'echo', 'henry']
content = input('please input your content: ')
message = True
for i in chars_list:
    if i in content:
        message = False
        break
if message:
    print(content)     
else：
		print('content includes senstive words')
# 1.昨天练习9
# 2.判断'v2' 是否在字典中
# 3.判断敏感字符

# exit()  直接退出程序
```

# 内容详细

## 1. 集合 set(无序，不重复)

```python
# set 格式
v = {1, 2, 3, 4, 5, 6}
# None
# int     v = int() --> 0
# bool    v = bool() --> False
# list    v = []/list()-->空
# dict    v = {} / v = dict()是空字典
# set     v = set() 是空集合
print(type(v))
```



## 2. 独有功能

### 2.1 **添加**

```python
v = set()
v.add('echo')
print(v)
```

### 2.2 **删除**

```python
v.discard('echo')   # 不会返回值
v.removre('echo')   # 不存在报错
```

### 2.3 **update(批量添加)**

Note: v2 可以是 **list**，**tuple**

```python
v1 = {1, 2, 3, 4, 5}
v2 = {1, 2, 6, 7, 8}
v1.update(v2)
print(v1)
```

### 2.4  clear

### 2.5 pop



### 2.6 集合操作（生成新值 4）

```python
# 生成新值，并不改变原有集合
# 交集
v = {1, 2, 3, 4, 'echo'}
v1 = {1, 'echo'}
v2 = v.intersection(v1)
print(v2)

# 并集
result = v.union(v1)
print(result)

# 差集
result = v.difference(v1) # v有，v1 没有
print(result)

# 对称差集
result = v.symmetric_difference(v1) 
print(result)
```





## 3. 公共功能（3，del无效）

### 3.1 len

```python
v = {1, 2, 3, 4, 'echo'}
len(v)
```

### 3.2 for循环

```python
v = {1, 2, 3, 4, 'echo'}
for i in v:
	print(i)
```

### 3.3 嵌套问题

1. list/ditc/set 不可以嵌套进集合，也不能作为dict的key（必须可hash）
2. hash（dict 的key 和 set()）
   - dict 和 set() 查找会非常快
   - 可用于大量数据的快速查
3. True 和 1 在set中认为是重复的（False一样）

```python
# set 认为True = 1，然后进行hash运算
v = {1, 2, 3, 4, True, 'echo'}
print(v)

# dict的key进行hash运算，认为True = 1，然后进行hash运算
v = {1: 2, '3': 'a', True: 'echo'}
print(v)   # 会输出{1: 'echo', '3': 'a'}
```



## 4. 内存（2）

###4.1 嵌套的应用

```python
# 示例一
# v1， v2 不是同一内存地址
v1 = [11, 22, 33, 44]
v2 = [11, 22, 33, 44]

v1 = 666
v2 = 666

v1 ='adsdf'
v2 ='adsdf'
# python 解释器会回收垃圾数据
# 按理v1 ， v2 应该是不同的，py中有缓存机制
	1. -5 -256  会缓存
  2. 字符串：非字母下滑线，或 * n（n != 1）,会重新开辟内存
  3. 只有str，int缓存
```

```python
# 示例二
# 第一个值会成为垃圾数据，会有两个地址
v1 = [11, 22, 33, 44]
v1 = [11, 22, 33]  # 赋值会重新开辟内存
```

```python
# 示例三
# v1 内部修改
v1 = [11, 22, 33, 44]
v2 = v1   # v2，v1 会指向同一地址

v1.append('666')
print(v2)    # v2 也会发生改变
# v1 重新赋值
v1 = [11, 22, 33, 44]
v2 = v1   
v1 = [1, 2, 3, 4]
print(v2)    # [11, 22, 33, 44]
```

```python
# 示例四
v = [1, 2, 3]
values = [11, 22, v]

# 
v.append(9)
print(values) # [1, 2, 3,[1, 2, 3, 9]]

#
values[2].append(999)
print(v) # [1, 2, 3, 999]

#
v = 999
print(values) # [11, 22, [1, 2, 3]]

#
values[2] = 666
print(v) # [1, 2, 3]
```

```python
# 示例五
v1 = [1, 2]
v2 = [2, 3]
v3 = [11, 22, v1, v2, v1]   # v1,v2 是内存地址
```

### 4.2 查看内存地址

1. id(v1)  # 查看v1内存地址
2. 小数据池(2)
   - -5 - 256  
   - 单个字符串，乘法结果 < 20
3. 问题： == 和 is 区别
   - == 比较的是**值**
   - is 比较的是**内存地址**