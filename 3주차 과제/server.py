import socket
import argparse
import os

def run_server(port,dir):
    host = ''

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen(1)

        conn, addr = s.accept()
        filename = conn.recv(1024)
        filename = filename.decode()
        strr = dir + filename
        
        if os.path.isfile(strr):
                file = open(strr, 'r' , encoding = "utf8")
                filesize = os.path.getsize(strr)
                print("size : ",filesize)
                conn.sendall(str(filesize).encode()) 
                print("사이즈전송 완료\n")

                sign = conn.recv(1024)
                 
                text_str = file.read()
                print(text_str)
                conn.sendall(text_str.encode())
                print("파일전송 완료.")
                file.close()
                
               
               
                conn.close()
        else:
                print ("해당 파일이 없습니다")
                return -1
        
        

if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Echo server -p port")
    parser.add_argument('-p',help="port_number",required=True)
    parser.add_argument('-d',help="directory",required=True)
    args=parser.parse_args()
    run_server(port=int(args.p), dir=args.d)