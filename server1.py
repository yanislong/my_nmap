#!/usr/bin/python
# -*- coding=utf-8 -*-

import socket
import threading, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',12345))
s.listen(2)
print "Waiting connection ..."

def tcplink(sock,addr):
    print "host %s connect success" % addr[0]
    sock.send('please select server number:\n1)open user.txt\n2)read phone')
    data = sock.recv(1024)
    while True:
        if data == "1":
            with open('/etc/passwd','r') as f:
                sock.send(f.read())
            f.close()
        elif data == "2":
            with open('/root/phone.txt','r') as f1:
                sock.send(f1.read())
            f1.close()
        else:
            print "play else"
            sock.close()
            break
        data = ""

while True:
    try:
        sock,addr = s.accept()
        t = threading.Thread(target=tcplink,args=(sock,addr))
        t.start()
    except KeyboardInterrupt:
        print "exit"
        sys.exit()
