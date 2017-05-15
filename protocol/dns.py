#!/usr/bin/python
# -*- cdoing=utf-8 -*-

from scapy.all import *

dhost = '202.106.0.20'
shost = "172.16.20.123"

request = IP(src=shost, dst=dhost)/UDP(dport=53)/DNS(id=1,qr=0,opcode=0,tc=0,rd=1,qdcount=1,ancount=0,nscount=0,arcount=0)
request[DNS].qd = DNSQR(qname='www.xueguoxue.com',qtype=1,qclass=1)

response = IP()/UDP()/DNS()

try:
    while True:
        send(request)
        break
except KeyboardInterrupt:
    print 'quit'
