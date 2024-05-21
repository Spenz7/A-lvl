import socket
#imagine socket as a pipe with 1 end connected to server and the other to client
#.socket() creates a socket object, use help('socket') in shell for more info or socket.socket

#create, bind, listen, accept, sendall, close


passivesocket = socket.socket()
#host aka ipv4 address, port no
passivesocket.bind(('127.0.0.1',12345))
#listen to incoming connection from client
passivesocket.listen()

#newsocket is a new socket that u use to send and receive data
#create new pipe with same port no and ip address on server side but port no
#and ip address must be diff on client side
newsocket, address = passivesocket.accept()
print('new socket object is ',newsocket)
print('connected to: ' + str(address))

#b' means in bytes
newsocket.sendall(b'Hello from server \n')
#same asnewsocket.sendall('Hello from server \n'.encode())

#RMB CLOSE SOCKETS
newsocket.close()
passivesocket.close()
      
