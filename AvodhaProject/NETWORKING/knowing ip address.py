import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    c=socket.gethostbyname('www.facebookxe.com')
    print(c)
except:
    print('invalid website')