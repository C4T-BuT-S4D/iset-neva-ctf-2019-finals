#!/usr/bin/env python3

import random
import time

from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import send


def send_icmp_packet(ip, t):
    print('type:', t)
    pkt = IP(dst=ip) / ICMP(type=t)
    p = send(pkt)
    return p


def encode(flag):
    return ''.join(map(lambda x: bin(ord(x))[2:].zfill(8), list(flag)))


flag = open('flag.txt').read()

encoded = encode(flag)
print(encoded)
print(len(encoded))

for c in encoded:
    send_icmp_packet('192.168.1.5', [0, 8][int(c == '1')])
    time.sleep(random.random())
    print(f'Sent {c}')

print('Done!')
