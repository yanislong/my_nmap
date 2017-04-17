#!/usr/bin/python
# -*- coding=utf-8 -*-

from scapy.all import *

dip = "172.16.9.238"
#host = '202.91.23'
port = 80

for i in range(1):
    pp = random.randint(10000,20000)
    ip = IP(src="172.16.20.123", dst=dip)
    tcp = TCP(dport=port,flags="S",sport=pp,seq=0)
    r1 = sr1(ip/tcp)
#    a = sniff(count=1, filter="tcp and host 172.16.9.238 and port 80")
    print r1[1].seq
    tcp_a = IP(src="172.16.20.123", dst=dip)/TCP(dport=port,sport=r1[1].dport,flags='A',seq=1,ack=r1[1].seq + 1)
    send(tcp_a)
    tcp_http = IP(src='172.16.20.123', dst=dip)/TCP(dport=port, sport=r1[1].dport, flags='PA', seq=1,ack=r1[1].seq + 1)/Raw('POST /discussion/save HTTP/1.1\r\nHost: course.lihailong.xueguoxuewang.cn\r\nContent-Length: 83\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nUser-Agent: python-requests/2.7.0 CPython/2.7.9 Linux/4.0.0-kali1-686-pae\r\nConnection: keep-alive\r\ncookie: course_xueguoxuewang_session=056otffaq7bih7ktv8rf4b9j63\r\nX-Requested-With: XMLHttpRequest\r\nContent-Type: application/x-www-form-urlencoded\r\nX-CSRF-TOKEN: Wvrw43YpYxoVu1wFc/4THoWz0aXIEW69ciTLnFwBaWHRO/nv5NgEU6oqXiLZkLZOIvdpY5wfetg=\r\n\r\nsource_id=783200374&source=10&content=ht%0Ctp%3A%2F%0C%2Fww%0Cw.baidu.c%0Com+%2C+_2')
    send(tcp_http)
c = sniff(count=1,filter="tcp and port 80")
print c[0].show()
