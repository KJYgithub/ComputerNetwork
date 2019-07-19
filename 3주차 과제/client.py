import socket
import argparse


def run(host, port,filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        s.sendall(filename.encode()) #server에 파일이름 전송
        
        filesize=s.recv(1024)
        print("파일 사이즈 : " ,filesize.decode())


        ok="ok"
        s.sendall(ok.encode())
        

        resp=s.recv(int(filesize))
        print(resp)
        file = open (filename,'w',encoding = 'utf8')
        file.write(resp.decode())
        file.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p',help="port_number",required=True)
    parser.add_argument('-i',help="host_name",required=True)
    parser.add_argument('-f',help="file_name",required=True)

    args = parser.parse_args()
    run(host=args.i,port = int(args.p),filename=args.f)