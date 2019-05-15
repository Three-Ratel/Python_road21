# from socket import socket
# sk = socket()
# sk.connect(('127.0.0.1', 9000))
# while True:
#     sk.send('hello'.encode('utf-8'))
#     msg = sk.recv(1024).decode('utf-8')
#     print('11111', msg)
#
# sk.close()





from socket import socket
sk = socket()
sk.connect(('127.0.0.1', 9000))
while True:
    msg = sk.recv(1024).decode('utf-8')
    print('11111', msg)
    sk.send('hello'.encode('utf-8'))


sk.close()