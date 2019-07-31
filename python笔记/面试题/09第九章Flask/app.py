'''
https://blog.csdn.net/weixin_39726347/article/details/88567117

'''


# import time
#
# from flask import Flask, g, redirect
#
# app = Flask(__name__)
#
# app.app_context()
# @app.route('/index')   #1.手写一个hello world
# def index():
#     g.time = time.time()
#     # hello()
#     # return "hello world"
#     return redirect('hello')
#
# @app.route('/hello')
# def hello():
#     print(g.time)
#
#     return 'hello'
#
# if __name__ == '__main__':
#     app.run()


#2.Flask框架的优势
'''
    Django web框架：
        优点 - 组件非常全，教科书框架，admin model-ORM session
        缺点 - 资源浪费，因为组件多，大，还是互相关联的，随便卸载组件，可能会造成项目的崩溃
        
    Flask web框架：
        优点 - 扩展性强，精简小，简单，第三方组件 session Flask-Session Flask-Admin
        缺点 - 稳定性相对较差 ，第三方组件新版兼容性
    
    Tornado web框架:
        优点 - 异步IO，非阻塞，原生Websocket
        缺点 - 全部手写
        
    Sanic web框架:
        优点 - 与Flask本是同根生，异步框架，集合Flask与Tornado所有优点
        缺点 - 复杂度较高
'''

#3.Flask框架依赖组件
'''
1.Werkzeug 一个WSGI工具包（web服务网关接口（Python Web Server Gateway Interface，缩写为WSGI）是为python语言定义的
web服务器和web应用程序或框架之间的一种简单而通用的借口，其他语言也有类似的接口）
2.jinja2模板引擎

Route(路由)
templates(模板)
Models(orm模型)
blueprint(蓝图)
Jinja2模板引擎

'''

#4.Flask蓝图的作用
'''
1.将不同的功能模块化
2.构建大型应用
3.优化项目结构
4.增强可读性,易于维护（跟Django的view功能相似）

'''
#5.列举使用过得flask的第三方组件
'''
Flask-session   
WTForms  相当于 WTF - Django ModelForm
'''

#6.简述Flask请求上下文管理流程
'''
RequestContext 请求上下文:
    Request 请求的对象，封装了Http请求(environ)的内容
    Session 根据请求中的cookie，重新载入该访问者相关的会话信息。

第一阶段：
    - 执行__call__--->app.wsgi-->将ctx（request,session）封装在RequestContext类中,并通过LocalStack将requestcontext
    放入Local类中
                   
第二阶段：
    - 视图函数导入：request/session ,通过偏函数(_lookup_req_object)在通过（LocalProxy()）
    去LocalStack中的Local类中对其进行增删改查操作 

第三阶段：请求处理完毕　　　　　　　 
　　　- 通过save_session将签名session保存到cookie 
　　　-通过ctx.pop()去LocalStack中的Local类- 将ctx删除 　


2.应用上下文
与请求上下文类似，当请求进来时，先实例化一个AppContext对象app_ctx，在实例化的过程中，提供了两个有用的属性，
一个是app，一个是g。self.app就是传入的全局的app对象，self.g是一个全局的存储值的对象。接着将这个app_ctx存放到LocalStack()。

class AppContext(object):
　　def __init__(self, app):
　　　　self.app = app
　　　　self.url_adapter = app.create_url_adapter(None)
　　　　self.g = app.app_ctx_globals_class()　　

视图函数中，我们就可以调用app对象和g对象，如果我们使用蓝图构建我们的项目时，在每一个直接引用app就会造成循环引用的异常，
这时，应用上下文就会显得非常有用，我们可以直接调用current_app就可以在整个生命周期中使用我们的app对象了。
比如使用我们的配置项：current_app.config

current_app = LocalProxy(_find_app)
　　最后，当视图函数执行结束后，从storage中pop掉app_ctx对象。

'''

#7.Flask中g的作用
'''
1.g对象用于存储数据的的全局变量
2.g对象在一次请求中的所有的代码的地方，都是可以使用的
'''
#8.如何编写flask中的离线脚本
'''
离线脚本，就是非 web 运行时（web服务器停止）的状态下，也能对flask进行操作的脚本

单app离线脚本
    app = create_app()
    with app.app_context():
        db.drop_all()
        # db.create_all()
        # data = db.session.query(models.Users).all()
        # print(data)
    
    RequestContext类中的方法:
    def __enter__(self):
        self.push()
        return self
    def __exit__(self, exc_type, exc_value, tb):
        self.auto_pop(exc_value)
    
        if BROKEN_PYPY_CTXMGR_EXIT and exc_type is not None:
            reraise(exc_type, exc_value, tb)
    
    db就我们在__init__文件中实例化的对象，它包含了create_all（创建表）和drop_all（删除表）的命令，
    但是由于在使用db时我们需要用到app中关于数据库的配置（从上下文中取），但是这时项目没有运行，没有请求，
    在local类中没有app的内容，所以我们使用with方法，利用应用上下文管理，将需要的内容添加到loacl对象中

多app离线脚本:
    with app1.app_context():
        # 取栈中获取栈顶的app_ctx,使用top方法取栈顶
        db.create_all()  # 创建

        with app2.app_context():
            db.create_all()
        
        # db.drop_all()

https://www.cnblogs.com/xiao987334176/p/9778183.html
'''
'''
#多app离线脚本
from flask import Flask,current_app,globals,_app_ctx_stack,request

app1 = Flask('app01')
app1.debug = True # 用户/密码/邮箱
# app_ctx = AppContext(self):
# app_ctx.app
# app_ctx.g

app2 = Flask('app02')
app2.debug = True # 用户/密码/邮箱
# app_ctx = AppContext(self):
# app_ctx.app
# app_ctx.g



with app1.app_context():# __enter__方法 -> push -> app_ctx添加到_app_ctx_stack.local
    # {<greenlet.greenlet object at 0x00000000036E2340>: {'stack': [<flask.ctx.AppContext object at 0x00000000037CA438>]}}
    print(_app_ctx_stack._local.__storage__)
    print(current_app.config['DEBUG'])

    with app2.app_context():
            # {<greenlet.greenlet object at 0x00000000036E2340>: {'stack': [<flask.ctx.AppContext object at 0x00000000037CA438> ]}}
        print(_app_ctx_stack._local.__storage__)
        print(current_app.config['DEBUG'])

    print(current_app.config['DEBUG'])
'''
#9.Flask上下文管理中主要涉及了哪些相关的类,并描述相关类的作用

'''
1.请求上下文:
    RequestContext类 存放request和session数据
    LocalStack类  将requestcontext放入Local类中,并且对Local中的线程的数据进行操作
    Local类       创建线程所对应的字典:
        {<greenlet.greenlet object at 0x00000000033EFF20>: {'stack': [<flask.ctx.RequestContext object at 0x00000000035B0048>]}}
    
    LocalProxy类  request和session都是LocalProxy对象，借助偏函数的概念将对应的值传入_lookup_req_object函数。
                  先从_request_ctx_stack（LocalStack对象）中获取ctx(请求上下文对象)，再通过反射分别获取request和session属性
    
'''

#10.为什么flask要把local对象中的值stack维护成一个列表
'''
1.因为通过维护成列表，可以实现一个栈的数据结构，进栈出栈时只取一个数据.
    在local对象中，存储的数据是这样的。app_ctx是应用上下文
    
    线程id:{stack:[app_ctx]}
    它永远存储的是单条数据，它不是真正的栈。如果搞一个字段，直接让stack=app_ctx，照样可以执行。
    
    那么它为什么要维护一个栈呢？因为它要考虑：    
        在离线脚本和多app应用的情况下特殊代码的实现。
        只有这2个条件满足的情况下，才会用到栈！
    {<greenlet.greenlet object at 0x00000000033EFF20>: {'stack': [<flask.ctx.AppContext object at 0x00000000035B0048>]}}

'''

#11.Flask中多app应用如何编写?
'''
多app应用的场景很少见，了解一下，就可以了！
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask, current_app

app1 = Flask('app01')
app2 = Flask('app02')


@app1.route('/index')
def index():
    return "app01"

@app2.route('/index2')
def index2():
    return "app2"


# app1匹配路由时不需要前缀，app2匹配路由时要加上/sec前缀
dm = DispatcherMiddleware(app1, {
    '/sec': app2,
})
# 得到的这个dm对象没有run方法
# 所以要用run_simple

if __name__ == "__main__":
    # app2.__call__
    run_simple('localhost', 5000, dm)


https://www.cnblogs.com/xiao987334176/p/9778183.html
'''
#12.flask中实现websocket需要什么组件
'''
flask-socketio组件

import json

from flask import Flask,request
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

ws_serv = Flask(__name__)

user_socket_dict = {}

@ws_serv.route("/server/<username>")
def server(username):
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    if user_socket:
        user_socket_dict[username] = user_socket
        print(len(user_socket_dict),user_socket_dict)

    while True:
        user_msg = user_socket.receive()
        if not user_msg:
            return "断了!友尽！"
        user_msg_dict = json.loads(user_msg)
        print(user_msg_dict)
        to_user = user_msg_dict.get("to_user",'')
        if to_user:
            to_user_socket = user_socket_dict.get(to_user)
            try:
                to_user_socket.send(user_msg)
            except:
                continue
        else:
            for ws in user_socket_dict.values():
                ws.send(user_msg)

if __name__ == '__main__':
    http_serv = WSGIServer(("127.0.0.1",9526),application=ws_serv,handler_class=WebSocketHandler)
    http_serv.serve_forever()

'''
#13.wtfforms组件de作用
'''
在flask内部并没有提供全面的表单验证，所以当我们不借助第三方插件来处理时候代码会显得混乱，而官方推荐的
一个表单验证插件就是wtforms。wtfroms是一个支持多种web框架的form组件，主要用于对用户请求数据的进行验证，
其的验证流程与django中的form表单验证由些许类似.:
    Forms: 主要用于表单验证、字段定义、HTML生成，并把各种验证流程聚集在一起进行验证。
    Fields: 主要负责渲染(生成HTML)和数据转换。
    Validator:主要用于验证用户输入的数据的合法性。比如Length验证器可以用于验证输入数据的长度。
    Widgets：html插件，允许使用者在字段中通过该字典自定义html小部件。
    Meta：用于使用者自定义wtforms功能，例如csrf功能开启。
    Extensions：丰富的扩展库，可以与其他框架结合使用，例如django。


组件的每个模块具体作用请看:
https://www.cnblogs.com/wdliu/p/10183645.html

'''

#14.Flask框架默认的session处理机制
'''
flask的session是基于cookie的会话保持。简单的原理即：
    当客户端进行第一次请求时，客户端的HTTP request（cookie为空）到服务端，服务端创建session，视图函数根据form表单填写session，
    请求结束时，session内容填写入response的cookie中并返回给客户端，客户端的cookie中便保存了用户的数据。

    当同一客户端再次请求时， 客户端的HTTP request中cookie已经携带数据，视图函数根据cookie中值做相应操作
    （如已经携带用户名和密码就可以直接登陆）。

flask用的secure cookie方式保存session, 即session数据是加密后保存在用户cookie里. secure cookie是flask唯一自带的session方案。
这很容易造成安全问题，如用户Cookie被盗取，而Cookie中有该用户登陆flask框架网站的session，就可以 用其身份登陆那个网站。
因此如果用flask session会话管理来实现登录，必须要使用服务端session，改进session方案。

'''

#15.解释下flask中的Local对象和threadinglocal对象的区别
'''
都是在多线程下实现数据安全的方式,flask中的request是导入进去的，就相当于全局变量，每一个视图都可以对它进行访问修改取值操作，
这就带来了共享数据的冲突问题，解决的思路就是利用协程和线程的唯一标识作为key.

对于单进程单线程：没有影响，基于全局变量

对于单进程多线程：利用threading.local()对象

对于单进程单线程的多协程：本地线程对象就做不到了，要用自定义,即使用Local
'''