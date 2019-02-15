#!/usr/bin/python
# -*-coding=utf-8 -*-

import time
import json
import requests
import config

def getTime(func):
    def sf():
        stime = time.time()
        func()
        etime = time.time()
        mtime = etime - stime
        print "use time %s" % mtime
    return sf

@getTime
def login():
    header = {}
    url = config.baseurl + "service-ucenter/user/login"
    data = {}
    data['loginName'] = "dddddd"
    data['password'] = "111111"
#    data['loginName'] = "RY000004278"
#    data['password'] = "lihailong"
    data['useCode'] = False
    data['businessSystem'] = "BOSS"
    data['sourceType'] = "PC"
    r = requests.post(url, headers=header, params=data)
    print r.json()['result']['token']
    print r.url
    return r.json()['result']['token']

if __name__ == "__main__":
    login()
