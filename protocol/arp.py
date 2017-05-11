#!/usr/bin/python
# -*- coding=utf-8 -*-

from scapy.all import *

request = Ether(dst=ff:ff:ff:ff:ff:ff, src=00-0c-29-9d-46-8f)/ARP(hwsrc=10:02:b5:0c:75:15,psrc="172.16.20.123",hwdst=00:00:00:00:00:00,pdst="172.16.20.254")

send(request)
