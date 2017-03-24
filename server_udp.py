#!/usr/bin/python
# -*- coding=utf-8 -*-

import socket

host = "0.0.0.0"
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

data,addr = s.recvfrom(1024)
print data
s.sendto('im root..',addr)
