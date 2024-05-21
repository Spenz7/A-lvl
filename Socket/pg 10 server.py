import socket
#create, bind, listen, accept, recv, close
#recv is used for reciever
#sendall is used for sender
#this is send from client to server 
my_socket = socket.socket()
my_socket.bind(('0.0.0.0',12345))
my_socket.listen()

#accepts client socket and ipv4 address and port no
#imagine server waiting for connection request to it, once client request,
#server say sure I accept so server allow client socket to connect to it and
#move server's original socket that was listening to somewhere else to listen
new_socket,addr = my_socket.accept()
print('connected to: ' + str(addr))
print(new_socket.recv(1024))

new_socket.close()
my_socket.close()
