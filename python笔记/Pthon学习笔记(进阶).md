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
#  server net stop mysql
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
   - 存储在内存：**表结构**， 表数据存储到硬盘上
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
show engines \g
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
  3. 第三层包含了**存储引擎**。**存储引擎负责MySQL中数据的存储和提取**。服务器通过API和存储引擎进行通信。这些接口屏蔽了不同存储引擎之间的差异，使得这些差异对上层的查询过程透明化。存储引擎API包含十几个底层函数，用于执行“开始一个事务”等操作。但存储引擎一般不会去解析SQL（InnoDB会解析外键定义，因为其本身没有实现该功能），不同存储引擎之间也不会相互通信，而只是简单的响应上层的服务器请求。
  4. 第四层包含了**文件系统**，所有的表结构和数据以及用户操作的日志最终还是以文件的形式存储在硬盘上

## 10.3 表的完整性约束

### 1. 约束

- 5.6版必须指定字段名，否则会报
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

- 默认值

```mysql
create table t2(id int not null,
               name char(12) not null,
               gender enum('male', 'female') not null default 'male'
               );       
insert into t2(id, name) values(1, 'henry');
```

#### 1.3 unique

- 不重复(**key UNI**)，所有的非空数据不重复

```mysql
create table t3(id int unique,
               username char(12) not null unique,
               pwd char(18)
               );
```

- 联合唯一(**key MUL**)

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
# 基于表级别
create table t1（id int...
    ）engine=innodb,auto_increment=2 步长=2 default charset=utf8;
# mysql自增的步长：
show session variables like 'auto_inc%'; 
# 基于会话级别
set session auto_increment_increment=2; #修改会话级别的步长
# 基于全局级别的
set global auto_increment_increment=2; #修改全局级别的步长（所有会话都生效）
# 查看设置，重新登陆有效,5.7版本直接失效
show variables like 'auto_incre%'; 
```

- If the value of **auto_increment_offset(起始偏移量)** is greater than that of **auto_increment_increment(步长)**, the value of auto_increment_offset is ignored. 
- **比如**：设置auto_increment_offset=3，auto_increment_increment=2

#### 1.5 primary key

- 一张表**只能**设置**一个主键**
- **innodb**表中最好设置一个主键
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
# 去掉unique约束
alter table 表名 drop index 字段名;
# 添加unique约束
alter table 表名 modify 字段名 int unique;
```

#### 2.6 修改库的默认编码

```mysql
alter database 库名 CHARACTER SET utf8;
```

#### 2.7 操作主键

```mysql
# 先删除主键，删除一个自增主键会报错
# 需要先去掉主键的自增约束，然后再删除主键约束
alter table 表名 drop primary key;
# 增加主键
alter table 表名 add primary key(id);
```

#### 2.8 操作外键

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
# 修改表中数据
update 表 set 字段=值 where 条件;
# 注意null只能使用 is 匹配
where name is null;
```





## 10.4 查询

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

















# 第十一章 前端开发

# 第十二章 Django框架
