#!/usr/bin/python
# -*- coding=utf-8 -*-

import socket
import MySQLdb
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
    for ii in range(1,num):
        url = "http://www.xicidaili.com/nn/" + str(ii)
        data = {}
        header = {}
        header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36cuimingwen"
        header['Referer'] = ""
        r = requests.get(url, headers=header, timeout=10)
        time.sleep(10)
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

    conn = MySQLdb.connect(host="172.16.20.123",port=3306,user='long',passwd='123',db="axt",charset="utf8")
    n = 0

    for l in range(24,len(ll),21):
        try:
            proxie = {ll[l+8][0].lower():ll[l+8][0].lower() + "://" + ll[l][0] + ":" + ll[l+2][0]}
            rrr = requests.get('https://www.baidu.com', headers=header, proxies=proxie, timeout=5)
            html = bs4.BeautifulSoup(rrr.content)
            if str(html.title.string) == "百度一下，你就知道":
                rrrr = requests.get('http://dev.www.xueguoxue.com', headers=header, proxies=proxie, timeout=5)
#                print rrrr.headers
                cur = conn.cursor()
#                print proxie
                print ll[l][0]
                print ll[l+2][0]
                print ll[l+4][0]
                print ll[l+8][0]
                print ll[l+16][0]
                sql = 'insert into proxy(pid,ip,port,protocol,area,uptime) value(%s,%s,%s,%s,%s,%s)'
                cur.execute(sql,(n,ll[l][0],ll[l+2][0],ll[l+8][0],ll[l+4][0],ll[l+16][0]))
                cur.close()
                conn.commit()
#                sys.exit()
        except KeyboardInterrupt:
            print "quit"
        except requests.exceptions.ReadTimeout:
            print 'Readtime out'
        except requests.exceptions.ConnectionError:
            print 'connectionErrof'
        except socket.error:
            print 'connection reset'
        finally:
            n += 1
            print "myql running " ,n
    conn.close()

for i in range(5):
    access_pro(i)
