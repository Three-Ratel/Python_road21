# 第八章 网络编程

1. 网络基础
2. 基于tcp协议和udp协议的**socket**
3. 解决tcp协议的**粘包问题**
4. **并发**

## 8.1 网络基础

### 1. 基本概念

1. 两个运行中的程序传递信息？
  
   - 通过**文件**
2. 两台机器上运行中的程序通信？
  
   - 通过**网络**
3. 网络应用开发架构
   - C/S：client/server（需要安装对应的客户端）
   - B/S：browser/server（不需要任何客户端）
     - 统一程序的入口
   - b/s是特殊的c/s

### 2. 网络中的概念

1. 网卡、mac地址：48位

2. **交换机(4)**
  
   - 负责局域网通信（只认识mac地址，通过arp/ rarp协议）
   - 广播、单播、组播(交换机只使用前面的**两种**)
   - **ARP**协议：地址解析协议，通过ip地址，获取其mac地址
   - **保留网段（私有IP）**：192.168.0.0-92.168.255.255 /172.16.0.0-172.31.255.255 /10.0.0.0-10.255.255.255
   
3. **路由器(2)**
  
   - 负责局域网间通信
   
   - **网关ip**：**局域网的网络出口**，访问局域网之外的区域都需要经过gateway
   
4. **协议**：server和client得到的内容都是二进制，双发预先约定好的一套语法规则 

5. Ipv6:冒分16进制，0:0:0:0:0:0:0:0- FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF(128bits, 16x8)

6. 每一个ip地址要想被所有人访问到，那么这个ip地址必须是申请的

7. **port 端口(4)**

   - 端口号0 - 65535

   - 一个端口同一时刻只能被一个服务占用
   - ip+port：可以确认一台机器上的一个应用
   - 1024以内只能是root才能启用



## 8.2 OSI&TCP/IP

### 1. TCP协议

- **应用场景**：文件上传下载（邮件、网盘、缓存电影）

- **特点**（3）：可靠、传输效率较低、全双工，重传机制、发送的每一帧都有确认回复
- **三次握手**：请求(SYN)—> 确认(ACK)+请求—>确认
  - 通信：建立在全双工连接的基础上
- **长连接**：会一直占用双方port
- I/O：相对于**内存**来说
  - write 是 send
  - read 是 recv

- **四次挥手**：请求(FIN)—> 确认—>请求—>确认
  - 断开：四次

![TCP](/Users/henry/Documents/截图/Py截图/TCP.png)

### 2. UDP协议

- **场景**：即时通讯（qq，wechat）
- **特点**：无连接、速度快，可能会丢帧
- UDP 是User Datagram Protocol的简称， 中文名是用户数据报协议

#### Note1(2)

- TCP传输**数据几乎没有限制**，UDP能够传递数据长度是有限的，是根据数据传递设备的设置有关
- Tcp可靠**长**连接，udp不可靠无连接
- 三次握手时，确认信息和请求连接信息合并为一帧，四次挥手，主动断开端，不能确定另一端是否还需要传输信息，所以不能合并。

### 3. OSI(Open System Interconnection)

1. 应用层
2. 表示层
3. 会话层
4. 传输层
5. 网络层
6. 数据链路层
7. 物理层

OSI**五层**协议(简化)

1. 应用层：代码
2. 传输层：tcp/udp 端口号，**四层路由器、四层交换机**
3. 网络层：ipv4/ipv6，**三层路由器、三层交换机**
4. 数据链路层：mac地址，arp协议，**(二层)交换机**
5. 物理层：二进制流

TCP/IP(**arp在tcp/ip中属于网络层**)

1. 应用层
2. 传输层
3. 网络层
4. 链路层

#### Note2(4)

1. 家用路由器集成了交换功能
2. **网络协议**
   1. **网际层**协议:IP协议、ICMP协议、ARP协议、RARP协议。 
   2. **传输层**协议:TCP协议、UDP协议。 
   3. **应用层**协议:FTP、Telnet、SMTP、HTTP、RIP、NFS、DNS

### 4. socekt(套接字)

- 工作在**应用层**和**传输层**之间的抽象层
- 帮助我们完成所有信息的组织和拼接
- socket历史：
  - 同一机器上的两个服务之间的通信(基于文件)
  - **基于网络**的多台机器之间的多个服务通信

### 5. Socket模块

**1. TCP**

```python
type = socket.SOCK_STREAM  # 表示tcp协议
sk.listen(n)        # n 表示允许多少个客户端等待，3.7之后无限制
sk.accept()         # 阻塞
# 服务端需要一直监听，不能关闭
```

需求：

1. server和client连接后，知道是哪一个好友
2. 不同好友的聊天颜色不同
3. 多个人能互相聊

**2. UDP**

```python
# server
import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))

msg, client_addr = sk.recvfrom(1024)
print(msg)
sk.sendto(b'received', client_addr)
sk.close()

# client
import socket
sk = socket.socket(type = socket.SOCK_DGRAM)

sk.sendto(b'hello', ('127.0.0.1', 9000))
ret = sk.recv(1024)
print(ret)
sk.close()
```

需求：

1. 实现一个人和多个人聊
2. 每个人标识

#### Note

1. socket收发的**必须是bytes**类型，经过编码的文件均是bytes类型
2. 网络传输数据一般使用**json**格式

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