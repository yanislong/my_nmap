#!/usr/bin/python
# -*- coding=utf-8 -*-

import sys
import socket
import time
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9999))
s.listen(5)
print "Waiting for connection..."

def tcplink(sock,add):
    print "Accept new connection for %s:%s..." %add
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == "exit":
            break
        sock.send('Hello, %s!'% data.decode('utf-8'))
    sock.close()
    print "conncetion from %s:%d close" % add

while True:
    try:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock,addr))
        t.start()
    except KeyboardInterrupt:
        print "eixit"
        sys.exit()
