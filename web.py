#!/usr/bin/python
# -*-coding=utf-8 -*-

import sys
import socket

host = "www.xueguoxue.com"
#host = '172.16.20.93'
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(b'GET /chineseCourse1 HTTP/1.1\r\nhost: ' + host +'\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
       break

data = b''.join(buffer)
try:
    header, html = data.split(b'\r\n\r\n',1)
except ValueError:
    print "geshi worry"
    sys.exit()
print header.encode('utf-8')
with open('/root/Desktop/index.html','wb') as f:
    f.write(html)
