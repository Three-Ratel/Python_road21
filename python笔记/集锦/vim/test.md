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
     - ethernet规定接入internet的设备都必须具备网卡，发送端和接收端的地址便是指网卡的地址，即**mac地址**。
   - mac地址：每块网卡出厂时都被**烧制**上一个世界唯一的mac地址，长度为48位2进制，通常由12个16进制数表示（**前六位是厂商编号**，后六位是流水线号）
2. **交换机(4)**
   - **功能**：负责局域网通信（只识别mac地址，通过arp/ rarp协议）
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
   - **语法、语义、时序**
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
6. **长连接**：会一直占用双方**port**
7. I/O：相对于**内存**来说
   - write 是 send
   - read 是 recv
   - i input 向内存中输入 **input**，**read**，**recv**， **recvfrom**， **accept**， **connect**， **close**
   - output 从内存中输出 **print**，**write**，**send**，**sendto**， **accept**， **connect**， **close**

![TCP](/Users/henry/Documents/截图/Py截图/TCP.png)

### 2. UDP协议

1. **UDP**（User Datagram Protocol）不可靠的、无连接的服务，传输效率高（发送前时延小），一对一、一对多、多对一、多对多、面向报文，尽最大努力服务，无拥塞控制。
2. 场景**：即时通讯（qq，wechat），域名系统 (DNS)；视频流；IP语音(VoIP)。
3. **特点**：面向数据报，不可靠，传输速度快，能完成一对多，多对一，和一对一的高效通信

#### Note1(3)

1. TCP传输**数据几乎没有限制**，UDP能够传递数据长度是有限的，是根据数据传递设备的设置有关
2. Tcp可靠**长**连接，udp不可靠无连接
3. 三次握手时，确认信息和请求连接信息合并为一帧，四次挥手，主动断开端，不能确定另一端是否还需要传输信息，所以不能合并。

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
6. 用**TCP协议发送**时**，由于TCP是数据流协议，因此不存在包大小的限制（暂不考虑缓冲区的大小），这是指在用send函数时**，数据长度**参数**不受限制。而实际上，所指定的这段数据并不一定会一次性发送出去，如果这段数据比**较长**，会被**分段发送**，如果比**较短**，可能会等待和下一次数据**一起发送**。

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

### 1. socketserver模块

```python
# server端
import socketserrever       # socket是socketserver的底层模块和time，datetime一样
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

### 2. socketserver模块进阶

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

