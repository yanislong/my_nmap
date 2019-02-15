#!/usr/bin/env python

from threading import Thread
import requests

import config

def login():
    url = config.url + "/oauth/client/token"
    header = {}
    data = {}
    data['appKey'] = config.akey
    data['appSecret'] = config.asecret
    r = requests.post(url, data=data, timeout=3)
#    print r.content
#    print "requests and response total time %s" % r.elapsed.total_seconds()
    return r.json()['result']['accessToken']

if __name__ == "__main__":
    for i in range(1):
        t = Thread(target=login)
        t.start()
    t.join()
