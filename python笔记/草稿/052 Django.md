## 1. web框架的本质

### 1.1 本质

- 实现socket服务端

```python
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8000))
sk.listen(5)
while True:
	con, addr = sk.accept()
  # 接收数据
  msg = con.recv(1024).decode('utf-8')
  # 返回数据
  con.send(b'ok')
  # 断开链接
  con.close()
sk.close()
```

### 1.2 返回html文件

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
from socket import SOL_SOCKET, SO_REUSEADDR
sk = socket.socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8000))
sk.listen(5)

def home(url):
    with open('./html/home.html', 'rb') as f:
        data = f.read()
    return data

def index(url):
    with open('./html/index.html', 'rb') as f:
        data = f.read()
    return data

url_li = {'/index': index, '/home': home}

while True:
    con, addr = sk.accept()
    data = con.recv(1024).decode('utf-8')
    url = data.split()[1]
    con.send(b'HTTP/1.1 200 ok\r\n\r\n')
    if url_li.get(url):
        data = url_li[url](url)
    else:
        data = b'404 not found'
    con.send(data)
    con.close()
sk.close()
```

### 1.3 返回动态网页

```python
# 返回动态页面
def home(url):
    with open('./html/home.html', 'r', encoding='utf-8') as f:
        data = f.read().replace('@@time@@', time.strftime('%H:%M:%S')).encode('utf-8')
    return data
url_li = {'/home': home}

while True:
    con, addr = sk.accept()
    data = con.recv(1024).decode('utf-8')
    url = data.split()[1]
    con.send(b'HTTP/1.1 200 ok\r\n\r\n')
    if url_li.get(url):
        data = url_li[url](url)
    else:
        data = b'404 not found'
    con.send(data)
    con.close()
sk.close()
```

### 1.2 HTTP

#### 1. http简介

1. 超文本传输协议（英文：Hyper Text Transfer Protocol，HTTP）是一种用于分布式、协作式和超媒体信息系统的应用层协议。HTTP是万维网的数据通信的基础。HTTP有很多应用，但最著名的是用于web浏览器和web服务器之间的双工通信。
2. HTTP的发展是由**蒂姆·伯纳斯-李**于1989年在欧洲核子研究组织（CERN）所发起。HTTP的标准制定由万维网协会（World Wide Web Consortium，W3C）和互联网工程任务组（Internet Engineering Task Force，IETF）进行协调，最终发布了一系列的RFC，其中最著名的是1999年6月公布的 RFC 2616，定义了HTTP协议中现今广泛使用的一个版本——HTTP 1.1。
3. 2014年12月，互联网工程任务组（IETF）的Hypertext Transfer Protocol Bis（httpbis）工作小组将HTTP/2标准提议递交至IESG进行讨论，于2015年2月17日被批准。 HTTP/2标准于2015年5月以RFC 7540正式发表，取代HTTP 1.1成为HTTP的实现标准。

1. hyper-text transfer protocol
2. 当前http1.1普及度最广
3. http默认端口为80
4. 请求—应答（一次请求对应一次应答）

#### 2. 协议概述

1. HTTP是一个客户端终端（用户）和服务器端（网站）请求和应答的标准（TCP）。通过使用网页浏览器、网络爬虫或者其它的工具，客户端发起一个HTTP请求到服务器上指定端口（默认端口为80）。我们称这个客户端为用户代理程序（user agent）。应答的服务器上存储着一些资源，比如HTML文件和图像。我们称这个应答服务器为源服务器（origin server）。在用户代理和源服务器中间可能存在多个“中间层”，比如代理服务器、网关或者隧道（tunnel）。
2. 尽管TCP/IP协议是互联网上最流行的应用，HTTP协议中，并没有规定必须使用它或它支持的层。事实上，HTTP可以在任何互联网协议上，或其他网络上实现。HTTP假定其下层协议提供可靠的传输。因此，任何能够提供这种保证的协议都可以被其使用。因此也就是其在TCP/IP协议族使用TCP作为其传输层。
3. 通常，由HTTP客户端发起一个请求，创建一个到服务器指定端口（默认是80端口）的TCP连接。HTTP服务器则在那个端口监听客户端的请求。一旦收到请求，服务器会向客户端返回一个状态，比如"HTTP/1.1 200 OK"，以及返回的内容，如请求的文件、错误消息、或者其它信息。

#### 3. 工作原理

1. HTTP协议定义Web客户端如何从Web服务器请求Web页面，以及服务器如何把Web页面传送给客户端。HTTP协议采用了请求/响应模型。客户端向服务器发送一个请求报文，请求报文包含请求的方法、URL、协议版本、请求头部和请求数据。服务器以一个状态行作为响应，响应的内容包括协议的版本、成功或者错误代码、服务器信息、响应头部和响应数据。
2. 以下是 HTTP **请求/响应的步骤**
   1. 客户端连接到Web服务器
      一个HTTP客户端，通常是浏览器，与Web服务器的HTTP端口（默认为80）建立一个TCP套接字连接。
   2. 发送HTTP请求
      通过TCP套接字，客户端向Web服务器发送一个文本的请求报文，一个请求报文由请求行、请求头部、空行和请求数据4部分组成。
   3. 服务器接受请求并返回HTTP响应
      Web服务器解析请求，定位请求资源。服务器将资源复本写到TCP套接字，由客户端读取。一个响应由状态行、响应头部、空行和响应数据4部分组成。
   4.  释放连接TCP连接
      若connection 模式为close，则服务器主动关闭TCP连接，客户端被动关闭连接，释放TCP连接;若connection 模式为keepalive，则该连接会保持一段时间，在该时间内可以继续接收请求;
   5. 客户端浏览器解析HTML内容
      客户端浏览器首先解析状态行，查看表明请求是否成功的状态代码。然后解析每一个响应头，响应头告知以下为若干字节的HTML文档和文档的字符集。客户端浏览器读取响应数据HTML，根据HTML的语法对其进行格式化，并在浏览器窗口中显示。
3. 在浏览器**地址栏键入URL**，按下回车之后会经历以下流程：
   1. 客户端连接到Web服务器
      一个HTTP客户端，通常是浏览器，与Web服务器的HTTP端口（默认为80）建立一个TCP套接字连接。
   2. 发送HTTP请求
      通过TCP套接字，客户端向Web服务器发送一个文本的请求报文，一个请求报文由**请求行、请求头部、空行和请求数据4部分**组成。
   3. 服务器接受请求并返回HTTP响应
      Web服务器解析请求，**定位请求资源**。服务器将资源复本写到TCP套接字，由客户端读取。一个**响应由状态行、响应头部、空行和响应数据4部分**组成。
   4.  释放连接TCP连接
      若connection 模式为close，则服务器主动关闭TCP连接，客户端被动关闭连接，释放TCP连接;若connection 模式为keepalive，则该连接会保持一段时间，在该时间内可以继续接收请求;
   5. 客户端浏览器解析HTML内容
      客户端浏览器首先解析状态行，查看表明请求是否成功的状态代码。然后解析每一个响应头，响应头告知以下为若干字节的HTML文档和文档的字符集。客户端浏览器读取响应数据HTML，根据HTML的语法对其进行格式化，并在浏览器窗口中显示。

#### 4. 请求方法

HTTP/1.1 协议规定了八种方法(动作)

1. HTTP/1.1协议中共定义了八种方法（也叫“动作”）来以不同方式操作指定的资源：

   ### GET

   向指定的资源发出“显示”请求。使用GET方法应该只用在读取数据，而不应当被用于产生“副作用”的操作中，例如在Web Application中。其中一个原因是GET可能会被网络蜘蛛等随意访问。

   ### HEAD

   与GET方法一样，都是向服务器发出指定资源的请求。只不过服务器将不传回资源的本文部分。它的好处在于，使用这个方法可以在不必传输全部内容的情况下，就可以获取其中“关于该资源的信息”（元信息或称元数据）。

   ### POST

   向指定资源提交数据，请求服务器进行处理（例如提交表单或者上传文件）。数据被包含在请求本文中。这个请求可能会创建新的资源或修改现有资源，或二者皆有。

   ### PUT

   向指定资源位置上传其最新内容。

   ### DELETE

   请求服务器删除Request-URI所标识的资源。

   ### TRACE

   回显服务器收到的请求，主要用于测试或诊断。

   ### OPTIONS

   这个方法可使服务器传回该资源所支持的所有HTTP请求方法。用'*'来代替资源名称，向Web服务器发送OPTIONS请求，可以测试服务器功能是否正常运作。

   ### CONNECT

   HTTP/1.1协议中预留给能够将连接**改为管道方式**的代理服务器。通常用于**SSL加密服务器的链接**（经由非加密的HTTP代理服务器）。

#### Note(2)

1. 方法名称是区分大小写的。当某个请求所针对的资源不支持对应的请求方法的时候，服务器应当返回状态码405（Method Not Allowed），当服务器不认识或者不支持对应的请求方法的时候，应当返回状态码501（Not Implemented）。
2. HTTP服务器至少应该实现GET和HEAD方法，其他方法都是可选的。当然，所有的方法支持的实现都应当匹配下述的方法各自的语义定义。此外，除了上述方法，特定的HTTP服务器还能够扩展自定义的方法。例如PATCH（由 RFC 5789 指定的方法）用于将局部修改应用到资源*。*

#### 5. 状态码(5)

- 所有HTTP响应的第一行都是状态行，依次是当前HTTP版本号，3位数字组成的状态代码，以及描述状态的短语，彼此由空格分隔。

1. 状态代码的第一个数字代表当前响应的类型
   1. **1xx消息**——请求已被服务器接收，继续处理
   2. **2xx成功**——请求已成功被服务器接收、理解、并接受
   3. **3xx重定向**——需要后续操作才能完成这一请求，当前服务器无法处理，响应另一个服务地址
   4. **4xx请求错误**——请求含有词法错误或者无法被执行，没有改资源，402表示认证错误、403表示权限不够
   5. **5xx服务器错误**——服务器在处理某个正确请求时发生错误

- 虽然 RFC 2616 中已经推荐了描述状态的短语，例如"200 OK"，"404 Not Found"，但是WEB开发者仍然能够自行决定采用何种短语，用以显示本地化的状态描述或者自定义信息。

#### 6. URL(统一资源定位符)

- http:默认端口是80(可省略)，https默认是443

1. 超文本传输协议（HTTP）的统一资源定位符将从因特网获取信息的五个基本元素包括在一个简单的地址中：
   1. 传送协议。
   2. 层级URL标记符号(为[//],固定不变)
   3. 访问资源需要的凭证信息（可省略）
   4. 服务器。（通常为域名，有时为IP地址）
   5. 端口号。（以数字方式表示，若为HTTP的默认值“:80”可省略）
   6. 路径。（以“/”字符区别路径中的每一个目录名称）
   7. 查询。（**GET模式的窗体参数**，以“?”字符为起点，每个参数以“&”隔开，再以“=”分开参数名称与数据，通常以UTF8的URL编码，避开字符冲突的问题）
   8. 片段。以“#”字符为起点，锚点

#### 7. http请求格式

![http请求格式](/Users/henry/Documents/截图/Py截图/http请求格式.jpg)

#### 8. 响应格式

![http响应格式](/Users/henry/Documents/截图/Py截图/http响应格式.jpg)

#### 小结：

1. 请求和应答的应用层协议

2. 状态码：1xx需要等待服务器处理，2xx成功，3xx重定向，4xx请求错误，5xx服务器错误

3. 请求方式：8种，get、post

4. url:协议、域名和端口、路径和参数

5. 请求：浏览器给服务器发送的消息，request

   - get请求没有请求数据

   1. 请求方式 路径 版本号 \r\n
   2. 请求头：name:value \r\n
   3. \r\n 数据 \r\n\r\n

6. 响应：server发送给浏览器，response

   1. 响应行：协议版本 状态码 状态码描述 \r\n
   2. 响应头：xx\r\n
   3. \r\n 响应数据(响应体) \r\n\r\n

### 1.3 web框架的功能

1. socket收发消息(wsgiref、uwsgi)
2. 根据不同的路径返回不同内容
3. 返回动态页面
4. **分类**
   1. Django支持：2和3
   2. Flask支持：2（轻量级，其他功能需要其他模块）
   3. Tornado支持：1、2和3(**异步非阻塞**)（同flask）

## 2. 服务器程序和应用程序

### 2.1 简介

1. 对于真实开发中的python web程序来说，一般会分为两部分：服务器程序和应用程序。
2. 服务器程序负责对socket服务端进行封装，并在请求到来时，对请求的各种数据进行整理。
3. **应用程序则负责具体的逻辑处理**。为了方便应用程序的开发，就出现了众多的Web框架，例如：Django、Flask、web.py 等。不同的框架有不同的开发方式，但是无论如何，开发出的应用程序都要和服务器程序配合，才能为用户提供服务。
4. **WSGI（Web Server Gateway Interface）就是一种规范**，它定义了使用Python编写的web应用程序与web服务器程序之间的接口格式，实现web应用程序与web服务器程序间的解耦。
5. 常用的WSGI服务器有**uwsgi(线上)**、**Gunicorn**。而Python标准库提供的独立WSGI服务器叫**wsgiref**(性能较差，用于测试)，**Django**开发环境用的就是这个模块来做服务器。
   - negix：把静态页面返回，不经过Django，动态交给uwsgi用于Django处理，在返回

### 2.2 wsgiref

- 利用wsgiref模块替换socket server 部分

```python
from wsgiref.simple_server import make_server

def home(url):
    s = '这是页面{}'.format(url)
    print(s)
    return s.encode('utf-8')

def index(url):
    s = '这是页面{}'.format(url)
    print(s)
    return bytes(s, encoding='utf-8')

url_li = {'/index': index, '/home': home}

def run(environ, start_response):
    # 设置http响应头
    start_response('200 ok', [('Content-Type', 'text/html;charset=utf8'), ])
    url = environ['PATH_INFO']
    print(url, )
    if url_li.get(url):
        response = url_li[url](url)
    else:response = b'404 not found'
    return [response, ]

if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, run)
    print("我在8090等你哦...")
    httpd.serve_forever()
```

### 2.3 模版渲染模块jinja2

- 模板的原理就是字符串替换，我们只要在HTML页面中遵循jinja2的语法规则写上，其内部就会按照指定的语法进行相应的替换，从而达到动态的返回内容。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jinja2 import Template
from wsgiref.simple_server import make_server

def index(url):
    with open('./html/index2.html', 'r', encoding='utf-8') as f:
        data = f.read()
        # 生成模版文件
        template = Template(data)
        # 把数据填充到模版
        res = template.render({'name': 'henry', 'hobby': ['reading', 'movies', 'musics']})
    return bytes(res, encoding='utf-8')

def run_server(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html;charset=utf8'), ])
    url = environ['PATH_INFO']
    reponse = index(url)
    return [response, ]

if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, run_server)
    print('here')
    httpd.serve_forever()
```

## 3. Django

### 3.1 下载

1. Django1.11最后一个版本支持python2.7
2. 命令行：pip3 install django==1.11.21 -i 指定源地址
3. Pycharm:settings-解释器

### 3.2 Django项目

#### 3.1 创建

1. 命令行
   2. 项目文件夹：**django-admin startproject 项目名称**
   3. **自动生成项目目录**
2. 虚拟环境和当前环境
   1. 虚拟环境：支持python提供的包
3. 使用pycharm默认会创建templates文件夹

```python
mysite/
├── manage.py  # 管理文件
└── mysite  # 项目目录
    ├── __init__.py
    ├── settings.py  # 配置
    ├── urls.py  # 路由 --> URL和函数的对应关系
    └── wsgi.py  # runserver命令就使用wsgiref模块做简单的web server
```

#### 3.2 启动

1. 命令行

```python
# 命令行启动django
# cd 项目根目录，默认127.0.0.1:8000
python manage.py runserver
# 修改默认端口,指定端口80
python manage.py runserver 80
# 修改默认ip,指定ip和端口0.0.0.0:80
python manage.py runserver 0.0.0.0:80 
# 修改settings
ALLOWED_HOSTS=['*']
```

2. 简单使用

```python
# 修改urls.py, 运行时需要运行django项目
from django.shortcuts import HttpResponse, render
# request为请求数据
def index(request):
  # 返回字符串
  return HttpResponse('index')
	# 返回页面，模板：html文件，放在templates中
 	return render(request, 'index.html')

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'index/', index)
]
```

- 项目中的文件夹名尽量不要更改



### 

















