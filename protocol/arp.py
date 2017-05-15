#!/usr/bin/python
# -*- coding=utf-8 -*-

from scapy.all import *

request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(hwsrc='10:02:b5:0c:75:15',psrc="172.16.20.123",pdst="172.16.20.75")

srploop(request)
