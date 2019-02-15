#!/usr/bin/python
#-*-coding=utf-8-*-

import json
from multiprocessing import Process

import requests

import config

def getGateway(tk=None,p=None,*iv):
    assert tk
    if not p:
        p = {}
    url = config.url + "/api/router/rest"
    header = {}
    header['Content-Type'] = "application/json"
    header['accessToken'] = tk
    header['version'] = iv[0][0]
    header['method'] = iv[0][1]
    r = requests.post(url, headers=header, data=json.dumps(p))
    print r.content
    print r.elapsed.total_seconds()

if __name__ == "__main__":
    getGateway(config.aToken,config.ff,config.api_v)
