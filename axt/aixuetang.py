#!/usr/bin/python
# -*- coding=utf-8 -*-

import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import chardet
import re
import requests
import bs4
import json

class pachong():
    """pa le aixuetang course"""
    pass

def aixuetang(page=1):
    header = {}
    u = "http://www.aixuetang.com"
    url = "http://www.aixuetang.com/zxxtCourseModule/searchCourseByModel?gradeId=&subjectId=&versionId=&pageNo=" + str(page) + "&sort_name=&card_discount=&startDate=&endDate=&is_live=&courseFlag=true&coursename=\u000"
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    r = requests.get(url, headers=header)
#    print r.content
    html = bs4.BeautifulSoup(r.content)
    tt = html.find_all(class_='courses_content')
    n = 0
    conn = MySQLdb.connect(host='172.16.20.123',port=3306, user='long', passwd='123', db='axt', charset='utf8')
    for i in tt:
        for j in i.contents:
            if hasattr(j, 'dl'):
                n += 1
                try:
#                    print j.h1.string
#                    print j.img['src']
#                    print j.p.string[1:]
#                    print j.span
                    l1 = re.findall(r'>(\d{1,10})',str(j.span))
#                    print l1[0]
                    print ">>>>>>>>>>>>>",n
                    t,p,m = (j.h1.string,j.p.string[1:],l1[0])
                    murl = u + j.img['src']
#                    r2 = requests.get(u+j.img['src'],headers=header)
#                    with open('./abc.jpg','wb+') as f:
#                        f.write(r2.content)
#                        f.seek(0)
#                        ff = f.read()
#                    print 't',type(t),'p',type(p),'m',type(m),'r2.content',type(r2.content)
#                    sys.exit()
                    cur = conn.cursor()
                    mysql = 'insert into aixuet(pid, title, money, people, img) values(%s,%s,%s,%s,%s)'
                    cur.execute(mysql,(n,t,p,m,murl))
                    cur.close()
                    conn.commit()
#                    sys.exit()
                except AttributeError:
                    print 'not hav attri'
    conn.close()    

def a_xgx():
    conn = MySQLdb.connect(host='172.16.20.123',user='long',passwd='123',port=3306,db='axt', charset='utf8')
    cur = conn.cursor()
    mysql = "select img from aixuet"
    cur.execute(mysql)
    ddd = cur.fetchone()
    with open('./test1.jpg','wb') as ff:
        ff.write(ddd[0])
    ff.close()
    cur.close()
    conn.close()

for i in range(29):
    aixuetang()
#a_xgx()
