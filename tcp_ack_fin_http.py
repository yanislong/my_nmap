#!/usr/bin/python
# -*- coding=utf-8 -*-

from scapy.all import *

dip = "172.16.9.238"
port = 80
#pp = 19400

def tcp():
    pp = random.randint(10000,20000)
#    global pp
    pp += 1
    ip = IP(src="172.16.20.123", dst=dip)
    tcp = TCP(dport=port,flags="S",sport=pp,seq=0)
    r1 = sr1(ip/tcp)
    tcp_a = IP(src="172.16.20.123", dst=dip)/TCP(dport=port,sport=r1[1].dport,flags='A',seq=1,ack=r1[1].seq + 1)
    send(tcp_a)
    tcp_http = IP(dst=dip)/TCP(dport=port,sport=r1[1].dport,flags='PA',seq=1,ack=r1[1].seq + 1,options=[('MSS', 10)])/Raw('GET /sdf.php HTTP/1.1\r\nHost:172.16.9.238\r\n\r\n')
    send(tcp_http)
    a = sniff(count=2, filter="tcp and host 172.16.9.238 and port 80")
    print a[1].show()
    l =  a[1].len - 40
    print l
#    print r2[0][0][0].show()
    tcp_ack = IP(dst=dip)/TCP(dport=port, sport=r1[1].dport,flags='A',seq=a[1].ack,ack=a[1].seq + l)
    send(tcp_ack)
    tcp_fin_ack = IP(dst=dip)/TCP(dport=port, sport=r1[1].dport,flags="FA",seq=a[1].ack,ack=a[1].seq + l)
    send(tcp_fin_ack)
    a2 = sniff(count=1,filter="tcp and host 172.16.9.238 and port 80")
    print a2[0].show()
    print a2[0].seq,a2[0].ack
    tcp_ack_fin_2 = IP(dst=dip)/TCP(dport=port, sport=r1[1].dport,flags="A",seq=a2[0].ack,ack=a2[0].seq + 1)
    send(tcp_ack_fin_2)

for i in range(1):
    print i
    tcp()

