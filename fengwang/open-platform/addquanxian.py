#!/usr/bin/python
# -*-coding=utf-8 -*-

import sys

import requests
import threading
import pymysql

import random
import json
import testdata
import config

def addP(i,dd):
    url = config.url + "/fw-open-admin/permission/add?updateUser="
    header = {}
    header['Content-Type'] = "application/json"
    header['userId'] = "2185009"
    header['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMTg1MDA5IiwiaWF0IjoxNTM4MTE5MjQ1LCJidXNpbmVzc1N5c3RlbSI6IkJPU1MiLCJzb3VyY2VUeXBlIjoiUEMiLCJ0b2tlbkV4cGlyZVRpbWUiOjg2NDAwfQ.Pm-rKpv8mY-Tx1_jxtgM_bDY9mFLGUeeaaIL_hbiww4pxKoyJb8oZlY_Riz_h4Z0wgszhA-6N4bMxrcSlw8OEw"
    data = {"id":"","name":i,"description":dd,"updateUser":2170070,"createUser":"2170070"}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

#@num = int(sys.argv[1])
#print num
#for i in range(num, num+10):
con = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="fengwang",charset="utf8")
cur = con.cursor()
sql = "select name from appName limit 0,30"
rows = cur.execute(sql)
rr = cur.fetchall()
for i in rr:#range(2):
    reload(testdata)
#    t = threading.Thread(target=addP)
#    t.start()
    dd = testdata.love
    addP(i[0],dd)
