import socket
def client():
    host = socket.gethostname()
    port = 2000
    while True:
        try:

            clientsock = socket.socket()
            print('socket creation was successful')
        except socket.error :
            print('socket creation was unsuccessful',socket.error)
        try:
            clientsock.connect((host,port))
            print('connection was successful')
        except socket.error:
            print('connection was unsuccessful')
        message = input('-->')
        while message.lower().strip()!='bye':
            clientsock.send(message.encode())
            data = clientsock.recv(1024).decode()
            print('client side: ',str(data))
            message = input('-->')
           # clientsock.close()
if __name__ == '__main__':
    client()


