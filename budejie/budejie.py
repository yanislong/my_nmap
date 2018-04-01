#!/usr/bin/python
# -*- utf-8 -*-

import time
import requests 
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
import pickle
import urllib
import bs4

n = 0
title = []
def result(num):
    global n
    global title
    url = "http://www.qiushibaike.com/pic/" + str(num)
    header = {}
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    r = requests.get(url ,headers=header)
    html = bs4.BeautifulSoup(r.content)
    tt = html.find_all(class_='article block untagged mb15')
    for i in tt:
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        p = i.img
#        print p['src']
#        print type(p)
        n += 1
        try:
            r1 = requests.get('http:' + p['src'],timeout=10).content
        except equests.exceptions.ConnectionError:
            print 'Connection aborted. gaierror(-2, Name or service not known)'
        with open('/root/Desktop/tu5/' + str(n) + ".jpg", 'wb') as f:
            f.write(r1) 
            f.close()
#	urllib.urlretrieve(p['src'],'/root/Desktop/tu5/'+ str(n)+ ".jpg")
#        title.append(i['alt'])

if __name__ == "__main__":
    for i in range(6,9):
        result(i)
#    with open('/root/title.txt','a') as f:
#        pickle.dump(title, f)
