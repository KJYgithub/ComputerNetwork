import socket
import argparse

def run(host, port,msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        s.sendall(msg.encode())
        resp=s.recv(1024)
        print(resp.decode())

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p',help="port_number",required=True)
    parser.add_argument('-i',help="host_name",required=True)
    parser.add_argument('-s',help="message",required=True)

    args = parser.parse_args()
    run(host=args.i,port = int(args.p),msg=args.s)