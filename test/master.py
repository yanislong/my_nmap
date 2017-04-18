#!/usr/bin/python
# -*- coding=utf-8 -*-

import Queue
from multiprocessing.managers import BaseManager
import sys
import os
import threading
import requests
import Queue
import multiprocessing
import time

acc = 0
err = 0
url = "http://www.baidu.com"
url1 = "http://www.xueguoxue.com"
def open():
    global acc
    global err
    for i in range(1):
        start = time.time()
        r = requests.get(url1, timeout=30)
        if r.status_code == 200:
            end = time.time()
            shijian = end - start
            print shijian
            ll.acquire()
            acc += 1
            ll.release()
        else:
            ll.acquire()
            err += 1
            ll.release()
            result2.put(r.status_code)
    print "runing .....",i
#    ll.acquire()
#    res = "ok=" + str(acc) + "worry=" + str(err) + "current processing is" + str(os.getpid())
#    result.put(res)   
#    ll.release()

queue = Queue.Queue()
queue2 = Queue.Queue()
class myfun():
    num = 3
    def a(self):
        global num
        self.num += 1
        print self.num
        print "hello"

BaseManager.register('test', callable=lambda: queue)
BaseManager.register('test1',callable=lambda: queue2)
m = BaseManager(address=('172.16.9.123',5555), authkey="abc")
m.start()

result = m.test()
result2 = m.test1()
ll = threading.Lock()
def oo():
    job = []
    for i in range(100):
        t = threading.Thread(target=open,args=())
        t.start()
        print 'xiancheng count:',threading.active_count()
        job.append(t)
    for j in job:
        j.join()
    res = {'chenggong':acc,'error':err,'pid':os.getpid(),'threadcount':threading.active_count()}
    result.put(res)

pl = multiprocessing.Lock()

job = []
for i in range(1):
    p = multiprocessing.Process(target=oo, args=())
    p.start()
    job.append(p)
    for j in job:
        j.join()

for i in range(0):
    try:
        r = result.get(timeout=20)
        print r
        print "result.get %d" %i
    except Queue.Empty:
        print "queue emput , quit"
        sys.exit()
    finally:
        m.shutdown()   

print 'result is qsize():',result.qsize()
print 'result2 is qsize():',result2.qsize()
num = 0
shibai = 0
while not result.empty():
    r = result.get(timeout=10)
    print r
    num += r['chenggong']
    shibai += r['error']

while not result2.empty():
    r = result2.get(timeout=10)
    print r

print 'access chenggong:',num
print 'access shibai:',shibai
print 'access count:', (num + shibai)
if shibai == 0:
    print 'access chenggonglv: 100%'
else:
    print 'access chenggonglv:%.6f%%'%((float(num)/float(num + shibai)) * 100)
m.shutdown()
print "Manager exit"
