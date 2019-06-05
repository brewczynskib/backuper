import sys
import socket
import os
import zlib

def imp_client(HOST, PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, int(PORT)))
    sock.send(bytes(str(os.path.getsize('./file.zip')), 'ascii'))
    with open('file.zip', 'rb') as f:
            src = f.read()
    sock.sendall(src)

    sock.send('OVER'.encode('ascii'))
    sock.close()
    print('over')

if __name__ == '__main__':
    HOST, PORT = sys.argv[1:]
    imp_client(HOST, PORT)
