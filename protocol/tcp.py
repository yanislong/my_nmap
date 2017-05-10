#!/usr/bin/python
# -*- coding=utf-8 -*-

from scapy.all import *
import time
import os

host = "172.16.9.238"  #请求地址
sp = 12782  #自己使用tcp的源端口

try:
    os.system("iptables -D OUTPUT 1")
except:
    print "iptables role not "
os.system("iptables -A OUTPUT -p tcp --tcp-flags RST RST -d 172.16.9.238 -j DROP")   #添加防火墙规则

request = IP(dst=host)/TCP(dport=80,sport=sp,flags="S")   #定义syn包
response = sr1(request)  #发送syn包,并保存返回包，存在request中

request2 = IP(dst=host)/TCP(dport=80,sport=sp,flags='A',ack=response[1].seq+1,seq=response[1].ack)  
#time.sleep(7) #tcp三次握手，服务端最后接受应答ack的时间大概7秒，超过7秒就过期，会返回RST
send(request2)

#request3 = IP(dst=host)/TCP(dport=80,sport=sp,flags='PA',ack=response[1].seq+1,seq=response[1].ack)/Raw('GET / HTTP/1.1\r\nHost:172.16.9.238\r\n\r\n') #定义http请求包

#send(request3)
#response2 = sr1(request2)

time.sleep(1)

request4 = IP(dst="172.16.9.238")/TCP(dport=80,sport=sp,flags='FA',seq=response[1].ack,ack=response[1].seq+1)  #客户端发送FIN包,四次挥手第一个包
send(request4)
request5 = IP(dst="172.16.9.238")/TCP(dport=80,sport=sp,flags='A',seq=response[1].ack+1,ack=response[1].seq+2)  #客户端回复ACK应答包，四次握手最后一个包
send(request5)

#bb = sniff(count=5,filter="tcp and host 172.16.9.238 and port 80")
#for i in bb:
#    print i[0][0]
while False:
    bar = sniff(count=1,filter="tcp and host 172.16.9.238 and port 80")
    if bar[0][TCP].flags == 16:
        print bar[0][TCP].flags
        request4 = IP(dst="172.16.9.238")/TCP(dport=80,sport=12344,flags='A',seq=bar[0][TCP].seq,ack=bar[0][TCP].seq+1)
        break
    else:
        print "sinff is running..."

print 'end'
