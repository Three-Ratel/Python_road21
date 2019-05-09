#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import time
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
while True:
    sk.send(b'hhhhhhhhhh')
    msg = sk.recv(1024)
    print(msg)
    time.sleep(0.2)

sk.close()





