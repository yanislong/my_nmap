#!/usr/bin/python

import requests
import threading
import json

def a():
    url = "http://web-gateway.beehivescm.com/service-ucenter/user/findUserListByPage?pageSize=20&pageNum=1&total=1348"
    header = {}
    header['Content-Type'] = "application/json"
    header['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMTcwMDcwIiwiaWF0IjoxNTM3NDE0NjAxLCJidXNpbmVzc1N5c3RlbSI6IkJPU1MiLCJzb3VyY2VUeXBlIjoiUEMiLCJ0b2tlbkV4cGlyZVRpbWUiOjg2NDAwfQ.RIM1wg8-uvQqYWvKrMf4Up6DxMMBD1DNGTjCEuw2voG3fI14TOvHNS3lYiUAG_F-gqEAw2vs-5o5-bNADHeppQ"
    header['userId'] = "2170070"
    data = {"id":2170070,"groupId":2,"source":"","userName":"","phone":"","enable":"","lock":""}
    r = requests.post(url, headers=header, data=json.dumps(data))
#    print r.content
    print r.status_code

while True:
    for i in range(100):
        t = threading.Thread(target=a)
        t.start()
        t.join()

