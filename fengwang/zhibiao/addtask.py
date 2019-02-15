#!/usr/bin/python
# -*-coding=utf-8 -*-

import json
import requests
import config
header = {}
header['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMTcwMDcwIiwiaWF0IjoxNTM2ODAwNDYwLCJidXNpbmVzc1N5c3RlbSI6IkJPU1MiLCJzb3VyY2VUeXBlIjoiUEMiLCJ0b2tlbkV4cGlyZVRpbWUiOjg2NDAwfQ.f6ctaPtxzAFPjfh_-tVl3AA7sMcaiMjzB4zqz_3YT9XQ04h4JdlzAiWrifOm9Fdo6FY5gpzROLxKbMei91R2Ow"

header['userName'] = "dddddd"
#header['userId'] = "2170940"
header['userId'] = "2170070"
header['Content-Type'] = "application/json"

def addTask(tname):
    global header
    url = config.url + "web/task/info/save"
#    tname = "拜访小店，促成签单"
    data = {}
    data['groupOrg'] = "2"
    data['unitOrg'] = "1"
    data['operateUser'] = "2170940"
    data['taskInfo'] = {"taskName":tname, "taskDesc":"","taskType":"指标任务","docId":""}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content
    print r.url

def taskList():
    global header
    url = config.url + "web/task/info/find/list"
    data = {}
    data['groupOrg'] = 2
    data['unitOrg'] = 1
    data['operateUser'] = "2170940"
    data['queryVO'] = {"taskName":""}  #{"id":"","taskName":"","exactTaskName":""}
    data['pageSize'] = 10
    data['pageNum'] = 1
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content
    print r.url

def addQuota(tname):
    global header
    g = "2"
    u = "1"
#    tname = "注册app数量"
    url = config.url + "web/quota/info/saveInfo/" + g + "/" + u
    data = {}
    data['groupOrg'] = "2"
    data['unitOrg'] = "1"
    data['operateUser'] = "2170940"
    data['quotaInfoVO'] = {"quotaName": tname,"quotaDesc": "所有的春天","quotaMeasure": "个","isGlobal": "","taskInfoId": 3,"isInput": True,"statsType": 12,"state": 1,"belongDepart": 2,"belongUnit": 4,"belongGroup": 21}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

tname = ["1.拜访新店","2.下载注册APP","3.首次下单","4.开通微店小程序","5.达标微店"]

taskname = []
with open('data.txt','r') as f:
    ff = f.readlines()

#for k in ff:
#    addTask(k)

taskList()
#for i in range(10):#tname:
#    addQuota(i)
