import socket
import os
import subprocess
""" example TCP server """
PORT = 5000 # default port
HOST = '127.0.0.1' # localhost
data = b""

def recv_data(sock, max):
    d = b''
    with open('fetched_d', 'wb') as f:
    # write received data to file
        while len(d) < max:
            data = sock.recv(max)
            d+=data
            if data == b'OVER':
                break
            elif data:
                f.write(data)
    return 'done'

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        sc, scname = sock.accept()
        # check how many bytes u need
        MAX = int(sc.recv(64).decode('ascii'))
        recv_message = recv_data(sc, MAX+4) # +4 needs for final message
        sc.close()
        break

    # change fetched file to zip format
    bashCommand = "mv fetched_d fetched_d.zip"
    output = subprocess.check_output(['bash','-c', bashCommand])

if __name__ == '__main__':
    server(HOST, PORT)
