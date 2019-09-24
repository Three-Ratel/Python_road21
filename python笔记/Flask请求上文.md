# 请求上文

## 1. 请求上下文的必要性

1.  当 Flask 应用处理经过 WSGI 处理好的请求数据时，将 `environ` 封装成 request 对象。
2.  为了区分不同请求的请求对象，无非就是只有两种(我只知道两种) 方法，全局变量和使用 Context locals(Werkzeug提供) 实现
3.  很明显Flask请求上下文使用的是第二种方式，当然你可能会有疑问，使用全局变量的方式不是更简单便捷吗？
4.  俗话说得好，一个硬币有两面。使用全局变量可以实现没毛病，那就意味着来多少的请求就需要定义多少个全局变量(细思极恐)，而且我们都知道全局变量在程序中应用时很“危险的”，谁都可以访问，也就会导致数据不安全的情况出现等等等问题。
5.  使用第二种方式就可以完美解决使用全局变量的问题，直到请求处理完毕，Flask 会 pop 掉处理完的请求上下文栈，保证了内存不会溢出。有的同学可能还会提出万一 Flask 应用接收到请求后，服务异常怎么办？Flask 也对此进行进行了相应的处理。

## 2. 源码剖析

**特别说明**

1.  图片中标注的红色数字表示 falsk 应用执行顺序
2.  红色标注代笔请求上文
3.  黄色标注代表请求下文

### 1. 请求上文

-   当请求到来时，Flask 会自动把封装 requst、view functions...的 RequstContext 对象 push 进 Local 对象中
-   当请求数据封装到 environ 后，WSGI 会调用 Flask 实例的 `__call__` 方法，即处理请求

![1 app.__call__](/Users/henry/Documents/截图/Py截图/Flask 请求上文/1 app.__call__.png)

-   我们可以看到，environ 就是请求数据

![2 RequestContext()类](/Users/henry/Documents/截图/Py截图/Flask 请求上文/2 RequestContext()类.png)

-   RequestContext 类实例化时，会对请求数据 environ 进行封装成 request 对象(就是Flask 导入的request)，由app.request_class(environ)，主要是对请求数据的格式化，并初始化request对象
-   我们可以很清晰的看到，request 在 RequestContext 实例化的过程中被封装进对象中了

![3 RequestContext()类-push()](/Users/henry/Documents/截图/Py截图/Flask 请求上文/3 RequestContext()类-push().png)

![4 _requsest_ctx_stack.png](/Users/henry/Desktop/4 _requsest_ctx_stack.png.png)

![5 LocalStack()类](/Users/henry/Documents/截图/Py截图/Flask 请求上文/5 LocalStack()类.png)

![6 Local()类](/Users/henry/Documents/截图/Py截图/Flask 请求上文/6 Local()类.png)

-   因为在 Local 类中重写了 `__setattr__` 方法，所以在实例化的过程中使用父类的 `__setattr__` 方法

### 2. 请求下文

-   当我们使用 request.method 时，请求下文就开始发挥作用了
-   首先需要导入 `from flask import request`

![4 _requsest_ctx_stack.png](/Users/henry/Documents/截图/Py截图/Flask 请求上文/4 _requsest_ctx_stack.png.png)

-   这里用到了 functools中的 partial() 函数，主要功能有点类似于装饰器，只要参数传递可以分开传递，也就是说可以多次传递，从底层讲可以维护一块内存空间，用于存储变量值
-   可以看到下图类初始化时，使用了`_LocalProxy__local`，这里使用的是私有变量的外部访问方式，私有变量在外部访问不到，本质就是在变量名前加上了 `_类名__私有变量名`的形式。

![7 LocalProxy](/Users/henry/Documents/截图/Py截图/Flask 请求上文/7 LocalProxy.png)

-   当请求处理结束，返回 reponse 给客户端后，Flask通过 信号机制调用`flask.reqeust_tearing_down`和`flask.``appcontext_tearing_down`等信号，把当前的request数据销毁，整个请求结束。



References：https://flask.palletsprojects.com/en/1.1.x/reqcontext/