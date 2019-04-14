message = 'k1|v1,k2|v2,k3| 123 '
# info = {'k1':'v1', 'k2':'v2', 'k3':'123'}
new_m = message.split(',')
info = {}
for item in new_m:
    u, v = item.split('|')
    info[u] = v
print(info)

mag = message.split(',')
info = {}
for i in range(len(mag)):
    mag2 = mag[i].split('|')
    mag2[0] = mag2[0].strip()  # 去除空格
    mag2[1] = mag2[1].strip()
    info[mag2[0]] = mag2[1]
print(info)


# 变量的命名需要加强
