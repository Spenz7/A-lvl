import socket

clientsocket = socket.socket()
address = input('Enter server address')
port = int(input('Enter port no'))

#.connect accepst tuple
clientsocket.connect((address,port))
#keeps on iterating till u 
while True:
    print('Waiting for server')
    data = b''
    #only worry about if data got \n for recv side
    while b'\n' not in data:
        data += clientsocket.recv(1024)

    if data == b'quit\n':
        break
    print('Server wrote:' + data.decode())
    data = input('Input client: ').encode()
    clientsocket.sendall(data+b'\n')
    if data == b'quit':
        break
clientsocket.close()
