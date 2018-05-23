import socket as s
import sys
import os
import struct
from ctypes import *

''' Basic network sniffer '''



# host to listen on 

def get_ip():
    test = s.socket(s.AF_INET,s.SOCK_DGRAM)
    test.connect(("8.8.8.8",80))
    
    return test.getsockname()[0]

host = get_ip()


# Ip header structure

class IP(Structure):
    _fields_ = [
        ("ihl",             c_ubyte, 4),
        ("version",         c_ubyte, 4),
        ("tos",             c_ubyte),
        ("len",             c_ushort),
        ("id",              c_ushort),
        ("offset",          c_ushort),
        ("ttl",             c_ubyte),
        ("protocol_num",    c_ubyte),
        ("sum",             c_ushort),
        #("src",             c_ulong), # not working on 64bits
        ("src",             c_uint32),
        #("dst",             c_ulong) # not working on 64bits
        ("dst",             c_uint32)
    ]

    def __new__(self,socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self,socket_buffer=None):

        # map protocol constants to their names
        self.protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}

        # human readable IP addresses
        self.src_address = s.inet_ntoa(struct.pack("<L",self.src))
        self.dst_address = s.inet_ntoa(struct.pack("<L",self.dst))

        # human readable protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)

# print IP
print(host)

# requires interface argument
print(len(sys.argv))
if len(sys.argv) < 2:
    print("[*] Interface required")
    print("[*] Exiting")
    sys.exit(1)
else:
    interface = sys.argv[1]
    print("[*] Interface %s supplied" % interface)

# special socket protocol on windows
if os.name == "nt":
    socket_protocol = s.IPPROTO_IP
    print("[*] Using %s protocol" % socket_protocol)
else:
    # Linux requires you to specify the exact protocol you are using
    socket_protocol = s.IPPROTO_ICMP
    print("[*] Using %s protocol" % socket_protocol)

try:
    # create raw socket and bind to supplied interface
    sniffer = s.socket(s.AF_INET, s.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
except PermissionError:
    print("[*] Needs to be run as root")
    sys.exit(2)

# Add IP headers in capture
sniffer.setsockopt(s.IPPROTO_IP, s.IP_HDRINCL, 1)

try:
    # sniff indefinitely
    while True:
        # read a packet
        raw_buffer = sniffer.recvfrom(65565)[0]
	# create ip header from the first 20 bytes of the buffer
	# ip_header = IP(raw_buffer[0:20]
        print("[*] printing raw buffer %s" % (raw_buffer))
        print("[*] printing raw buffer 32bits %s" % (raw_buffer[0:20]))
        print("[*] printing raw buffer 64bits %s" % (raw_buffer[0:32]))
        ip_header = IP(raw_buffer)
        print("[*] showing avaiable obj methods :\n %s " % ip_header.__dict__)
        #print(ip_header.__dict__.keys())
	#proto = ip_header.protocol_map[ip_header.proto
        # print out the protocol that was detected and the hosts
        print("[*] Protocol: %s %s -> %s" % (ip_header.protocol, ip_header.src_address, ip_header.dst_address))

#except Exception as e:
#    print(e)
# handle CTRL-C
except KeyboardInterrupt:
    exit(0)

