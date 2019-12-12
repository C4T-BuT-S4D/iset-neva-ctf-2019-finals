#!/usr/bin/env python3

from scapy.all import *
from scapy.layers.inet import IP, ICMP

cap = rdpcap('task/capture.pcapng.gz')
print('Done reading capture')

print(cap)

results = ''


def decode(data):
    decoded = ''.join(chr(int(data[i:i + 8], 2)) for i in range(0, len(data), 8))
    return decoded


for pkt in cap:
    if ICMP in pkt:
        dst = pkt[IP].dst
        if dst == '192.168.1.5':
            t = pkt[ICMP].type
            print(t)
            results += ['0', '1'][t == 8]

print(results)

print(f'Got flag data: {decode(results)}')
