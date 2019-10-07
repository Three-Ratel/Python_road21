import select
import socket

s1 = socket.socket()
s1.bind(('127.0.0.1', 8001))
s1.listen(5)

s2 = socket.socket()
s2.bind(('127.0.0.1', 8002))
s2.listen(5)

while True:
    rlist, wlist, elist = select.select([s1, s2], [], [], 0.05)
    print(rlist, wlist, elist)
    for s in rlist:
        conn, addr = s.accept()
        # print(conn.recv(1024))
