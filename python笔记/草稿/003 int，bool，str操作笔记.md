

# 今日安排

1. 整型 int
2. 字符串 str（30）
3. 布尔 bool

# Review：

1. 思维导图
   - xmind
   - processon 网站（在线）

# 补充（2）

1. 运算符补充

   - in 

   ```python
   value = '我是中国人'
   # '中国'是否是value代指的子序列
   v1 = '中国' in value
   
   # 示例
   content = input('请输入内容：')
   if '退钱' in content:
     print('包含敏感字符')
   # 示例
   while True:
   			content = input('请输入内容：')
   				if '退钱' in content:
    						print('包含敏感字符')
           else:
             	print(content)
               break
   ```

   -  not in

2. 优先级

   算术运算 > 逻辑判断

# 作业

```python
"""
"""
放在文件头时，是对整个文件的注释
```

## pycharm 设置头文件

![设置头文件](/Users/henry/Documents/截图/Py截图/设置头文件.png)

# 内容详情

## 1.整型（int/integer）

```python
age = 18
```

py区别三：

**Py2 有int 和 long，py3只有int**

- py2 

  - int(eg. 9 / 2 = 4 )
    - 在32bit机器上，-2\*\*31 ～ -2\*\*31-1
    - 在64bit机器上，-2\*\*63 ～ -2\*\*63-1
    - 超出范围，py自动将其转换到long（长整型）

  ```python
  # 解决除法只取整数的问题
  from __future__ import division
  v = 9 / 2
  print(v)
  ```

- py3

  - int几乎没有限制，此时没有long型

## 2.布尔值（bool/boolen）

- 只有两个值True / False
- 转换
  - 数字转：只有 0 是False
  - 字符串转：只有""是False

## 3.字符串（str/string）

Note：所有操作**都**不改变原来字符串值

1. s.upper() :都变成大写

```python
value = 'henry'
new_value = value.upper()
print(new_value)
```

- s.lower(): 都变成小写

```python
示例：
check_code = 'iyUF'
meg = input('please enter code %s: ' % (check_code,))
# meg = meg.upper()
# check_code = check_code.upper()
if meg.upper() == check_code.upper():
    print('success')

```

2. s.isdigit() ：判断是否为数字(T or F)

```python
s = '12.3'
print(s.isdigit())
```

3. s.rstrip()：去除右边空格
   - s.lstrip()：去除左边空格
   - s.strip()：去除两边空格

```python
s = '  henry  '
print('-->', s.strip(), '<--')
```

4. s.replace(a, b, i)：把前 i a 替换成 b 。

```python
message = input('please input words: ')
data = message.replace('presidnet','**')
print(data)
```

5. s.split('a', i) ：用 a 进行切割，前i个a

   - **切割元素会被删除**

   - **s.rsplit('a', i) ：右边前i个a切割**
   - s.lsplit('a', i) ：左边前i个a切割

```python
message = input('please input words: ')
data = message.split('a')
print(data)
```

```python
ord()：转换为ASCII

chr()：把ASCII转换为字符
```





##4.数据的处理

1. 计算字符长度：len(a）
2. **索引取值text[index]**
   - text[-1]：负值---反向取值

```python
# 索引取值示例
# 让用户任意输入字符串，获取字符串后计算其中有多少个数字
# string index： 0 ~ len(s)-1
text = input('please input your text: ')
index_len = len(text)
index = 0
count = 0
while True:
    if text[index].isdigit():
        count += 1
    index += 1
    if index == index_len:
        break
print(count)
```

3. 切片( 0 开始)

```python
# 切片示例1
text = 'henry'
text1 = text[2:4]
print(text1)
text2 = text[2:]	# 表示取到最后
print(text2)
text3 = text[:-1] #表示最前取到-1之前
print(text3)
```

```python
# 切片示例2
# 取最后两个
data = input('please input your text: ')
v1 = data[-2:]
v2 = data[len(data)-2:]
print(v1, v2)9
```



## 5.码云的使用

1. 创建组织
2. 邀请成员：url
3. 确认加入组织
4. 创建自己的仓库
5. 公开，不选择使用readme.md 文件初始化仓库

- 上传：
  - 指定文件夹
  - 进入目录
  - git init #初始化
  - git config —global user.name "henry"
  - git config —global user.email "958976577@qq.com"
  - git remote add henry 仓库的url
  - git add .
  - git commit -m '提示语'
  - git push henry master
- 其他git命令
  - git status