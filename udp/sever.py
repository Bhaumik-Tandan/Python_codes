import socket
from pickle import *
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP,localPort))

print("UDP server up and listening")

def transpose(m):
	t=[]
	for i in range(len(m[0])):
		te=[]
		for j in range(len(m)):
			te.append(m[j][i])
		t.append(te)
	return t
while(True):
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	matrix = (bytesAddressPair[0])
	address = bytesAddressPair[1]
	matrixToSend=transpose(loads(matrix))
	print(matrixToSend)
	UDPServerSocket.sendto(dumps(matrixToSend),address)
	clientMsg = "Message from client: {}".format(loads(matrix))
	print(clientMsg)