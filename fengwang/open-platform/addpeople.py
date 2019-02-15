#!/usr/bin/python
# -*-coding=utf-8 -*-

import sys
import random

import pymysql
import requests

import json
import config

def addP(i):
    imgurl = "http://open-1254060329.cosbj.myqcloud.com/admin/4dd4e187840d45c084f7610002cd2110.jpg"
    url = config.url + "/fw-open-admin/personalDeveloper/add" #?updateUser=2185009" 
    header = {}
    header['Content-Type'] = "application/json"
    header['userId'] = "2185009"
    header['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMTg1MDA5IiwiaWF0IjoxNTM4MTE5MjQ1LCJidXNpbmVzc1N5c3RlbSI6IkJPU1MiLCJzb3VyY2VUeXBlIjoiUEMiLCJ0b2tlbkV4cGlyZVRpbWUiOjg2NDAwfQ.Pm-rKpv8mY-Tx1_jxtgM_bDY9mFLGUeeaaIL_hbiww4pxKoyJb8oZlY_Riz_h4Z0wgszhA-6N4bMxrcSlw8OEw"
    data = {"personalName":i,"email":"","idNumber":"342401198807" + str(random.randint(100000,999999)),"image":'["' + imgurl + '","' + imgurl + '","' + imgurl + '"]',"phone":"1" + str(random.randint(10000,99999)) + str(random.randint(10000,99999)),"updateTime":None,"createUser":"2170070"}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

#num = int(sys.argv[1])
#print num
con = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="fengwang",charset="utf8")
cur = con.cursor()
sql = "select name from data_name limit 0,30"
rows = cur.execute(sql)
rr = cur.fetchall()
for i in rr:
    addP(i[0])
#cur.close()
#con.close()
