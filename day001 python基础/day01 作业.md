# s21day01作业

1. 操作系统的作用?

   - OS主要是为各个应用服务协调分配硬件资源（CPU、RAM、HDD/SSD资源），从而使各个应用可以有效使用资源

     

2. 列举你听过的操作系统及区别？

   1. windows： win98，vista，7，8，10（前面全是个人桌面系统，用于办公）；Windows server（用于服务器）

   2. Linux：centos（开源，多用于服务器），Ubuntu（GUI相对友好）, RedHat（企业级收费，用于服务器）

   3. macOS —>办公，coding

      

3. 列举你了解的编码及他们之间的区别？

   1. ASCII：1byte，包含英文字母、数字、常用符号

   2. Unicode：

      - 4bytes，万国码
      - 用于统一全球语言，普及计算机
      - 浪费存储资源

   3. UTF-8：

      - 解决unicode耗费存储空间的问题
      - 可变长unicode：英文（8bits），欧洲文字（16bits），中文（24bits）

   4. GBK （为亚洲语言设计）

      

4. 列举你了解的Python2和Python3的区别？

   1. py2的解释器默认使用ASCII编解码，py3默认使用utf-8

   2. 输入输出格式不同

      - py2输出使用print 内容，py3输出使用print(输出内容)

      - py2输入使用name = raw_input('提示语')，py3使用name = input('提示语')

      

5. 你了解的python都有那些数据类型？

   1. str：字符串

   2. int：整型

   3. bool：布尔型

      

6. 补充代码，实现以下功能。

   ```
   value =  _____ 
   print(value)  # 要求输出  alex"烧饼
   ```

   ```
   value = 'alex"烧饼'
   print(value)  # 要求输出  alex"烧饼
   ```

   

7. 用print打印出下面内容：

   ```
   ⽂能提笔安天下,
   武能上⻢定乾坤.
   ⼼存谋略何⼈胜,
   古今英雄唯是君。
   ```

   ```python
   poem = '''⽂能提笔安天下,
   武能上⻢定乾坤.
   ⼼存谋略何⼈胜,
   古今英雄唯是君。'''
   print(poem)
   ```

   

8. 变量名的命名规范和建议？

   1. 只能由数字、字母和下划线组成
   2. 不能以数字打头
   3. 不能是python的关键字
      - 见名知意
      - 推荐使用_分割英文单词（python中较为常见）
      - 使用单词首字母大写（驼峰式）

   

9. 如下那个变量名是正确的？

   ```python
   name = '武沛齐'
   _ = 'alex'
   _9 = "老男孩"
   9name = "景女神"		#错误，不能以数字打头
   oldboy(edu = 666	#错误，不能包含(
   ```

10. 简述你了解if条件语句的基本结构。

   ```python
   #第一种，简单判断
   if 条件判断：
      	代码块
   #第二中，双重判断
   if 条件判断1:
      	代码块1
   else：
      	代码块2
   #第3中，多重判断
   if 条件判断1:
      	代码块1
   elif 条件判断2:
     	代码块2
   .
   .
   .
   else：
      	代码块n
      
   ```

   

11. 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。

    ```python
    num = 66
    user_num = int(input('please input a num: '))
    if user_num > 66:
      print('your number is bigger than the num')
    elif user_num < 66:
      print('your number is smaller than the num')
    else:
      print('your are right')
    ```

    

12. 提⽰⽤户输入⿇花藤. 判断⽤户输入的对不对。如果对, 提⽰真聪明, 如果不对, 提⽰你 是傻逼么。

```python
name = input('please input your name')
if name == '麻花藤'：
	print('you are so smart')
else:
  print('you are so stupid')
```

