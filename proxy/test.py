#!/usr/bin/python
# -*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import bs4
import requests

with open('data.txt','r') as f:
    ip = json.load(f)

url = "http://dev.www.xueguoxue.com"
header = {}
data = {}

print 'shell start ....'
for i in range(1,905):
    while True:
        i = str(i)
        proxie = {'http': ip[i][3][0] +'://' + ip[i][0][0] + ":" + ip[i][1][0]}
        city = ip[i][2][0]
#        print proxie
        try:
            r = requests.get(url, proxies=proxie, timeout=5)
        except:
            print "tiaoguo"
            break
#        print "**********************************************************"
        if r.status_code == 200:
            tt = bs4.BeautifulSoup(r.content)
            try: 
                print tt.title.string
            except:
                break
            if tt.title.string == "学国学网 | 专注优秀传统文化教育":
                ip_c = []
                ip_c.append(proxie)
                ip_c.append(city)
                data[i] = ip_c
                print data[i]
with open('keyong.txt','a') as ff:
    json.dump(data,ff)
print ">>>>> shell stop"
