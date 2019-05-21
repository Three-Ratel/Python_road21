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

## 10.2 表的介绍

### 1. 表存储

#### 1.1 表的存储方式(3)

1. 方式1：**MyISAM** mysql5.5- 默认存储方式
   - 存储的文件个数：表结构、表中数据、索引
   - 不支持行级锁、事务和外键
2. 方式2：**InnoDB** mysql5.6+ 默认存储方式
   - 存储文件个数：表结构、表中数据
   - 支持**行级锁**(默认)：脏数据（+表级锁），支持数据并发
   - 支持**事务**：把多句操作，变成原子操作
   - 支持**外键**：通过外键(**有约束**)在其他表(**有约束**)中查找信息
3. 方式3：**MEMORY**
   - 存储文件个数：**表结构**
   - **优势**：增删改查速度快
   - **劣势**：重启数据消失、容量有限
4. **存储引擎介绍**

- **InnoDB**
  - 用于事务处理应用程序，支持**外键**和**行级锁**。如果应用对事物的完整性有比较高的要求，在并发条件下要求数据的一致性，数据操作除了插入和查询之外，还包括很多更新和删除操作，那么InnoDB存储引擎是比较合适的。InnoDB除了有效的降低由删除和更新导致的锁定，还可以确保事务的完整提交和回滚，对于类似**计费系统**或者**财务系统**等对数据准确要求性比较高的系统都是合适的选择。
- **MyISAM**
  - 如果应用是以**读操作**和**插入操作**为主，只有很少的更新和删除操作，并且对事务的完整性、并发性要求不高，那么可以选择这个存储引擎。
- **Memory**
  - 将所有的数据保存在**内存**中，在需要快速定位记录和其他类似数据的环境下，可以提供极快的访问。Memory的**缺陷是对表的大小有限制**，虽然数据库因为异常终止的话数据可以正常恢复，但是一旦数据库关闭，存储在内存中的数据都会丢失。

#### 1.2 查看mysql所有的配置

```mysql
# 查看与存储引擎相关配置
show variables like '%engine%';
show variables like "default_storage_engine";
# 查看当前数据库支持的存储引擎
show engines \G;
# 修改已经存在表的存储引擎
alter table 表名 engine = innodb;
# 查看与编码相关的配置
show variables like '%chara%';
# 查看
show variables like '%关键字%';
```

- 指定存储引擎

```mysql
# 创建表
create table t1(id int, name char(10)) engine=innodb;
# 查看表的结构，包括存储引擎和编码 \G 格式化输出，带	\G 不能使用分号
show create table t1 \G
# 只查看表字段基础信息
describle t1;

t1.frm frame 表结构
t1.ibd innoDB 存储引擎
```

```mysql
# 指定engine为myisam
create table t2(id int, name char(10)) engine=MyISAM;

t2.frm 表结构
t2.MYD 数据
t2.MYI 索引
```

```mysql
# 指定engine为memory
create table t2(id int, name char(10)) engine=memory;

t2.MYD 数据
```

### 2. mysql数据类型

```mysql
# 语法：
create table 表名(
字段名1 类型[(宽度) 约束条件],
字段名2 类型[(宽度) 约束条件],
字段名3 类型[(宽度) 约束条件]);

# 注意：
1. 在同一张表中，字段名是不能相同
2. 宽度和约束条件可选
3. 字段名和类型是必须的
```

- 数值：
  - TINYINT(1byte)，SMALLINT(2byte)，MEDIUMINT(4byte)，**INT**(4byte)，BIGINT(8byte)
- 日期时间
- 字符
- **ENUM**和**SET**类型

#### 2.1数字

- 整数(int)

```mysql
# 创建无符号int型表
create table t3(id1 int, id2 int unsigned);
```

- 小数(float/double)

```mysql
# 一共有5位，小数2位
float(5, 2)/ double(5, 2)
# 创建表
create tables t4(f1 float(5,2), double(5,2));
# 不指定长度，单精度和双精度
create tables t4(f1 float, double);
# decimal精度,默认存储（10，0）整数
create tables t5(d1 decimal, d2 decimal(25, 20));
# decimal内部存储是按照字符串存的
```

#### Note1(3)

1. 默认int类型有符号
2. int类型数据范围不被**宽度**约束
3. 5.5版只能约束数字的显示宽度，5.6不受限制
4. 5.6版插入数据超过最大长度会默认显示最大值，5.7版直接会提示：Out of range value

#### 2.2 时间和日期

- data：年月日
- time：时分秒
- year：年份值
- datetime：年月日时分秒
- timestamp：年月日时分秒
  - 1970-01-01 00:00:00/2038结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07

```mysql
# 创建表
create table t6(d1 date, y year, ts timestamp);
insert into t6(now(), now(), now());
# 指定传y,datetime默认为更新时间
insert into t6(y) values(2019);
# 指定datetime更新方式
create table t6(d1 date, y year, 
                dt datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
# 可以使用字符串，纯数字
# 5.7版本，插入参数不全，会报错，5.6版不会
```

#### 2.3 字符串

- char：定长字符串
  - 补齐指定长度的
  - 长度变化小的情况使用、浪费空间，存储效率较高
  - 用户名、密码、身份证、手机号
- varchar：变长字符串
  - 存储输入长度的+1 eg.alex    则存储alex4
  - 节省空间、存储效率s相对低
  - 评论、微博、说说、微信状态

```mysql
create table t7(name1 char(5), name2 varchar(5));
# 分别存储 'echo ' 和 'echo4'
insert into t7 values('echo', 'echo')
select concat(name1, '---') from t7;
select concat(name2, '---') from t7;
```

#### 2.4 enum和set类型

- en ENUM('male', 'female')：单选框
- s set('')：多选框
- 5.6版本取交集，5.7版本必须完全一样，不然会报错

```mysql
create table t8(name char(12), 
                gender ENUM('male', 'female'),
               hobby set('play', 'drink', 'eat')s
               );
```

### 3. mysql工作流程

![sql工作流程](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/sql%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B.png)

- MySQL架构总**共四层**，在上图中以虚线作为划分。 
  1. 最上层的服务并不是MySQL独有的，大多数给予网络的客户端/服务器的工具或者服务都有类似的架构。比如：连接处理、授权认证、安全等。 
  2. 第二层的架构包括大多数的MySQL的核心服务。包括：查询解析、分析、优化、缓存以及所有的内置函数（例如：日期、时间、数学和加密函数）。同时，所有的跨存储引擎的功能都在这一层实现：存储过程、触发器、视图等。
  3. 第三层包含了存储引擎。存储引擎负责MySQL中数据的存储和提取。服务器通过API和存储引擎进行通信。这些接口屏蔽了不同存储引擎之间的差异，使得这些差异对上层的查询过程透明化。存储引擎API包含十几个底层函数，用于执行“开始一个事务”等操作。但存储引擎一般不会去解析SQL（InnoDB会解析外键定义，因为其本身没有实现该功能），不同存储引擎之间也不会相互通信，而只是简单的响应上层的服务器请求。
  4. 第四层包含了文件系统，所有的表结构和数据以及用户操作的日志最终还是以文件的形式存储在硬盘上



















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
47. print和文件的读写都是io操作
48. 使用线程可以有效规避io操作时间，提高程序的效率
49. 解耦程序、默认参数是list