#!/usr/bin/env python
#-*-coding=utf-8 -*-

import random, time, Queue
import sys
import os

import json
import socket
from multiprocessing.managers import BaseManager
from multiprocessing import Process
from threading import Thread

import requests

def sendReq(tk=None,p=None,*iv):
    wo = os.popen('whoami')
    global clientLog
    url = "http://open-gateway.beescm.cn:10030/api/router/rest"
    header = {}
    header['Content-Type'] = "application/json"
    header['version'] = iv[0][0]
    header['method'] = iv[0][1]
    header['accessToken'] = tk
    sss = ""
    try:
        r = requests.post(url, headers=header, data=json.dumps(p), timeout=3)
    except requests.exceptions.ConnectTimeout:
        ss = "time request timeout 3 seconds"
        sss = ss
        res = (sss,wo.read())
        clientLog.put(res)
        return None
    except requests.exceptions.Timeout:
        ss = "time request timeout 3 seconds"
        sss = ss
        res = (sss,wo.read())
        clientLog.put(res)
        return None
    sss = r.text
    res = (sss,r.elapsed.total_seconds(),wo.read())
    clientLog.put(res)
    return None

#task_queue = Queue.Queue()
#result_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('task_order')
QueueManager.register('send_result')
QueueManager.register('control_params')
QueueManager.register('mylog')
QueueManager.register('thnum')

m = QueueManager(address=("192.168.171.224",5000),authkey=b'long')
jie = QueueManager(address=("192.168.171.224",5001),authkey=b'abc')

while True:
    try:
        m.connect()
        jie.connect()
        t = m.task_order()
        res = m.send_result()
        conn = m.control_params()
        tn = m.thnum()
        clientLog = jie.mylog()
        print "connect success"
        time.sleep(3)
        while True:
            s = None
            time.sleep(1)
            if not t.empty():
                s = t.get()
            if s == "lihailong":
                while True:
                    time.sleep(1)
                    if not tn.empty():
                        num = tn.get()
                        ss = conn.get()
                        while True:
                            for i in range(int(num)):
                                p = Thread(target=sendReq,args=(ss[0],ss[1],ss[2]))
                                p.start()
                            if not res.empty():
                                stop = res.get()
                                if stop == "stop":
                                    sys.exit()
                    else:
                        continue
    except socket.error:
        print "[Errno 111] Connection refused"
        time.sleep(3)
        continue
