import socket
#create a socket at the client side
#create, connect, recv , close
#only server need to bind
mysocket = socket.socket()

address = input('enter address of server:')
#rmb port no is integer
port = int(input('enter port no of server:'))

#connect other end of pipe to the server socket
mysocket.connect((address,port))
print(mysocket.recv(1024))
mysocket.close()
