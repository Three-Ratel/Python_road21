# 练习5
# 创建一个用户列表，让用户输入，用户名和密码进行登录
# user_list = [{'user':'用户输入'}
# {'user':'用户输入'}
# {'user':'用户输入'}
# ...
# ]
#

# # 方法一
# user_list = []
#
# while True:
#     u = input('请录入用户名：')
#     if u == 'n':
#         break
#     v = input('请录入密码：')
#     info = {}
#     info['user'] = u
#     info['password'] = v
#     user_list.append(info)
# print(user_list)
# name = input('用户名：')
# pwd = input('密码：')
# for i in range(len(user_list)):
#     if name in user_list[i]['user'] and pwd == user_list[i]['password']:
#         print('登陆成功')
#         break
#     if i == len(user_list) - 1:
#         print('登陆失败')
#         break

# 方法二
# print("方法二")
# user_list = [{'user': 'q', 'password': '1'},
#  {'user': 'w', 'password': '2'},
#  {'user': 'e', 'password': '3'},
#  {'user': 'r', 'password': '4'}]
#
# username = input('please input your name: ')
# pwd = input('please input your pwd: ')
# message = '登陆失败'
# for items in user_list:
#     if items['user'] == username and items['password'] == pwd:
#         message = '登陆成功'
#         break
# print(message)


# 方法三
user_list = [{'user': 'q', 'password': '1'},
 {'user': 'w', 'password': '2'},
 {'user': 'e', 'password': '3'},
 {'user': 'r', 'password': '4'}]
user = input('请输入用户名：')
pwd = input('请输入密码：')

for y in user_list:
    li = []
    for value in y.values():
        li.append(value)
    if li[0] == user and li[1] == pwd:
        print('登陆成功')
