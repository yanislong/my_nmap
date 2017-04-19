#!/usr/bin/python
# -*- coding=utf-8 -*-

import json
import time
import sys
import requests, bs4, re

def access_pro(num=1):
    url = "http://www.xicidaili.com/nn/" + str(num)
    ll = []
    data = {}
    header = {}
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    header['Referer'] = ""
    r = requests.get(url, headers=header)
    html = bs4.BeautifulSoup(r.content)
    tt = html.find('table').find_all('tr')
    for i in tt:
        for j in i.contents:
            if type(j) != bs4.element.NavigableString:
                ll.append(j.string)
    for l in range(11,1000,10):
        try:
            ip = []
#            print ll[l]
#            print ll[l+1]
#            print ll[l+4]
            ip.append(ll[l])
            ip.append(ll[l+1])
            ip.append(ll[l+4])
            for i in range(400):
                data[i] = ip
        except:
            print "quit"
#            sys.exit()
        finally:
            with open('data.txt' + str(num),'w') as ff:
                json.dump(data,ff)

for i in range(1,10):
    print i
    access_pro(i)
