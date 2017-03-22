#!/usr/bin/python
# -*- coding=utf-8 -*-

import hashlib
import json

def register(name,passwd):
    s = hashlib.md5(name + passwd + "123".encode('utf-8'))
    m = s.hexdigest()
    up = {"name":name,'passwd':m}
    ups = json.dumps(up)
    with open(r'c:\users\huang\Desktop\userp.txt','a') as f:
        f.write(ups + "\n")
    f.close()

def login(name,passwd):
    with open(r'c:\users\huang\Desktop\userp.txt','r') as f:
        for i in f.readlines():
            s = json.loads(i)
            if i == "":
                break
            elif s['name'] == name and s['passwd'] == passwd:
                print "login ok"
                print u"************机密文件*************"
                print i
                print "*********************************"
                break
            else:
                print "worry about"
    f.close()

while True:
    print "0)exit\n1)register new user\n2)login\n"
    s = str(raw_input('please select opetion number:\n'))
    if s == "1":
        n = raw_input("please input new username:\t")
        p = raw_input("please input" + n + " password:\t")
        register(n,p)
        print "register is succssful"
    elif s == "2":
        x = raw_input('please input login name:\t')
        y = raw_input('please input login password:\t')
        m = hashlib.md5( x + y + "123".encode('utf-8'))
        y = m.hexdigest()
        login(x,y)
    elif s == "0":
        print "bye"
        break
    else:
        continue
        
        
        

