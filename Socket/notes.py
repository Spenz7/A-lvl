.connect((address,port)) and .bind((address,port)) accepts a tuple

listen not in while loop cuz listen occurs all the time

.recv() will block the prog and prevent it from continuing until at least
1 byte is received

.accept() too until a connection request is recevied

if u wan keep receving data till u detect \n, then rmb
new.sendall(msg.encode()+b'\n')

