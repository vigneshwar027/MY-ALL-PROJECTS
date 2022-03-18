import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=5003
s.bind((host,port))
s.listen(5)
while True:
    clynt, address=s.accept()
    sm=input('Server:')
    clynt.send(bytes(sm,'utf-8'))
    cr=clynt.recv(100)
    print('Client: ',cr.decode('utf-8'))

