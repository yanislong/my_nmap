#!/usr/bin/python

import requests
import json

def a():
    url = "http://web-gateway.beehivescm.com/fw-open-admin/app/getAppSecret?appId=42801983190601728&updateUser=2170070"
    header = {}
    header['Content-Type'] = "application/json"
    data = {}
    r = requests.post(url, headers=header)
#    print r.content
    print r.json()['result']

for i in range(10):
    a()

