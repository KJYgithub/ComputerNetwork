import socket
import threading
import argparse

def socket_handler(conn):
                msg = conn.recv(1024)
                msg = msg[::-1]
                print(msg.decode())

                conn.sendall(msg)
                conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Thread server -p port")
    parser.add_argument('-p', help = "port_number", required = True)

    args = parser.parse_args()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', int(args.p)))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        t= threading.Thread(target=socket_handler,args=(conn,))
        t.start()

    server.close()
