# SQLAlchemy

-   ORM框架、通用
-   Django-Model：基于django

## 1. 安装

```python
pip install sqlalchemy
```

## 2. 使用

### 1. 约束

-   primary_key
-   auto_increment
-   nullable
-   index
-   unique

### 2. 数据类型

-   INT、INTEGER、Integer：都是整型
-    CHAR、 NCHAR、VARCHAR、 NVARCHAR、String：都是字符串

```python
# 声明一个基类
from sqlalchemy.ext.declarative import declarative_base
BaseModel = declarative_base()

from sqlalchemy import Column, INT, String
# ORM：object relationship mapping
class User(BaseModel):
    # 创建一个table
    __tablename__ = 'user'
    id = Column(INT, primary_key=True, auto_increment=True)
    name = Column(String(32), nullable=False, index=True, unique=True)
  
# 数据库引擎创建
from sqlalchemy.engine import create_engine
# 数据库连接驱动语句
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy?charset=utf8')

# 利用 User 去数据库创建 user Table
BaseModel.metadata.create_all(engine)
```

-   增加数据

```python
# 1. 选择数据库
from sqlalchemy.engine import create_engine
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy?charset=utf8')
from sqlalchemy_study import engine
# 2. 选择表
from sqlalchemy_study import User
# 3. 创建查询窗口
from sqlalachemy.orm import sessionmaker
# 选中数据库
select_db = sessionmaker(engine)
# 已经打开查询窗口
db_session = select_db()
```

-   插入、批量插入，add、add_all

```python
# 1. 写入sql语句
user = User(name='henry')
db_session.add(user)
# 批量创建
user_list = [User(name=i) for i in ['henry', 'echo', 'dean'...]]
db_session.add_all(user_list)
# 2. 提交sql
db_session.commit()
# 3. 关闭窗口
db_session.close()
```

-   查询，query

```python
# 查询所有数据
res = db_session.query(User).all()
print(res[0].id, res[0].name)
# 查询第一条数据
res = db_session.query(User).first()
print(res.id, res.name)

# 查询id=3的数据，数据是list
res = db_session.query(User).filter(User.id==3, User.name=='123').all()
or 
res = db_session.query(User).filter_by(id=3, name='123').all()
print(res[0].id, res[0].name)
```

-   修改，update

```python
# 修改数据
db.session.query(User).filter(User.id==1).update({'name':'dean'})
db_session.commit()
db_session.close()
```

-   删除数据，delete

```python
# 删除数据
db.session.query(User).filter(User.id==1).delete()
db_session.commit()
db_session.close()
```

## 3. 外键

### 1. 创建表

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.engine import create_engine
# 几乎支持所有的关系型数据库
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy?chrset=utf8')
BaseModel = declarative_base()
```

-   一对多的关系

```python
# ORM 精髓, relationship 所在的类是正向类
from sqlalchemy.orm imoprt relationship
class School(BaseModel):
    __tablename__ = 'school'
    # auto_increment可以省略
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

class Student(BaseModel):
    __tablename__ = 'studnet'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    sch_id = Column(Integer, ForeignKey('shool.id'))
	# mapping
    stu2sch = 'cf'('School', backref='sch2stu')

BaseModel.metadata.create_all(engine)
```

### 2. 操作

```python
from sqlalchemy.orm import sessionmaker
from xxx import engine
select_db = sessionmaker(engine)
db_session = select_db()
```

#### 1. 增加

```python
# 1. 创建一个学校、查询其id，利用id再去创建学生添加 sch_id
# 2. relastionship 正向添加，字段出现在哪个类
from xxx import Student, School
stu = Student(name='iris', stu2sch=School(name='BeiJing'))
db_session.add(stu)
db_session.commit()
db_seesion.close()
# 3. relastionship 反向添加
sch = School(name='ShangHai')
sch.sch2stu = [Student(name='iris'),
               Student(name='oleg'),
              ]
db_session.commit()
db_seesion.close()
```

#### 2. 删除

-   当前学校被引用的时候不可以删除

#### 3. 查询

```python
# 正向查询
res = db_session.query(Student).all()
print([stu.name, stu.stu2sch.name for stu in res])
# 反向查询
res = db_session.query(School).all()
print([sch.name, len(sch.sch2stu) for sch in res])
print([sch.name, *[stu.name for stu in sch.sch2stu] for sch in res])
```

## 4. ManyToMany

### 1. 创建表

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.orm imoprt relationship
# 几乎支持所有的关系型数据库
engine=create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy?chrset=utf8')
BaseModel = declarative_base()
```

-   多对多表

```python
class Girl(BaseModel):
    __tablename__ = 'girl'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    # 注意secondary是表层面的
    gyb = relationship('Boy', backref='byg', secondary='hotel')

class Boy(BaseModel):
    __tablename__ = 'boy'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

class Hotel(BaseModel):
    __tablename__ = 'hotel'
    id = Column(Integer, primary_key=True)
    bid = Column(Integer, ForeignKey('boy.id'))
    gid = Column(Integer, ForeignKey('girl.id')) 

BaseModel.metadata.create_all(engine)
```

### 2. 操作

-   第三张表的数据是自动添加的

```python
from sqlalchemy.orm import sessionmaker
from xxx import engine, Girl, Boy
select_db = sessionmaker(engine)
db_session = select_db()
```

#### 1. 增加

```python
# 使用relationship正向增加
g = Girl(name='echo', gyb=[Boy(name='ehco1'),Boy(name='echo2')])
db_session.add(g)
db_session.commit()
db_sesion.close()

# 反向添加
b = Boy(name='dean')
b.byg = [Girl(name='dean1'),
         Girl(name='dean2')
        ]
db_sesion.add(b)
db_session.commit()
db_sesion.close()
```

#### 2. 查询

```python
# 正向查询
res = db_session.query(Girl).all()
for g in res:
    print(g.name, len(g.gyb))
    
# 反向查询
res = db_session.query(Boy).all()
for b in res:
    print(b.name, len(b.byg))
```

# Flask-SQLAlchemy

## 1. 安装

```python
pip install flask-sqlalchemy
```

## 2. flask项目结构

### 1. app01包

-   templates：文件夹
-   static：文件夹
-   `__init__.py`

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# 创建 db 时，注意导入蓝图的顺序
from views import user

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy?charset=utf8'
    # 一般小于50，默认不开启
    app.config['SQLALCHEMY_POOL_SIZE'] = 5
    # 默认是 15s
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 15
    # 每个链接重复使用次数，一般不写
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 10
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.register_blueprint(user.users)
    # 读取 config 文件
    db.init_app(app=app)
    return app
```

-   models.py

```python
# db是 sqlalchemy 对象
from app01 import db

# db.Model 就是 BaseModel，使用的是sqlalchemy
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

if __name__ == '__main__':
    from app01 import create_app
    app = create_app()
    db.drop_all(app=app)
    db.create_all(app=app)
```

-   views：存放蓝图文件夹
    -   user.py

```python
from flask import Buleprint
from app01.models import db, Users
user = Blueprint('user', __name__)

@user.route('/reg/<username>')
def reg(username):
    u = Users(name=username)
    db.session.add(u)
    db.sessoin.commit()
    return 'reg 200 OK!'  

@user.route('/user_list')
def user_list():
    res = Users.query.filter('条件').all()
    print(res)
    return f'当前有{len(res)}个用户。'
```

### 2. manager.py

```python
from app01 import create_app
from flask_script import Manager
app = create_app()
if __name__ == '__main__':
    app.run()
```

## 3. 终端启动

### 1. 下载

```python
pip install flask-script
```

### 2. 使用

-   manager.py

```python
from app01 import create_app
from flask_script import Manager
app = create_app()
manager = Manager(app)
"""
# 进阶
@manager.command
def func1(args):
    print(args)
   	return args
   	
@manager.option('-w', '--who', dest='who')
@manager.option('-a', '--age', dest='age')
def func(who, age):
    print(who, age)
   	return who, age
"""

if __name__ == '__main__':
    manager.run()
```

-   终端命令

```python
# 此时注意当前的 python 解释器
python manager.py runserver -h 0.0.0.0 -p 9527
```

-   **指令集**

```python
# func1 函数传参
python manager.py func1 haha
# 多重传参
python manager.py -w henry
python manager.py -w henry -s echo
```

### 3. flask-migrate

-   **如果使用，必须安装flask-script**

```python
from app01 import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
app = create_app()
Migrate(app, db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
```

-   终端使用

```python
# 初始化数据库
python manager.py db init
# 相当于Django的makemigrations
python manager.py db migrate
# 相当于Django的migrate
python manager.py db upgrade
```