import socket
from pickle import *

msgFromClient = "Hello from udp client"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1",20001)

bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
m=[]

for i in range(r):
    temp=[]
    for j in range(c):
        temp.append(input("Enter "+str(i)+", "+str(j)+" of the matrix: "))
    m.append(temp)
UDPClientSocket.sendto(dumps(m), serverAddressPort)


msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from server:{}".format(loads(msgFromServer[0]))
print(msg)