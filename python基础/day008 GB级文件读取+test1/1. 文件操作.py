
#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
 mode = 'rb'
"""
f = open('a.txt', mode='rb')
data = f.read()
f.close()
print(data)

# 二进制读取，并采用指定编码进行解码
f = open('a.txt', mode='rb')
data = f.read()
data = data.decode('utf-8')
f.close()
print(data)

"""
 mode = 'wb'
"""
f = open('a.txt', mode='wb')
s = '你好吗'
s1 = s.encode('utf-8')
f.write(s1)
f.close()


"""
 mode = 'ab'
"""
f = open('a.txt', mode='ab')
s = '你好吗'
s1 = s.encode('utf-8')
f.write(s1)
f.close()




