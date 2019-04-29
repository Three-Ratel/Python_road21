## 今日内容

- 模块
- 内置模块
  - time
  - datetime
  - json
  - 其他

## 补充

- 如果有if …else 判断，简单业务先处理
- 减少代码层级
- 构造字典和函数对应关系
- 终止程序：import sys      sys.exit(0)
- xrang / range
- 在遍历某个变量时，不可修改

py2: 

- range：在内存中，立即生成数据
- xrange：对xrange进行循环的时候产生数据

py3: 

- range是py2的xrange
- list(range(10))



# 模块

## 1. 模块的基本知识

1. **分类**：

   - **内置模块**（py内部提供的功能）

   - **第三方模块**

   ```python
   # pip 安装模块
   pip install moudle_name
   # 安装成功，如果导入不成功，需要重启pycharm 
   ```

   - **自定义模块**

   ```python
   # a.py
   def f1():
     pass
   def f2():
     pass 
   ```

   ```python
   # 调用自定义模块中的功能
   import a
   a.f1()
   ```

2. **内置模块**

   1. os

      - os.mkdir：创建文件夹(一级目录)
      - os.makedirs：递归创建文件夹
      - os.rename(a, b)：文件和文件夹

   2. sys

      - sys.path（是个list）
      - paython解释器会按sys.pathon的路径查找

      ```python
      # sys包含python 和 工作目录
      # pycharm也会自动添加工作目录和pycharm的目录
      # python导入模块时默认查找路径
      # 只能导入目录下的第一层文件
      
      sys.path.append('moudle_path')
      ```

   3. **json**(**重点**)

      - 特殊的字符串（list和dict嵌套的string）
      - 不同语言间的数据交互
      - 序列化/反序列化：把其语言的数据转化成**json**格式/ 相反
      - **格式**

      ```python
      # 只能包含，int，str，list，dict，bool
      # 最外层必须是list/dict
      # json 中如果包含str，必须是 双引号
      ```

      ```python
      import json
      v = [12, 3, 4, {'k1': 1}, True, 'adsf']
      # 序列化
      v = json.dumps(v)
      # 反序列化
      json.loads(v)
      ```

      

      

