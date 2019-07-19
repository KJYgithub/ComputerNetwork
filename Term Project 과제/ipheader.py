import struct
import socket

class IpHeader:
    version = 0
    headerlength = 0
    totallength = 0
    id = 0
    flag = 0
    offset = 0
    ttl = 0
    protocol = 0
    checksum = 0
    src = 0
    dst = 0
    ssrc = 0
    sdst = 0
    raw = None

    def __init__(self, src ="0.0.0.0", dst ="0.0.0.0"):
        self.version = 0
        self.headerlength = 0
        self.totallength = 0
        self.id = 0
        self.flag = 0
        self.offset = 0
        self.ttl = 0
        self.protocol = socket.IPPROTO_ICMP
        self.checksum = 0
        self.src = src
        self.dst = dst
    
    def make_ipheader(self):
        self.version = 4
        self.headerlength = 5
        self.totallength = 50
        self.ttl = 40
        self.id = 54321
        self.ssrc = socket.inet_aton(self.src)
        self.sdst = socket.inet_aton(self.dst)

    def pack(self):
        bite = struct.pack("!BBHHHBBH4s4s", self.version, self.headerlength, self.totallength, self.id, self.flag, self.offset, self.ttl, self.protocol, self.checksum, self.src, self.dst)
        return bite