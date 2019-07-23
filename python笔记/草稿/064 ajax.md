## 1. csrf装饰器

### 1.1 装饰器

- **csrf_exempt,** 只能加到dispatch方法上(类中或者重写dispatch方法)
- **ensure_csrf_cookie**，一般加在get请求上，确保生成cookies

```python
from django.views.decorators.scrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator
# csrf_exempt,只能加到dispatch方法上
@method_decorator(scrf_exempt, name='dispatch')
class Login(View):
  # 或者
  @method_decorator(scrf_exempt)
  def dispatch(View):
    ret = super().dispatch(request, *args, **kwargs)
    return ret
  # 确保生成csrf校验的cookie
  @method_decorator(ensure_csrf_cookie)
  def get(self, request):
    pass
```

```python
# csrf_exempt，某个视图不需要csrf校验
# scrf_protect,某个视图需要csrf校验(方法没有限制)
# ensure_csrf_cookie，确保生成csrf校验的cookie
class Login(View):
  @method_decorator(scrf_protect)
  def post(View):
    pass
```

### 1.2 csrf功能

1. csrf中间件中执行process_request
   1. 从cookie中获取到scrftoken值
   2. csrftoken的值放入request.META中
2. 执行process_view，执行流程
   1. 查询视图函数是否使用**csrf_exempt**装饰器，使用了,不使用csrf校验
   2. 判断请求方式：
      - 如果是（GET，HEAD、OPTIONS，TRACE）**不进行校验**
   3. 其他请求方式(POST,PUT)，进行csrf校验
      1. 获取cookies中的csrftoken值
      2. 获取post请求中的csrfmiddlewaretoken值
         - 能获取到赋值给—> **request_csrf_token**
         - 获取不到—>获取请求头**x-csrftoken**的值赋值给—>  **request_csrf_token**
      3. 比较request_csrf_token和csrf_token两个值，成功则接受请求，否则拒绝

## 2. ajax简介

### 2.1 什么是json

1. JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
2. JSON 是轻量级的文本数据交换格式
3. JSON 独立于语言 
4. JSON 具有自我描述性，更易理解
5. JSON 使用 JavaScript 语法来描述数据对象，但是 JSON 仍然独立于语言和平台。JSON 解析器和 JSON 库支持许多不同的编程语言。

![js和python的json](/Users/henry/Documents/截图/Py截图/js和python的json.jpg)

### 2.2 xml

- json出现之前使用
- 和json一样是一种数据格式

### 2.3 ajax

发送请求的方式：地址栏输入url、form表单、a标签、**ajax**

#### 1. 定义

- ajax：使用js的技术发送和接受请求响应
- 特点：**异步(不用等待响应)**、局部刷新、传输的数据量小
- 基于js的

#### 2. 简介

1. AJAX（Asynchronous Javascript And XML）翻译成中文就是“异步的Javascript和XML”。即使用Javascript语言与服务器进行异步交互，传输的数据为XML（当然，传输的数据不只是XML）。
2. AJAX 不是新的编程语言，而是一种使用现有标准的新方法。
3. AJAX 最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。（这一特点给用户的感受是在不知不觉中完成请求和响应过程）
4. AJAX 不需要任何浏览器插件，但需要用户允许JavaScript在浏览器上执行。
   - 同步交互：客户端发出一个请求后，需要等待服务器响应结束后，才能发出第二个请求；
   - 异步交互：客户端发出一个请求后，无需等待服务器响应结束，就可以发出第二个请求。

## 3. ajax示例

### 3.1 input数值加

```html
<input type="text" name="num1">+
<input type="text" name="num2">=
<input type="text" name="num3">
<button type="button" id="b1">计算</button>
<script src="/static/js/jquery.js"></script>
<script>
    $('#b1').click(function () {
        $.ajax({
            url: '/sum/',
            type: 'post',
            data: {
                a: $('[name="num1"]').val(),
                b: $('[name="num2"]').val(),
            },
            success: function (res) {
                $('[name="num3"]').val(res);
            }, error: function (error) {
                console.log(error);
            }
        })
    })
</script>
```

```python
# views.py
def sum(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = int(a) + int(b)
        print(request.POST)
        return HttpResponse(c)
    return render(request, 'sum.html')
```

### 3.2 

```python
hobby:JSON.stringify(['movies', 'reading'])
import json
data = JSON.loads(request.POST.get('hobby'))
print(data)
```

### 3.3 上传文件

#### 1. contentType:

- 为Fasle时，Content-Type: application/x-www-form-urlencoded; charset=UTF-8
- 为True时，multipart/form-data; boundary=----WebKitFormBoundarydH6Ju8KqrsQJrAmz

#### 2. 上传文件

```js
// upload.html
<input type='file' id='f1'>
<button id='b1'>上传</button>
$('#b1').click(function(){
  var form_data = new FormData();
  // 只有dom对象有file属性
  form.append('file', document.getElementById('f1').files[0]);
  // 先把jquery对象转为，js对象
  //  form.append('file', $('#f1')[0].files[0]
  
  $.ajax({
    url:'/uplaod/',
    type:'post',
    data:form_data,
    // 按照enctype='mulipart/form-data',如果不写content-type=form表单的第一格式提交
    processData:false,
    // 不让浏览器处理请求头，如果不写默认true，即content-type=true
    contentType:false,
    success:function(res){
      console.log(res)
    }
  });
})
```

```python
# views.py
def upload(request):
    if request.method == 'POST':
        data = request.FILES.get('file')
        print(data, type(data),'*'*8, data.name, type(data.name))
        # 必须for循环取出文件的数据
        with open(data.name, mode='wb') as f:
            for i in data.chunks():
                f.write(i)
        return HttpResponse('ok')

    return render(request, 'upload.html')
```

### 3.3 ajax请求通过csrf校验

#### 1. 通过csrf条件

1. 确保有csrftoken的cookie
   - 在页面中使用{% csrf_token %}
   - 加装饰器ensure_csrf_token
2. **给data中添加csrfmiddlewaretoken**

```js
$('#b1').click(function () {
        $.ajax({
            url: '/sum/',
            type: 'post',
            data: {
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
                a: $('[name="num1"]').val(),
                b: $('[name="num2"]').val(),
            },
            success: function (res) {
                $('[name="num3"]').val(res);
            }, error: function (error) {
                console.log(error);
            }

        })
    });
```

- **或者设置请求头**
-  headers: { 'x-csrftoken': $('[name="csrfmiddlewaretoken"]').val()},

```js
// ajax中的参数；
{% csrf_token %}
$('#b2').click(function () {

        $.ajax({
            url: '/test/',
            type: 'post',
            headers: {
                'x-csrftoken': $('[name="csrfmiddlewaretoken"]').val()
            },
            data: {
                name: 'henry',
                age: 19,
                hobby: JSON.stringify(["movies", "reading"]),
            },
            success: function (res) {
                console.log(res);
            }, error: function (error) {
                console.log(error);
            }

        })
    })
```

#### 3. 使用文件 

1. 新建js文件
2. script引入即可

- **getCookie方法**

```js
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
```

- 使用**$.ajaxSetup()**方法为ajax请求统一设置

```js
function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});
```

#### Note(3)

1. 如果使用从cookie中取csrftoken的方式，需要确保cookie存在csrftoken值。
2. 如果你的视图渲染的HTML文件中没有包含 {% csrf_token %}，Django可能不会设置CSRFtoken的cookie。
3. 这个时候需要使用ensure_csrf_cookie()装饰器强制设置Cookie。





