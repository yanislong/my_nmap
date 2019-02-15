#!/usr/bin/python
# -*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random
import pymysql
import json
import requests

import config

def addApi(num):
    url = config.url + "/fw-open-admin/api/add"
    header = {}
    header['Content-Type'] = "application/json"
    data = {"createUser":"2170070","updateUser":2170070,"createTime":1537178473000,"updateTime":1537178473000,"id":"42499519530799104","apiName": str(num),"apiMethod":"api" + str(random.randint(1,1000)),"params":"[{\"name\":\"id\",\"type\":\"string\",\"isRequired\":\"是\",\"describe\":\"1\",\"sampleValue\":\"1\"},{\"name\":\"year\",\"type\":\"Number\",\"isRequired\":\"是\",\"describe\":\"1988\",\"sampleValue\":\"1988\"}]","response":"[{\"name\":\"status\",\"type\":\"string\",\"describe\":\"test\",\"sampleValue\":\"200\"}]","errorCode":"[{\"code\":\"1001\",\"errordescribe\":\"参数锁雾\",\"methods\":\"输入参数\"}]","apiVersion":"V1.0","categoryId":"40649228279746560","apiType":"0","personalLimit":100,"companyLimit":200,"rpcType":"2","status":"0","principal":"朱熹","description":"测试数据","accessType":"1","productUrl":"http://www.baidu.com","testUrl":"http://www.baidu.com","devUrl":None,"requestExample":"id=1&time=1988","responseExample":"status=200","permissionIds":[40674185525202940,40925011514626050,40999291392757760,41012250240225280],"contentType":"0","sourceType":None,"categoryName":"默认类目","permissionNames":["移动端应用","web网站组","查询库","权限认证库"]}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

def addApi1():
    url = config.url + "/admin/api/add"
    header = {}
    header['Content-Type'] = "application/json"
    data = {}
    data['accessType'] = ""
    data['apiMethod'] = ""
    data['apiName'] = ""
    data['apiType'] = ""
    data['apiVersion'] = ""
    data['categoryId'] = ""
    data['companyLimit'] = ""
    data['contentType'] = ""
    data['createTime'] = ""
    data['createUser'] = ""
    data['description'] = ""
    data['devUrl'] = ""
    data['errorCode'] = ""
    data['id'] = ""
    data['params'] = ""
    data['permissionIds'] = []
    data['personalLimit'] = ""
    data['principal'] = ""
    data['productUrl'] = ""
    data['requestExample'] = ""
    data['rpcType'] = ""
    data['sourceType'] = ""
    data['status'] = ""
    data['testUrl'] = ""
    data['updateTime'] = ""
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content
    print r.url

if __name__ == "__main__":
    con = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="fengwang",charset="utf8")
    sql = "select content from FM_title;"
    cur = con.cursor()
    rows = cur.execute(sql)
    res = cur.fetchall()
    for i in res[:20]:
        print i[0]
        addApi(i[0])
    cur.close()
    con.close()
