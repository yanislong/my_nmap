#!/usr/bin/python
# -*- coding=utf-8 -*-

import time
import sys
import requests, bs4, re

def access_pro():
    url = "http://www.xicidaili.com/nn/1"
    header = {}
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    header['Referer'] = ""
    r = requests.get(url, headers=header)
    html = bs4.BeautifulSoup(r.content)
    tt = html.find('table').find_all('tr')
    n = 0
    ll = []
    for i in tt:
        for j in i.contents:
            if type(j) != bs4.element.NavigableString:
#                print j.string
                ll.append(j.string)
        print '*****************'
        n += 1
#    print ll
    for l in range(11,10000,10):
        try:
            print ll[l]
            print ll[l+1]
            print ll[l+4]
        except:
            print "quit"
            sys.exit()
#    for k in ll:
#        print k

access_pro()
