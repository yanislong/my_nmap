#!/usr/bin/python
# -*-coding=utf-8 -*-

import json
import requests
import config
header = {}
header['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMTcwMDcwIiwiaWF0IjoxNTM3MTQ2OTc0LCJidXNpbmVzc1N5c3RlbSI6IkJPU1MiLCJzb3VyY2VUeXBlIjoiUEMiLCJ0b2tlbkV4cGlyZVRpbWUiOjg2NDAwfQ.2XF524IRr1GrNNfIV2ZfFoF4oltZiwMVUVIFedda7Ne3cDxzfRg0GcwPt6ocyCTjhlqHs7EJJ5-VVxVAQ9GQIg"

header['userName'] = "dddddd"
header['userId'] = "2170070"
header['Content-Type'] = "application/json"

num = 0
def addTask():
    global header
    global num 
    url = "http://web-gateway.beehivescm.com/fw-crm-bd/web/allcust/getCityPartnerList"
    data = {}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content
    if r.json()['status']['statusCode'] == 0:
        print r.url
    else:
        num += 1
        print r.content

for i in range(1):
    addTask()
print "request error %d" %num

