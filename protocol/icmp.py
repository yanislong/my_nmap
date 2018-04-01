#!/usr/bin/python
# -* coding=utf-8 -*-

from scapy.all import *

dhost = "172.16.20.92"
shost = "172.16.20.123"

pack_ip = IP(dst=dhost, src=shost)


