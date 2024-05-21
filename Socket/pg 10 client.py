import socket
#create, connect, sendall, close
client = socket.socket()
address = input('Address')
port = int(input('Port'))

#need extra() cuz u combine 2 items into one
client.connect((address,port))
client.sendall(b'Hello from client')

client.close()
