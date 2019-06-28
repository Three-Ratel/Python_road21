1. res为http的响应体
2. 使用Jsonresponse,浏览器接收后会自动反序列化

## 今日内容

### 1. form组件

1. 生成页面可用的HTML标签
2. 对用户提交的数据进行校验，提供错误提示
3. 保留上次输入内容

### 1.1 普通手写功能

```python
# views.py
def register(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username, len(username))
        if len(username) < 6:
            msg = '用户名长度至少6位'
        else:
            # 把用户名和密码写入数据库
            return HttpResponse('注册成功')
    return render(request, 'register.html', {'msg': msg})
```

```django
{# register.html #}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
</head>
<body>
<form action='/register/' method='post'>
    {% csrf_token %}
    <p>
        <input type='text' name='username' placeholder="用户名" autofocus>{{ msg }}
    </p>
    <p>
        <input type='password' name='pwd' placeholder="密码">
    </p>
    <p>
        <button>提交</button>
    </p>
</form>
</body>
</html>
```

### 1.2 使用form组件实现

```python
# views.py
from django import forms

class RegForm(forms.Form):
    username = forms.CharField()
    pwd = forms.CharField()

def register(request):
    obj = RegForm()
    if request.method == 'POST':
        obj = RegForm(request.POST)
        if obj.is_valid():
            return HttpResponse('注册成功')
    return render(request, 'register.html', {'obj': obj})
```

```django
{# register.html #}
{# form表单中的novalidate属性表示浏览器不进行校验 #}
<form action="/register/" method="post" novalidate>
    {% csrf_token %}
    {{ obj.as_p }}  {# 使用默认方式生成input和label标签 #}
		
  	{# 指定label的值 #}
    <p>
        <label for="{{ obj.username.id_for_label }}">用户名:</label>
        {{ obj.username }} {{ obj.username.errors.0 }}
    </p>
    <p>
        <label for="{{ obj.pwd.id_for_label }}">密码:</label>
        {{ obj.pwd }} {{ obj.pwd.errors.0 }}
    </p>
  	{{ obj.errors }}
    <button>提交</button>
    </p>
</form>
```

form 表单的功能

- 前端页面是form类的对象生成的                                      -->生成HTML标签功能
- 当用户名和密码输入为空或输错之后 页面都会提示        -->用户提交校验功能
- 当用户输错之后 再次输入 上次的内容还保留在input框   -->保留上次输入内容

### 2. form组件字段与插件

- 创建Form类时，主要涉及到 【字段】 和 【插件】，**字段用于对用户请求数据的验证**，**插件用于自动生成**HTML;
- **常用字段**
  - CharField
  - ChoiceField
  - MultipleChoiceField

#### 2.1 initial

- 初始值，input框中的默认值

```python
from django import forms
class RegForm(forms.Form):
   username = forms.CharField(
     min_length=6,
     # 给username字段设置默认值
     label = '用户名',
     initial = 'henry',
   )
    pwd = forms.CharField(min_length=6, label='密码')
```

#### 2.2 error_messages

- 重写错误信息

```python
from django import forms
class RegForm(forms.Form):
   username = forms.CharField(
     min_length=6,
     # 给username字段设置默认值
     label = '用户名',
     initial = 'henry',
     error_messages = {
       'required': '不能为空',
       'invalid': '格式有误',
       'min_length': '用户名最短6位'
     }
   )
    pwd = forms.CharField(min_length=6, label='密码')
```

#### 2.3 password

```python
from django import forms
class RegForm(forms.Form):
    pwd = forms.CharField(
      min_length=6, 
      label='密码',
      # 表示输入密码时，为密文显示
      widget = forms.widgets.PasswordInput,
    )
```

#### 2.4 radioSelect

- 单radio值为字符串，单选点击框
- **生成ul标签**

```python
from django import forms
class RegForm(forms.Form):
   username = forms.CharField(
     min_length=6,
     # 给username字段设置默认值
     label = '用户名',
     initial = 'henry',
     error_messages = {
       'required': '不能为空',
       'invalid': '格式有误',
       'min_length': '用户名最短6位'
     }
   )
  pwd = forms.CharField(min_length=6, label='密码',)
	gender = forms.fields.ChoiceField(
  	choices=((0, 'female'), (1, 'male'), (3, 'secret')),
    label = '性别',
    initial = 3,
    widget = forms.widgets.RadioSelect()
  )
```

#### 2.5 单选select

- 单选下拉框

```python
from django import forms
class RegForm(forms.Form):
  ...
  hobby = forms.ChoiceField(
  	choices = ((1, 'travelling'), (2, 'reading'), (3, 'listening'),),
    label = '爱好',
    initial = 3,
    widget=forms.widgets.Select(),
  )
```

#### 2.6 多选select

```python
from django import forms
class RegForm(forms.Form):
  ...
  hobby = forms.MultipleChoiceField(
          choices=(('1', 'travelling'), ('2', 'reading'), ('3', 'listening'),),
          label='爱好',
          initial=['3'],
          widget=forms.widgets.SelectMultiple(),
      )
```

#### 2.7 单选checkbox

```python
from django import forms
class RegForm(forms.Form):
  ...
  keep = forms.ChoiceField(
  	label = '是否记住密码',
    initial = 'checked',
    widget=forms.widgets.CheckboxInput(),
      )
```

#### 2.8 多选checkbox

```python
from django import forms
class RegForm(forms.Form):
  ...
   hobby = forms.fields.MultipleChoiceField(
       choices=((1, 'travelling'), (2, 'reading'), (3, 'listening'),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple()
    )
```

**关于choice的注意事项**

1. 在使用选择标签时，需要注意choices的选项可以从数据库中获取，但是由于是静态字段 **获取的值无法实时更新**，那么需要自定义构造方法从而达到此目的。

#### 2.9  自定义

- 使用MutipleChoiceField

```python
from django import forms
hobby = forms.MutipleChoiceField(
  # 从数据库中读取
	choices=models.Hobby.objects.all().values_list('pk', 'name')
)
```

- 使用ModelChoiceField

```python
from django import forms
hobby = forms.ModelChoiceField(
  # 从数据库中读取
	queryset=models.Hobby.objects.all()
)
```

- 刷新页面更新数据

```python
class RegForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(RegForm, self).__init__( *args, **kwargs):
    	self.fields['hobby'].choices = models.Hobby.objects.values_list()
    hobby = forms.ModelChoiceField(
    # 从数据库中读取
    queryset=models.Hobby.objects.all()
  	)
```

### 3. 校验

#### 3.1 内置校验

```python
from django.forms improt Form
from django.core.validators import RegexValidator

class MyForm(From):
  phone = forms.CharField(
    # 正则校验器中，第二个参数是提示信息
    validators=[RegexValidator(r'1[3-9]\d{9}$', '手机号不合法')]
    )
```

#### 3.2 自定义校验

```python
from django.core.exceptions import ValidationError
def checkname(value):
  if 'o' in value:
    rasie ValidationError('用户名不合法')
    
class RegForm(forms.Form):
   username = forms.CharField(
     min_length=6,
     # 给username字段设置默认值
     label = '用户名',
     initial = 'henry',
     validators = [checkname,...]
    )
    pwd = forms.CharField(
    	widget = forms.widgets.PasswordInput(),
    )
```

#### 3.3 钩子

- 局部钩子

```python
class RegForm(forms.Form):  
  username = forms.CharField(label='用户名')
  def clean_username(self):
        if 'o' in self.cleaned_data.get('username'):
            raise ValidationError('用户名不合法。。。。。')
```

- 全局钩子

```python
class RegForm(forms.Form):  
  pwd = forms.CharField(
        label='密码',
        widget=forms.widgets.PasswordInput,
    )
  re_pwd = forms.CharField(
        label='密码',
        widget=forms.widgets.PasswordInput,
    )
  def clean(self):
    if not self.cleaned_data.get('pwd') == self.cleaned_data.get('re_pwd'):
      self.add_error('re_pwd','两次密码不一致')
      raise ValidationError('两次密码不一致')
```

#### 3.4 批量添加样式

```python
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        label="用户名",
        initial="henry",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短5位"
        }
    ...

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

```

#### 3.5 ModelForm

```python
class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = "__all__"
        labels = {
            "title": "书名",
            "price": "价格"
        }
        widgets = {
            "password": forms.widgets.PasswordInput(attrs={"class": "c1"}),
        }
```

```python
model = models.Student  # 对应的Model中的类
fields = "__all__"      # 字段，如果是__all__,就是表示列出所有的字段
exclude = None          # 排除的字段
labels = None           # 提示信息
help_texts = None       # 帮助提示信息
widgets = None          # 自定义插件
error_messages = None   # 自定义错误信息
```































### 自定义校验器

- 写函数

```python
from django.core.exeception import ValidationError

def checkname(value):
  # 通过校验规则不做任何操作
  # 没有通过校验规则，抛出异常
  if 'alex' in value:
    raise ValidationError('不符合要求')
  
username = forms.CharField(label='用户名', 
                            min_length=6，
                            initial = '默认值',
                           	# 自定义校验优先
                            validators = [checkname],
                            error_message = {
                               'required':'用户名必填',
                               'min_length':'用户名长度不能少于6位'
                             }
                           )
```

- 使用内置校验器

```python
from django.core.validators import RegexValidators
phone = forms.CharField(
  validators=[RegexValidators(r'^1[3-9]\d{9}$', '手机号格式不正确')]
)
```

- 

```python
if obj.is_valid():
  print(obj.cleaned_data)
```

- is_valid执行流程

1. 执行full_clean方法
   1. 定义错误字典
   2. 存放清洗过数据的字典
2. 执行clean_field方法，
   1. 循环所有字段，获取当前字段值，
   2. 对值校验(内置和自定义校验)
      - 通过校验self.clean_data[name] = value
        1. 如果有局部钩子，就要执行校验
        2. 通过则，self.clean_data[name] = value
        3. 不通过，self._errors添加当前字段错误，并且删除：del self.clean_data[name]
      - 没有通过self._errors添加当前字段错误
   3. 执行全局钩子clean方法

```python
# 局部钩子
def clean_username(self):
  # 通过校验规则，必须返回当前字段值
  # 没有通过校验规则，抛出异常
  v = self.clean_data.get('username')
  if 'xx' in v:
     raise ValidationError('不符合要求')
  return v
```

- 全局钩子

```python
def clean(self):
    # 通过校验规则，必须返回所有字段值
    # 没有通过校验规则，抛出异常 '__all__'
    pwd = self.clean_data.get('pwd')
    re_pwd = self.clean_data.get('re_pwd')
  	if pwd == re_pwd:
      return self.cleaned_data
    else: 
      self.add_error('re_pwd', '密码不一致')
      raise ValidationError('密码不一致!!!')
```























1. jsonresponse测试
2. 用户名校验
3. sweetalter
4. 箭头函数保留当前this指向：success:(res) = > {$(this)}