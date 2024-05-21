import socket
serversocket = socket.socket()
serversocket.bind(('127.0.0.1',6789))
serversocket.listen()

clientsocket, addr = serversocket.accept()
while True:
    #server send to client first then recv later
    data = input('Input server: ').encode()
    #using socket created by client to send data to client
    #rmb to add newline character when u send msg
    clientsocket.sendall(data + b'\n')
    #server side quit as in u quit from the shell of the server prog
    #if detect quit in ur input then exit out while loop
    #rmb data is in bytes alr so need use b'quit'
    if data == b'quit':
        break
    print('Waiting for client...')
    data = b''
    #inner while loop for recv data
    while b'\n' not in data:
        #all ur data that u send contain newline char to indicate end of msg
        #eg. b'same\n' is shown when statement below runs and u enter 'same' from client side
        #print(clientsocket.recv(1024))
        data += clientsocket.recv(1024)

    #client side quit
    #whenever u input from client side u add one more 
    #newline character so quit\n means if quit is the only word u wrote in
    #ur message and u press enter
    if data == b'quit\n':
        break
    print('Client wrote:'+data.decode())

clientsocket.close()
serversocket.close()
