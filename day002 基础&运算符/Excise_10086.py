message = '''
1.话费查询
2.流量服务
3.业务办理
4.人工服务
5.其他：输入错误
'''
print(message)

index = int(input('please input a service: '))
# index = int(index)
if index == 1:
    print('话费查询')
elif index == 2:
    print('流量服务')
elif index == 3:
    content = '''业务办理
    1.修改密码
    2.更改套餐
    3.停机；
  '''
    print(content)
    value = int(input('请输入办理的业务'))
    if value == 1:
        print('修改密码')
    elif value == 2:
        print('更改套餐')
    else:
        print('停机')

elif index == 4:
    print('人工服务')
else:
    print('输入错误')
