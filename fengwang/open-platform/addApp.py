#!/usr/bin/python
# -*-coding=utf-8 -*-

import sys

import requests
import threading
from multiprocessing import Process
import random

import json
import testdata
import time
import config

def addP(i,dd):
    imgurl = "http://open-1254060329.cosbj.myqcloud.com/admin/3713c16aebe946fa8cb80a02c2188366.png"
    url = config.url + "/fw-open-admin/app/add?updateUser=undefined" 
    header = {}
    header['userId'] = "2185009"
    header['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMTg1MDA5IiwiaWF0IjoxNTM4MTE5MjQ1LCJidXNpbmVzc1N5c3RlbSI6IkJPU1MiLCJzb3VyY2VUeXBlIjoiUEMiLCJ0b2tlbkV4cGlyZVRpbWUiOjg2NDAwfQ.Pm-rKpv8mY-Tx1_jxtgM_bDY9mFLGUeeaaIL_hbiww4pxKoyJb8oZlY_Riz_h4Z0wgszhA-6N4bMxrcSlw8OEw"
    header['Content-Type'] = "application/json"
    data = {"authorizeLevel":0,"appType":"1","name": i,"createType":"","callbackUri":"","description":dd,"developer":"40916157489876992","status":2,"logoUri":imgurl, "permissionIds":["40674185525202944"],"permissionNames":["40674185525202944"],'appKey':'abc',"createUser":"2170070"}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

name = ["Google智能AI项目","科斯拉自动驾驶","智能客物联网_01","阿里云D&B大数据服务"]

for i in name:
    reload(testdata)
    dd = testdata.love
    t = Process(target=addP,args=(i,dd))
    t.start()
    t.join()
'''
num = int(sys.argv[1])
print num
for i in range(num, num+1):
    reload(testdata)
    time.sleep(3)
    addP(i)
'''
