## 今日内容

1. 什么是黏包现象？

- 为了减少tcp协议中的'确认收到'的网络延迟时间 
- **发送端**：由于两个数据的发送时间间隔短+数据长度小，tcp协议的优化机制将两条信息作为一条信息发送出去
- **接收端**：由于tcp协议中所传输的数据无边界，来不及接收的多条数据会在接收端内核的缓存端黏在一起
- **本质**：接收信息的边界不清晰

2. 解决黏包问题

- 自定义协议：首先发送报头(**4**bytes) ，内容是即将发送报文字节长度
  - struct：把所有数字都固定的转换为4bytes
  - 再发送数据信息

3. tcp：面向连接、可靠、流式传输的全双工通信

   udp：面向数据报，不可靠，传输速度快，能完成一对多，多对一，和一对一的高效通信

   - 即时通信
   - 在线视频

4. 三次握手

   - sercer **accept** 接收过程中等待客户端的连接
   - **connect** 会发送一个syn连接请求
     - 如果收到了server响应ack和由server端发来的syn连接请求
     - client端进行回复ack信息后，建立了一个tcp连接
   - 三次握手过程在代码过程中是由accept和connect共同完成，具体细节在socket没有体现

5. 四次挥手

   - server 端和clinet端在代码中都有**close**方法，每一端发起的close操作都是断开**fin**请求，得到断开确认**ack**之后，就可以结束一端的数据发送
   - 如果两端发起close请求，那么就是**两次请求**和**两次确认**，一共是四次操作
   - 可以结束数据发送，表示连接断开

## 内容详情

1. Socket **阻塞**和**非阻塞**，利用tcp可以实现并发通信的socket server
2. 验证客户端的合法性(自动化开发)
3. socketsever模块 直接实现tcp可并发的server端



## 1. 模型

阻塞io模型，非阻塞io模型，事件驱动io，io多路复用，异步io模型**五种**。

**非阻塞io模型**

```python
# server端
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.setblocking(False)         # 设置为非阻塞状态
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
                i.send(content.upper().encode('utf-8')) 
                # 发送的bytes类型可以直接解释出(ascii字符)
            except BlockingIOError:pass     # 注意异常，会报错
        for i in del_user:
            user.remove(i)
        del_user.clear()
sk.close()
```

```python
# clinet端
import socket
import time
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
while True:
    sk.send(b'hello')
    msg = sk.recv(1024)
    print(msg)
    time.sleep(0.2)
sk.close()
```

- socket的非阻塞io模型 + io多路复用实现(框架)
- 非阻塞提高了cpu利用率，cpu有效率很低

**验证客户端的合法性**

```python
# 客户端使用对象是用户，直接登陆验证
	# 可以看到源码
# 客户端使用对象是机器
```

**摘要算法：hmac算法**

```python
import hmac
secret_key = b'asdfgh'
random_seq = os.urandom(32)
hmac.new(secret_key, random_seq)
ret = hmac.digest()   # 结果是bytes类型数据
```

**使用hmac验证客户端的合法性**

```python
# 使用TCP协议发送数据为空时，默认不会发送
# server端
import os
import socket
import hmac

def chat(con):
    while True:
        msg = con.recv(1024).decode('utf-8')
        print('------>', msg)
        con.send(msg.upper().encode('utf-8'))
        # con.send(''.encode('utf-8'))
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

com_key = b'henry'
while True:
    con, addr = sk.accept()
    sec_key = os.urandom(32)
    con.send(sec_key)          # 第一次发送
    val = hmac.new(com_key, sec_key).digest()
    data = con.recv(32)   # 第一次接收
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
sk.send(val)             # 第一次发送
chat(sk)

sk.close()
```

**socketserver模块**

```python
# server端
import socketserver  # socket是socketserver的底层模块和time，datetime一样
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











