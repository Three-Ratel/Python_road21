# 字符格式化的意义：
# name = input('Name: ')
# do = input('what: ')
# template = '%s在教室，%s。' % (name, do,)
# print(template)


# %s 作为占位符（string）
# %d int

# template = '我是%s,年龄%s，职业%s。' % ('henry', 25, 'study',)
# print (template)


# name = 'henry'
# template = '%s现在手机的电量是100%%' % (name,)
# print(template)

# name = input('Name: ')
# do = input('what: ')
# template = '%s在教室，%s。' % (name, do,)
# print(template)


# name = input('Name: ')
# age = int(input('age: '))
# template = 'name:%s ''\n''age:%d ' % (name, age,)
# print(template)


# battery = input('please input how much battery do you have: ')
# name = input('please input your name:')
# s = '%s电量还有%s%%'
# s = s % (name, battery,)
# print(s)

name = input("Enter your name: ")
age = input('Enter your age: ')
job = input('Enter your job: ')
hobby = input('enter your hobby: ')
msg = '''
------------info of henry------------
Name: %s
Age: %s
Job: %s
Hobby: %s
----------------end------------------
'''
msg = msg % (name, age, job, hobby)
print(msg)
