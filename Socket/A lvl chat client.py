import socket
#client side, client is socket that client is gonna use
client = socket.socket()
client.connect(('localhost',9999))
while True:
    data = b''
    while b'\n' not in data:
        data += client.recv(1024)
    if data == b'quit\n':
        print('server ended chat')
        break
    
    print('data sent by server: ',data.decode())
    
    msg = input('enter what u wan send to server: ')
    
    if msg == 'quit':
        print('client ended chat')
        client.sendall(b'quit\n')
        break
    client.sendall(msg.encode()+b'\n')

client.close()

