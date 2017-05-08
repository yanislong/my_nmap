#!/usr/bin/python
# -*- coding=utf-8 -*-

from scapy.all import *
import time
import os

os.system("iptables -A OUTPUT -p tcp --tcp-flags RST RST -d 172.16.9.238 -j DROP")
a = IP(dst='172.16.9.238')/TCP(dport=80,sport=5432,flags="S")  #定义syn包
b = sr1(a)  #发送syn包,并保存返回包，存在b中

a1 = IP(dst="172.16.9.238")/TCP(dport=80,sport=5432,flags='A',ack=b[1].seq+1,seq=b[1].ack)  
sr1(a1)    #获取seq,完成3次握手

time.sleep(5)
f = IP(dst="172.16.9.238")/TCP(dport=80,sport=5432,flags='FA')
#sr1(f)
os.system("iptables -D OUTPUT 1")
