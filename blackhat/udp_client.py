#!/usr/bin/python2

import socket as s

target_host = "127.0.0.1"
target_port = 80

# Still creating socket object
udp_cli = s.socket(s.AF_INET, s.SOCK_DGRAM)

# Send data ; UDP is connectionless
udp_cli.sendto("This is a UDP fucking client, bitch", (target_host, target_port))

# Receive the response

response, whatever = udp_cli.recvfrom(4096)

print response

