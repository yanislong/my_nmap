#!/usr/bin/python
# -*-coding=utf-8 -*-

import json
import requests
import config
import login


print ">>>>>>>>"
def hehe(func):
    def abab(*a):
        print "start"
        func(*a)
        print a
        print "end"
    return abab

@hehe
def a(*a1):
    print "running"

a(1,2)
a(1,2,4)
print "<<<<<<<<<"

#login.login()

def addRole(num):
    global tk
    url = config.url + "web/appraise/role/addAppraiseRole"
    header = {}
    header['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMTcwOTQwIiwiaWF0IjoxNTM2Mjg2MTk1LCJidXNpbmVzc1N5c3RlbSI6IkJPU1MiLCJzb3VyY2VUeXBlIjoiUEMiLCJ0b2tlbkV4cGlyZVRpbWUiOjg2NDAwfQ.aSfK1u15J5fXGFWoeUT7W7WB5YaCxiHitxf0yBW2S9Yjq1YYN2hx7v1HoTp-Qr8AMB1cBtJ-MwXNft5oGE1ATw"
    header['Content-Type'] = "application/json"
    header['userName'] = "dddddd"
    header['userId'] = "2170940"
    data = {}
    data['groupOrg'] = "2"
    data['unitOrg'] = "1"
    data['operateUser'] = "2170940"
    data['roleStaffIds'] = ""
    #新增不带id，修改带id
#    data['roleVO'] = {"id":4, "belongGroup": 2, "belongUnit": 1, "city": 130500000000, "province": 130000000000, "roleName": "测试3", "roleType": "测试类型3", "staffVOList": [{"id":8, "belongGroup": 2, "belongUnit": 3, "staffId": 4, "staffType": "市场"},{"belongGroup": 4, "belongUnit": 9, "staffId": 4, "staffType": "销售"}]} 
    data['roleVO'] = {"belongGroup": 2, "belongUnit": 1, "city": 130500000000, "province": 130000000000, "roleName": "a" + str(num), "roleType": "测试类型3", "staffVOList": []}#[{"id":8, "belongGroup": 2, "belongUnit": 3, "staffId": 4, "staffType": "市场"},{"belongGroup": 4, "belongUnit": 9, "staffId": 4, "staffType": "销售"}]} 
#    data['jsonParm'] = {"taskInof":{"taskName":"","taskDesc":"","taskType":"","docId":""}}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content
    print r.url

for i in range(0):
    addRole(i)
