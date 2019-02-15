#!/usr/bin/env python
#-*-coding=utf-8 -*-

import time
import random, time, Queue
from multiprocessing.managers import BaseManager
import logging

import config

LOG_FORMAT= "%(asctime)s %(levelname)s %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"
FNAME = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT,datefmt=DATE_FORMAT,filename='./log/' + FNAME + '.log')

log_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('mylog',callable=lambda:log_queue)
manager = QueueManager(address=("",5001),authkey=b'abc')
manager.start()

mylog = manager.mylog()

while True:
    if not mylog.empty():
        r = mylog.get()
        logging.debug(r)
