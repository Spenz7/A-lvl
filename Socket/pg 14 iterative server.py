import socket
#if server is sender: create, bind, listen, accept, sendall, close
#connect is always for client
#then client would be: create, connect, recv, close
passivesocket = socket.socket()
passivesocket.bind(('127.0.0.1',12345))
#.listen() not in while loop cuz .listen() is running all the time
passivesocket.listen()
#this is caled iterative server, which means server is always listening for
#multiple connection requests
while True:
    newsocket, clientaddress = passivesocket.accept()
    #rmb add \n add the back
    newsocket.sendall(b'Hello\n')
    newsocket.close()
#this while loop is infinite, when passivesocket.accept() has nth to accept
#then rest of the code below stop running and restart while loop so need
#ctrl c to force stop shell
