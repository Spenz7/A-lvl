#if client is receving then create, connect, recv, close
import socket
client = socket.socket()
client.connect('127.0.0.1',12345)

#rmb b before the string
data = b''
while b'\n' not in data:
    data += client.recv(1024)

client.close()
