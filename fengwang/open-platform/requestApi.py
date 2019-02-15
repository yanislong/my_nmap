#!/usr/bin/python
# -*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random
import pymysql
import json
import requests
import multiprocessing

import config

def addApi():
#    tt = ["eyJhbGciOiJIUzI1NiJ9.eyJhcHBLZXkiOiI2ZjZlNDg5M2U2MTE0Y2JmOWMyMTE2NTY3ZmYxNGE1ZCJ9.vob4OFoTw6LC-7W17otIVAVKVTYCmv1cEnrN8-G-S4I","eyJhbGciOiJIUzI1NiJ9.eyJhcHBLZXkiOiJjMWZjMjlmZmU3MWY0NjA2YWMxYjkwZTRmZjZhNTVmYyJ9.Yri3knNVXuV1TYFyE9Z4CMv57I8KgJb0h7stEt0ZUHE","eyJhbGciOiJIUzI1NiJ9.eyJhcHBLZXkiOiIzNWFkMDg0Yzk1Nzg0MGYzYjc1MTg1MmM1ZDFmZjMxMiJ9.7otD2qd7XjkgJJrHDfjkeRbrVj10xPjbw0xwNRlU_-c"]
    tt = ["eyJhbGciOiJIUzI1NiJ9.eyJhcHBLZXkiOiJkOGEyY2E4YjY2ZTg0Y2I1OTM3ZTcyNzZlNTczYzdiOCIsImNyZWF0ZVRpbWUiOjE1MzkxMzkwNjcyNjh9.MRMd1WoVyjci4aio-xqcrwUwynG5UerW92LjwJbF8Zg"]
#    mm = ["addMember","getIdFindDep","memberFind"]
    mm = ["addMember"]
    url = config.aurl + "/api/router/rest?groupId=1&orgId=1&memberSource=1&mobile=1&createUser=1&userId=2170070"
    header = {}
    header['Content-Type'] = "application/json"
    header['method'] = random.choice(mm)
    header['version'] = "v2.0"
    header['accessToken'] = random.choice(tt)
    data = {}
    data['updateUser'] = "1"
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

if __name__ == "__main__":
    num = 0
    for j in range(1):
        for i in range(5):
            p = multiprocessing.Process(target=addApi)
            p.start()
            num += 1
    print ">>>>>>>>>>>> %s" %num
