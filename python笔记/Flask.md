# 1. Flask基础

## 1. 框架对比

| Django               | Flask                                              |
| -------------------- | -------------------------------------------------- |
| Admin - Model        | 原生无                                             |
| Model                | 原生无                                             |
| Form                 | 原生无                                             |
| **session**          | 有-颠覆认知(存储到服务端内存中，浏览器的cookies中) |
| 教科书式框架         | 第三方组件非常丰富。一切从简                       |
| **优势对比**         |                                                    |
| 组件、功能全，教科书 | 轻，快                                             |
| **劣势对比**         |                                                    |
| 占用资源，cpu，ram   | 先天不足，第三方组件稳定性较差                     |
| 创建项目复杂度高     |                                                    |

## 2. Flask

1. 安装：pip3 install Flask
   - 直接创建python文件
   - ps：不要使用工具中的插件创建Flask项目
2. 三行启动flask项目
3. Flask：框架源码
   - Jinja2：模版语言
   - MarkupSafe：render基于此，防止xss攻击
   - Werkzeug：类似django的uwsgi底层都是基于wsgi，承载flask服务，类似tomcat

## 3. 创建项目

### 1. 创建py文件

- 设置DEBUG：项目会自动重启

```python
from flask import Flask
# 命名
app = Flask('app.py')
# 或 app = Flask(__name__)
app.config['DEBUG'] = True
# 或 app.debug = True

@app.route('/')
def home():
  	return 'AH, you are visiting Flask-site!'

if __name__ == '__main__':
		app.run()
```

### 2. Flask的response

-  content type：浏览器根据此参数，判断响应类型

#### 1. "xxx"

- django中的 HttpResponse('hello')，Flask是 'hello'

```python
@app.route('/index')
def index():
  	return  'hello world i am Flask'
```

#### 2. render_template

- 响应模版

```python
@app.route('/index')
def index():
  	return render_template('index.html')
```

#### 3. redirect

- 在Response Header中加入 Location简直对

```python
@app.route('/login')
def login():
  	return render_template('/index')
```

- **以上是web框架的三剑客**

#### 4. send_file()

- response instance：流媒体类型

- 打开文件并自动识别文件类型，在content-type中添加文件类型，content-type:文件类型
- **浏览器特性**：可识别的 content-type 自动渲染，不识别时，自动下载该文件

#### content-type(6)

1. text/html
2. text/plain，保留当前文件格式
3. image/jepg或者 image/png
4. audio/mpeg：<video> ，应该是<audio>，chrome完成
5. video/mp4：<video> 标签
6. application/x-msdownload：xx.exe

- 文件类型：一般是文件第一行就是文件类型

```python
from flask import send_file
@app.route('/get_file')
def get_file():
  	# 返回文件内容，自动识别文件类型
  	return send_file('app.py')
```

#### 5. jsonify

- flask 1.1.1 版本中，dict直接作为返回值返回，无须 jsonify
- **返回标准json格式字符串，api接口，先序列化字典，并设置content-type: Application/json**

```python
@app.route('/get_json')
def get_json():
  	d = {'k':'v'}
    return jsonify(d)
```

## 4. request

- request在flask中是够公共变量(顶头小写)，请求上下文管理
- 从reqeust中获取的数据类型为：ImmutableMultiDict([('id', '1')])

1. request.method
2. request.form
   - 获取 FormData 中数据(ajax)
   - request.from.to_dict()：返回对应的字典
   - 类型：ImmutableMultiDict([])
3. request.args
   - 获取url中的参数
4. reqeust.values
   - 获取 url 和 FormData 中的数据，如果key相同 url中的会覆盖 form中数据
   -  **CombinedMultiDict**([ImmutableMultiDict([('id', '1')]), ImmutableMultiDict([])])
5. request.host：ip + port
6. request.path：url路由地址
7. request.url：完整路径
8. request.cookies
   - 字典，获取浏览器请求时带上的cookies
9. request.files
   - 获取Form中文件，返回 **FileStroage**中有 **save() 方法和 filename属性**
10. request.json
    - 请求中的Content-type:application/json
    - 请求体中的数据被序列化到request.json中，以字典的形式存放
11. request.data
    - 请求中的Content-type 中不包含 Form 或 FormData，保留请求体中的原始数据，**b""类型**

```python
from flask import Flask
app = Flask(__name__)

@app.route('/login', methods=['GET','POST',])
def login():
  	# 优先判断请求方式
    # 如果是GET请求
    if request.method == 'GET':
      	return render_template('login.html')
    # 如果是POST请求，获取 用户名，密码 校验
    else: # 405 请求方式不被允许
      	# request.form.to_dict()
        my_file = request.files.get('my_file')
        filename = my_file.filename
        filepath = os.path.join('avatar', filename)
        my_file.save(filepath)
        if request.form.get('username') == 'xxx':
          	return 'Login OK!'
    return '200 ok'

if __name__ == '__main__':
		app.run()f
```

- ImmutableMultiDict类型数据用法和dict类型相同，都有 values(), item()，keys() 方法

## 5. Jinja2

### 1.  与templates不同

1. {{ my_input(arg1, arg2...) }}：引用或执行，函数必须有括号
2. {% %}：逻辑，方法需要有()
3. dict类型可以使用 info['username']
4. 如果变量没有定义会报错

### 2. 传递变量

```python
app.config['DEBUG'] = True
或 app.debug = True

@app.route('/')
def stu():
  	return render_template('stu.html', stu=STUDENT,)
app.run('0.0.0.0:9527')
```

### 3. 传递函数

- @app.template_global()：项目中任何地方都可以使用被装饰的函数

```python
@app.template_global()
def ab(a,b):
  	return a+b

@app.route('/a')
def homea():
  	return render_template('a.html')
```

### 4. 宏指令

- 在jinja2模版中使用

```jinja2
{% macro my_input(na, ty) %}
		<input type="{{ ty }}" name="{{ na }}">
{% endmacro %}
{{ my_input('username', 'text') }}
```

### 5. Markup

- 在view 函数中先生成标签在使用

```python
from markupsafe import Markup

@app.route('/a')
def homea():
  	inp = Markup("<input type='submit' value='xxx'>")
    return render_template('a.html', btn=inp)

def my_input(na, ty):
  	s = f"<input type='{ty}' value='{na}'>"
    return Markup(s)
```

```jinja2
{{ btn | safe }} 或者使用  Markup{{ btn }}
{{ my_input('username', 'text') }}
```

## 6. session

1. 基于请求上下文
2. 一般和 request 一起导入
3. **交由客户端保管机制**，加密后存到浏览器的cookies中。
4. 原生：不建议添加过多的 key:values，健值对越多，浏览器需要保存的cookies越长，Flask会先对健值对进行压缩在加密
5. flask理念：一切从简为服务器减轻压力
6. flask-session：把session从浏览器，移动到服务端

```python
from flask import session
# 密钥不能为空
app.secret_key = "1!@#$8943:''.,xvzn;5lk12@!lg)*743%^&"
# 装饰器

def warpper(func):
  	def inner(*args, **kwargs):
      	# 校验登录状态、校验session中有没有 user key
      	if session.get('user'):
          	return func()
        else:  # 校验失败，跳转到登录页面
          	return redirect('/login')
		return inner

@app.route('/login', methods=['GET', 'POST'])
def login():
  	if request.method == 'GET':
      	return render_template('login.html')
    else:
      	if request.form.get('username') == 'henry':
          	return 'Login OK!'
        else:
        		return 'failed'

@app.route('/')
@warpper
def homea():
    return render_template('a.html')
```

# 2. Flask项目

## 1. 路由

### 1. 装饰器装饰多个函数

1. 自定义装饰器最终会出现多个 inner 函数最终为 endpoint，flask中通过endpoint查找view
2. 基于functools 修改 `__name__`
3. 添加endpoint参数

```python
@app.route('/a', endpoint='end_a')
@warpper
def a():
    pass
  
@app.route('/b', endpoint='end_b')
@warpper
def b():
    pass
  
@app.route('/', endpoint='home')
@warpper
def home():
    pass
```

- endpoint值必须唯一

### 2. route参数(5)

#### 1. methods=[]/()

- 请求方式不区分大小写

```python
@app.route(rule, methods=['get', 'POST', 'options'])
```

- getatter() or ('GET', )
- set(item.upper() for item in methods)

#### 2. endpoint=None

- 解决装饰器不能装饰多个函数的问题
- 路由地址和endpoint的mapping)
- 路由地址和视图之间mapping
- 默认是视图函数名

```python
@app.route('/', endpoint=None)
def home():
    return 'ok!'
```

#### 3. defaults={'count': 20}

- 默认20，用于分页
- url_for()

```python
from flask import Flask
url_for('end_a')
url_for('home')
# {'end_a':'/a', 'home': '/'}
```

```python
@app.route(rule, endpoint=None, defaults={'count':20})
def home(count):
    count = request.args.get('count', count)
    return f'200 ok!{count}'
```

#### 4. strict_slashes=False

- 是否严格遵循地址匹配

```python
@app.route(rule, endpoint=None, strict_slashes=True)
def home():
    return f'200 ok!{count}'
```

#### 5. redirect_to='/'

- 永久重定向，状态码，308/301

```python
@app.route(rule, endpoint=None, redirect_to='/')
```

### 3. 动态参数路由

- str：可以收一切，默认是 str 类型
- rule：`/ge t_music/<filename>`， `/home/<int:page>`， `/home/<ty>_<page>_<id>`，分页、获取文件、解决分类，解决正则路由
- send_file()：需要限定文件目录

```python
@app.route('/home/<int:page>', endpoint='home',)
def home(page):
    print(type(page))
    return '200 ok!'
  
@app.route('/home/<page>_<ty>_...', endpoint='home',)
def home(page, ty, ...):
    pass
  
@app.route('/home/<filename>', endpoint='home',)
def home(filename):
    return send_file(f'media/{filename}')
```

## 2. Flask中的配置

### 1. 初始化配置

#### 1. template_folder=''

- 指定模板存放路径，默认时templates

```python
app = Flask(__name__,  template_folder='templates')
```

#### 2. staic_folder='static'

- 锁定访问目录，静态文件存放目录，默认：static

```python
app = Flask(__name__, static_folder='img', static_url_path='/static')
# http://127.0.0.1:5000/static/1.jpeg
```

#### 3. static_url_path='/static'

- 静态文件访问路径，默认`/staic_folder`
- 自动拼接 host

```python
<img src='访问地址'>
<img src='static/1.jpg'>
```

- static_host=None：其他主机

- instance_path：多app

### 2. 实例配置(app配置)

#### 1. default_config

- default_config = {} ：默认配置
- 'TESTING'：False，日志级别为Debug
- ''：31days
- JSONIFY_MIMETYPE='application/json'

```python
# 开启 debug 模式
app.debug = True
# 使用session
app.secret_key = 'R&w34hr*&%^R7ysdjh9qw78r^*&A%863'
# session名称
app.session_cookie_name = 'ah'
# session生命周期，20s过期为 None
app.permanent_session_lifetime = 20
# respone头中content-type:xxx
app.config['JSONIFY_MIMETYPE']='xxx'
```

#### 2. settings.py

```python
import hashlib

class DubugConfig(object):
    DEBUG = True
    SECRET_KEY = '#$%^&fguyhij&^$EHBksdj`109u23'
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_COOKIE_NAME = 'ah'

class TestConfig(object):
    TESTING = True
    SECRET_KEY = hashlib.md5(f'{time.time()}#$%^&124:"hfag(&sfdgh3ir;dfguyhij&^$EHBksdj`109u23{time.time()}'.encode('utf-8')).hexdigest()
	PERMANENT_SESSION_LIFETIME = 360000
    SESSION_COOKIE_NAME = '$%^&124:"hfag('
```

#### 3. 配置生效

```python
from settings.py import DubugConfig,TestConfig
app.config.from_object(DubugConfig)
app.config.from_object(TestConfig)
```

## 3. Blueprint

- 不能被run的flask实例，不存在config

```python
from flask import Blueprint

bp = Blueprint('app01', __name__,url_prefix='/car')

@bp.route('/user')
def user():
    return 'I am app01!'
```

```python
from app01 import bp
app.register_blueprint(bp)
```

## 4. 特殊装饰器

- requset校验没过时，绕过view 执行全部after_request
- 只要有响应返回，af全部执行

### 1. @app.before_request

- 在请求进入视图函数之前，作出处理

```python
@app.before_reqeust
def be1():
    print('i am be1')
    
@app.before_reqeust
def be2():
    print('i am be2')
```

### 2. @app.after_request

- 在响应返回客户端之前，结束view之后

```python
@app.after_request
def af1(res):
    print('i am in af1')
    return res

@app.after_request
def af2(res):
    print('i am in afp2')
    return res
```

### 3. @app.errorhandler(404)

- 监听状态码只能是 4xx和5xx
- 需要接受错误信息

```python
@app.errorhandler(404)
def error404(error_message):
    print(error_message)
    return 'xxx' 		# 5种类型
```