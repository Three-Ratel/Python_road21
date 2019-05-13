#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
from socketserver import *
PRO_DIE = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PRO_DIE)
from config import settings
from bin.server import Myserver


def run():
    TCPServer.allow_reuse_address = True
    server = ThreadingTCPServer(settings.IP_PORT, Myserver)
    server.serve_forever()


run()
