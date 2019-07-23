# 1. 项目创建流程

1. 创建虚拟环境(使用pycharm下载)

   - 新建django项目师，创建虚拟环境，pycharm默认会安装最新版的django
   - 在普通的django中创建虚拟环境，之后使用虚拟环境创建Django
   - 勾选 make  avaliable to all projects

2. 下载Django包

   - 创建django项目，如果没有虚拟项目需要手动添加虚拟环境的解释器

3. 创建django项目和app1(**web**)

   - 主要用于web页面的展示和处理

4. 测试用的数据库不同

   - 新建local_settings.py 文件

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

   - settings.py文件需要导入本地测试配置文件

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

6. 创建app2：backend

   - 用于后台管理

7. 创建app3：repository

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
../../(.*)"
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
CKEDITOR_UPLOADS_PATH = 'ckeditor/'
```

### 3. 在**model.py**中使用字段

- 导入和使用

```python
from ckeditor_uploader.fields import RichTextUploadingField

class ArticleDetail(models.Model):
		content = RichTextUploadingField(verbose_name='文章详情')
```

### 4. 配置url

- 配置url

```python
from ckeditor_uploader import views
urlpatterns = [
  	url(r'^media/(?P<path>.*)$', serve, {'document_root'}: settings.MEDIA_ROOT, name='img')
		url(r'^ckeditor/', include('ckeditor_uploader.urls'))
		url(r'^ckeditor/upload/', views.upload)
]
```

### 5. 在模版中导入js

```django
<script src="{% static 'ckeditor/ckeditor/ckeditor.js' %}"></script>
<script src="{% static 'ckeditor/ckeditor-init.js' %}"></script>
```

### 4. 使用

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