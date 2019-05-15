# 第八章 网络编程

1. 网络基础
2. 基于tcp协议和udp协议的**socket**
3. 解决tcp协议的**粘包问题**
4. **并发**

## 8.1 网络基础

### 1. 基本概念(2)

1. 两个运行中的程序传递信息？
  
   - 通过**文件**，通过**网络**
3. 网络应用开发架构
   - C/S：client/server（需要安装对应的客户端）
   
   ![c:s架构](/Users/henry/Documents/截图/Py截图/c:s架构.png)
   
   - B/S：browser/server（不需要任何客户端）
     - 统一程序的入口
   - B/S是特殊的C/S

### 2. 网络中的概念(7)

1. **网卡(3)**
   - mac地址：48位, 6位冒分十六进制
   - head中包含的源和目标地址由来
     - ethernet规定接入internet的设备都必须具备网卡，发送端和接收端的地址便是指网卡的地址，即mac地址。
   - mac地址：每块网卡出厂时都被烧制上一个世界唯一的mac地址，长度为48位2进制，通常由12位16进制数表示（**前六位是厂商编号**，后六位是流水线号）
2. **交换机(4)**
   - **功能**：负责局域网通信（只认识mac地址，通过arp/ rarp协议）
   - **通信方式**：广播、单播、组播(交换机只使用前面的**两种**)
   - **ARP**协议：地址解析协议，通过ip地址，获取其mac地址
   - **保留网段（私有IP）**：192.168.0.0-92.168.255.255 /172.16.0.0-172.31.255.255 /10.0.0.0-10.255.255.255
   - **广播限制**在二层交换机的局域网范围内，**禁止广播数据穿过路由器**，防止广播数据影响大面积的主机
3. **路由器(2)**
   - 负责局域网间通信
   - **网关ip**：**局域网的网络出口**，访问局域网之外的区域都需要经过gateway
   - 路由器（Router）又称**网关设备**（Gateway）是用于连接多个逻辑上分开的网络
4. **协议**
   - server和client得到的内容都是二进制，双发预先约定好的一套语法规则 
   - 语法、语义、时序
5. **IP地址**
   - Ipv6:冒分16进制，0:0:0:0:0:0:0:0- FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF(128bits, 16x8)
   - 每一个ip地址要想被所有人访问到，那么这个ip地址必须是申请的
6. **port 端口(4)**
   - 端口号0 - 65535

   - 一个端口同一时刻只能被一个服务占用
   - ip+port：可以确认一台机器上的一个应用
   - 1024以内只能是root才能启用



## 8.2 OSI&TCP/IP

### 1. TCP协议(6)

1. **TCP**（Transmission Control Protocol）可靠的、面向连接的协议（eg:打电话）、传输效率低全双工通信（发送缓存&接收缓存）、**面向字节流**。
2. **应用场景**：文件上传下载（邮件、网盘、缓存电影）、Web浏览器；电子邮件、文件传输程序。
3. **特点**（3）：面向连接、可靠、流式传输的全双工通信
4. **三次握手**：请求(SYN)—> 确认(ACK)+请求—>确认
   - **server端** **accept** 接收过程中等待客户端的连接
   - **connect** 会发送一个**syn**连接请求
     - 如果收到了server响应**ack**和由server端发来的**syn**连接请求
     - client端进行回复ack信息后，建立了一个tcp连接
   - 三次握手过程在代码过程中是由**accept**和**connect**共同完成，具体细节在socket没有体现
5. **四次挥手**：请求(FIN)—> 确认—>请求—>确认
   - server 端和clinet端在代码中都有**close**方法，每一端发起的close操作都是断开**fin**请求，得到断开确认**ack**之后，就可以结束一端的数据发送
   - 如果两端发起close请求，那么就是**两次请求**和**两次确认**，一共是四次操作
   - 可以结束数据发送，表示连接断开
6. **长连接**：会一直占用双方port
7. I/O：相对于**内存**来说
   - write 是 send
   - read 是 recv

![TCP](/Users/henry/Documents/截图/Py截图/TCP.png)

### 2. UDP协议

1. **UDP**（User Datagram Protocol）不可靠的、无连接的服务，传输效率高（发送前时延小），一对一、一对多、多对一、多对多、面向报文，尽最大努力服务，无拥塞控制。
2. 场景**：即时通讯（qq，wechat），域名系统 (DNS)；视频流；IP语音(VoIP)。
3. **特点**：面向数据报，不可靠，传输速度快，能完成一对多，多对一，和一对一的高效通信
4. **UDP** 是User Datagram Protocol的简称， 中文名是用户数据报协议

#### Note1(3)

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
2. 传输层：tcp/udp **端口号**，**四层路由器、四层交换机**
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
   - **网际层**协议:IP协议、ICMP协议、ARP协议、RARP协议。 
   - **传输层**协议:TCP协议、UDP协议。 
   - **应用层**协议:FTP、Telnet、SMTP、HTTP、RIP、NFS、DNS

### 4. socekt(套接字)

1. 工作在**应用层**和**传输层**之间的**抽象层**，帮助我们完成所有信息的**组织**和**拼接**
   - Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是**一组接口**。在**设计模式中**，Socket其实就是一个门面模式，它把复杂的**TCP/IP协议族隐藏在Socket接口后**面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。
2. socket历史
   1. 套接字起源于 20 世纪 70 年代加利福尼亚大学伯克利分校版本的 Unix,即人们所说的 **BSD Unix**。 因此,有时人们也把套接字称为“伯克利套接字”或“BSD 套接字”。一开始,套接字被设计用在同 一台主机上多个应用程序之间的通讯。这也被称**进程间通讯**,或 **IPC**。**套接字有两种**（或者称为有两个种族）,分别是**基于文件**型的和**基于网络**型的。 
   2. **基于文件类型的套接字家族**
      - 套接字家族的名字：**AF_UNIX**，unix一切皆文件，基于文件的套接字**调用**的就是**底层的文件系统**来取数据，两个套接字进程运行在同一机器，可以通过访问同一个文件系统间接完成通信
   3. **基于网络类型的套接字家族**
      - 套接字家族的名字：**AF_INET**，(还有**AF_INET6**被用于ipv6，还有一些其他的地址家族，不过，他们要么是只用于某个平台，要么就是已经被废弃，或者是很少被使用，或者是根本没有实现，所有地址家族中，AF_INET是使用最广泛的一个，python支持很多种地址家族，但是由于我们只关心网络编程，所以大部分时候我么只使用AF_INET)
3. 同一机器上的两个服务之间的通信(基于文件)
   - **基于网络**的多台机器之间的多个服务通信

![socket](/Users/henry/Documents/截图/Py截图/socket.png)

4. **其实站在你的角度上看，socket就是一个模块**。我们通过调用模块中已经实现的方法建立两个进程之间的连接和通信。也有人将**socke**t说成**ip+port**，因为ip是用来标识互联网中的一台主机的位置，而port是用来标识这台机器上的一个应用程序。所以我们只要确立了ip和port就能找到一个应用程序，并且使用**socket**模块来与之通信。

## 8.3 Socket模块

![socket使用](/Users/henry/Documents/截图/Py截图/socket使用.jpg)

### 1. socket参数的详解

```python
import socket
socket.socket(family=AF_INET,type=SOCK_STREAM,proto=0,fileno=None)
# 创建socket对象的参数说明：
```

| 参数       | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| **family** | 地址系列应为**AF_INET**(默认值),AF_INET6,AF_UNIX,AF_CAN或AF_RDS。 （AF_UNIX 域实际上是使用本地 socket 文件来通信） |
| **type**   | 套接字类型应为**SOCK_STREAM**(默认值),SOCK_DGRAM,SOCK_RAW或其他SOCK_常量之一。 **SOCK_STREAM** 是基于**TCP**的，有保障的（即能保证数据正确传送到对方）面向连接的SOCKET，多用于资料传送。  **SOCK_DGRAM** 是基于UDP的，无保障的面向消息的socket，多用于在网络上发广播信息。 |
| **proto**  | 协议号通常为零,可以省略,或者在地址族为AF_CAN的情况下,协议应为CAN_RAW或CAN_BCM之一。 |
| **fileno** | 如果指定了**fileno**,则其他参数将被忽略,导致带有指定文件描述符的套接字返回。 与socket.fromfd()不同,fileno将返回相同的套接字,而不是重复的。 这可能有助于使用socket.close()关闭一个独立的插座。 |

### 2. TCP信息传输

```python
type = socket.SOCK_STREAM  # 表示tcp协议
# server 端
import socket 
sk = socket.socket()
sk.bind(('127.0.0.1'), port号)
sk.listen(n)               # 监听链接，n 表示允许多少个客户端等待，3.7之后无限制可省略
con,cli_addr = sk.accept() # 接受客户端链接，阻塞,服务端需要一直监听，不能关闭
con.recv(size)    				 # 接收字节数
con.send('content'.encode('utf-8')) 
# socket 发送接收都是字节流，即二进制
con.close()           		 #关闭客户端套接字
sk.close()								 #关闭服务器套接字(可选)

# client 端
import socket
sk = socket.socket()
sk.connet(('ip', port号))
sk.send('content'.encode('utf-8'))
sk.recv(size)
sk.close()
```

```python
# ip和端口占用解决方法，针对macos
import socket
from socket import SOL_SOCKET,SO_REUSEADDR # 加入一条socket配置，重用ip和端口
sk = socket.socket()
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 		# 就是它，在bind前加
sk.bind(('127.0.0.1',8898))  						 		# 把地址绑定到套接字
```

### 3. TCP黏包问题

#### 1. 黏包现象

- **提高效率**：为了减少tcp协议中的**确认收到**的网络延迟时间 
- **发送端**：由于两个数据的发送**时间间隔短**+**数据长度小**，tcp协议的优化机制将两条信息作为一条信息发送出去
- **接收端**：由于tcp协议中所传输的**数据无边界**，来不及接收的**多条数据**会在接收端**内核的缓存端黏在一起**
- **本质**：接收信息的边界不清晰，主要是接收方不知道消息之间的界限，不知道一次性提取多少字节的数据所造成的

#### 2. 成因机制

1. **tcp协议的拆包机制**
   - 当发送端缓冲区的长度大于网卡的MTU时，tcp会将这次发送的数据拆成几个数据包发送出去。 
   - MTU是Maximum Transmission Unit的缩写。意思是网络上传送的最大数据包。**MTU**的单位是**字节**。 **大部分网络设备的MTU都是1500**。
   - 如果**本机的MTU比网关的MTU大**，大的数据包就会被拆开来传送，这样会产生很多数据包碎片，增加丢包率，降低网络速度。
2. **面向流的通信特点和Nagle算法**
   - TCP（transport control protocol，**传输控制协议**）是面向连接的，面向流的，提供高可靠性服务。
   - 收发两端（客户端和服务器端）都要有**一一成对的socket**，因此，**发送端为了将多个发往接收端的包，更有效的发到对方，使用了优化方法（Nagle算法）**，将多次间隔较小且数据量小的数据，合并成一个大的数据块，然后进行封包。这样，接收端，就难于分辨出来了，必须提供科学的拆包机制。 **即面向流的通信是无消息保护边界的。**
   - **对于空消息**：**tcp**是基于数据流的，于是收发的**消息不能为空**，这就需要在客户端和服务端都添加空消息的处理机制，防止程序卡住，而**udp**是基于数据报的，即便是你输入的是**空内容(直接回车)，也可以被发送**，udp协议会帮你封装上消息头发送过去。 
   - **可靠黏包的tcp协议**：tcp的协议数据不会丢，没有收完包，下次接收，会继续上次继续接收，己端总是在收到ack时才会清除缓冲区内容。**数据是可靠的，但是会粘包**。

#### 3. Tcp黏包现象

- **自定义协议**：首先发送报头(**4**bytes) ，针对发送数据大小进行提前声明，内容是即将发送**报文字节长度**
  - struct：把所有数字都固定的转换为4bytes
  - 再发送数据信息

```python
# 自定义协议，解决黏包问题
# server端
import struct
import socket
sk = socket.socket()
sk.bind(('ip', port))
sk.listen()
con, cli_addr = sk.accept()
size = con.recv(4)
size = struct.unpack(size)[0]							# unpack,为一tuple类型
content = con.recv(size).decode('utf-8')	# 接收文件内容
con.close()
sk.close()

# client端
import struct
import socket
sk = socket.socket()
sk.connect(('ip', port))
content  = '我是henry'.encode('utf-8')     # 字节流
size = struct.pack('i', len(content))			# 发送内容长度进行struct
sk.send(size)
sk.send(content)
sk.close()
```

### 4. UDP信息传输

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

#### Note3(2)

1. socket收发的**必须是bytes**类型，经过编码的文件均是bytes类型
2. 网络传输数据一般使用**json**格式

#### 1. UDP不会发生黏包(6)

1. **UDP（user datagram protocol，用户数据报协议）**是无连接的，面向消息的，提供高效率服务。 
2. **不会使用块的合并优化算法**，由于UDP支持的是一对多的模式，所以接收端的skbuff(套接字缓冲区）采用了**链式结构来记录每一个到达的UDP包**，在每个UDP包中就有了消息头（消息来**源地址**，**端口**等信息），这样，对于接收端来说，就容易进行区分处理了。 即**面向消息的通信是有消息保护边界的**。 
3. **对于空消息**：tcp是基于数据流的，于是收发的消息不能为空，这就需要在**客户端**和**服务端**都添加**空消息的处理机制**，防止程序卡住，而udp是基于数据报的，即便是你输入的是空内容（直接回车），也可以被发送，udp协议会帮你封装上消息头发送过去。 
4. **不可靠不黏包的udp**协议：udp的**recvfrom**是**阻塞**的，一个recvfrom(x)必须对唯一一个sendto(y),收完了x个字节的数据就算完成,若是y;x数据就丢失，这意味着udp根本不会粘包，但是会丢数据，不可靠。
5. 用**UDP协议发送**时，用sendto函数最大能发送数据的长度为：**65535- IP头(20) – UDP头(8)＝65507字节**。用sendto函数发送数据时，如果发送数据长度**大于该值，则函数会返回错误**。（丢弃这个包，不进行发送） 
6. 用**TCP协议发送**时**，由于TCP是数据流协议，因此不存在包大小的限制（暂不考虑缓冲区的大小），这是指在用send函数时，**数据长度**参数**不受限制。而实际上，所指定的这段数据并不一定会一次性发送出去，如果这段数据比**较长**，会被**分段发送**，如果比**较短**，可能会等待和下一次数据**一起发送**。

### 5.  socket其他操作

```python
import socket
# 服务端套接字函数
s.bind()    # 绑定(主机,端口号)到套接字
s.listen()  # 开始TCP监听
s.accept()  # 被动接受TCP客户的连接,(阻塞式)等待连接的到来

# 客户端套接字函数
s.connect()     # 主动初始化TCP服务器连接
s.connect_ex()  # connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

# 公共用途的套接字函数
s.recv()            # 接收TCP数据
s.send()            # 发送TCP数据
s.sendall()         # 发送TCP数据

s.recvfrom()        # 接收UDP数据
s.sendto()          # 发送UDP数据

s.getpeername()     # 连接到当前套接字的远端的地址
s.getsockname()     # 当前套接字的地址
s.getsockopt()      # 返回指定套接字的参数
s.setsockopt()      # 设置指定套接字的参数
s.close()           # 关闭套接字

# 面向锁的套接字方法
s.setblocking()     # 设置套接字的阻塞与非阻塞模式
s.settimeout()      # 设置阻塞套接字操作的超时时间
s.gettimeout()      # 得到阻塞套接字操作的超时时间

# 面向文件的套接字的函数
s.fileno()          # 套接字的文件描述符
s.makefile()        # 创建一个与该套接字相关的文件
```

```python
# 官方文档对socket模块下的socket.send()和socket.sendall()解释如下：
socket.send(string[, flags])
Send data to the socket. The socket must be connected to a remote socket. The optional flags argument has the same meaning as for recv() above. Returns the number of bytes sent. Applications are responsible for checking that all data has been sent; if only some of the data was transmitted, the application needs to attempt delivery of the remaining data.
# send()的返回值是发送的字节数量，这个数量值可能小于要发送的string的字节数，也就是说可能无法发送string中所有的数据。如果有错误则会抛出异常。

socket.sendall(string[, flags])
Send data to the socket. The socket must be connected to a remote socket. The optional flags argument has the same meaning as for recv() above. Unlike send(), this method continues to send data from string until either all data has been sent or an error occurs. None is returned on success. On error, an exception is raised, and there is no way to determine how much data, if any, was successfully sent.
# 尝试发送string的所有数据，成功则返回None，失败则抛出异常。

# 故，下面两段代码是等价的：
sock.sendall('Hello world\n')

buffer = 'Hello world\n'
while buffer:
    bytes = sock.send(buffer)
    buffer = buffer[bytes:]        # ？？？？
```

## 8.4 非阻塞模型

- 阻塞io模型，非阻塞io模型，事件驱动io，io多路复用，异步io模型**五种**

### 1. 非阻塞io模型模型

- 利用**tcp**可以实现**并发**
- server端使用setblocking(False)方法进行设置，此时需要使用异常处理
- **客户端下线**时，在**非阻塞**情况下，**msg为空**

```python
# server端
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.setblocking(False)               # 设置为非阻塞状态
sk.listen()

user = []
del_user = []
while True:
    try:
        con, addr = sk.accept()
        user.append(con)
    except BlockingIOError:
        for i in user:
            try:
                content = i.recv(1024).decode('utf-8')
                if not content:
                    del_user.append(i)
                    continue
                i.send(content.upper(). encode('utf-8')) 
                # 发送的bytes类型可以直接解释出(ascii字符)
            except BlockingIOError:pass     # 注意异常，会报错
        for i in del_user:
            user.remove(i)
        del_user.clear()
sk.close()
```

```python
# clinet端
import time
import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
while True:
    sk.send(b'hello')
    msg = sk.recv(1024)
    print(msg)
    time.sleep(0.2)
sk.close()
```

#### Note4(3)

1. socket的非阻塞io模型 + io多路复用实现(**框架实现方式**)
2. 非阻塞提高了cpu利用率，但cpu有效率很低
3. TCP**断开连接**后，只要有数据发送就会**报错**

### 2. 验证客户端的合法性

- 验证客户端的合法性(自动化开发)

```python
# 客户端使用对象是用户，直接登陆验证
	# 可以看到源码,在服务端进行验证登陆
# 客户端使用对象是机器
```

1. **摘要算法：hmac算法**

```python
import hmac
secret_key = b'asdfgh'
random_seq = os.urandom(32)
hmac.new(secret_key, random_seq)
ret = hmac.digest()   # 结果是bytes类型数据
```

2. **使用hmac验证客户端的合法性**

```python
# 使用TCP协议发送数据为空时，默认不会发送
# server端
import os
import hmac
import socket

def chat(con):
    while True:
        msg = con.recv(1024).decode('utf-8')
        print('------>', msg)
        con.send(msg.upper().encode('utf-8'))
        # con.send(''.encode('utf-8'))         # tcp不会发送
        
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

com_key = b'henry'
while True:
    con, addr = sk.accept()
    sec_key = os.urandom(32)
    con.send(sec_key)                 # 第一次发送
    val = hmac.new(com_key, sec_key).digest()
    data = con.recv(32)               # 第一次接收
    if data == val:
        print('客户端合法')
        chat(con)
    else:
        print('客户端不合法')
        con.close()
sk.close()
```

```python
# client 端
import socket
import hmac

def chat(sk):
    while True:
        sk.send('hello'.encode('utf-8'))
        msg = sk.recv(1024).decode('utf-8')
        print('------>', [msg])

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
sec_key = sk.recv(32)      # 第一次接收
com_key = b'henry'
val = hmac.new(com_key, sec_key).digest()
sk.send(val)               # 第一次发送
chat(sk)

sk.close()
```

```python
# 进阶示例
from socket import *
import hmac,os

secret_key=b'henry bang bang bang'
def conn_auth(conn):
    ''' 认证客户端链接'''
    print('开始验证新链接的合法性')
    msg=os.urandom(32)
    conn.sendall(msg)
    h=hmac.new(secret_key,msg)
    digest=h.digest()
    respone=conn.recv(len(digest))
    return hmac.compare_digest(respone,digest)

def data_handler(conn,bufsize=1024):
    if not conn_auth(conn):
        print('该链接不合法,关闭')
        conn.close()
        return
    print('链接合法,开始通信')
    while True:
        data=conn.recv(bufsize)
        if not data:break
        conn.sendall(data.upper())

def server_handler(ip_port,bufsize,backlog=5):
    '''只处理链接'''
    tcp_socket_server=socket(AF_INET,SOCK_STREAM)
    tcp_socket_server.bind(ip_port)
    tcp_socket_server.listen(backlog)
    while True:
        conn,addr=tcp_socket_server.accept()
        print('新连接[%s:%s]' %(addr[0],addr[1]))
        data_handler(conn,bufsize)

if __name__ == '__main__':
    ip_port=('127.0.0.1',9999)
    bufsize=1024
    server_handler(ip_port,bufsize)
```

```python
# 客户端
__author__ = 'Linhaifeng'
from socket import *
import hmac,os

secret_key=b'linhaifeng bang bang bang'
def conn_auth(conn):
    '''验证客户端到服务器的链接'''
    msg=conn.recv(32)
    h=hmac.new(secret_key,msg)
    digest=h.digest()
    conn.sendall(digest)

def client_handler(ip_port,bufsize=1024):
    tcp_socket_client=socket(AF_INET,SOCK_STREAM)
    tcp_socket_client.connect(ip_port)
    conn_auth(tcp_socket_client)
    while True:
        data=input('>>: ').strip()
        if not data:continue					# tcp协议不支持发送数据为空
        if data.lower() == 'q':break

        tcp_socket_client.sendall(data.encode('utf-8'))
        respone=tcp_socket_client.recv(bufsize)
        print(respone.decode('utf-8'))
    tcp_socket_client.close()

if __name__ == '__main__':
    ip_port=('127.0.0.1',9999)
    bufsize=1024
    client_handler(ip_port,bufsize)
```

## 8.5 socketserver模块

#### 1. socketserver模块

```python
# server端
import socketserver       # socket是socketserver的底层模块和time，datetime一样
class Myserver(socketserver.BaseRequestHandler):
  def handle(self):				# 自动触发handle方法，self.request == con
    print(self.request)   # con
server = socketsever.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)
server.server_forever()

# client 
import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
```

#### 2. socketserver模块进阶

```python 
# 进阶示例
import socketserver
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        # self.client_address
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9999
    # 设置allow_reuse_address允许服务器重用地址
    socketserver.TCPServer.allow_reuse_address = True
    # 创建一个server, 将服务地址绑定到127.0.0.1:9999
    server = socketserver.TCPServer((HOST, PORT),Myserver)
    # 让server永远运行下去，除非强制停止程序
    server.serve_forever()
   
# client端
import socket
HOST, PORT = "127.0.0.1", 9999
data = "hello"
# 创建一个socket链接，SOCK_STREAM代表使用TCP协议
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))                # 链接到客户端
    sock.sendall(bytes(data + "\n", "utf-8")) # 向服务端发送数据
    received = str(sock.recv(1024), "utf-8")  # 从服务端接收数据

print("Sent:     {}".format(data))
print("Received: {}".format(received))
```

# 第九章 并发编程

## 9.1 操作系统基础

- 操作系统发展史
- 并发和并行
- 阻塞和非阻塞
- 同步和异步
- 进程：三状态图，唯一标示，开始和结束
- 线程

### 1. 操作系统发展史

#### 1.1 人机矛盾(cpu利用率低)

—>磁带存储+批处理(降低数据的读取时间,提高cpu的利用率)

—>**多道操作系统**：数据隔离、时空复用(能够遇到**I/O**操作的时候主动把cpu让出来，给其他任务使用，切换需要时间，由OS完成)

—> 短作业优先算法、先来先服务算法

—>**分时OS**：时间分片，CPU轮转，每一个程序分配一个时间片，**降低了cpu利用率**，**提高了用户体验**

—>**分时**OS + **多道**OS：多个程序一起执行，遇到IO切换，时间片到了也要切换

- **多道技术介绍**

1. 产生背景：针对单核，实现并发
2. 现在的主机一般是多核，那么每个核都会利用多道技术有4个cpu，运行于cpu1的某个程序遇到io阻塞，会等到io结束再重新调度，会被调度到4个 cpu中的任意一个，具体由操作系统调度算法决定。
3. 空间上的复用：如内存中同时有多道程序
4. 时间上的复用：复用一个cpu的时间片

**Note**：遇到io切，占用cpu时间过长也切，**核心**在于切之前将进程的状态保存下来，这样
才能保证下次切换回来时，能基于上次切走的位置继续运行。  

#### 2.2 操作系统**分类**(4)

**OS作用**：将应用程序对硬件资源的竞态请求变得有序化

- **实时OS**：实时控制，实时信息处理
- **通用OS**：多道、分时、实时处理或其两种以上
- **网络OS**：自带网络相关服务
- **分布式OS**：python中可使用：**celery**模块

### 2. 进程

####2.1 进程：运行中的程序
   - 程序只是一个文件，进程是程序文件被cpu运行
   - 进程是计算机中最小的**资源分配**单位
   - 在OS中有唯一标示符**PID**
####2.2 OS调度算法(4)
   - 短作业优先
   - 先来先服务
   - 时间片轮转
   - **多级反馈算法**：分时+先来先服务+短作业优先
####2.3 并行与并发
   - **并行**：程序分别独占cpu自由执行，看起来同时执行，实际每一个时间点都各自执行
   - **并发**：多个程序占用同一cpu，每个程序交替使用cpu，看起来同时执行，实际上仍是串行



   - **并发**（concurrency）：把任务在不同的时间点交给处理器进行处理。在同一时间点，任务并不会同时运行。
- **并行**（parallelism）：把每一个任务分配给每一个处理器独立完成。在同一时间点，任务一定是同时运行。

### 3. 同步异步阻塞非阻塞

1. **同步**：调用一个函数/方法，需要**等待**这个函数/方法**结束**
   - **一个功能调用时，没有得到结果之前，就不会返回，可以说是一种操作方式。**
2. **异步**：程序同时运行，没有**依赖**和**等待**关系，调用一个方法，**不等待**这个方法**结束**，不关心这个方法做了什么
3. **阻塞**：cpu不工作
   - 阻塞调用是指调用结果返回之前，**当前线程**会被挂起。函数只有在得到结果之后才会返回
4. **非阻塞**：cpu工作
   - 调用指在不能立刻得到结果之前，该调用不会阻塞当前线程。
5. **同步阻塞**
   - con.recv()，socket阻塞的tcp协议
6. **同步非阻塞**
   - 没有io操作的func()
   - socket非阻塞tcp协议； 调用自定义函数(不存在io操作)
7. **异步非阻塞**（重点）
   - 没有io操作，把func扔到其他任务里各自执行，cpu一直工作
8. **异步阻塞**
   - 程序中出现io操作

#### Note1(2)

1. 同步和异步关注的是**消息通信机制** (synchronous communication/ asynchronous communication)
2. 阻塞和非阻塞关注的是**程序在等待调用结果（消息，返回值）时的状态**

### 4. 进程的三状态图

#### 1. 进程状态

**进程状态**：运行(runing)  就绪(ready)  阻塞(blocking)

![进程三状态图](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/%E8%BF%9B%E7%A8%8B%E4%B8%89%E7%8A%B6%E6%80%81%E5%9B%BE.png)

#### 2. 进程的创建与结束

- **进程创建**

1. 系统初始化(**ps**)
2. 一个进程开启了一个子进程(os.fork，subprocess.Popen)
3. 用户交互式请求(用户双击app)
4. 批处理作业的初始化(只在大型机的批处理系统中应用)

- **进程结束**

1. 正常退出
2. 出错退出
3. 严重错误
4. 被其他进程杀死(**kill -9 pid**)



## 9.2 进程

### 1. 进程与线程

#### 1.1 分别做多件事

- 如果是两个程序分别做两件事
  - 起两个进程
- 如果是一个程序，要分别做两件事
  - 起线程，视频软件：下载电影1，电影2，电影3

#### 1.2 进程解析

1. **进程**（Process）是计算机中的程序关于**某数据集合上**的一次运行活动，是系统进行**资源分配和调度**的**基本单位**，是OS结构的基础。

   

2. 在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；在当代**面向线程设计**的计算机结构中，**进程是线程的容器**。程序是指令、数据及其组织形式的描述，**进程是程序的实体。**

3. 顾名思义，进程即正在执行的一个过程。**进程**是对正在运行程序的一个抽象。

4. 进程的概念起源于操作系统，是操作系统最核心的概念，也是操作系统提供的最古老也是最重要的**抽象概念**之一。操作系统的其他所有内容都是围绕进程的概念展开的。

   **PS**：即使可以利用的cpu只有一个（早期的计算机确实如此），也能保证支持（伪）并发的能力。将一个单独的cpu变成多个虚拟的cpu（多道技术：时间多路复用和空间多路复用+硬件上支持隔离），没有进程的抽象，现代计算机将不复存在。

5. **进程概念**

   - 进程是一个程序实体。每**一个进程**都有它自己的**地址空间**，一般情况下，包括**文本区域**（text region）、**数据区域**（data region）和**堆栈**（stack region）。文本区域存储处理器执行的代码；数据区域存储变量和进程执行期间使用的**动态分配**的内存；堆栈区域存储着活动过程调用的**指令和本地变量**。
   - 进程是一个“执行中的程序”。程序是一个没有生命的实体，只有处理器赋予程序生命时（操作系统执行之），它才能成为一个活动的实体，我们称其为进程。
   - 进程是操作系统中最基本、重要的概念。是多道程序系统出现后，为了刻画系统内部出现的动态情况，描述系统内部各道程序的活动规律引进的一个概念,所有**多道程序设计操作系统**都建立在**进程**的基础上。

6. 特点

   - 是计算机中最小的**资源分配单位**，**数据隔离**。
   - 创建、销毁、切换进程时间**开销大**

#### 1.3 线程

1. 线程是进程中的一部分，不能脱离进程存在
2. 任何进程中至少有一个线程，**只**负责执行代码，不负责存储共享的数据，也不负责资源分配
3. **进程**负责数据隔离
4. **线程**负责执行代码，共享**全局资源**
5. 进程是计算机中最小资源分配单位
6. **线程**是计算机中能被**cpu调度的最小单位**
   - 爬虫使用需要配合前端
7. 一个进程中的多个线程可以共享这个进程的数据——  数据共享

#### 1.4 开销

1. 线程的创建和销毁
   - 需要一些开销(一个存储局部变量的数据结构，记录状态)
   - 创建、销毁、切换**开销**远**远小于**进程
2. python中的线程比较特殊，所以进程也有可能被用到
3. **进程**：数据隔离、开销大  同时执行几段代码
4. **线程**：数据共享、开销小  同时执行几段代码

### 2. 进程的创建

​      仔细说来，multiprocess不是一个模块而是python中一个操作、管理进程的包。 之所以叫multi是取自multiple的多功能的意思,在这个包中几乎包含了和进程有关的所有子模块。由于提供的子模块非常多，为了方便大家归类记忆，我将这部分大致分为四个部分：**创建进程**部分，**进程同步**部分，**进程池**部分，进程之间**数据共享**。

#### 2.1 multiprocessing

- 基于process模块

```python
# 获取进程的pid, 父进程的id及ppid
import os
import time
print('start')
time.sleep(20)
print(os.getpid(),os.getppid(),'end')
```

#### 2.2 子进程和父进程

1. pycharm中启动的所有py程序都是pycharm的子进程

```python
# 把func函数交给子进程执行
import os
import time
from multiprocessing import Process

def func():
  print('start', os.getpid())
  time.sleep(1)
  print('end', os.getpid())

if __name__ == '__main__':	  
  p = Process(target=func)				# 创建一个即将要执行的进程对象
  p.start()	                      # 开启一个进程，异步非阻塞
  p.join()												# 同步阻塞，直到子进程执行完毕
  print('main', os.getpid())			# 异步的程序，调用开启进程的方法，并不等待这个进程的开启
```

2. **创建子进程注意**

ps：_\_name__ 只有两种情况，**文件名**或**双下划线**main字符串

```python
# windows
通过（模块导入）执行父进程文件中的代码获取父进程中的变量
只要是不希望被子进程执行的代码，就写在if __name__ == '__mian__'下
进入导入时，父进程文件中的 __name__ != '__mian__'
# linux/macos
创建新的子进程是copy父进程内存空间，完成数据导入工作（fork）,正常写就可以

公司开发环境都是linux，无需考虑win中的缺陷
# windows中相当于把主进程中的文件又从头执行了一遍

# linux，macos不执行代码，直接执行调用的函数在Windows操作系统中由于没有fork(linux操作系统中创建进程的机制)，在创建子进程的时候会自动 import 启动它的这个文件，而在 import 的时候又执行了整个文件。因此如果将process()直接写在文件中就会无限递归创建子进程报错。所以必须把创建子进程的部分使用if __name__ ==‘__main__’ 判断保护起来，import 的时候  ，就不会递归运行了。
```

- 父进程(主进程)存活周期

![父子进程](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/%E7%88%B6%E5%AD%90%E8%BF%9B%E7%A8%8B.png)

#### Note2(5)

1. 进程之间不能共享内存
2. 主进程需要等待子进程结束，主进程负责**创建**和**回收**子进程
3. 子进程执行结束，若父进程没有回收资源，即**僵尸**进程。
4. 主进程结束逻辑：主进程**代码结束**、所有子进程结束、回收子进程资源、主**进程结束**
5. **进程里面无法进行input**：所有print都是向文件里**写**数据

#### 2.3 join方法

- 把一个进程的结束事件封装成一个join方法
- 执行join方法效果，**阻塞**，直到子进程结束，就结束
- 所有的进程执行的先后是由**OS控制的**

```python
# 在多个子进程中使用join方法
from multiprocessing import Process
def send_mail(i):
    print('邮件已发送', i)
if __name__ == '__main__':
    li = []
    for i in range(10):
        p = Process(target=send_mail, args=(i,))  # args必须是元组，给子进程中的函数传参数
        p.start()
    li.append(p)
    for p in li: p.join()													# 阻塞，知道所有子进程执行完毕
    print('100封邮件已发送')
# 主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程 
```



## 9.3 锁&进程间通信

### 1. Process类

#### 1.1 守护进程

- 生产者消费者模型
- 和守护线程做对比

 **p.daemon**：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置

```python
import time
from multiprocessing import Process

def son1():
  	while True:
        print('is alive')
        time.sleep(0.5)
    
def son2():
  	for i in range(5):
      print('in son2')
      time.sleep(1)
              
if __name__ == '__main__':
    p = Process(target=son1)
    p.daemon = True                    # 把p子进程设置成了守护进程															 
    p.start()
    p2 = Process(target=son2)
    p2.start()
    time.sleep(2)
# 守护进程是随着主进程‘代码’结束而结束
# 所有子进程都必须在主进程结束之前结束
# 守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
```

#### 1.2 Process的方法

- p.terminate(), p.is_alive()
- **异步非阻塞**
  - 使用terminate方法后，再查看进程是否还存活时，会发现进程还存活，并没有等待OS关闭进程，说明terminate方法请求后，程序会继续执行

```python
import time
from multiprocessing import Process

def son1():
  	while True:
        print('is alive')
        time.sleep(0.5)
              
if __name__ == '__main__':
    p = Process(target=son1)
    p.start()                   # 开启了一个进程
  	print(p.is_alive)           # 判断子进程时候存活, Ture和False
    time.sleep(1)
    p.terminate()               # “异步非阻塞”，强制结束一个子进程
    print(p.is_alive)           # True，os还没来得及关闭进程
   	time.sleep(0.01)
    print(p.is_alive)           # False，OS已经响应了关闭进程的需求，再去检测的时候，结果是进程已经结束
```

#### 1.3 面向对象开启进程

- 当创建子进程需要传参时，需要使用**super()._\_init__()**

```python 
import os
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, x, y):   # 子进程如果不需要参数，可以省略
        self.x = x
        self.y = y
        super().__init__()        
        
    def run(self):
        while True:
            print(self.x, self.y, os.getpid())
            print('in myprocess')

if __name__ == '__main__':
    mp = MyProcess(1, 2)
    mp.daemon = True
    mp.start()                  # 开启一个子进程，会调用run()方法
    time.sleep(1)
    mp.terminate()							# 结束进程，异步非阻塞						
    print(mp.is_alive())				# True
    time.sleep(0.01)				
    print(mp.is_alive())				# False
```

- p.join() : 同步阻塞
- p.terminate() 和 p.start()：异步非阻
- p.is_alive()：获取当前进程状态
- daemon = True：设置为守护进程，守护进程在主进程代码执行结束而结束

### 2. 锁

1. 在并发的场景下，设计某部分的内容

   - 需要修改一些所有进程共享数据资源

   - 需要加锁来维护数据的安全

2. 在数据安全的基础上，才考虑效率问题

   - with lock：内部会有异常处理
   - 在主进程中进行实例化
   - 把锁传递给子进程

3. 在子进程中对需要加锁的代码进行with lock

   - with lock相当于lock.acquire()和lock.release()

4. 需要加锁的场景

   - 操作共享的数据资源
   - 对资源进行修改操作
   - 加锁之后能够保证数据的安全性，但会降低程序执行效率

```python 
# 数据操作时，不能同时进行修改
import json
from multiprocessing import Process, Lock             # 导入Lock

def search_ticket(user):
    with open('tickets.txt') as f:
        dic = json.load(f)
        print('%s查询结果：%s张余票' %(user, dic['count']))

def buy_ticket(user, lock):
    # with lock:
    lock.acquire()
    # time.sleep(0.01)
    with open('tickets.txt') as f:
        dic = json.load(f)
    if dic["count"] > 0:
        print('%s已买到票' % user)
        dic["count"] -= 1
    else:
        print('%s没买到票' % user)
    with open('tickets.txt', 'w') as f:
        json.dump(dic, f)
    lock.release()


if __name__ == '__main__':
    lock = Lock()                                      # 实例化一个对象
    for i in range(10):
      	search_ticket('user%s '%(i+1),)
        p = Process(target=buy_ticket, args=('user%s '%(i+1), lock))
        p.start()
```

### 3. 进程间的通信

#### 3.1 进程间数据隔离

```python
from multiprocessing import Process
n = 100
def func():
	global n
  n -= 1
 
li = []
for i in range(10):
  p = Process(target=func)
  p.start()
  li.append(p)
  
 for p in li:p.join()
 print(n)
```

#### 3.2 进程间通信

- 文件或网络只有这两种
- 进程间通信(**IPC**， inter-process communication):**Queue和Pipe**
- **Queue(3)**：先进先出，文件家族的**socket**，写文件基于**pickle**，基于**Lock**
  - 数据安全，**Pipe**管道：天生数据不安全（socket通信）
  - Queue = **Pipe**(socket + picket)**+Lock**
- **第三方提供(5)**：redis，memcache，kafka，rabbitmq（消息中间件(消息转发)）
  - 并发需求
  - 高可用
  - 实现集群的概念
  - 断电保存数据
  - 解耦

```python
from multiprocessing import Process,Queue

def func(exp,q):
    res = eval(exp)
    q.put(res)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=func, args=('1+2+3',q))
    p.start()
    print(q.get())
```

```python
from multiprocessing import Pipe
pip = Pipe()
pip.send()
pip.recv()
```

```python
# Process中的队列
import queue
from multiprocessing import Queue
q = Queue(3)													# 可设置队列长度
q.put(1)
q.put(2)															# 对列为满时，继续放数据会发生阻塞
q.put(3)
print('----------')
try:
	q.put_nowait(4)                     # 对列为满时，继续放数据会报错和丢失
except queue.Full:pass
print('----------')

q.get()
q.get()
q.get()                                # 对列为空时，会发生阻塞
try:
	q.get_nowait()											 # 对列为空时，会报错，阻塞会取消
except queue.Empty:pass
```

```python
q.empty()                              # 有缺陷
q.qsize()
q.full()
```



## 9.4 cp模型&操作线程

### 1. 生产者消费者模型

#### 1.1 程序的解藕

- 把写在一起的功能分开成多个小的功能处理
  - 修改和复用，增加可读性
  - 计算速度有差异，执行效率最大化，节省进程

- **生产者**：生产数据
- **消费者**：处理数据

![生产者消费者模型](/Users/henry/Documents/截图/Py截图/生产者消费者模型.jpg)

#### 1.2 生产者和消费者

1. 一个进程就是一个生产者/消费者
2. 生产者和消费者之间的容器就是队列(**队列有大小，控制内存消耗**)

```python
# 生产者消费者模型示例
import time
import random
from multiprocessing import Process, Queue

def producer(q, name, food):
    for i in range(10):
        time.sleep(random.random())
        fd = '%s%s' % (food, i)
        q.put(fd)
        print('%s生产了一个%s' % (name, food))

def consumer(q, name):
    while True:
        food = q.get()
        if not food:
            q.put(None)
            break
        time.sleep(random.randint(1, 3))
        print('%s吃了%s' % (name, food))

def cp(num1, num2):
    q = Queue(10)
    p_l = []
    for i in range(num1):
        p = Process(target=producer, args=(q, 'henry', 'food'))
        p.start()
        p_l.append(p)
    for i in range(num2):
        c = Process(target=consumer, args=(q, 'echo%s' % (i+1,)))
        c.start()
    for i in p_l:
        i.join()
    q.put(None)

if __name__ == '__main__':
    cp(1, 4)
```

```python
# 生产者消费者模型示例之爬虫
import re
import requests
from multiprocessing import Process, Queue

def producer(q, url):
    response = requests.get(url)
    q.put(response.text)

def consumer(q):
    while True:
        s = q.get()
        if not s:
            q.put(None)
            break
        com = re.compile(
            '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
            '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)
        ret = com.finditer(s)
        for i in ret:
            print({
                "id": i.group("id"),
                "title": i.group("title"),
                "rating_num": i.group("rating_num"),
                "comment_num": i.group("comment_num"),
            })

if __name__ == '__main__':
    count = 0
    q = Queue()
    p_l = []
    for i in range(10):
        count += 25
        p = Process(target=producer, args=(q, 'https://movie.douban.com/top250?start=%s&filter=' % count))
        p.start()
        p_l.append(p)
    for i in range(5):
        c = Process(target=consumer, args=(q,))
        c.start()
    for i in p_l:
        i.join()
    q.put(None)
```

#### 1.3 joinablequeue

1. **q.join()**：阻塞，知道队列中所有内容被取走且**q.task_done**
   - 生产者将使用此方法进行阻塞，直到队列中所有项目均被处理。阻塞将持续到为队列中的每个项目均调用
2. 先设置消费者为守护进程
   - **c.daemon = True**
3. 阻塞生产者
   - 其中的队列阻塞结束后，才会结束
4. 在生产者中使用阻塞队列
   - 阻塞一结束，所有数据都已经消费完
5. 队列阻塞结束代表消费者，把所有生产数据消费完（**jq.taks_done()操作**）
   - 使用者使用此方法发出信号，表示q.get()返回的项目已经被处理。如果调用此方法的次数大于从队列中删除的项目数量，将引发**ValueError**异常。

![joinable_queue](/Users/henry/Documents/截图/Py截图/joinable_queue.png)

![joinable逻辑](/Users/henry/Documents/截图/Py截图/joinable逻辑.png)

```python
# joinable实现生产者、消费者模型
import time
import random
from multiprocessing import Process,JoinableQueue

def producer(q, name, food):
  for i in range(10):
    time.sleep(random.random())
    fd = '%s%s'%(food,i)
    print('%s生产了一个%s'%(name, food))
  q.join()

def consumer(q, name, food):
  while True:
    food = q.get()
    if not food:
      q.put(None)
      break
    time.sleep(random.randint(1, 3))
    print('%s吃了%s'%(name, food))
    q.task_done()
 
if __name__ = '__main__':
  jq = JoinableQueue()
  p = Processor(target=producer, args=(jq, 'henry', 'food'))
  p.start()
```

### 2. 进程间数据共享

1. 与数据共享相关：**Manager模块**(Manager().list(), Manager().Queue)
2. multiprocessing 中有一个manager类
3. 封装了所有和进程相关的数据共享、数据传递
4. 但是对于dict、list这类进行数据操作时，会产生数据不安全
5. m = Manager()也可以使用with Manager() as m:

```python
# 进程间数据是独立的，可以借助于队列或管道实现通信，二者都是基于消息传递的
# 虽然进程间数据独立，但可以通过Manager实现数据共享，事实上Manager的功能远不止于此
A manager object returned by Manager() controls a server process which holds Python objects and allows other processes to manipulate them using proxies.

A manager returned by Manager() will support types list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array.
```

```python
from mutliprocessing import Manager,
def func(dic, lock):
  with lock:
		dic['count'] -= 1

if __name__ = '__main__':
  # m = Manager()
  lock = Lock
  with Manager() as m:
    l = Lock()
    dic = m.dict({'count': 100})    							# 共享的dict
    p_l = []
    for i in range(100):
      p = Process(target=func, args=(dic,lock))
      p.start()
      p_l.append(p)
    for p in p_l:p.join()
    print(dic)
```

### 3. 线程

- cpython解释器当中的线程问题

- https：加证书，需要购买
- **四核八线程**
  - 每个核心被虚拟成两个核心，可以同时执行8个线程。
  - 如果是计算复杂数据，会转换到四核

#### 3.1垃圾回收机制

1. **cpython**解释器不能实现多线程利用多核
2. 垃圾回收机制(gc)：**引用计数** + **分代回收**
   - 专门有一条线程完成垃圾回收机制，对每一个在程序中的变量**统计引用计数**

#### 3.2 GIL锁

**GIL**(global interpreter lock)：**全局解释器锁**

1. 保证了整个python程序中，只能有一个线程被CPU执行
   - 导致了py程序不能并行
   - 使用多线程并不影响高IO型操作，只会对高计算型程序有效率的影响
   - 遇到高计算：多进程+多线程，分布式
2. 原因：**cpython**解释器中特殊的垃圾回收机制
3. cpython、pypy，jpython(先翻译为java字节码，在java上执行)、iron python

#### 3.3 遇到IO操作的时候

1. 5-6亿条cpu指令
2. 5-6cpu指令 == 一句python代码
3. 几千万条python代码

#### 3.4 web框架几乎都是多线程

- 利用IO操作，类似多道系统

### 4. python操作线程(重点)

#### 4.1 开启线程

- 使用**Threading**类

```python
# multiprocessing 是完全仿照Threading类的
import os
import time
from threading imoprt Thread
def func():
  print('start son thread')
  time.sleep(1)
  print('end son thread', os.getpid())
  
Thread(target=func).start()                 # 开启一个线程的速度非常快
print('start')
time.sleep(0.5)
print('end', os.getpid())
```

```python
# 开启多个线程
import os
import time
from threading imoprt Thread
def func():
  print('start son thread')
  time.sleep(1)
  print('end son thread', os.getpid())
 
for i in range(10):
  Thread(target=func).start()                 # 开启一个线程的速度非常快
  																					  # 线程的调度由OS决定
```

#### 4.2 join方法

1. join阻塞知道子线程执行结束

- **主线程**如果结束了，**主进程**也就结束了
- **主线程**需要等待**所有子线程结束**才能结束

```python
import os
import time
from threading imoprt Thread
def func():
    print('start son thread')
    time.sleep(1)
    print('end son thread', os.getpid())

t_l = []
for i in range(10):
    t = Thread(target=func)
    t.start()
    t_l.append(t)
for i in t_l:i.join()
print('子线程执行结束')
```

#### 4.3 面向对象启动线程

```python
from threading import Thread

class MyThread(Thread):
    def __init__(self, i):
        self.i = i
        super().__init__()               # 注意变量名避免与父类init中的变量重名  

    def run(self):
        print(self.i, self.ident)        # 通过self.ident，查看子线程的id

t_l = []
for i in range(100):
    t = MyThread(i)
    t_l.append(t)
    t.start()                             # start 方法封装了开启线程的方法和run方法

for t in t_l: t.join()
print('主进程结束')       
```

#### 4.4 线程中的其他方法

```python
from threading import current_thread, enumerate, active_count

def func():
    print('start son thread', i , current_thread.ident)
    time.sleep(1)
    print('end son thread', os.getpid())

t = Thread(target=func)
t.start()
print(t.ident)
print(current_thread().ident)   # current_ident()在哪个线程，就得到这个线程id
print(enumerate())					    # 统计当前进程中多少线程活着，包含主线程
print(active_count())				    # 统计当前进程中多少线程活着，个数，包含主线程
                                # 线程中不能从主线程结束一个子线程
```

#### 4.5 效率差

```python
import time
from threading import Thread
from multiprocessing import Process
def func(a, b):
  	c = a + b
 
if __name__ == '__main__':
    p_l = []
    start = time.time()
    for i in range(100):
        p = Process(target=func, args=(i, i*2))
        p.start()
        p_l.append(p)
     for i in P_l:i.join()
     print(time.time() - start)
    
     t_l = []
     start = time.time()
     for i in range(100):
         t = Thread(target=func, args=(i, i*2))
         t.start()
         t_l.append(t)
     for i in t_l:i.join()
     print(time.time() - start)
```

#### 4.6 数据共享

```python
# 不要在子线程里随便修改全局变量
from threading import Thread
n = 100
def son():
  global n
  n -= 1

t_l = []
for i in range(100):
		t = Thread(target=son)
    t_l.append(t)
    t.start()
    
for t in t_l:t.join()
print(n)
```

#### 4.7 守护线程

- 守护线程会一直等到所有非守护线程结束之后才结束
- 除了**守护主线程**的代码之外，也会**守护子线程**
- 只要有非守护线程存在，主进程就不会结束

```python
import time
from threading imoprt Thread
def son():
  	while True:
      		time.sleep(0.5)

def son2():
  	for i in range(5):
      
t = Thread(target=son)
t.daemon = True
t.start()
time.sleep(3)
```

#### Note(4)

1. 对主进程来说，运行完毕指的是主进程代码运行完毕
2. 对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程执行完毕
3. 主进程在其代码结束后就已经运行完毕了（守护进程在此时就被回收），然后主进程会一直等非守护进程都运行完毕后回收子进程资源（否则会产生僵尸进程），才会结束
4. 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收），因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。





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