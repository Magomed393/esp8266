import socket

server = socket.socket()
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('',5562))
server.listen(1)

def data():
dat = conn.recv(1024)
print(dat.decode('utf-8'))

while True:
    conn, addr = server.accept()
    #print('connected:', addr)
    data() 
    conn.close()
