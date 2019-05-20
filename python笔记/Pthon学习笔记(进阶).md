# 第十章 数据库

## 10.1 数据库

### 1. 概念

1. 用户认证
   - 注册：用户名不能重复
   - 登陆
2. 只是通过文件操作，改变数据是非常繁琐的
3. 解决对于多台机器或多个进程操作同一份数据我们需要自己解决并发和安全问题比较麻烦
4. 自己处理数据备份，容错措施
5. c/s架构的操作数据文件的一个**管理软件**
   - 解决并发问题
   - 实现用更简单快速的方式完成数据的增删改查
   - 提供一些容错、高可用的机制
   - 权限的认证
6. 数据操作
   1. 连接server
   2. 指令
7. 专有名词
   1. 数据库管理系统(DBMS)：专门用来管理数据文件，帮助用户更简洁的操作数据的软件
   2. 数据(data)、文件
   3. 数据库(database, DB)：每一个项目都有一个数据库
   4. 数据库管理员(DBA)
8. 常见的数据库
   - 关系型数据库
     1. sql server/sqllite
     2. oracle：收费，比较严谨，安全性高（国企、事业单位银行、金融行业）
     3. mysql：开源（小公司互联网公司）
   - 非关系型数据库(key:value结构)eg：快递单号（redis、mongodb）

### 2. mysql的安装

1. 路径必须是全英文
2. bin目录
3. my.ini文件（文件名必须是这个）

```python
# 客户端
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8 

# server端
[mysqld]
#设置3306端口
port = 3306 
# 设置mysql的安装目录
basedir=C:\Program Files\mysql-5.6.39-winx64 
# 设置mysql数据库的数据的存放目录
datadir=C:\Program Files\mysql-5.6.39-winx64\data 
# 允许最大连接数
max_connections=200
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
```

1. 安装路径：不能有空格，不能有中文，不能带着转义特殊字符开头的文件夹名
2. 安装之后发现配置有问题：再修改配置文件往往不能生效
   - 卸载之后重装
   - mysqld remove，把所有配置、PATH修改正确
   - 重启计算机—清空注册表
   - 重新安装：mysqld install

### 3. mysql的cs架构

```mysql
# windows
mysqld install
net start mysql
server net stop mysql
mysql -u'用户名' -p'密码'
# 客户端，可以是python代码也可以是一个程序
# mysql.exe是一个客户端
```

#### 3.1 mysql中的用户和权限

- 在安装数据库之后，有一个最高权限的用户root
- mysql server端的ip 用户名/密码
- Mysql -h192.168.12.87 -uroot -p123

**Note**：可以连接网络上的某一个数据库

#### 3.2 数据库中的概念

- 库、表、数据
  - 一条数据data(一行数据)
  - 多条数据组成一个表
  - 多个表组成一个库
  - 一般情况下：一个项目占用一个或以上个库

#### 3.3 mysql的操作

- sql语句(structure query language)
  1. DDL语句 数据库定义语言：数据库，表，视图，索引，存储规程
  2. DML语句 数据库操纵语言：插入数据insert，delete，update，alter
  3. DCL语句 数据库控制语言：创建用户。grant    revoke 取消授权

```mysql
# 查看当前用户
select user(); 
# 设置密码，password 表示密文存储
set password = password('123');
# 创建用户
create user '用户名'@'网段.%' identified by '密码';
# 查看当前库
show databases;
# 创建文件夹henry
create databases henry；
# 查看指定用户权限
show grants for '用户名'@'网段.%';
# 授权 * 表示所有
grant	all(select/insert) on henry.* to '用户名'@'ip网段.%';
# 设置立即生效
flush privileges
# 创建账号并授权
grant all on herny.* to 'henry'@'%' identified by '123';
```

- 库的操作

```mysql
# 创建库
create database demo;
# 查看库
show databases;
# 删除库，demo
drop database demo
# 查看当前使用的库
select database();
# 切换库，到demo库下
use demo；
```

- **表操作(4)**

```mysql
# 创建表,char()默认一个字符
create table student(id int, name char(10));
# 查看当前文件夹中的表
show tables;
# 删除表
drop table student;
# 查看表结构
desc student;
```

- **操作表中数据(4)**

```mysql
# 数据插入
insert into student values(1, 'henry');
# 数据查看
select * from student;
# 修改数据，必须设置条件，确定为一条数据data
update 表 set 字段名=值 where id=2;
# 删除数据
delete from 表 where id=1；
```

















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
   
   
   
8. [][Errno 9]OSError: [Errno 9] Bad file descriptor

   - 因为关闭了套接字对象后，又再次去调用了套接字对象。

9. BrokenPipeError:[Errno 32] Broken pipe

  - 由于客户端请求的链接，在一次循环之后，产生的套接字关闭，没有新的客户端套接字进行请求连接，所以产生broken pipe错误

10. BlockingIOError: [Errno 35] Resource temporarily unavailable

  - 非阻塞模型中，接收不到client端发来的数据，此时会报错
  - client端会出现 ConnectionResetError: [Errno 54] Connection reset by peer的报错

11. [Errno 41] Protocol wrong type for socket

12. ConnectionResetError: [Errno 54] Connection reset by peer

   - tcp连接一旦断开，发送数据会报错
   - 发送空字符不会报错

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