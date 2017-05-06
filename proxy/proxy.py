#!/usr/bin/python
# -*- coding=utf-8 -*-

import json
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests, bs4, re

def access_pro(num=1):
    ll = []
    n = 0
#    proxie = {'http':'http://61.186.164.98:8080'}
    for ii in range(1,2):
        url = "http://www.xicidaili.com/nn/" + str(ii)
        data = {}
        header = {}
        header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36cuimingwen"
        header['Referer'] = ""
        r = requests.get(url, headers=header, timeout=10)
        html = bs4.BeautifulSoup(r.content)
        tt = html.find('table').find_all('tr')
        for i in tt:
            for j in i.contents:
                jia = []
                if type(j) == bs4.element.NavigableString:
                    pass
#                    print "NavigableString..."
                elif type(j) == bs4.element.Tag:
#                    print j.string
                    if j.string:
                        jia.append(j.string)
                    for y in j.contents:
                        if y.name == 'a':
                            jia.append(y.string)
#                    print '>>>>>>>>>>>>>>' +str(jia)+'<<<<<<<<<<<<<<'
                ll.append(jia)

    for i in range(0):
        if ll[i]:
            print ll[i][0],i

    for l in range(24,len(ll),21):
        try:
            proxie = {ll[l+8][0].lower():ll[l+8][0].lower() + "://" + ll[l][0] + ":" + ll[l+2][0]}
            rrr = requests.get('https://www.baidu.com', headers=header, proxies=proxie, timeout=5)
            html = bs4.BeautifulSoup(rrr.content)
            if str(html.title.string) == "百度一下，你就知道":
                rrrr = requests.get('http://dev.www.xueguoxue.com', headers=header, proxies=proxie, timeout=5)
                print rrrr.headers
            print proxie
            print ll[l]
            print ll[l+2]
            print ll[l+4][0]
            print ll[l+8]
        except KeyboardInterrupt:
            print "quit"
#            sys.exit()
        except requests.exceptions.ReadTimeout:
            print 'Readtime out'
        except requests.exceptions.ConnectionError:
            print 'connectionErrof'
        except socket.error:
            print 'connection reset'
        finally:
            with open('data.txt','w') as ff:
                json.dump(data,ff)

for i in range(1):
    access_pro(i)
