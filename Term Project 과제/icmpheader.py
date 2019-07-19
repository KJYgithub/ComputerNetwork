import struct
import socket
from functools import reduce

class IcmpHeader:
    type = 0
    code = 0
    checksum = 0
    id = 0
    sqc = 0
    data = 0

    def __init__(self):
        self.type = 0
        self.code = 0
        self.checksum = 0
        self.id = 0
        self.sqc = 0
        self.data = 1

    def packing(self):
        packheader = struct.pack("!bbHHhH", self.type, self.code, self.checksum, self.id, self.sqc, self.data)
        return packheader

    def make_checksum(self, header):
        size = len(header)
        if (size % 2) == 1:
            header += b'\x00'
            size += 1
        size = size // 2
        header = struct.unpack('!'+str(size) + 'H', header)
        sum = reduce(lambda x, y: x+y, header)
        chksum = (sum >> 16) + (sum & 0xffff)
        chksum += chksum >> 16
        chksum = (chksum ^ 0xffff)

        return chksum

    def make_icmpheader(self):
        self.type = 8
        self.checksum = self.make_checksum(self.packing())
 