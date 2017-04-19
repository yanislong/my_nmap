#!/usr/bin/python
# -*- coding=utf-8 -*-

import json
import requests

with open('data.txt1','r') as f:
    ip = json.load(f)

url = "http://dev.www.xueguoxue.com"
header = {}
for i in range(3):
    i = str(i)
    print ip[i][0]
    print ip[i][1]
    proxie = {'http':'http://' + ip[i][0] + ":" + ip[i][1]}
    print proxie
    try:
        r = requests.get(url, proxies=proxie, timeout=10)
        print r.content
    except:
        print "tiaoguo"
