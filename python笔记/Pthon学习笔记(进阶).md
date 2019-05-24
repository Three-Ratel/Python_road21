# 第十章 数据库mysql

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
     
     - Relational Database Management System：(RDBMS)是指包括**相互联系的逻辑组织**和**存取这些数据的一套程序** (数据库管理系统软件)。关系数据库管理系统就是管理关系数据库，并将数据逻辑组织的系统。
     
     1. sql server/ sqllite/ db2/ access/ 
     2. oracle：收费，比较严谨，安全性高（国企、事业单位银行、金融行业）
     3. mysql：开源（小公司互联网公司）
     4. 注意：sql语句通用
     
   - 非关系型数据库(key:value结构)eg：快递单号（redis、mongodb、mongodb，redis、memcache）
   
   - 在 WEB 应用方面，MySQL是最好的 **RDBMS**(Relational Database Management System，关系数据库管理系统) 应用软件。

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
#  server net stop mysql
mysql -u'用户名' -p'密码'
# 客户端，可以是python代码也可以是一个程序
# mysql.exe是一个客户端
```

```mysql
# mac
sudo mysql.server status
sudo mysql.server start/stop/restart
```

#### 3.1 mysql中的用户和权限

- 在安装数据库之后，有一个最高权限的用户root
- mysql server端的ip 用户名/密码
- Mysql -h192.168.12.87 -uroot -p123

**Note**：可以连接网络上的某一个数据库

#### 3.2 数据库中的概念

- 库、表、数据
  - **描述事物的符号记录称为数据**，如：一条数据data(一行数据)
  - **表就相当于文件，表中的一条记录就相当于文件的一行内容**，多条数据组成一个表
  - **数据库即存放数据的仓库**，多个表组成一个库
  - 一般情况下：一个项目占用一个或以上个库

#### 3.3 mysql的操作

- sql语句(structure query language)
  
  - SQL : 结构化查询语言(**Structured Query Language)**简称SQL(发音：/ˈes kjuː ˈel/ "S-Q-L")，是一种特殊目的的编程语言，是一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统
  - SQL语言主要用于存取数据、查询数据、更新数据和管理关系数据库系统,SQL语言由IBM开发。**SQL语言分为3种类型**：
  
  1. **DDL**语句 数据库定义语言：数据库，表，视图，索引，存储规程
  2. **DML**语句 数据库操纵语言：插入数据insert，delete，update，alter
  3. **DCL**语句 数据库控制语言：创建用户。grant    revoke 取消授权

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
show grants for '用户名'(@'网段.%');
# 授权 * 表示所有
grant	all(select/insert) on henry.* to '用户名'@'ip网段.%';
# 设置立即生效
flush privileges
# 创建账号并授权,必须有密码
grant all on herny.* to 'henry'@'%' identified by '123';
#select, insert, update, delete, create, drop, index, alter, grant, references, reload, shutdown, process, file等14个权限

# 取消用户权限
revoke all on test.* from 'henry'@'%';
# 删除用户
delete from mysql.user where host='192.168.12.%' and user='test';
drop user 'test'@'192.168.12
# 修改指定用户密码
update mysql.user set password=password('新密码') where User='test' and Host='%';
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
# 删除多个表
drop tables s2,s3,s4;
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

### 1. 存储引擎

- 选择**如何存储和检索**你的数据的这种**灵活性**是MySQL为什么如此受欢迎的主要原因。其它数据库系统(包括大多数商业选择)仅支持一种类型的数据存储。
- mysql5.6/5.7支持的存储引擎包括**InnoDB**、 **MyISAM**、 **MEMORY**、 **CSV**、 **BLACKHOLE**、 **FEDERATED**、 **MRG_MYISAM**、 **ARCHIVE**、 **PERFORMANCE_SCHEMA**。其中**NDB**和**InnoDB**提供**事务安全表**，其他存储引擎都是非事务安全表。

#### 1.1 表的存储方式(3)

1. 方式1：**MyISAM** mysql5.5- 默认存储方式
   - 存储的文件个数：**表结构**、**表数据**、**索引**
   - **不支持**行级锁、事务和外键
2. 方式2：**InnoDB** mysql5.6+ 默认存储方式
   - 存储文件个数：**表结构**、**表数据**
   - 支持**行级锁**(默认)：脏数据（+表级锁），支持数据并发
   - 支持**事务**：把多句操作，变成原子操作
   - 支持**外键**：通过外键(**有约束**)在其他表(**有约束**)中查找信息
3. 方式3：**MEMORY**
   - 存储在内存：**表结构**， 表数据存储到硬盘上
   - **优势**：增删改查速度快
   - **劣势**：重启数据消失、容量有限

#### 1.2 存储引擎介绍

- **InnoDB**
  - 用于事务处理应用程序，支持**外键**和**行级锁**。如果应用对事物的完整性有比较高的要求，在并发条件下要求数据的一致性，数据操作除了插入和查询之外，还包括很多更新和删除操作，那么InnoDB存储引擎是比较合适的。InnoDB除了有效的降低由删除和更新导致的锁定，还可以确保事务的完整提交和回滚，对于类似**计费系统**或者**财务系统**等对数据准确要求性比较高的系统都是合适的选择。
- **MyISAM**
  - 如果应用是以**读操作**和**插入操作**为主，只有很少的更新和删除操作，并且对事务的完整性、并发性要求不高，那么可以选择这个存储引擎。
- **Memory**
  - 将所有的数据保存在**内存**中，在需要快速定位记录和其他类似数据的环境下，可以提供极快的访问。Memory的**缺陷是对表的大小有限制**，虽然数据库因为异常终止的话数据可以正常恢复，但是一旦数据库关闭，存储在内存中的数据都会丢失。

**其他存储引擎**

1. InnoDB
   - MySql 5.6 版本默认的存储引擎。InnoDB 是一个事务安全的存储引擎，它具备提交、回滚以及崩溃恢复的功能以保护用户数据。InnoDB 的行级别锁定以及 Oracle 风格的一致性无锁读提升了它的多用户并发数以及性能。InnoDB 将用户数据存储在聚集索引中以减少基于主键的普通查询所带来的 I/O 开销。为了保证数据的完整性，InnoDB 还支持外键约束。
2. MyISAM
   - MyISAM既不支持事务、也不支持外键、其优势是访问速度快，但是表级别的锁定限制了它在读写负载方面的性能，因此它经常应用于只读或者以读为主的数据场景。
3. Memory
   - 在内存中存储所有数据，应用于对非关键数据由快速查找的场景。Memory类型的表访问数据非常快，因为它的数据是存放在内存中的，并且默认使用HASH索引，但是一旦服务关闭，表中的数据就会丢失
4. BLACKHOLE
   - 黑洞存储引擎，类似于 Unix 的 /dev/null，Archive 只接收但却并不保存数据。对这种引擎的表的查询常常返回一个空集。这种表可以应用于 DML 语句需要发送到从服务器，但主服务器并不会保留这种数据的备份的主从配置中。
5. CSV
   - 它的表真的是以逗号分隔的文本文件。CSV 表允许你以 CSV 格式导入导出数据，以相同的读和写的格式和脚本和应用交互数据。由于 CSV 表没有索引，你最好是在普通操作中将数据放在 InnoDB 表里，只有在导入或导出阶段使用一下 CSV 表。
6. NDB
   - (又名 NDBCLUSTER)——这种集群数据引擎尤其适合于需要最高程度的正常运行时间和可用性的应用。注意：NDB 存储引擎在标准 MySql 5.6 版本里并不被支持。目前能够支持
   - MySql 集群的版本有：基于 MySql 5.1 的 MySQL Cluster NDB 7.1；基于 MySql 5.5 的 MySQL Cluster NDB 7.2；基于 MySql 5.6 的 MySQL Cluster NDB 7.3。同样基于 MySql 5.6 的 MySQL Cluster NDB 7.4 目前正处于研发阶段。
7. Merge
   - 允许 MySql DBA 或开发者将一系列相同的 MyISAM 表进行分组，并把它们作为一个对象进行引用。适用于超大规模数据场景，如数据仓库。
8. Federated
   - 提供了从多个物理机上联接不同的 MySql 服务器来创建一个逻辑数据库的能力。适用于分布式或者数据市场的场景。
9. Example
   - 这种存储引擎用以保存阐明如何开始写新的存储引擎的 MySql 源码的例子。它主要针对于有兴趣的开发人员。这种存储引擎就是一个啥事也不做的 "存根"。你可以使用这种引擎创建表，但是你无法向其保存任何数据，也无法从它们检索任何索引。

#### 1.3 查看mysql所有的配置

```mysql
# 查看与存储引擎相关配置
show variables like '%engine%';
show variables like "default_storage_engine";
# 查看当前数据库支持的存储引擎
show engines \g
show engines;
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

#### 2.1数值

1. MySQL支持所有标准SQL数值数据类型。这些类型包括严格数值数据类型(**INTEGER**、 **SMALLINT**、 **DECIMAL**和**NUMERIC**)，以及近似数值数据类型(**FLOAT**、 **REAL**和**DOUBLE PRECISION**)。
2. 关键字INT是INTEGER的同义词，关键字DEC是DECIMAL的同义词。
3. MySQL支持的整数类型有TINYINT、MEDIUMINT和BIGINT。下面的表显示了需要的每个整数类型的存储和范围。
4. 对于小数的表示，MYSQL分为**两种方式**：**浮点数和定点数**。浮点数包括float(单精度)和double(双精度),而**定点数**只有**decimal**一种，在mysql中**以字符串的形式存放**，比浮点数更精确，适合用来表示货币等精度高的数据。
5. BIT数据类型保存位字段值，并且支持MyISAM、MEMORY、InnoDB和BDB表。

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

#### 2.2 时间和日期(5)

1. **data**：年月日
2. **time**：时分秒
3. **year**：年份值
4. **datetime**：年月日时分秒
5. **timestamp**：年月日时分秒
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

1. 字符串类型指**CHAR**、**VARCHAR**、BINARY、VARBINARY、BLOB、TEXT、**ENUM**和**SET**。该节描述了这些类型如何工作以及如何在查询中使用这些类型。
2. BINARY 和 VARBINARY 类似于 CHAR 和 VARCHAR，不同的是它们包含二进制字符串而不要非二进制字符串。也就是说，它们包含字节字符串而不是字符字符串。这说明它们没有字符集，并且排序和比较基于列值字节的数值值。
3. BLOB 是一个二进制大对象，可以容纳可变数量的数据。有 4 种 BLOB 类型：TINYBLOB、BLOB、MEDIUMBLOB 和 LONGBLOB。它们区别在于可容纳存储范围不同。
4. 有 4 种 TEXT 类型：TINYTEXT、TEXT、MEDIUMTEXT 和 LONGTEXT。对应的这 4 种 BLOB 类型，可存储的最大长度不同，可根据实际情况选择。

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

1. ENUM中文名称叫枚举类型，它的值范围需要在创建表时通过枚举方式显示。ENUM**只允许从值集合中选取单个值，而不能一次取多个值**。
2. SET和ENUM非常相似，也是一个**字符串对象**，里面可以包含0-64个成员。根据成员的不同，存储上也有所不同。set类型可以**允许值集合中任意选择1或多个元素进行组合**。对超出范围的内容将不允许注入，而对重复的值将进行自动去重。

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
  3. 第三层包含了**存储引擎**。**存储引擎负责MySQL中数据的存储和提取**。服务器通过API和存储引擎进行通信。这些接口屏蔽了不同存储引擎之间的差异，使得这些差异对上层的查询过程透明化。存储引擎API包含十几个底层函数，用于执行“开始一个事务”等操作。但存储引擎一般不会去解析SQL（InnoDB会解析外键定义，因为其本身没有实现该功能），不同存储引擎之间也不会相互通信，而只是简单的响应上层的服务器请求。
  4. 第四层包含了**文件系统**，所有的表结构和数据以及用户操作的日志最终还是以文件的形式存储在硬盘上

## 10.3 表的完整性约束

### 1. 约束

-  unsigned：设置无符号

1.  **NOT NULL** ：非空约束，指定某列不能为空； 
2.  **UNIQUE** : 唯一约束，指定某列或者几列组合不能重
3.  **PRIMARY KEY** ：主键，指定该列的值可以唯一地标识该列记
4.  **FOREIGN KEY** ：外键，指定该行记录从属于主表中的一条记录，主要用于参照完整性

#### 1.1 not null

- 非空

```mysql
create table t1(id int not null,
               name char(12) not null,
               age int
               );
insert into t1(id, name) values(1, 'henry');
```

#### 1.2 default

- 默认值，创建列时可以指定默认值，当插入数据时如果未主动设置，则自动添加默认值

```mysql
create table t2(id int not null,
               name char(12) not null,
               gender enum('male', 'female') not null default 'male'
               );       
insert into t2(id, name) values(1, 'henry');
```

#### 1.3 unique

- 不重复(**key UNI**)，所有的非空数据不重复
- 唯一约束，指定某列或者几列组合不能重复

```mysql
create table t3(id int unique,
               username char(12) not null unique,
               pwd char(18)
               );
```

- **联合唯一**(**key MUL**)

```mysql
create table t4(id int not null unique,
               ip char(15),
               server char(10),
               port int,
               unique(ip, port))  # 联合唯一,不能同时重复
```

#### 1.4 auto_increment

- 自增(只能用于数值)，**自带非空属性**
- 设置自增字段必须是数字且唯一 **unique +  auto_increment**
- 约束字段为自动增长，被约束的字段必须同时被key约束

```mysql
create table t5(id int unique auto_increment,
               username char(10),
               pwd char(18));

insert into t5(username, pwd) values('henry', '123');
# 自增大小只增不减
# 对于自增的字段，在用delete删除后，再插入值，该字段仍按照删除前的位置继续增长
```

- 应该用**truncate清空表**，比起delete一条一条地删除记录，truncate是直接清空表，在删除大表时用它 mysql> truncate student;

```mysql
# 也可以创建表时指定auto_increment的初始值，注意初始值的设置为表选项，应该放到括号外
create table student(id int primary key auto_increment,
                     name varchar(20),
                     gender enum('male','female') default 'male'
                    )auto_increment=3;
```

- **mysql自增步长**

```mysql
#设置步长
# sqlserver：自增步长
# 基于表级别,指定步为2，从0开始计数
create table t1（id int unique auto_increment, age int
    ）engine=innodb,auto_increment=2 default charset=utf8;
# mysql自增的步长：
show session variables like 'auto_inc%'; 
# 基于会话级别
set session auto_increment_increment=2;# 修改会话级别的步长
# 基于全局级别的
set global auto_increment_increment=2; # 修改全局级别的步长（所有会话都生效）
# 查看设置，重新登陆有效,5.7版本直接失效
show variables like 'auto_incre%'; 
```

- If the value of **auto_increment_offset(起始偏移量)** is greater than that of **auto_increment_increment(步长)**, the value of auto_increment_offset is ignored. 
- **比如**：设置auto_increment_offset=3，auto_increment_increment=2

#### 1.5 primary key

- 一张表**只能**设置**一个主键,innodb**表中最好设置一个主键
- 主键约束这个字段，非空且唯一即：**not null unique**

```mysql
create table t6(id int not null unique,
               name char(10) not null unique);
# 第一个指定为not null nuique 字段被定义为主键
```

```mysql
create table t7(id int primary key,
               name char(10) not null unique);
```

- 联合主键

```mysql
create table t8(id int,
               ip char(15),
               server char(10),
               port int,
               primary(ip, port))  # 联合主键
```

#### Note(4)

1. 主键为了保证表中的每一条数据的**该字段**都是表格中的**唯一值**。换言之，它是用来独一无二地确认一个表格中的每一行数据。 
2. 主键可以包含**一个**字段或**多个字段**。当主键包含多个栏位时，称为**组合键** (Composite Key),也可以叫**联合主键**。
3. **主键**可以在建新表格时设定 (运用 CREATE TABLE 语句)，或是以改变现有的表格架构方式设定 (运用 ALTER TABLE)。
4. **主键必须唯一**，主键值**非空**；可以是单一字段，也可以是多字段组合。

#### 1.6 foreign key

- 外键，涉及到两张表
- 关联的数据类型必须一致
- 被关联的表**必须唯一**，mysql最好关联主键
- 先创建**外表**，再创建**关联表**

```mysql
create table staff(id int primary key auto_increment,
                   age int,
                   gender enum('male', 'female'),
                   salary float(10,2),
                   hire_date date,
                   post_id int,
                   foreign key(post_id) references dept(pid);
                   
create table dept(pid int primary key, name char(10) not null nuique);
```

- 级联删除和更新
- foreign key(post_id) references dept(pid) **on update cascade on delete cascade**

```mysql
create table staff(id int primary key auto_increment,
                   age int,
                   gender enum('male', 'female'),
                   salary float(10,2),
                   hire_date date,
                   post_id int,
                   foreign key(post_id) references dept(pid) 
                   on update cascade 
                   on delete set null);
                   
create table dept(pid int primary key, name char(10) not null nuique);
```

### 2. 修改表结构

- 创建项目之前
- 项目开发、运行过程中

#### 2.1 修改表名

```mysql
# 修改表名
alter table 表名 rename 新表名;
```

#### 2.2 增加/删除字段

```mysql
# 添加字段
alter table 表名 add 添加字段名 数据类型(宽度)  约束
# 删除字段
alter table 表名 drop 删除字段名;
```

#### 2.3 修改字段

```mysql
# 修改已经存在字段的类型、宽度 约束，不能修改字段名字
alter table 表名 modify 字段名 类型() 约束
# 修改已经存在字段的类型、宽度 约束、字段名字
alter table 表名 change 字段名 新字段名 类型() 约束
```

#### 2.4 修改字段顺序

```mysql
# 把字段放在第一列
alter table 表名 modify age 类型+约束 first；
# 把字段放在id之后
alter table 表名 modify age int not null after id；
# 也可以与 add、change 连用
```

#### 2.5 修改字段约束

```mysql
#去掉null约束
alter table t modify name char(10) null;
# 添加null约束
alter table t modify name char(10) not null;
```

```mysql
# 去掉unique约束,特殊
alter table 表名 drop index 字段名;
# 添加unique约束
alter table 表名 modify 字段名 int unique;
```

#### 2.6 修改库的默认编码

```mysql
alter database 库名 CHARACTER SET utf8;
```

#### 2.7 操作主键add/drop

```mysql
# 先删除主键，删除一个自增主键会报错
# 需要先去掉主键的自增约束，然后再删除主键约束
alter table 表名 drop primary key;
# 增加主键
alter table 表名 add primary key(id);
```

#### 2.8 操作外键add/drop

```mysql
# 添加外键
alter table 表名 add constraint 外键名 foreign key(字段) references press(字段);
# 删除外键
alter table 表名 drop foreign key 外键名;
```

#### 2.9 删除表

```mysql
drop table 表名；
```

### 3. 操作数据

两张表的数据关系：多对一、一对一、多对多(书、作者)

#### 3.1 多对一

- 永远在多的表中设置外键
- **例如**：一对多（或多对一）：一个出版社可以出版多本书

```mysql
create table press(id int primary key auto_increment,
                   name varchar(20));

create table book(id int primary key auto_increment,
                  name varchar(20),
                  press_id int not null,
                  foreign key(press_id) references press(id)
                  on delete cascade
                  on update cascade);

insert into press(name) values('henry publisher'),
('echo publisher'),('dean publisher');

insert into book(name,press_id) values('henry',1),('echo',2),
('dean',2),('brad',3),('dianel',2),('oleg',3);
```

#### 3.2 一对一

- 外键+unique   
- **后出现**的表中字段作为**外键**

```mysql
# 两张表：学生表和客户表
create table customer(id int primary key auto_increment,
                      name varchar(20) not null,
                      qq varchar(10) not null,
                      phone char(16) not null);

create table student(id int primary key auto_increment,
                     class_name varchar(20) not null,
                     customer_id int unique, #该字段一定要是唯一的
                     foreign key(customer_id) references customer(id) 
                     on delete cascade
                     on update cascade);
# 增加客户
insert into customer(name,qq,phone) values('henry', '12345', 12312312311), ('echo','123123123',12312312311),('dean', '283818181', 12312312311), ('brad','283818181',12312312311), ('oleg', '888818181', 12312312311), ('dianel','112312312',12312312311);
# 增加学生
insert into student(class_name,customer_id) values('1班',3),('2班',4),('3班',5);
```

#### 3.3 多对多

- 利用第三张表，把两个关联关系的字段作为第三张表的外键

```mysql
create table author(id int primary key auto_increment,
                    name varchar(20));
create table book(id int primary key auto_increment,
                    name varchar(20));
# 这张表就存放作者表与书表的关系，即查询二者的关系查这表就可以了
create table author_book(id int not null unique auto_increment,
                         author_id int not null,
                         book_id int not null,
                         constraint fk_author foreign key(author_id) references author(id)
                         on delete cascade
                         on update cascade,
                         constraint fk_book foreign key(book_id) references book(id)
                         on delete cascade
                         on update cascade,
                         primary key(author_id,book_id));

# 插入作者和书籍信息
insert into author(name) values('henry'),('echo'),('dean'),('diane');
insert into book(name) values('1'),('2'),('3'),('4'),('5'),('6')
insert into author_book(author_id,book_id) values(1,1),(1,2),(1,3）,(1,4),(1,5),(1,6),(2,1),(2,6),(3,4),(3,5),(3,6),(4,1);
```

#### 3.4 on delete/update

```mysql
# 在父表上update/delete记录时，同步update/delete掉子表的匹配记录
cascade方式	

# 在父表上update/delete记录时，将子表上匹配记录的列设为null要注意子表的外键列不能为not null  
set null方式 

# 如果子表中有匹配的记录,则不允许对父表对应候选键进行update/delete操作
No action方式

# 同no action, 都是立即检查外键约束
Restrict方式

# 父表有变更时,子表将外键列设置成一个默认的值 但Innodb不能识别
Set default方式
```

### 4. 记录操作

#### 4.1 数据增加

1. insert into 表名 values(值…)：一次性可以写入**多行**数据
2. insert into 表名(字段名) values(值...)
3. insert into 表名 value(值…)：一次性只可以写入**一**行数据

```mysql
# 写入一行数据
insert into t1 values(1, 'henry', 19);
insert into t1 value(1, 'henry', 19);
# 写入多行数据
insert into t1 values(1, 'henry', 19), (2, 'echo', 18);
# 指定字段写入
insert into t1(name, age) value('henry', 19);
```

#### 4.2 删除

```mysql
# 删除条件匹配到的数据
delete form 表 where 条件;
```

#### 4.3 修改

```mysql
# 修改表中数据， set 后的字段可以为一个或多个
update 表 set 字段=值 where 条件;
# 注意null只能使用 is 匹配
where name is null;
```



## 10.4 查询

- select 语法

```mysql
SELECT DISTINCT 字段1,字段2... FROM 表名
                              WHERE 条件
                              GROUP BY field
                              HAVING 筛选
                              ORDER BY field
                              LIMIT 限制条数
```

### 1. 基本查询

```mysql
# 查看表中所有数据
select * from 表
# 查看指定字段
select 字段1,字段2... from 表
# 查看指定字段，自动去重
select distinct 字段1,字段2... from 表
# 数值型四则运算，并名别名显示
select name,sarlary*12 (as) annual_sarlary form 表
# 数值型四则运算，并名别名， 拼接显示
select concat ('姓名：',name,'薪资：',sarlary*12) (as) annual_sarlary form 表
# 使用':'进行拼接
select concat_ws (':', name,sarlary*12 (as) annual_sarlary) form 表
```

```mysql
# 结合CASE语句：
SELECT(CASE
       WHEN emp_name = 'jingliyang' THEN
           emp_name
       WHEN emp_name = 'alex' THEN
           CONCAT(emp_name,'_BIGSB')
       ELSE
           concat(emp_name, 'SB')
       END
       ) as new_name FROM employee;
```

### 2 . where

- **逐行过滤**

1. 比较运算：<>/!= 不等于，> ，< ，>=，<=
2. 范围筛选
   - 多选一个
   - 在一个模糊的范围里
     - 在一个数值区间
     - 字符串模糊查询
     - 正则匹配
3. 逻辑运算—条件拼接
   - 与、或、非

#### 2.1 比较/逻辑运算

- **in / not in / is / is not** 

```mysql
select * from t1 where sarlary>1000;

# 和数值类型无关
select * from t1 where sarlary=20000 or sarlary=30000;
# 逻辑运算
select * from t1 where gender='male' and age=18;
# 多选一,可以使用 in
select 字段名，... from t1 where sarlary in (20000, 30000, 19000);
# not in 
select 字段名，... from t1 where sarlary not in (20000, 30000, 19000);

# is is not 
select 字段名 from t1 where 字段 is null;
```

#### 2.2 模糊查找(3)

1. **between…and...**

```mysql
# between ... and ...
select  name,sarlary from t1 where sarlary between 10000 and 20000;
```

2. **字符串**模糊匹配，**like**

```mysql
# like ， % 通配符，匹配任意长度，任意内容
select * from t1 where name like '程%';
# like ， _ 通配符，匹配一个任意字符
select * from t1 where name like '程_';
# like ， 以 n 结尾
select * from t1 where name like '%n';
```

3. 正则匹配，**regexp**

```mysql
select * from t1 where name regexp 正则表达式;
SELECT * FROM employee WHERE emp_name REGEXP 'on$';
```

### 3. 分组聚合

#### 3.1 group by

- group by 后的这个字段，也就是post字段中的每一个不同的项目保留下来
- 并且把值是这一项的所有行归为一组，并**只显示组中第一个**

```mysql
# 显示一个组的第一个,必须有group的字段
select post from employee group by post;
# distinct 基于group by完成
```

#### 3.2 聚合函数(5)

- 把多行的同一字段进行一些统计，最终得到一个结果

1. count(字段)：统计这个字段有多少项
2. sum(字段)：统计这个字段对应的数值和，数值类型
3. avg(字段)：平均值
4. **min、max**：
   - 只能取到最小、最大值，但不能取到对应的其他项(名字)，显示组中第一项
   - 使用多表查询

- **count**

```mysql
select count(*/ 主键) from employee;
# 只算id不为空的字段个数
select count(id) from employee;
```

- **avg/sum**

```mysql
select avg(salary) from employee;
select sum(salary) from employee;
```

#### 3.3 分组聚合

- group by

```mysql
# 分别对各个组,统计人数
select post,count(*) from employee group by post;
# 对某一组进行统计人数
select post,count(*) from employee where post='teacher';
# 各部门的平均薪资
select post,avg(sarlary) from employee group by post;
```

```mysql
# 最晚入职
select max(hire_date) from employee;
# 最早入职
select min(hire_date) from employee group by post;
```

- **查询分组内所有成员名**
  - group_concat()

```mysql
# 查询岗位名以及岗位包含的所有员工名字
select post, group_concat(emp_name) from employee group by post;
# 查询岗位名以及各岗位内包含的员工个数
select post, count(id) from employee group by post;
# 查询公司内男员工和女员工的个数
select sex, count(id) from employee group by sex;
```

#### Note2(2)

1. 总是根据会重复的项进行分组
2. 分组总是和聚合函数一起使用

#### 3.4 having

- having 条件，**组过滤**， 一般与**group**一起使用
-  **Where** 发生在分组**group by之前**，因而Where中可以有任意字段，但是**绝对不能**使用聚合函数。
- **Having**发生在分**组group by之后**，因而Having中可以使用分组的字段，**无法直接取到其他字段**,可以使用**聚合函数**

```mysql
# 部门人数大于3
select post from employee group by post having count(*) > 3;
# 平均薪资大于10000
select post from employee group by post having avg(salary) > 10000;
# 过滤整张表,必须有 age 字段，否则报错
select emp_name, age from employee having avg(age)>18;
```

- having 过滤示例

```mysql
# 查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
select post, group_concat(emp_name), count(*) from employee group by post having count(id) < 2;
# 查询各岗位平均薪资大于10000的岗位名、平均工资
select post,avg(salary) from employee group by post having avg(salary) > 10000;
# 查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
select post,avg(salary) from employee group by post having avg(salary) > 10000 and avg(salary) < 20000;
# 使用 between ... and...
select post,avg(salary) from employee group by post having avg(salary) between 10000 and 20000;
```

#### 3.5 order by

```mysql
# desc 表示降序排
# asc 表示生序排列，默认值
select * from employee order by salary desc;
# 多个个字段排序，先根据第一个字段排列后，再根据第二个字段排列
select * from employee order by age asc, salary desc;
```

- having 和 order by综合使用示例

```mysql
# 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资升序排列
select post, avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) asc;
# 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资降序排列
select post, avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) desc;
```

#### 3.6 limit

```mysql
# 分页显示
# 默认从0开始，显示前5个
select * from employee limit 5;
# 显示下5个, 5+1 位置开始取
# limit m,n 表示从m+1开始取到5个
# limit n offset m等价于limit m,n
select * from employee limit 5,5;
# 显示下5个
select * from employee limit 10,5;
```

#### Note3(3)

1. **关键字执行的优先级(8)**
   - **join优先级要高于from**
   - **from**—> **where** —> **group by** —> **select** —> **distinct** —> **having** —> **order by** —>**limit**
2. 用户认证—>解析、优化、执行sql、找到存储引擎
3. select之前把行数限制在小的范围

![sql语句执行顺序](/Users/henry/Documents/截图/Py截图/sql语句执行顺序.png)

### 4. 多表查询

- 数据准备

```mysql
#建表
create table department(id int,
                        name varchar(20) );

create table staff(id int primary key auto_increment,
                   name varchar(20),
                   gender enum('male','female') not null default 'male',
                   age int,
                   dep_id int);
#插入数据
insert into department values(200,'技术'),(201,'人力资源'),(202,'销售'),(203,'运营');
insert into staff(name,gender,age,dep_id) values
('henry','male',18,200), 
('echo','female',48,201),
('dean','male',38,201),
('diane','female',28,202),
('oleg','male',18,200),
('iris','female',18,204);

#查看表结构和数据
mysql> desc department;
mysql> desc employee;

mysql> select * from department;
mysql> select * from employee;
```

#### 4.1 连表查询

- **通常使用内连接和左外连接**

```mysql
select 字段列表
    FROM 表1 INNER|LEFT|RIGHT JOIN 表2
    ON 表1.字段 = 表2.字段;
```

1. **交叉连接：不适用任何匹配条件。生成笛卡尔积**

```mysql
# 笛卡尔积
select 字段 from t1,t2 where 字段1=字段2;
# 连表查询,staff,department 两个表，和 inner join 效果一致
select * from staff, department as dept where dep_id=dept.id;
```

2. **内连接(inner join)**
   - 两张表条件不匹配的项不出现结果中

```mysql
select 字段 from t1 inner join t2 on t1(字段1) = t2(字段2);
```

3. **外连接**
   1. **左外连接(left join)：全量显示左边的表中数据**
      - **本质**就是：在内连接的基础上增加**左边有右边没有**的结果
   2. 右外连接(right join)：全量显示右边的表中数据
      - **本质**就是：在内连接的基础上增加**右边有左边没有**的结果
   3. 全外连接**(左外连接 union 右外连接)**：mysql没有全外连接
      - **在内连接的基础上增加左边有右边没有的和右边有左边没有的结果**
   4. **sqlserver**中有全外连接(**full join**)，没有右外连接

```mysql
# t1连接t2，显示全量的左表，只显示匹配到的t2
select 字段 from t1 left join t2 on t1(字段1) = t2(字段2);
select 字段 from t1 right join t2 on t1(字段1) = t2(字段2);
# 全连接
select 字段 from t1 left join t2 on t1(字段1) = t2(字段2) union
select 字段 from t1 right join t2 on t1(字段1) = t2(字段2);
```

```mysql
# 通过左外、和右外连接实现全外连接示例
select * from staff left join department as dept on dep_id = dept.id union select * from staff right join department as dept on dep_id = dept.id;
```

- **注意 union与union all的区别：union会去掉相同的纪录**

4. **连表查询示例**
   - **连表查询效率更高**

```mysql
# 以内连接的方式查询staff和department表，并且staff表中的age字段值必须大于25,即找出年龄大于25岁的员工以及员工所在的部门
# 此时括号可以省略
select staff.name, dept.name from staff left join department as dept on dep_id = dept.id where age > 25;
# 以内连接的方式查询staff和department表，并且以age字段的升序方式显示
select * from staff inner join department as dept on dep_id = dept.id order by age;
```

#### 4.2 子查询

1. 基本语法

```mysql
1：子查询是将一个查询语句嵌套在另一个查询语句中。
2：内层查询语句的查询结果，可以为外层查询语句提供查询条件。
3：子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字
4：还可以包含比较运算符：= 、 !=、> 、<等
```

```mysql
# 子表中匹配到唯一值
select name from emp where dep_id = (select id from department where name='技术');
# 子表中匹配到多个值
select name from emp where dep_id in (select id from department where name in ('技术', '销售'));
```

2. 带**in**关键字的查询

```mysql
# 查询平均年龄在25岁以上的部门名
select name from department where id in (select dep_id from staff group by dep_id having avg(age) > 25);
# 查看技术部员工姓名
select name from staff where dep_id in (select id from department where name = '技术' )
# 查看不足1人的部门名(子查询得到的是有人的部门id)
select name from department where id not in (select dep_id from staff group by dep_id);
```

3. 带比较运算符

```mysql
# 查询大于所有人平均年龄的员工名与年龄
select name, age from staff where age > (select avg(age) from staff);
# 查询大于部门内平均年龄的员工名、年龄
select name, age from staff t1 inner join (select dep_id, avg(age) avg_age from staff group by dep_id) t2 on t1.dep_id = t2.dep_id where t1.age > t2.avg_age;
```

4. 带EXISTS关键字的子查询

- EXISTS关字键字表示存在。在使用EXISTS关键字时，内层查询语句不返回查询的记录。而是返回一个真假值。
- 当返回True时，外层查询语句将进行查询；当返回值为False时，外层查询语句不进行查询

```mysql
# exists后为真
select * from staff where exists (select id from department where id=200);
# 输出staff中所有数据

# exists后为假
select * from staff where exists (select id from department where id=200);
# 输出为空
```

5. **示例**
   - **查询每个部门最新入职的那位员工**

```mysql
# 连表查询
select t1.emp_name, t1.hire_date, t1.post from employee as t1 inner join (select depart_id, max(hire_date) as max_date from employee group by depart_id) as t2 on t1.depart_id = t2.depart_id where t1.hire_date = t2.max_date;
```

```mysql
# 子查询
select t3.emp_name,t3.post,t3.hire_date from employee as t3 where id in (select (select id from employee as t2 where t2.depart_id=t1.depart_id order by hire_date desc limit 1) from employee as t1 group by depart_id);
```



## 10.5 pymysql模块

### 1. 第三方模块

```mysql
mysql -uroot -p
mysql.exe              # mysql的一个客户端
```

- **ip port 用户名 密码 使用的库** 连接mysqld的server端

```python
import pymysql
con = pymysql.connect(host='127.0.0.1', user='root', password='123', database='test')
# 数据库操作符，游标
# dict取值，默认元组
cur = con.cursor(pymysql.cursors.DictCursor)
# 操作
cur.execute('sql语句')
# 获取返回值,cur类似操作文件的游标指针
ret = cur.fetchone()/ fetchmany(n)/ fetchall()
con.commit()
con.close()
```

- localhost：不过网卡，127.0.0.1过网卡

### 2. 事物和锁

```mysql
# 开启事务
begin; 或者 start transction;
# 查询id值，for update添加行锁；
select * from emp where id = 1 for update;
# 完成更新
update emp set salary=10000 where id = 1;
# 提交事务
commit;
```

### 3. sql注入

```mysql
-- 表示注释掉之后的sql语句

```

- 怎么避免

```python
sql = 'select * from 表'
# 参数为可迭代对象
cur.execute(sql, (username, password))
cur.close()
con.close()
```













# 第十一章 前端开发

# 第十二章 Django框架
