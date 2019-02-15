#!/usr/bin/python
# -*-coding=utf-8 -*-

import sys

import requests
import threading

import json
import testdata
import config

def addP(name,dd):
    url = config.url + "/fw-open-admin/category/add?&updateUser=2170070"
    print url
'''
    header = {}
    header['Content-Type'] = "application/json"
    header['userId'] = "2185009"
    header['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMTg1MDA5IiwiaWF0IjoxNTM4MTE5MjQ1LCJidXNpbmVzc1N5c3RlbSI6IkJPU1MiLCJzb3VyY2VUeXBlIjoiUEMiLCJ0b2tlbkV4cGlyZVRpbWUiOjg2NDAwfQ.Pm-rKpv8mY-Tx1_jxtgM_bDY9mFLGUeeaaIL_hbiww4pxKoyJb8oZlY_Riz_h4Z0wgszhA-6N4bMxrcSlw8OEw"
    data = {"id":"","name":name,"description":dd,"updateUser":2170070,"createUser":"2170070"}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

#num = int(sys.argv[1])
#print num
name = ["WMS1"]#,"TMS","SCM","供应商","BOSS基础平台","运营平台","后台服务商","B2b","城市合伙人"]
for i in name:#range(num, num+10):
#for i in range(2):
    reload(testdata)
    dd = testdata.love
    addP(i,dd)
 #   t = threading.Thread(target=addP,args=("test",dd))
 #   t.start()
 #   t.join()
'''
addP(1,2)
