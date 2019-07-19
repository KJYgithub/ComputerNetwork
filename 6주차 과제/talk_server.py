import socket
import threading
import argparse

def getting(conn):
    while True:
        msg = conn.recv(1024)  
        print("From : ",addr[0], ':', addr[1],msg.decode())

def sending(conn):
    while True:
        msg = input()
        conn.sendall(msg.encode())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Thread server -p port")
    parser.add_argument('-p', help = "port_number", required = True)

    args = parser.parse_args()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', int(args.p)))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        t= threading.Thread(target=getting,args=(conn,))
        y= threading.Thread(target=sending,args=(conn,))
        t.start()
        y.start()

    server.close()