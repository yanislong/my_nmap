#!/usr/bin/python
# -*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import hashlib
import json
import xlrd
import xlwt
from xlutils.copy import copy

def login(nrow):
    global t1
    global ws
    url = t1[5]
    header = {}
    if t1[7] == "json":
        header['Content-Type'] = "application/json"
    elif t1[7] == "from":
        pass
    else:
        pass
    if t1[6] == "post":
        data = json.loads(t1[4])
        r = requests.post(url, headers=header, data=data)
    elif t1[6] == "get":
        param = json.loads(t1[4])
        r = requests.post(url, headers=header, params=param)
    elif t1[6] == "put":
        data = json.loads(t1[4])
        r = requests.post(url, headers=header, data=data)
    elif t1[6] == "delete":
        param = json.loads(t1[4])
        r = requests.post(url, headers=header, params=param)
    ws.write(nrow,8,r.content.decode('utf-8'))
    print r.content
    print r.headers

def m5(pw):
    mm = hashlib.md5()
    mm.update(pw)
    return mm.hexdigest()

if __name__ == "__main__":
    a = sys.argv[1]
    data = xlrd.open_workbook(a)
    new_excel = copy(data)
    ws = new_excel.get_sheet(0)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    for i in range(nrows-1):
        t1 = table.row_values(i+1)
        login(i+1)
        del t1[:]
    new_excel.save('caseRes.xls')
