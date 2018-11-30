import socket
def server():
    host = socket.gethostname()
    port = 2000
    while True:
        try:
            # while True:
            sersock = socket.socket()
            print('socket is created successfully')
        except socket.error:
            print('socket creation was unsuccessfull', socket.error)
        sersock.bind((host, port))
        sersock.listen()
        print('server is waiting for connection')
        try:
            conn, addr = sersock.accept()
            print('connection was successful with client having address', str(addr))
        except socket.error:
            print('connection was unsuccessful')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('receiver side : ', str(data.decode()))
            message = input('-->')
            conn.send(message.encode())
         #   conn.close()
if __name__ == '__main__':
    server()
