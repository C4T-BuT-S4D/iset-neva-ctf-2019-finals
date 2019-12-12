#!/usr/bin/env python3

from scapy.all import *
from scapy.layers.ntp import NTPExtension
from scapy.layers.inet import IP

cap = rdpcap('task/capture.pcapng.gz')
print('Done reading capture')

print(cap)

for pkt in cap:
    if NTPExtension in pkt:
        data = pkt[NTPExtension]
        # print(data)
        dst = pkt[IP].dst
        print('dst:', dst)
        if dst == '195.167.30.249':
            pl = bytes(data).decode(errors='replace')
            print(pl[:30].encode())
            res = pl[14:18]
