import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=5003
s.connect((host,port))
while True:
    sr=s.recv(100)
    print( 'Server:',sr.decode('utf-8'))
    a=input('CLient:')
    s.send(bytes(a,'utf-8'))




