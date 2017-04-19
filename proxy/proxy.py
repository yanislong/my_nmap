#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests, bs4, re

def access_pro():
    url = "http://www.xicidaili.com/nn/1"
    header = {}
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    header['Referer'] = ""
    r = requests.get(url, headers=header)
    html = bs4.BeautifulSoup(r.content)
    tt = html.find('table').findall('tr')
    print tt
    for i in tt:
        print i.td.next_elements
        print '\n'
        n += 1
    print n

access_pro()
