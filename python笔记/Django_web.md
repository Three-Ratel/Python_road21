# 1. 项目创建流程

1. 创建虚拟环境(使用pycharm下载)

   - 新建django项目师，创建虚拟环境，pycharm默认会安装最新版的django
   - 在普通的django中创建虚拟环境，之后使用虚拟环境创建Django
   - **勾选** make  avaliable to all projects

2. 下载Django包

   - 创建django项目，如果没有虚拟项目需要手动添加虚拟环境的解释器

3. 创建django项目和app1(**web**)

   - 主要用于web页面的展示和处理

4. 测试用的数据库不同

   - 新建**local_settings**.py 文件

   ```python
   # local_settings.py
   import os
   BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   ALLOWED_HOSTS = []
   # 用于本地debug
   DEBUG = True
   DATABASES = {
   	'default': {
   		'ENGINE': 'django.db.backends.sqlite3',
   		'NAME': os.path.join(BASE_DIR, 'db.local_sqlite3'),}
   }
   ```

   - **settings**.py文件需要导入本地测试配置文件

   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['*']
   LANGUAGE_CODE = 'zh-hans'
   TIME_ZONE = 'Asia/Shanghai'
   USE_L10N = False
   DATE_FORMAT = 'Y/m/d'
   DATETIME_FORMAT = 'Y/m/d H:i:s'
   
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static')
   ]
   # 需要导入local_settings.py中的所有变量
   # 线上使用没有local_settings.py 文件，需要进行异常处理
   try:
   	from .local_settings import *
   except ImportError:
     pass
   ```

5. git版本控制(.gitignore)

   - 忽略虚拟环境目录
   - github找忽略文件，添加.idea/、db.local_sqlite3

6. 创建**app2**：backend

   - 用于后台管理

7. 创建**app3**：repository

   - 用于models的创建

# 2. 上传文件

1. 富文本编辑框

2. 伪静态地址**xx/x.html**（seo）

3. pycharm查找可以使用命名分组进行查找和替换

4. 设计表结构

   - 类别表
     1. 列表的名称
     2. 文章详情表

   - content(textfield)

   - 文章表
     1. title
     2. create_at
     3. profile
     4. category(外键类别表)
     5. content(外键关联文章详情表)

## 1. meida的配置

- pycharm中使用正则进行匹配和替换

```python
../../(.*?)
{% static '$1' %}
```

### 1.1 配置settings.py

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 1.2 配置urls.py

```python
# 项目根的urls.py
from django.views.static import serve
from django.conf import settings
urlpatterns = [
  	url(r'^media/(?P<path>.*)', serve, {'document_root':settings.MEDIA_ROOT})
]
```

### 1.3 ImageField()下载pillow

```python
# 下载pillow包
pip install pillow
```

### 1.4 models.py使用

- 更改完成后使用迁移命令

```python
from django.db import models

class Article(models.Model):
		img = ImageField(upload_to='img/article/', verbose_name='图片')
```

## 2. 富文本编辑器

### 1. 需要下载

- django-ckeditor

```python
# ckeditor
pip install django-ckeditor
```

### 2. 配置文件(2)

```python
# 项目的setting.py
1. 注册 ckedior app
INSTALLED_APPS = [
  	'ckeditor',
		'ckeditor_uploader',
]
2. 配置文件上传路径
CKEDITOR_UPLOAD_PATH = 'ckeditor/'
```

### 3. 在**model.py**中使用字段

- 导入和使用

```python
from ckeditor_uploader.fields import RichTextUploadingField

class ArticleDetail(models.Model):
		content = RichTextUploadingField(verbose_name='文章详情')
```

### 4. 配置url

- 配置url，注意url顺序

```python
from ckeditor_uploader import views
urlpatterns = [
  	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='img'),
  url(r'^ckeditor/upload/', views.upload),
		url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
```

### 5. 在模版中导入js

```django
<script src="{% static 'ckeditor/ckeditor/ckeditor.js' %}"></script>
<script src="{% static 'ckeditor/ckeditor-init.js' %}"></script>
```

### 6. 使用

- models文件使用富文本之后
- 迁移数据库

```python
# repository中的 models.py
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
  	name = models.CharField('分类名', max_length=16)
    
class ArticleDetail(models.Model):
		content = RichTextUploadingField(verbose_name='文章详情')

class Article(models.Model):
  	title = models.CharField('文章标题', max_length=32)
    profile = models.CharField('文章简介', max_length=256)
    img = models.ImageField(upload_to='img/article/', verbose_name = '显示图片')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    category = models.ForeignKey('Category', blank=True, null=True, verbose_name='文章类别')
    # OneToOneField：一对一，并且外键唯一，包含 unique 约束
    detail = models.OneToOneField('ArticleDetail', verbose_name='文章详情')
```

# 3. 滚动请求数据

## 1. url设计

```python
url(r'^(learning_notes|student_evaluation|student-interview).html', views.feedback_list, name='feedback')
```

## 2. 静态页面

- web中的template
- 继续使用模板和继承

## 3. pycharm

```python
# pycharm比较文件或文件夹的不同
compare with
```

## 4. 使用字典取值传参

- 使用字典进行banner和title的分类

- 使用模版进行渲染

## 5. models设计

- 数据库迁移

```python
# repository中的models.py
from django.db import models
class Feedback(models.Model):
  	type_choice = ((0, '未分类'), (1,'学习笔记'), (2, '学员评价'), (3, '入职邀约'),)
  	img = models.ImageField(upload_to='img/feedback/')
    img_type = models.IntegerField(choices=type_choice, default=0)
```

## 2. 滚动尾页请求数据

### 1. 设计url

```python
# urls.py
urlpatterns = [
  	url(r'^ajax_feedback/', views.AjaxFeedback.as_view()),
]
```

### 2. 请求分页使用流程

#### 1. 下载和注册

- djangorestframework

```python
# 一般使用pycharm安装
pip install djangorestframework
```

- 注册

```python
# 注册app
'rest_framwork'
```

#### 2. 使用modelserializer

- **类变量(5)**：queryset、serializer_class、pagination_class、filter_backends和filter_fields

```python
# views.py
from repository import models
from rest_framework import generics
from web.serializer import FeedbackSerializer
from web.pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend

class AjaxFeedback(generics.ListAPIView):
    queryset = models.Feedback.objects.all()
    # 序列化器
    serializer_class = FeedbackSerializer
    # 分页器
    pagination_class = DefaultPagination
    # 过滤条件，和过滤依据
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['img_type']
```

#### 3. 序列化器

- **除了继承类，与modelform写法完全相同**

```python
# serializer里的__init__.py中
from rest_framework import serializers
from repository import models

class FeedbackSerializer(serializers.ModelSerializer):
  	class Meta:
      	model = models.Feedback
        fields = ['img']
```

#### 4. 分页器

- **类变量(4)**：page_size、page_query_param、(page_size_query_param、max_page_size)

```python
# pagination里的__init__.py中
from rest_framwork.pagination import PageNumberPagination
class DefaultPagination(PageNumberPagination):
  	# 一页的数据
  	page_size = 8
    # 分页查询条件的key
    page_query_param = 'page'
    # 当定义page_size有效
    page_size_query_param = 'size'
    max_page_size = 4
```

### 3. 筛选条件使用流程

#### 1. 下载django-filter

```python
# 一般使用pycharm
pip install django-filter
```

#### 2. 注册app

```python
'django_filters'
```

#### 3. models中使用

```python
from django_filters.rest_framework import DjangoFilterBackend

class AjaxFeedback(serializers.ModelSerializer):
		# 过滤条件，和过滤依据
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['img_type']
```

## 3. 滚动触发ajax

- ajax属于异步请求，需要使用**tag**标志，转换成同步
- 这里的data返回的是一个js对象(相当于python的字典)

```js
$(function () {
    var img_type = $('.thisli').attr('img_type');
    var page = 1;		// 请求的页码
    var num = 0;		// 当前请求数据的总条数
    var next = 1;		// data中的字段 next是下次请求的url
    var tag = 1;		// 用于标示当前是否有ajax请求

    function get_info() {

        if (next && tag) {
            tag = 0;
            $.ajax({
                url: `/ajax_feedback/?img_type=${img_type}&page=${page}`,
                success: function (data) {
                    // console.log(data);
                    var results = data.results;
                    next = data.next;

                    for (var i in  results) {
                        var row = results[i];
                        var col = $('.column')[num % 4];
                      	// 需要加入的 html 标签
                        var item = `<div class="item">
                                    <div class="animate-box">
                                    <a href="${row.img}"class="image-popup fh5co-board-img">
                                     <img src="${row.img}"alt="Free HTML5 Bootstrap template">
                                    </a>
                                    </div>
                                    </div>`;
                      
                        $(col).append(item);
                        magnifPopup();
                        animateBoxWayPoint();
                        num += 1
                    }

                    page += 1;
                    tag = 1;
                }
            })
        }
    }

    get_info();
    //同学说分批加载
    $(window).scroll(function () {
        //$(document).scrollTop() 滚动条位置距页面顶部的距离；
        //$(document).height() 整个页面的总高度；
        //$(window).height() 当前窗口的高度；
        //判断是否已经滚动到页面底部；
        if ($(document).scrollTop() >= $(document).height() - $(window).height() - 180) {
            get_info();
        }
    });
}());
```

