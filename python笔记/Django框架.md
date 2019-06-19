# 1. Django基础

## 1. web框架的本质

### 1.1 本质

#### 1. 实现socket服务器

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

#### 2. 返回html文件

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
    # 响应头
    con.send(b'HTTP/1.1 200 ok\r\n\r\n')
    if url_li.get(url):
        data = url_li[url](url)
    else:
        data = b'404 not found'
    con.send(data)
    con.close()
sk.close()
```

#### 3. 返回动态网页

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

1. 超文本传输协议（英文：Hyper Text Transfer Protocol，HTTP）是一种用于**分布式**、**协作式**和超媒体信息系统的**应用层协议**。**HTTP是万维网的数据通信的基础**。HTTP有很多应用，但最著名的是用于web浏览器和web服务器之间的双工通信。
2. HTTP的发展是由**蒂姆·伯纳斯-李**于1989年在欧洲核子研究组织（CERN）所发起。HTTP的标准制定由**万维网协会（World Wide Web Consortium，W3C）**和**互联网工程任务组（Internet Engineering Task Force，IETF）**进行协调，最终发布了一系列的**RFC**，其中最著名的是1999年6月公布的 RFC 2616，定义了HTTP协议中**现今广泛使用**的一个版本——**HTTP 1.1。**
3. 2014年12月，互联网工程任务组（IETF）的Hypertext Transfer Protocol Bis（httpbis）工作小组将HTTP/2标准提议递交至IESG进行讨论，于2015年2月17日被批准。 HTTP/2标准于2015年5月以RFC 7540正式发表，取代HTTP 1.1成为HTTP的实现标准。

#### 2. 协议概述

1. **HTTP是一个客户端终端（用户）和服务器端（网站）请求和应答的标准（TCP**）。通过使用网页浏览器、网络爬虫或者其它的工具，客户端发起一个HTTP请求到服务器上指定端口（**默认端口为80**，https默认时443）。我们称这个客户端为**用户代理程序（user agent）**。应答的服务器上存储着一些资源，比如HTML文件和图像。我们称这个应答服务器为**源服务器（origin server）**。在用户代理和源服务器中间可能存在多个“中间层”，比如代理服务器、网关或者隧道（tunnel）。
2. 尽管TCP/IP协议是互联网上最流行的应用，HTTP协议中，并没有规定必须使用它或它支持的层。事实上，HTTP可以在任何互联网协议上，或其他网络上实现。**HTTP假定其下层协议提供可靠的传输。**因此，任何能够提供这种保证的协议都可以被其使用。因此也就是其在TCP/IP协议族使用TCP作为其传输层。
3. 通常，**由HTTP客户端发起一个请求，创建一个到服务器指定端口（默认是80端口）的TCP连接。**HTTP服务器则在那个端口监听客户端的请求。一旦收到请求，服务器会向客户端返回一个状态，比如"HTTP/1.1 200 OK"，以及返回的内容，如请求的文件、错误消息、或者其它信息。

#### 3. 工作原理

1. HTTP协议定义Web客户端如何从Web服务器请求Web页面，以及服务器如何把Web页面传送给客户端。HTTP协议采用了**请求/响应模型**。客户端向服务器发送一个请求报文，请求报文包含请求的**方法、URL、协议版本、请求头部和请求数据**。服务器以一个状态行作为响应，响应的内容包括**协议的版本、成功或者错误代码、服务器信息、响应头部和响应数据**。
2. 以下是 HTTP **请求/响应的步骤(5)**
   1. **客户端连接到Web服务器**
      一个HTTP客户端，通常是浏览器，与Web服务器的HTTP端口（默认为80）建立一个TCP套接字连接。
   2. **发送HTTP请求**
      通过TCP套接字，客户端向Web服务器发送一个文本的请求报文，一个**请求报文由请求行、请求头部、空行和请求数据4部分组成**。
   3. **服务器接受请求并返回HTTP响应**
      Web服务器**解析**请求，**定位**请求资源。服务器将资源复本写到TCP套接字，由客户端读取。一个**响应由状态行、响应头部、空行和响应数据4部分组成。**
   4. **释放连接TCP连接**
      若**connection** 模式为**close**，则服务器主动关闭TCP连接，客户端被动关闭连接，释放TCP连接;若connection 模式为**keepalive**，则该连接会保持一段时间，在该时间内可以继续接收请求;
   5. **客户端浏览器解析HTML内容**
      客户端浏览器首先解析状态行，查看表明请求是否成功的状态代码。然后解析每一个响应头，响应头告知以下为若干字节的HTML文档和文档的字符集。客户端浏览器读取响应数据HTML，根据HTML的语法对其进行格式化，并在浏览器窗口中显示。

#### 4. 请求方法

- HTTP/1.1 协议规定了八种方法(动作)
- HTTP/1.1协议中共定义了八种方法（也叫“动作”）来以不同方式操作指定的资源：

1. GET
   - 向指定的资源发出**“显示**”请求。使用GET方法应该只用在**读取数据**，而不应当被用于产生“副作用”的操作中，例如在Web Application中。其中一个原因是GET可能会被网络蜘蛛等随意访问。
2. HEAD
   - 与GET方法一样，都是向服务器发出**指定资源的请求**。只不过服务器将不传回资源的本文部分。它的好处在于，使用这个方法可以在不必传输全部内容的情况下，就可以获取其中“关于该资源的信息”（元信息或称元数据）
3. POST
   - **向指定资源提交数据**，请求服务器进行处理（例如提交表单或者上传文件）。数据被包含在请求本文中。这个请求可能会创建新的资源或修改现有资源，或二者皆有。
4. PUT
   - 向**指定资源位置上传**其最新内容。
5. DELETE
   - 请求服务器**删除Request-URI所标识的资源**。
6. TRACE
   - 回显服务器收到的请求，主要用于**测试或诊断。**
7. OPTIONS
   - 这个方法可使服务器传回该资源所支持的所有HTTP请求方法。用来代替资源名称，向Web服务器发送OPTIONS请求，可以测试服务器功能是否正常运作。
8. CONNECT
   - HTTP/1.1协议中预留给能够将连接**改为管道方式**的代理服务器。通常用于**SSL加密服务器的链接**（经由非加密的HTTP代理服务器）。

#### Note1(2)

1. 方法名称是**区分大小写**的。当某个请求所针对的**资源不支持**对应的请求方法的时候，服务器应当返回状态码405（Method Not Allowed），当服务器**不认识或者不支持对应的请求方法**的时候，应当返回状态码501（Not Implemented）。
2. HTTP服务器至少应该实现GET和HEAD方法，其他方法都是可选的。当然，所有的方法支持的实现都应当匹配下述的方法各自的语义定义。此外，除了上述方法，特定的HTTP服务器还能够扩展自定义的方法。例如PATCH（由 RFC 5789 指定的方法）用于将局部修改应用到资源*。*

#### 5. 状态码(5)

1. 所有HTTP响应的**第一行都是状态行**，依次是**当前HTTP版本号**，**3位数字组成的状态代码**，以及描述**状态的短语**，彼此由**空格分隔**。
2. 状态代码的第一个数字代表当前响应的类型
   1. **1xx消息**——请求已被服务器接收，继续处理
   2. **2xx成功**——请求已成功被服务器接收、理解、并接受
   3. **3xx重定向**——需要后续操作才能完成这一请求，当前服务器无法处理，响应另一个服务地址
   4. **4xx请求错误**——请求含有词法错误或者无法被执行，没有该资源，**402表示认证错误、403表示权限不够**
   5. **5xx服务器错误**——服务器在处理某个正确请求时发生错误，500服务端，代码问题。
3. 虽然 RFC 2616 中已经推荐了描述状态的短语，例如"200 OK"，"404 Not Found"，但是WEB开发者仍然能够自行决定采用何种短语，用以显示本地化的状态描述或者自定义信息。

#### 6. URL(统一资源定位符)

- http:默认端口是80(可省略)，https默认是443

1. 超文本传输协议（HTTP）的统一资源定位符将从因特网获取信息的**五个基本元素**包括在一个简单的地址中
   1. **传送协议**。
   2. **层级URL标记符号**(为[//],固定不变)
   3. 访问资源需要的凭证信息（可省略）
   4. **服务器**。（通常为域名，有时为IP地址）
   5. **端口号**。（以数字方式表示，若为HTTP的默认值“:80”可省略）
   6. **路径**。（以“/”字符区别路径中的每一个目录名称）
   7. **查询**。（**GET模式的窗体参数**，以“**?**”字符为起点，每个参数以“&”隔开，再以“=”分开参数名称与数据，通常以UTF8的URL编码，避开字符冲突的问题）
   8. **片段**。以“#”字符为起点，锚点(history模式)
   
   
   
2. **浏览器发送请求和接受响应的过程？**

   - HTTP/1.1默认是短暂的长链接，保持一个阈值时间

   1. 在浏览器中地址栏输入url，发送get请求
   2. 服务器接收到请求，获取url的路径，根据路径做不同操作，把返回的数据封装到响应体中，返回给浏览器
   3. 浏览器接收响应，双发断开链接
   4. 浏览器从响应体中获取数据，进行解析渲染

#### 7. http请求和响应格式

- 请求格式

![ http请求格式](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/http%E8%AF%B7%E6%B1%82%E6%A0%BC%E5%BC%8F.jpg)

- 响应格式

![http响应格式](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/http%E5%93%8D%E5%BA%94%E6%A0%BC%E5%BC%8F.jpg)

### 1.3 web框架的功能

1. socket收发消息(wsgiref(测试)、**uwsgi(线上)**)
2. 根据不同的路径返回不同内容
3. 返回动态页面
4. **Django**:支持2和3；**Flask**:支持2（轻量级，其他功能需要其他模块）；**Tornado**:支持1、2和3(**异步非阻塞**)（同flask）



## 2. 服务器程序和应用程序

### 2.1 简介

1. 对于真实开发中的python web程序来说，一般会分为两部分：**服务器程序**和**应用程序**。
2. 服务器程序负责对socket服务端进行封装，并在请求到来时，对请求的各种数据进行整理。
3. **应用程序则负责具体的逻辑处理**。为了方便应用程序的开发，就出现了众多的Web框架，例如：Django、Flask、web.py 等。不同的框架有不同的开发方式，但是无论如何，开发出的应用程序都要和服务器程序配合，才能为用户提供服务。
4. **WSGI（Web Server Gateway Interface）就是一种规范**，它定义了使用Python编写的web应用程序与web服务器程序之间的接口格式，实现web应用程序与web服务器程序间的解耦。
5. 常用的WSGI服务器有**uwsgi(线上)**、**Gunicorn**。而Python标准库提供的独立WSGI服务器叫**wsgiref**(性能较差，用于测试)，**Django**开发环境用的就是这个模块来做服务器。
   - negix：把静态页面返回，不经过Django，动态交给uwsgi用于Django处理，再返回

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
3. Pycharm:settings-解释器-下载django

### 3.2 Django项目

#### 1. 创建

1. 命令行
   1. 项目文件夹：**django-admin startproject 项目名称**
   2. **自动生成项目目录**
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

#### 2. 启动

1. 命令行

```python
# 命令行启动django
# cd 项目根目录，默认127.0.0.1:8000
python manage.py runserver
# 修改默认端口,指定端口80
python manage.py runserver 80
# 修改默认ip,指定ip和端口0.0.0.0:80, 上线时使用
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

#### 3. Django基础必备三件套

```python
from django.shortcuts import HttpResponse, render, redirect
```

1. **HttpResponse**
   - 内部传入一个字符串参数，返回给浏览器。

```python
def index(request):
    # 业务逻辑代码
    return HttpResponse("OK")
```

2. **render**
   - 除request参数外还接受一个待渲染的模板文件和一个保存具体数据的字典参数。
   - 将数据填充进模板文件，最后把结果返回给浏览器。（类似于我们上面用到的jinja2）

```python
def index(request):
    # 业务逻辑代码
    return render(request, "index.html", {"name": "henry", "hobby": ["movies", "reanding"]})
```

3. redirect
   - 接受一个URL参数，表示跳转到指定的URL

```python
def index(request):
    # 业务逻辑代码
    return redirect("/home/")
```

![redirection](/Users/henry/Documents/截图/Py截图/redirection.png)

# 2.Django简介

**django处理请求流程**

1. 浏览器地址输入url，发送get请求
2. wsgi服务器接受到请求
3. 根据url路径找到对应的函数
4. 执行函数，返回响应给wsgi按照http协议格式返回浏览器

## 1. 静态文件

- 静态文件包括：css，javascript，images

### 1.1 静态文件配置流程

- **配置**

```python
# 配置静态文件夹路径
STATIC_URL='/staic/'
STATICFILES_DIRS=[
  os.path.join(BASE_DIR, 'static'),
  os.path.join(BASE_DIR, 'static1'),
  os.path.join(BASE_DIR, 'static2'),
]

# 创建一个static文件夹，存放静态文件
css，js和img文件夹，plugins文件夹
# static是STATIC_URL='/staic/'中的static
<link rel='stylesheet' href='/static/css/xxx.css'></link>
```

### 1.2 简单使用

#### 1. form中的元素(4)

- 可以建立多个static文件夹
- 如果静态资源有重名的文件，则按照静态文件夹路径中的列表顺序(一旦找到即停止

1. input中可以使用**autofocus**，即请求页面自动聚焦
2. form表单提交使用：action和method='post'
3. 所有的input框需要**name属性**，使用sumbit或button
4. 提交post请求，**把settings中的MIDDLEWARE：csrfvirew注释掉即可**，即禁用csrf校验

#### 2. 提交表单中的方法

1. **获取请求方式**：request.method(GET/POST)
2. form表单中的数据：request.POST **querydict对像**，可以使用dict方式取值,可以使用get方法
3. 导入django中的redirect
4. /index/第一个**/是根目录**，如果没有根目录，**则进行路径拼接**.
   - **响应头**：Location。/index/

```python
# 在view.py文件中处理请求数据，如认证操作
def login(request):
    if request.method == 'POST':
      	# 获取用户名和密码，form表单中数据
        username = request.POST['username']
        # username = request.POST.get('username', '用户不存在')
        pwd = request.POST['pwd']
     # 重定向，返回一个网址，或当前网站资源的路径
     return redirect('/index/')
```

#### **3. get和post**

- **get**
  1. **获取数据，传递参数(在url中)**
  2. **提交数据暴露在url中**
  3. **django获取参数**
     - **request.GET.get('username')**
- **post**
  1. **数据是隐藏的(在请求体中)**
  2. **request.POST**

## 2. app

- 把功能进行划分

### 2.1 命令行

#### 1. 创建app

```python
python manage.py startapp app1
# 放置迁移文件
migrations
# django提供后台管理，对数据库表结构进行增删改查
admin.py
# 和ORM相关
models.py
# 测试文件
test.py
# 视图，函数位置
views.py
```

#### 2. 注册app

```python
# 在settings中的installed_apps
直接添加app名称
# 推荐使用,执行类
或app01.apps.App01Config
```

### 2.2 pycharm

- 创建Django项目时，可以添加app(和templates一同)，pycharm创建并注册

```python
# 创建
tools --> runmanage.py task --> 
startapp app02(名称)
```

```python
# 注册,修改settings中的INSTALLED_APPS
INSTALLED_APPS = [
	...
    'app01',
    'app01.apps.App01Config',  # 推荐写法
]
# 重复注册会报错
```

### 2.3 注意事项

1. app更名需要同步到数据库中
2. 有关app名称里面的模块导入时，也需要更改为响应的app名称

## 3. ORM

### 3.1 概念

- **对象关系映射**（Object Relational Mapping，简称**ORM**）模式是一种为了**解决面向对象与关系数据库存在的互不匹配的现象的技术。**
- 简单的说，ORM是通过使用描述对象和数据库之间映射的**元数据**，将**程序中的对象自动持久化到关系数据库中。**
- **ORM在业务逻辑层和数据库层之间充当了桥梁的作用**。

### 3.2 特点

#### 1.优势

1. ORM解决的主要问题是对象和关系的映射。它通常将一个类和一张表一一对应，类的每个实例对应表中的一条记录，类的每个属性对应表中的每个字段。 
2. ORM提供了对数据库的映射，不用直接编写SQL代码，只需操作对象就能对数据库操作数据。
3. 专注业务逻辑，提高开发效率

#### 2. 劣势

1. 牺牲了程序的执行效率
2. ORM的缺点是会在一定程度上牺牲程序的执行效率。
3. ORM的操作是有限的，也就是ORM定义好的操作是可以完成的，一些复杂的查询操作是完成不了。

### 3.3 Django使用mysql(6)

#### 1. 创建mysql数据库

```python
create database django53;
```

#### 2. settings.py

- django链接mysql，settings中的文件是明文的

```python
# 使用mysql数据库
DATABASES = {
  'default':{
        # 引擎
      'ENGINE':'django.db.backbends.mysql',
      'NAME':'django53',
      'HOST':'127.0.0.1',
      'PORT':3306,
      'USER':'root',
      'PASSWORD':'123',
    }
  } 
```

#### 3. _\_init__.py

- 配置链接模块，与settings同级，导入pymysql告诉Django使用其链接数据库
- django默认使用**mysqldb**模块(只支持py2)

```python
# 与settings同级目录下的__init__.py文件中添加，替换默认
import pymysql
pymysql.install_as_MySQLdb()
```

#### 4. models.py

1. 通过**models**创建表

```python
from django import models
class User(models.Model):
  # 在db中创建一个varchar(32)的username字段
  username = models.CharField(max_length=32)
  pwd = models.CharField(max_length=32)  
```

#### 5. mysql的迁移(2)

- 命令行输入

```python
# 检查每个注册app的models中是否有变化，即变更记录models.py
python manage.py makemigrations (app名称可选)
# 同步变更记录到数据库中，一开始生成表名app名称+类名(小写)
python manage.py migrate
```

- 创建超级用户

```python
python manage.py createsuperuser
# 输入以上命令后，根据提示输入用户名、邮箱、密码、确认密码。密码的要求至少是不八位，不能和邮箱太接近，两次密码需要一致。
```

#### 6. views.py

- **orm操作**，获取数据
  - models.User.objects.all()
  - models.User.objects.get()
  - models.User.objects.filter()
  - **获取的是一个列表**
- views可以视为python的回调函数

```python
from app01 import models
def orm_test(request):
  # 获取表中所有数据，ret为QuerysSet，对象列表
  ret = models.User.objects.all()
  for i in ret:
    print(i.username, i.password)
```

- 获取符合条件数据，**获取不到或多个会报错**

```python
from app01 import models
def orm_test(request):
  # 获取表中一条数据,User object
  ret = models.User.objects.get(username='herny', password='123')
  print(ret.username, ret.password)
```

- 使用**filter方法**做认证

```python
from app01 import models
def orm_test(request):
  # 获取满足条件的对象，没有获取到即为空即False
  ret = models.User.objects.filter(username='herny', password='123')
  print(ret.username, ret.password)
```

#### 3.4 ORM中的批量操作

1.数据模型定义

```python
# 创建商品表对象
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

2.批量插入数据

- 批量插入数据的时候，首先要**创建一个对象的列表**，然后调用**bulk_create**方法，一次将列表中的数据插入到数据库中。

```python
product_list_to_insert = list()
for i in range(10):
  		product_list_to_insert.append(Product(name='producet name ' + str(i), price))
Product.objects.bulk_create(product_list_to_insert)
```

3.批量更新数据

- 批量更新数据时，先进行数据过滤，然后再调用**update**方法进行一次性地更新。下面的语句将生成类似update....from....的SQL语句。

```python
Product.objects.filter(name__contains='name').update(name='new name')
```

4.批量删除数据

- 批量更新数据时，先是进行数据过滤，然后再调用**delete**方法进行一次性删除。下面的语句讲生成类似delete from ... where ... 的SQL语句。

```python
Product.objects.filter(name__contains='name query').delete()
```

### 3.4 已有数据库加入一个字段

#### 1. 表中添加字段

1. 可以使用pycharm提供的图形化界面进行插入或通过终端进行插入
2. 更新models.py 中的类属性
3. 更新迁移文件中的对应字段，至此完成

# 3. Django实例

## 1.出版社管理

### 1.1 展示

#### 1. 创建数据库

```python
# 命令行，mysql中
create database dj_bookmanager
```

#### 2. settings.py

1. BASE_DIR：项目根目录
2. debug = True(开发) / False(上线)
3. INSTALL_APPS：注册app
4. MIDDLEWARW：注释掉csrf校验
5. TEMPLATES：模版文件目录
6. DATABASES：配置mysql数据库(6)
7. STATICFILES_DIRS：配置静态文件 

#### 3. models.py

- 在__init.py中导入**pymysql**模块，替换默认链接方式
- 并创建model类，并**指定约束**
  1. models.AutoField(**primary_key = True**) #**自增并指定主键**
  2. models.CharField(max_length=32, **unqiue/default=xxx**)
  3. models.IntegerField(default=0)

```python
from django.db import models

class Publisher(models.Model):
  pid = models.AutoField(primary_key = True)
  name = models.CharField(max_length=32, unique=True)
  # 后续添加，需要指定默认值
  addr = models.CharField(max_length=32, default='xxx')
  # 或者更改迁移文件
```

#### 4. 迁移数据库

```python
python manage.py makemigrations
python manage.py migrate
# 插入数据
```

#### 5. urls.py

```python
from django.conf.urls import url
from django.contrib import admin
# 导入视图模块
from app1 import views
# 添加调用关系
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login', views.publisher_list),
]
```

#### 6. views.py

```python
from django.shortcuts import render, HttpResponse, redirect
def publisher_list(request):
  # 业务逻辑
    all_pubulisher = models.Pbulisher.objects.all().order_by(pk)
    return render(request, 'publisher_list.html', {'all_pubulisher':all_pubulisher})
```

#### 7. xxx.html

1. 这里使用的是django的渲染语法(在创建app也可以指定jinja2)
2. **{{变量}}**，**{% for 循环%}{%endfor%}(需要闭合)**
3. 如果没有参数传入时，html中的{{变量}}在页面中不显示

```django
{# for循环中有 forloop.counter 自动记录循环次数 #}
{% for publisher in all_publisher %}
	<tr>
    <td>{{forloop.counter}}</td>
    <td>{{publisher.pid/pk}}</td>
    <td>{{publisher.name}}</td>
	</tr>
{% endfor %}
{# if条件判断 #}
{% if 条件判断 %}
{% else %} / {% elif %}
{% endif %}
```

### 1.2 新增

- **models.类名.objects.create(字段=值)**

```python
# orm插入数据
obj = models.Publisher.objects.create(name=publisher_name)
# publisher object
print(obj)
```

- **实例化方式**

```python
obj = models.Publisher(name=publisher_name)
obj.save()   # 保存到数据库中
# obj打印结果：Publisher obj
print(obj) 
```

### 1.3 删除

- **obj.delete()，obj_list.delete()**
- 对像和对象列表都有delete方法

```python
pk = request.GET.get('id')
obj_list = models.Publisher.objects.filter(pk=pk)
# 删除对象
if not obj_list:
  return HttpResponse('删除数据不存在')
obj_list.delete()
```

### 1.4 编辑

- obj.字段=值
- obj.save() 更新数据到数据库

```python
# 从url中获取的参数，不是get请求的数据
pk = request.GET.get('id')
obj_list = models.Publiser.objects.filter(pk=pk)
if not obj_list:
  return HttpResponse('编辑数据不存在')

obj = obj_list[0]
# 内存中修改
obj.name = publisher_name
# 内存中数据，提交到数据库
obj.save()
```

## 2. 书籍管理

### 2.1 创建表结构

#### 1. book表

- name、作者、出版社、出版时间

```python
class Book(models.Model):
  title = models.CharField(max_length=32)
  pub_id = models.ForeignKey(to=Publisher,on_delete=models.SET(字段))
  # on_delete=models.CASCADE（默认）
  # on_delete=models.SET(‘具体值’)
  # on_delete=models.SET_DEFAULT， defalut='xxx'
  # on_delete=models.SET_NULL
	# on_delete参数在django2.0之后必填
  # 通过反射获取, on_delete默认级联删除
  pub = models.ForeignKey('Publisher', on_delete=models.SET_NULL)
```

#### 2. 数据库迁移

```python
python manage.py makemigrations
python manage.py migrate
# 外键名django自动加 _id
# django.migrations也会在数据库中创建
```

### 2.2 查询

- models.py 
- models中的**pub**是被**关联类的对象**
- django会自动生成 pub_id

```python
for book in all_Book.objects.all():
    # book类中属性
    print(book.pk)
    print(book.title)
    print(book.pub_id)
    print(book.pub, type(book.pub))
    # publisher中属性
    # print(book.pub_id)只需要出版社id，建议使用
    print(book.pub.pk)
    print(book.name)
```

```python
for+table,自动补全，pycharm提供
# __str__方法
print(book.pub)
```

### 2.3 展示

```python
def list_book(request):
    all_books = models.Book.objects.all()
    return render(request, 'list_book.html', {'all_books': all_books})
```

### 2.4 添加

- views.py

```python
def add_book(request):
    error = ''
    if request.method == 'POST':
        title = request.POST.get('book_name')
        pk = request.POST.get('id')
        print(title, pk)
        # 可以使用多个字段进行查找
        book_set = models.Book.objects.filter(title=title, pub_id=pk)
        if book_set:
            error = '书籍已存在'
        if not title: error = '请输入书名'
        if not error:
            models.Book.objects.create(title=title, pub_id=pk)
            return redirect('/list_book/')
    all_publisher = models.Publisher.objects.all()
    return render(request, 'add_book.html', {'all_publisher': all_publisher, 'error': error})
```

### 2.5 删除

- 数据库查询到的对象 或 query set 都可以使用delete方法直接删除数据

```python
def del_book(request):
    if request.method == 'GET':
        pk = request.GET.get('id')
        models.Book.objects.filter(id=pk).delete()
        return redirect('/list_book/')
```

### 2.6 修改

- 通过 GET 、 POST 获取的数据一般为 **字符串类型**
- 获取的 pub_id 是 str 类型，注意和数据库中字段类型一样

```python
def edit_book(request):
    error = ''
    pk = request.GET.get('id')
    book = models.Book.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('book_name')
        # 获取的 pub_id 是 str 类型，注意和数据库中字段类型一样
        pub_id = request.POST.get('id')
        print(type(title), type(book.title), type(pub_id), type(book.pub_id))
        # 判断 书名+出版社 是否被修改
        if book.title == title and book.pub_id == int(pub_id):
            error = '未做任何修改'
        if not title: error = '请输入书名'
        # 判断 书名+出版社 是否唯一
        if models.Book.objects.filter(title=title, pub_id=pub_id):
            error = '该书籍已存在'
        if not error:
            book.title = title
            book.pub_id = pub_id
            book.save()
            return redirect('/list_book/')
    all_publisher = models.Publisher.objects.all().order_by('pid')
    return render(request, 'edit_book.html', {'book': book, 'all_publisher': all_publisher, 'error': error})
```

## 3. 作者的管理

### 3.1 设计作者表和外键

```python
# models.py
class Author(models.Model):
  name.CharField(max_length=32)
  # books为关系管理对象,django会自动生成第三张表
	books = models.ManyToMangField('Book')
```

### 3.2 数据库迁移

### 3.3 关系管理对象

```python
# 关系管理对象，books为外键
auther.books  # books.None
# queryset类型的书籍对象
auther.books.all()
```

### 3.4 模版

- 模版里面方法不用加括号，会自动调用

```python
# forloop.last为bool值，最后一次为真
{% if forloop.last/first %}
```

### 3.5 增加作者

```python
# get只能拿到一个值
books = request.POST.get('books')
# 获取一个list
books = request.POST.getlist('books')
```

```python
# 更新数据库, set方法设置第三张表
# ORM操作
# 插入作者信息
author_obj = models.Auther.objects.create(name=author_name)
# 通过关系管理对象插入数据
author_obj.books.set(books)
# 重定向
```

### 3.6 删除作者

```python
# 通过pk查找到作者的对象，利用.delete()进行删除
```

### 3.7 编辑作者

- request.POST.getlist('key')

```python
# 使用getlist获取books
books = request.POST.getlist('books')
# 每次重新设置，会有覆盖操作，把数据写入到第三张表中
author_obj.books.set(books)
```

### 3.8 多对多建表

#### 1. ManyToManyField(关联类)

- 不在author产生外键字段

```python
# django 生成的第三张表
class Author(models.Model):
  name.CharField(max_length=32)
  # books为关系管理对象，不在author产生字段
	books = models.ManyToMangField('Book')
```

![django的多对多外键](/Users/henry/Documents/截图/Py截图/django的多对多外键.png)

#### 2. 自己创建第三张表

```python
class Author(models.Model):
  name.CharField(max_length=32)
  
class AuthorBook(models.Model):
  author = models.ForeignKey('Author', on_delete=models.CASCADE)
  book = models.ForeignKey('Book', on_delete=models.CASCADE)
  date = models.DateField()
```

#### 3. 自己建表和django关联

- 通过**through**参数，查询上有优势
- 插入时需要**操作第三张表**，没有**set**方法

```python
class Author(models.Model):
  name.CharField(max_length=32)
  # books为关系管理对象
	books = models.ManyToManField('Book', through='AuthorBook', through_fields=['author', 'book'])

class AuthorBook(models.Model):
  author = models.ForeignKey('Author',related_name='a',on_delete=models.CASCADE)
  book = models.ForeignKey('Book',related_name='b',on_delete=models.CASCADE)
  recomm = models.ForeignKey('Author', on_delete=models.CASCADE)
  
  date = models.DateField()
```

# 4. Django框架

## 1. MVC和MTV

- MVC，全名是**Model View Controller**，是软件工程中的一种软件架构模式，把软件系统分为三个基本部分：**模型(Model)**、**视图(View)**和**控制器(Controller)**，具有耦合性低、重用性高、生命周期成本低等优点。
  - controller：调度和传递指令

![MTV框架](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/MTV%E6%A1%86%E6%9E%B6.png)

- Django框架的设计模式借鉴了MVC框架的思想，也是分成三部分，来降低各个部分之间的耦合性。
- Django框架的不同之处在于它拆分的三部分为：Model（模型）、Template（模板）和View（视图），也就是MTV框架。

## 2. Django的MTV模式

1. **Model(模型)**：负责业务对象与数据库的对象(ORM)
2. **Template(模版)**：负责如何把页面展示给用户
3. **View(视图)**：负责业务逻辑，并在适当的时候调用Model和Template

- 此外，Django还有一个**urls分发器**，它的**作用是将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template**

![Django框架](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/Django%E6%A1%86%E6%9E%B6.png)

## 3. Model

### 1. model简介

- **在Django中model是你数据的单一、明确的信息来源**。它包含了你存储的数据的重要字段和行为。通常，一个模型（model）映射到一个数据库表。

### 2. 基本情况：

- 每个模型都是一个Python类，它是django.db.models.Model的子类。
- 模型的每个属性都代表一个数据库字段。
- 综上所述，Django为您提供了一个自动生成的数据库访问API

![ORM与DB](/Users/henry/Documents/%E6%88%AA%E5%9B%BE/Py%E6%88%AA%E5%9B%BE/ORM%E4%B8%8EDB.png)

#### Note2(4)

- model一些说明

```mysql
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```

1. **表app名称_类名(小写)的名称是自动生成的**，如果你要自定义表名，需要在**model的Meta类中指定 db_table 参数**，强烈建议使用**小写**表名，特别是使用MySQL作为数据库时。
2. id字段是自动添加的，如果你想要指定自定义主键，只需在其中一个字段中指定 primary_key=True 即可。如果Django发现你已经明确地设置了Field.primary_key，它将不会添加自动ID列。
3. 本示例中的CREATE TABLE SQL使用PostgreSQL语法进行格式化，但值得注意的是，Django会根据配置文件中指定的数据库类型来生成相应的SQL语句。
4. Django支持MySQL5.5及更高版本。

## 4. Templates

1. MVC：model view(html) controller(控制器，路由传递指令，业务逻辑)
2. MTV：model(ORM操作) template(html) view(业务逻辑)

- {{ }}表示变量，在模板渲染的时候替换成值，{% %}表示逻辑相关的操作。

### 4.1 变量

- 通过key取值
- 传值时，是**本质是字符串的替换**
- .索引、.key、.属性、.方法
- 变量的 . 方法的优先级是：**dict —> 属性、方法—>索引**
- {{ 变量名 }}变量名由**字母数字**和**下划线**组成。
- **点（.）**在模板语言中有特殊的含义，用来获取对象的相应属性值。

#### 1. 取值

**1. 列表**

-  hobby.**索引**，只支持正向索引

```django
hobby = ['movies', 'musics', 'reading', 'play badminton']
{{hobby.0}}
```

**2. 字典**

- **通过key取值**
- 没有get方法。也可以使用**request**对象取值
- 模版里方法不用加括号

```django
hobby = ['movies', 'musics', 'reading', 'play badminton']
dic = {1: a, 2: b, 3: hobby}
{{ dic.3.1 }}
<br>
{{ dic.keys }}
<br>
{{ dic.values }}
<br>
{{ dic.items }}
<br>
{{ request }}
```

**3. 类**

- 定义的方法不能使用形参，否则无法使用
  

```python
# views.py中
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def talk(self):
    return '咱也不知道，咱也不敢问'
  def __str__(self):
      return '<Person obj: {}-{}>'.format(self.anme, self.age)

def my_test(request):
  person_obj = Person('henry', 19)
  return render(request, {'person_obj': person_obj})
```

```django
{{ person_obj }}
<br>
{#此时talk不能传参#}
{{ person_obj.talk }}
```

#### 2. filter(过滤器)

- 作用：**修改变量的显示结果**
- 语法：**{{value|filter_name:参数}}**
- **default用法**，变量为**False**显示默认值
- **default和指定值之间不能有空格**

**1. default**

- 变量值为False时，采用默认值

```html
<p>{{xxx}}</p>
<p>{{xxx|default:变量/指定值}}</p>
<p>{{xxx|default:''}}</p>
```

```python
# settings.py中的templates中的options中设置
# 只有变量不存在时有效
'string_if_invalid' = '变量不存在'
```

**2. filesizeformat**

- 文件默认**byte**为单位
- 文件大小格式化

```python
# 文件单位换算，最大有效单位为 PB
{变量|filesizeformate}
```

**3. add**

- 数值加法
- 字符串/list拼接

```python
# 结果为6,优先使用数字的加法，有其他类型时，进行拼接
{{2|add:'4'}
```

```python
hobby = ['movies', 'musics', 'reading', 'play badminton']
{{hobby|add:hobby}}
# add:hobby之间不能有任何空格，否则会报错
```

**4. lower / upper / title(所有单词首字母大写)**：

**5. ljust / rjust / center**

```django
"{{'Django'|center:"15" }}"
Ifvalueis"Django",theoutputwillbe" Django ".
```

**6. length**

- 计算长度

```django
string = 'hello bugs'
li = [1,2]
{{string|length}}
{{li|length}}
```

**7. slice**

- **string** 和**list**

```python
li = [1,2,3,4]
{{li|slice:'1:3'}}     # [2, 3]
{{ li|slice:'2' }}     # [1, 2]
{{ li|slice:'-1' }}    # [1, 2, 3]
{{li|slice:'-2::-1'}}  # [3, 2, 1]
{{ li |slice:'::-1' }} # [4, 3, 2, 1]
```

**8. first /last**

- 取当前第一个

```django
{{li|last}}
```

**9. join**

```django
{{li|join':'}}
```

**10. truncatechars**

- 其后必须有参数，少于3时均为**...**

```python
string = 'welcome to China, welcome to BeiJing'
{{string|truncatechars:'10'}}
# 会有三个点,也要占位
welcome...
{{string|truncatewords:'10'}} 
# 对中文无效，10个单词，10个单词+3个点
```

**11. date**

- {{ value|date:"Y-m-d H:i:s"}}
- django模版中的日期格式化，**和python中不同**

```python
import datetime
now = datetime.datetime.now()
{{now|date:'Y-m-d H:i:s'}}
```

```python
# settings.py
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:i:s'
USE_L10N = False
```

**12. safe/urlize**

- Django的模板中会对HTML标签和JS等语法标签进行自动转义
- 安全，告诉Django不用做转义
- js、超链接

```python
# 作为render传参中字典的元素
'value' : "<a href='#'>点我</a>"
{{ value|safe }}
```

#### 3. 自定义filter

1. 在app下创建一个名为**templatetags**的python包(包名是固定的)
2. 创建xxx.py 文件，文件名自定义(**my_tags**)
3. 导入模块、添加装饰器
4. 文件夹名和register

```python
# app/templatetags/xxx.py
from django import template
# register 名称不能改变
register = template.Library()
# 参数可以省略，形参最多有两个r
@register.filter
def add_(value, arg):
  return '{}-{}'.format(value, arg)
# 使用
{% load my_tags %}
{{'henry'|add_:'hello'}}
```

- 使用filter指定的函数名

```python
# 定义
@register.filter(name='henry')
def add_(value, arg):
  return '{}-{}'.format(value, arg)
# 使用
{% load my_tags %}
{{'henry'|henry:'hello'}}
```

- 取消转义

```python
value = 'https://www.baidu.com'
# 自定义,不会转义
@register.filter(is_safe=True)
def add_(value, arg):
  return '{}{}'.format(value, arg=None)

# 自定义，不会转义
from django.utils.safestring import mark_safe
@register.filter
def add_(value, arg):
  return mark_safe('{}-{}'.format(value, arg))
```



**4. 示例**

```django
加法{{ a }} + {{ b }} =
{{ a|add:b }}
<br>
减法
{{ a }} - 1 =
{{ a|add:-1 }}
<br>
乘法
{{ a }} * {{ b }} =
{% widthratio a 1 b %}
<br>
除法
{{ a }} * {{ b }} =
{% widthratio a b 1 %}
{% load show_a %}
<br>
```



















## 









## 番外篇：

1.查看django版本

```django
python -m django --version
```

2. When to use include()

```python
You should always use `include()` when you include other URL patterns. `admin.site.urls` is the only exception to this.
# 项目中如果有其他的urls.py，这时就需要使用include()
# 当admin.site.urls
```

3. django中的路由机制是由**urls.py**完成的
4. settings.py
   - If you set DEBUG to **False**, you also need to properly set the **ALLOWED_HOSTS**setting.
   - 修改配置文件名称需要同步修改wsgi中的**DJANGO_SETTINGS_MODULE**
5. Default settings
   1. A Django settings file doesn’t have to define any settings if it doesn’t need to. Each setting has a sensible default value. These defaults live in the module `django/conf/global_settings.py`.
   2. Here’s the algorithm Django uses in compiling settings:
      1. Load settings from `global_settings.py`.
      2. Load settings from the specified settings file, overriding the global settings as necessary.
   3. **Note** that a settings file should *not* import from `global_settings`, because that’s redundant











