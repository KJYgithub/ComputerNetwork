import struct
from ipheader import*
import socket
from icmpheader import*

s = socket.socket(socket.AF_INET , socket.SOCK_RAW , socket.IPPROTO_RAW)
ip = IpHeader()
icmp = IcmpHeader()

if __name__ == '__main__':
    a = input()
    addr = socket.gethostbyname(a)
    ip.dst = addr
    ip.make_ipheader()
    IPpacket = ip.pack()
    icmp.make_checksum(icmp.packing())
    icmp.make_icmpheader()
    ICMPpakcet = icmp.packing ()
    Datapacket = IPpacket + ICMPpakcet
    


    while Datapacket:
        sending = s.sendto(Datapacket, (addr,1))
        Datapacket = Datapacket[sending:]