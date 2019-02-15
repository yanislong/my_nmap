#!/usr/bin/python
# -*-coding=utf-8 -*-

import sys
#reload(sys)
#sys.setdefaultencoding('gb2312')
import pymysql
import time

import requests
from bs4 import BeautifulSoup

def a():
    global con
    global cur
    url = "https://www.qumaishu.com/zhangxiaoxian/73564.html"
    header = {}
    header['Cookie'] = "Hm_lpvt_83c5bfe4d0b8be1afcf05ddf0efddbe2=1538279328; Hm_lvt_83c5bfe4d0b8be1afcf05ddf0efddbe2=1538278621,1538278674,1538278715,1538279328"
    r = requests.get(url, headers=header)
    s = r.text.encode(r.encoding).decode('gb2312',errors="ignore")
#    s = r.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(r.text)[0],errors='ignore')
#    print s
#    print requests.utils.get_encodings_from_content(r.text)
    html = BeautifulSoup(s,fromEncoding="utf-8")
#    print html
    xian = html.find_all(class_="wz-txtrr")
    for i in xian:
        for j in i:
            zxx = "".join(j.string)
#            print zxx.encode('utf-8').decode('utf-8')
            print zxx
            sql = "insert into zhangxiaoxian(content,w_time) value('%s','%s')" %(zxx,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
            cur.execute(sql)
            con.commit()
            print ">>>>>>>>>>>>>>"


if __name__ == "__main__":
    con = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="fengwang",charset="utf8")
    cur = con.cursor()
    a()
    cur.close()
    con.close()

