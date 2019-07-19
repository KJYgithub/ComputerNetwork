import socket
import argparse
import threading
            
def bada(sock):
     while True:
    
        resp=sock.recv(1024)
        print("From : ", resp.decode())      

def bonae(sock):
    while True:
        msg = input()
        sock.sendall(msg.encode())

def run(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        t= threading.Thread(target=bada,args=(s,))
        y= threading.Thread(target=bonae,args=(s,))
        t.start()
        y.start()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p',help="port_number",required=True)
    parser.add_argument('-i',help="host_name",required=True)
    args = parser.parse_args()
    run(host=args.i,port = int(args.p))