# 修改值
info = {'name': 'henry', 'age': 18, 'gender': 'male'}
age = info['age'] = 19
print(info)


# 改key
# 删除后在增加
del info['name']
info['new_name'] = 'echo'   # 没有key值默认添加
print(info)

# key值对是整体
info = {'name': 'henry', 'age': 18, 'gender': 'male'}
del info['name']
print(info)

# 删除是对key值对整体的删除


