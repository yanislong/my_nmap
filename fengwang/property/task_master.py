#!/usr/bin/env python

import random, time, Queue
from multiprocessing.managers import BaseManager
import logging

import config

'''
LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"
FNAME = time.strtime("%Y-%m-%d %H:%M:%S",time.localtime())

logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT,datefmt=DATE_FORMAT,filename='./log/' + FNAME + '.log')
'''

#send task queue
task_queue = Queue.Queue()

#get task queue
result_queue = Queue.Queue()

con_queue = Queue.Queue()
th_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('task_order', callable=lambda:task_queue)
QueueManager.register('send_result', callable=lambda:result_queue)
QueueManager.register('control_params',callable=lambda:con_queue)
QueueManager.register('thnum',callable=lambda:th_queue)

manager = QueueManager(address=("",5000),authkey=b'long')
manager.start()
print "start ..."

task = manager.task_order()
result = manager.send_result()
conn = manager.control_params()
tn = manager.thnum()

for i in range(2):
    time.sleep(1)
    s = raw_input("shell>>").strip()
    task.put(s)

for i in range(2):
    time.sleep(1)
    s = int(raw_input("num>>").strip())
    tn.put(s)
'''
    if s == "lihailong":
        while 1:
            try:
                print "please input a number:\t"
                s = int(raw_input("shell>>").strip())
                task.put(s)
                break
            except:
                print "input process number error"
        break
'''

pp = (config.aToken,config.ff,config.api_v)
conn.put(pp)

#if result.qsize()>0:
print "client running..."

for i in range(2):
    stop = raw_input("are you input stop >> ").strip()
    result.put(stop)

time.sleep(5)
manager.shutdown()
print "master exit."
