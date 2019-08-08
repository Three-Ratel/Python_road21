info = {'1': 5, '2': 2, '3': 10}
# new_info = sorted(info, key=info.values(), )
# print(info.items())
li = sorted(info.items(), key=lambda e: e[1], reverse=True)
print(li)