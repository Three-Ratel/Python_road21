## 今日内容

1. 抽象类/接口类

2. _\_new__：创建实例的，指针

   - 对象：指针、空间，在_\_init__之前

3. logging模块：

   - 记录日志
     - 用户：eg.银行流水
     - 程序员：统计、故障排除的 debug、错误完成代码优化
   - basicConfig：使用方便，不能实现中文编码，不同同时向文件和屏幕上输出
   - logger对像
     - 复杂：创建一个logger对象、文件操作符、屏幕操作符、格式
     - 给logger绑定文件操作和屏幕操作
     - 给屏幕操作符和文件操作符设置格式
     - 用logger对象操作

   ```python
   # warning和error写入不同文件，需要创建不同对象
   import logging
   # 需要加入name参数
   logger = logging.getLogger() 
   fh = logging.FileHandler('log.log') # 写入文件
   sh = logging.StreamHander()  # 不需要参数，输出到屏幕
   logger.addHander(fh)
   logger.addHander(sh)
   fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s'
   
   logger.waring('message')
   ```

4. collections模块
   - OrderedDict()

```python
# dict创建过程
d = dict([('a', 1), ('b', 2), ('c', 3)])

from collections import OrderedDict
odict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

- defaultDict
- deque
- namedtuple

```python
from collections import namedtuple
# 可命名tuple（time 结构化时间）
# 创建了一个Course类，这个类没有方法，所有属性值不能修改
Course = namedtuple('Course', ['name',  'price', 'teacher'])
python = Course('python', 999, 'alex')

print(python)
print(python.name)
print(python.price)
```

5. 模块和包

   1. 什么是模块

      - py文件，写好了的对程序员直接提供某方面功能
      - import / from xxx import xx
      - 包：存储了多个py文件的文件夹，pickle，json，urlib
      - 如果导入一个包，包里默认模块是不能使用的
      - 导入一个包相当于执行_\_init__.py文件内容

      ```python
      # 在__init__.py中使用
      from pack import policy
      ```

   2. 项目开发规范

      1. bin：start
      2. config：配置文件settings
      3. src：业务逻辑
      4. db：数据文件
      5. lib：扩展模块
      6. log：日志文件

6. Stack: lifo / Queue：fifo

7. 反射

   1. **hasattr**
   2. **getattr**

   ```python
   # 反射当前文件内容
   getattr(sys.modules[__name__], 'ab')
   # 通过对象获取、示例变量、绑定方法
   # 通过类来获取类变量、类方法、静态方法
   # 通过模块名获取模块中的任意变量(普通变量、函数、类)
   # 通过本文件反射任意变量
   ```

   3. setattr
   4. delattr

8. Foo抽象类/接口类

   1. 给子类一个规范，让子类必须按照抽象类实现方法

   ```python
   class Foo:
     def func(self):
       pass
     
   class Son(Foo):
     pass
   
   s = Son()
   s.func()
   ```

9. 模块

   1. os和操作系统打交道：文件(夹)、路径

      1. os.path.isdir()
      2. os.path.isfile()

   2. sys：

      1. sys.path：模块导入路径
      2. sys.argv：获取命令行参数
      3. sys.modules：存储当前程序中用到的所有模块

   3. datetime：

      1. now()：datetime对象
      2. utc()
      3. strftime
      4. strptime
      5. timestamp()：datetime转时间戳
      6. fromtimestamp()：时间戳转datetime

   4. time：

      1. time.time()
      2. time.sleep()

   5. hashlib：摘要算法模块，密文验证/校验文件独立性

      1. md5 / sha
      2. 摘要文件内容一样，无论怎么分割，md5摘要后一致（大文件一致性校验）

   6. json/pickle：

      **序列化**：把其他数据类型转换为str数据类型/bytes类

      1. json：
         - 所有字符串都是双引号
         - 最外层只能是list/dict
         - 支持int，float，str， list， dict，bool，dict中key只能是str
         - 不能连续load多次
      2. pickle
         1. 几乎所有类型数据类型都可以写到文件中
         2. 支持连续load多次

   7. random

      1. random.choice([1, 2, 3])：随机选择一个：验证码，抽奖
      2. random.sample([1, 2, 3, 4, 5], 3)：随机选3个不重复，抽奖多个人
      3. random.uniform(1, 5)：随机1-5中的随机小数
      4. random.shuffle：洗牌，算法

   8. logging

   9. **collections**：python核心模块

      1. OrderedDict
      2. namedtuple
      3. deque：双端队列
      4. defaltDict：默认dict，可以给dict的value设置一个默认值

   10. shutil

       1. shutil.make_archive()
       2. shutil.unpack_archive()
       3. shutil.rmtree()
       4. shutil.move()

   11. getpass

       1. getpass.getpass()

   12. importlib

       1. 使用str导入模块
       2. _\_import__(和importlib.import_module('模块名'))

       os = _\_import__('os')

   13. functools

       1. reduce

   ## OOP

   1. 基础概念

      1. 类：具有相同方法和属性的一类事物
      2. 什么是对象、实例：一个拥有具体属性值和动作的具体个体
      3. 实例化：从一个类得到一个具体对象的过程

   2. 组合

      1. 一个类的对像作为另一类对象的实例变量
      2. Foo().name

   3. 三大特性

      1. 继承:所有的查找名字(调用方法和属性)。如果自己和父类都有，希望自己和父类都调用，super()/指定类名直接调

         1. 父类、基类、超类
         2. 派生类、子类
         3. 多继承、单继承
         4. 查找顺序
         5. 多态：一个类变现出来的多种状态—>多个类表现出相似的状态
         6. 鸭子类型：list，tuple，python的多态是通过鸭子类型实现的

      2. 封装

         1. 广义封装：类中成员

         2. 狭义封装：私有成员

            1. 只能在类的内部使用，类的外部不能调用，也不能在子类中使用
            2. _类名__名字：命名

            ![私有方法的访问](/Users/henry/Documents/截图/Py截图/私有方法的访问.png)

   4. 类成员

      1. _\_call__：源码中
      2. _\_enter__ with
      3. _\_dict__

   5. 特殊方法/魔术方法/内置方法/双下方法

   6. 相关内置函数

      1. isinstance
      2. issubclass
      3. type
      4. super（新式类支持，遵循mro顺序）

   7. 新式类和经典类

      1. 新式类：继承object，super，多继承（广度优先c3），具有mro方法
      2. 经典类：py2不继承object，无super/mro ， 深度优先