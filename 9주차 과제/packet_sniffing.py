import os
import socket
import argparse
import struct
ETH_P_ALL = 0x0003
ETH_SIZE = 14
def make_ethernet_header(raw_data):
	ether = struct.unpack('!6B6BH',raw_data)
	if ether[12] == 0x0800:
    		return {'[dst]': '%02x:%02x:%02x:%02x:%02x:%02x' % ether[:6],
  	    		'[src]': '%02x:%02x:%02x:%02x:%02x:%02x' % ether[6:12],
    	    		'[ether_type]':ether[12]}

def dumpcode(buf):
	print ("raw data")
	print("%7s"% "offset ", end='')

	for i in range(0, 16):
		print("%02x " % i, end='')

		if not (i%16-7):
			print("- ", end='')

	print("")

	for i in range(0, len(buf)):
		if not i%16:
			print("0x%04x" % i, end= ' ')

		print("%02x" % buf[i], end= ' ')

		if not (i % 16 - 7):
			print("- ", end='')

		if not (i % 16 - 15):
			print(" ")

	print("")

def make_ip_header(raw_data):
	ip = struct.unpack('!BBHHHBBH4B4B',raw_data)
	num = str(bin(ip[4]))
	flag = int((num[2:4]),2)
	off = int((num[4:17]),2)
	return {'[version]': '%d'% (ip[0]//16),
		'[header_length]' : '%d'% (ip[0]%16),
 		'[tos]': '%d'% ip[1],
		'[total_length]': '%d'% ip[2],
		'[id]': '%d'% ip[3],
		'[flag]': '%d'% flag,
		'[offset]': '%d'% off,
		'[ttl]': '%d'% ip[5],
		'[protocol]': '%d'% ip[6],
		'[checksum]': '%d'% ip[7],
		'[src]': '%d.%d.%d.%d'% ip[8:12],
		'[dst]': '%d.%d.%d.%d'% ip[12:16]}


def sniffing(nic):
	if os.name == 'nt':
		address_familiy = socket.AF_INET
		protocol_type = socket.IPPROTO_IP
	else:
		address_familiy = socket.AF_PACKET
		protocol_type = socket.ntohs(ETH_P_ALL)

	with socket.socket(address_familiy, socket.SOCK_RAW, protocol_type) as sniffe_sock:
		sniffe_sock.bind((nic, 0))

		if os.name == 'nt':
			sniffe_sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
			sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

		data, _ = sniffe_sock.recvfrom(65535)
		ip = struct.unpack('!B',data[ETH_SIZE:ETH_SIZE+1])
		ip_length = (ip[0] % 16)*4

		ethernet_header = make_ethernet_header(data[:ETH_SIZE])
		print("\nEthernet Header")
		for item in ethernet_header.items():
			print('{0}:{1}'.format(item[0],item[1]))

		ip_header = make_ip_header(data[ETH_SIZE:ETH_SIZE+ip_length])
		print("\nIP Header")
		for item in ip_header.items():
			print('{0}:{1}'.format(item[0],item[1]))
		print("\n")

		dumpcode(data)
		if os.name == 'nt':
			sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This is a simpe packet sniffer')
	parser.add_argument('-i', type=str, required=True, metavar='NIC name', help='NIC name')
	args = parser.parse_args()
	while(True):
		sniffing(args.i)
