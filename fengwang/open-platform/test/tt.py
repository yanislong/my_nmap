#!/usr/bin/python
#-*-coding=utf-8 -*-

import requests

url = "http://web-gateway.beehivescm.com/fw-open-admin/category/add?&updateUser=2170070"
r = requests.post(url, data={"id":"","name":"我是充数的","description":"","updateUser":2170070})
result = r.json()
print(result)
assert r.status_code == 200
assert result['status'] == "success"
assert result['data']['start_time'] == "2016-10-15T18:00:00"
