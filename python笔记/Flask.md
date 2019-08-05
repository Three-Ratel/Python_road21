# Flask基础

## 1. 框架对比

| Django               | Flask                          |
| -------------------- | ------------------------------ |
| Admin - Model        | 原生无                         |
| Model                | 原生无                         |
| Form                 | 原生无                         |
| session              | 有-颠覆认知                    |
| 教科书式框架         | 第三方组件非常丰富。一切从简   |
| **优势对比**         |                                |
| 组件、功能全，教科书 | 轻，快                         |
| **劣势对比**         |                                |
| 占用资源，cpu，ram   | 先天不足，第三方组件稳定性较差 |
| 创建项目复杂度高     |                                |

## 2. Flask

1. 安装：pip3 install Flask
   - 直接创建python文件
   - ps：不要使用工具中的插件创建Flask项目
2. 三行启动flask项目
3. Flask：框架源码
   - Jinja2：模版语言
   - Markup：render基于此，防止xss攻击
   - Werkzeug：类似django的uwsgi底层都是基于wsgi，承载flask服务，类似tomcat

## 3. 创项目

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
- 浏览器特性：可识别的 content-type 自动渲染，不识别时，自动下载该文件

#### content-type(6)

1. text/html
2. text/plain，保留当前文件格式
3. image/jepg或者 image/png
4. audio/mpeg：<video> ，应该是<audio>，chrome完成的
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
- 返回标准json格式字符串，api接口，先序列化字典，并设置content-type: Application/json

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
    - 请求中的Content-type 中不包含 Form 或 FormData，保留请求体中的原始数据，b""类型

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

1. {{ my_input(arg1, arg2...) }}：引用或执行
2. {%%}：逻辑，方法需要有()
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
from flask import Markup
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

- 基于请求上下文
- 一般和 request 一起导入
- 交由客户端保管机制，加密后存到浏览器的cookies中。
- 原生：不建议添加过多的 key:values
- flask理念：一切从简为服务器减轻压力
- flask-session：把session从浏览器，移动到服务端

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