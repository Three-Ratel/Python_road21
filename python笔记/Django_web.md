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

