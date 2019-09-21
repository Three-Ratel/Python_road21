

# redis

## 1. 概念

1.  数据默认写入到内存，断电数据会丢失
2.  redis是内存型数据库
3.  selenium操作浏览器时，需要注意浏览器资源释放，防止内存泄漏
4.  redis持久化：防止数据丢失，以文件形式存储
5.  Redis是vmware开发的开源免费的KV型NoSQL缓存产品

### redis特性

1.  Redis 是一个开源（BSD许可）的，内存中的数据结构存储系统，它可以用作数据库、缓存和消息中间件
2.  redis是c语言编写的，支持数据持久化，是key-value类型数据库。
3.  应用在缓存，队列系统中
4.  redis支持数据备份，也就是master-slave模式

### 优势

1.  Redis具有很好的性能，可以提供10万次/秒的读写
2.  用作缓存数据库，数据放在内存中
3.  替代某些场景下的mysql，如社交类app
4.  大型系统中，可以存储session信息，购物车订单

## 2. redis安装

### 1. 安装方式

1.  yum安装，简单，需要配置yum源
2.  源码编译安装，可以指定安装路径，自定制第三方扩展模块功能
3.  rpm安装，需要手动解决依赖关系

### 2. 源码安装

#### 1. 环境准备

```shell
wget   http://download.redis.io/releases/redis-4.0.10.tar.gz
tar xzvf redis-4.0.10.tar.gz
```

-   解决依赖包

```shell
yum install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel openssl openssl-devel -y
```

#### 2. 释放makefile

-   告诉gcc编译器，redis安装路径
-   如果默认没有configure脚本，但有**makefile**，直接make && make install即可

```shell
make && make install
```

#### 3. 编译完成

-   即可使用redis，启动redis服务端

```shell
redis-server 			# 直接执行
redis-cli				# 测试，ping回显PONG
```

-   redis可执行文件

```shell
./redis-benchmark 		# 用于进行redis性能测试的工具
./redis-check-dump 		# 用于修复出问题的dump.rdb文件
./redis-cli 			# redis的客户端
./redis-server 			# redis的服务端
./redis-check-aof 		# 用于修复出问题的AOF文件
./redis-sentinel 		# 用于集群管理
```

-   云服务器中招了

```shell
kill -9 pid
# 查看定时任务，并编辑**文件的定时任务
crontab -l
crontab -e
# 全局搜索病毒文件，并删除(注意恶意病毒，篡改了文件名)
find / -name 病毒文件
# 找到后 rm -rf 删除
lsattr filename.txt
# 去掉文件的锁,即可删除
chattr -a  -i  filename.txt
```

#### 4. 指定配置文件

-   安全的启动redis服务端
    1.  更改启动端口
    2.  添加redis密码
    3.  开启redis安全模式
-   默认配置文件，redis.conf

```shell
# 过滤出配置文件的有益信息(去掉注释和空白行)
grep -v '^#' redis.conf | grep -v '^$' > myredis.conf
```

#### 5. 指定配置启动

-   test.py

```python
import redis
# redis默认有 16 个库，0-15
conn = redis.StrictRedis(host='172.16.44.142', port=6379, db=0, password='')
conn.set('name', 'henry')
```

-   myredis.conf

```shell
bind 172.16.44.142				# 绑定redis服务器地址
protected-mode yes				# 开启安全模式
port 6800						# 指定端口
requirepass xxx					# 设置密码
pidfile /var/run/redis_6379.pid	# 进程id文件
loglevel notice					# 日志等级
daemonize yes					# 后台运行 
```

-   启动

```shell
redis-server myredis.conf
# 测试
redis-cli -p 6800 -h 172.16.44.142
172.16.44.142:6800> ping
(error) NOAUTH Authentication required.
172.16.44.142:6800> AUTH test
OK
```

## 3. redis数据

### 1. 常用命令

```shell
keys *
type key						# 查看key对应的value类型
expire queue seconds			# 设置过期剩余时间
eg. expire test 10				# 10s 后过期
ttl queue						# 查看剩余时间
persist	queue					# 取消queue的过期时间
exists key						# 判断key是否存在
del key							# 删除key，可以删除多个
dbsize key						# 当前库key的数量
flushdb							# 清除redis的所有key
flushall						# 清空所有数据库的所有 key
```

### 2. 数据类型

-   redis是一种高级的key：value存储系统，其中value支持五种数据类型
    1.  字符串（strings）
    2.  散列（hashes）
    3.  列表（lists）
    4.  集合（sets）
    5.  有序集合（sorted sets）

#### 1. 字符串（strings）

```shell
# string 类型，通过set命令设置
set key value
set 'name' 'xixi'
# 获取指定的key
get 'name'
# key存在，则追加到该key原来值的末尾。
append 'name' 'haha'
# 批量设置和获取
mset 'name' 'henry' 'age' 18
mget 'name' 'age'
# 将已存在 key 的值设为value，并返回key的旧值(old value)
getset name echo
# 返回 key 中字符串值的子字符 value[start, end],包含end
getrange name 1 2
# 获取 name 值的长度
strlen name
# 自增1
incr 'prize'
# 自减1
decr 'prize'
```
#### 2. 散列（hashes）

```shell
# 将哈希表 key 中的字段 field 的值设为 value
hset stu name 'henry' age '18' height '180' 
# 获取存储在哈希表中指定字段的值
hget stu name
# 如果给定字段已经存在且没有操作被执行
hsetnx key field value

# 同时将多个 field-value (域-值)对设置到哈希表 key 中
hmset key field1 value1 field2 value2 ...
hmset stu name echo age 19
# 获取所有给定字段的值
hmget key field1 field2 ...
hmget stu name height

# 删除一个或多个哈希表字段
hdel key field1 field2 ...
# 查看哈希表 key 中，指定的字段是否存在
hexists key field

# 获取所有哈希表中的字段
hkeys key
# 获取哈希表中所有值
hvals key
# 获取在哈希表中指定 key 的所有字段和值
hgetall key
# 获取哈希表中字段的数量
hlen key
```

#### 3. 列表（lists）

```shell
# 双向队列
# 从list左边(右边)插入
lpush/rpush key value1 value2 ...
lpush/rpush test 1

# 索引查看list, [start, end]
lrange test start end	
# 通过索引设置列表元素的值
lset key index value
# 通过索引获取列表中的元素
lindex key index

# 移出并获取列表的第一个(最后一个)元素
lpop/rpop key
# 移出并获取列表的第一个(最后一个)元素，如果列表为空会阻塞直到等待超时或发现可弹出元素为止
blpop/brpop key1 [key2 ] timeout 

# 获取列表长度
llen key
# 对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除
ltrim key start stop 						
# key 存在不处理，不存在添加
lpushx/rpushx key 
```

#### 4. 集合（sets）

-   redis的集合，是一种无序的集合，集合中的元素没有先后顺序。

```shell
# set 集合类型
# 默认是无序的
sadd url 'http://www.baidu.com' 'http://www.jd.com'
# 查看所有的成员
smembers url
# 删除
srem url 'http://www.jd.com'
# 判断是否是集合的元素
sismember url 'http://www.jd.com'
# 列出 url - url2
sdiff url url2
# 返回集合的交集
sinter url url2
# 返回集合的并集
sunion url url2
```

## 4. redis发布订阅

```shell
# 发布者
publish python 'hello python'
publish python 'hello go'
# 订阅者1
subscribe linux python
# 正则模式订阅
psubscribe python*
# 订阅者2
subscribe go
```

## 5. 持久化

-   **触发机制**
    	1. 手动执行save命令
     	2. 或者配置触发条件  save  200   10   #在200秒中内,超过10个修改类的操作

### 1. 方式一：rdb

#### 1. 触发方式

1.  手动执行或定期执行
2.  产生了一个经过压缩的二进制文件，保存到磁盘
3.  配置文件
    -   myredis_rdb.conf

```shell
dbfilename dbmp.conf
# 持久化文件保存位置
dir /data/6379
# 每900s只要有1个修改记录就保存一次
save 900 1
save 60 10000
```

```shell
# 启动
redis-server myredis_rdb.conf
```

-   手动触发

```python
save
```

#### 2. 基于快照的持久化

-   速度更快，一般用作备份，主从肤质也是依赖rdb持久化

### 2. 方式二：aof

-   AOF（append-only log file）
-   AOF 文件中的命令全部以**redis协议的格式**保存，新命令追加到文件末尾。
-   优点：最大程序保证数据不丢
-   缺点：日志记录非常大

#### 1. aof配置文件

-   aof_redis.json

```python
daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379
dbfilename  dbmp.rdb
requirepass test
save 900 1
save 300 10
save 60  10000
appendonly yes
appendfsync always			# 总是修改类操作
			everysec		# 每秒保存
    		no				# 依赖于系统自带的缓存大小机制
```

#### 2. 基于

-   

### 3. rdb方式转换aof

#### 1. 环境准备

```shell
# 版本>4.0
redis -v 
# 准备rdb配置文件

# 临时生效
redis-cli
config set appendonly yes
config set save ''
# 永久生效，修改配置文件



```

## 6. redis主从复制

### 1. redis 支持多实例

-   环境准备：运行3个redis数据库，达到1主2从的配置
-   主库：6379.conf
-   从库
    -   6380.conf、6381.conf
    -   `sed 's/6379/6380/' 6379.conf > 6380.conf`
-   开启主从配置功能

```shell
# 查看数据库信息
redis-cli info replication
# 6380和 6381配置主从
redis-cli -p 6380 slaveof 127.0.0.1 6379
redis-cli -p 6381 slaveof 127.0.0.1 6379
# 主库用于插入数据、从库用于读取，实现读写分离
```

### 2. master故障

#### 1. 手动切换 6380 为主库

```shell
# 1. 关闭从库身份
redis-cli -p 6380 slaveof no one
# 2. 设置其他从库的主库
redis-cli -p 6381 slaveof 127.0.0.1 6380
# 3. 修改配置文件中的主从关系
```

### 3. Redis-Sentinel

-   高可用，用于检测主从集群，自动发信master宕机，进行自动切换主从

#### 1. 环境准备

-   三个redis数据库实例，三个配置文件

```shell

```

-   三个哨兵监控，三个配置文件
-   sentinel-26379.conf、sentinel-26380.conf、sentinel-26381.conf

```shell

```

-   启动数据库

```shell
redis-server 6379.conf
redis-server 6380.conf
redis-server 6381.conf
```

-   启动哨兵：第一次启动后配置文件会自动修改
    -   daemonize yes

```shell
redis-sentinel sentienl-26379.conf
redis-sentinel sentienl-26380.conf
redis-sentinel sentienl-26381.conf
# 测试哨兵是否启动成功
redis-cli -p 26379 info sentinel
```

-   断掉主库检查主从状态

## 7. redis-cluster配置

-   支持更大的并发
-   解决redis内存不足的情况

### 1. 环境准备

-   配置文件：redis-7001.conf、redis-7002.conf、redis-7003.conf、redis-7004.conf
-   仅仅是端口的区别

```shell

```

### 2. 启动

```shell
redis-cli 7000.conf
redis-cli 7001.conf
...
```

### 3. 分配redis slot 槽位

-   手动编写c语言，分配
-   使用ruby的一个redis 模块，自动分配
-   配置ruby脚本环境

```shell
# 安装
yum install -y ruby
# 使用 ruby和gem
```

-   下载ruby操作redis的模块

```shell
wget 
```

-   使用ruby包管理工具安装

```shell
gem install -l redid-3.3.0.gem
```

-   通过ruby一键分配槽位

```shell
# 找到redis-trib.rb命令
find / -name redis-trib.rb
# 开启集群开启槽位

# 分配好集群后，向集群中写入数据
redis-cli -c -p 7000
set name 'xiake'
```

# python操作redis

## 1. 安装

```python
# win
下载redis到指定目录，配置PATH即可
# mac
brew install redis
```

## 2. 使用

1.  redis使用 key:value 方式存储，**哈希存储结构{key:value}**
2.  多次设置同一个key 会被覆盖

```python
# 终端
redis-cli
# 总共 16 个库，0-15，用来数据隔离
select 8					# 切换 8 号库，默认 0 号库
set key value				# 设置一个健值对，哈希存储结构{key:value}
keys pattern				# 查询当前数据库中所有的key,如keys * 查询当前数据库中所有key
		 a*					# 查询以 a开头
  	 *n*					# 包含 n
...
get key						# 查询 key 对应的 value
```

## 3. python操作redis

1.  --protected-mode no：测试使用，没有设置密码可以使用主机ip
2.  redis只能存储：**byte, string or number**

```python
from redis import Redis
redis_cli = Redis(host='127.0.0.1', port=6379, db=6)
redis_cli.set('name', 'echo')
```