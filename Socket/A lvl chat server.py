import socket

#create
passive = socket.socket()
#bind tuple
passive.bind(('localhost',9999))
passive.listen()
#accept only 1 connection
new , addr = passive.accept()
while True:
    msg = input('msg to send to client:')
    if msg == 'quit':
        print('server ended chat')
        new.sendall(b'quit\n')
        break
    new.sendall(msg.encode()+b'\n')
    
    data = b''
    while b'\n' not in data:
        data+=new.recv(1024)
        
    if data == b'quit\n':
        print('client ended chat')
        break
        
    print('msg recevied by client: ',data.decode())
    
    

new.close()
passive.close()
