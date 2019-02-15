#!/usr/bin/python
# -*-coding=utf-8 -*-

import sys
#reload(sys)
#sys.setdefaultencoding('gb2312')
import pymysql
import time

import requests
from bs4 import BeautifulSoup

def a(num):
#    global con
#    global cur
    url = "https://www.juzimi.com/writer/张爱玲?page=1"# + str(num)
    header = {}
    header['User-Agent'] =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
#    header['Cookie'] = "Hm_lpvt_83c5bfe4d0b8be1afcf05ddf0efddbe2=1538279328; Hm_lvt_83c5bfe4d0b8be1afcf05ddf0efddbe2=1538278621,1538278674,1538278715,1538279328"
    r = requests.get(url, headers=header)
    print r.status_code
    print r.url
    print r.content
    html = BeautifulSoup(r.content)
    xian = html.find_all(class_="xlistju")
    for i in xian:
        for j in i:
            zxx = "".join(j.string)
            print zxx
            sql = "insert into zhangxiaoxian(content,w_time) value('%s','%s')" %(zxx,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#            cur.execute(sql)
#            con.commit()
            print ">>>>>>>>>>>>>>"


if __name__ == "__main__":
#    con = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="fengwang",charset="utf8")
#    cur = con.cursor()
    a(1)
#    cur.close()
#    con.close()

