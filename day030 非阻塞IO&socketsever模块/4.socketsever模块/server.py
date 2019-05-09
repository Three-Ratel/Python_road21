#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver


class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        print(self.request)


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)
server.serve_forever()


