import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555
CONNECTIONOBJ = (HOST,PORT)
BUFFER = 1024
FORMAT = 'utf-8'

#Creating Client Socket
ClientSocket = socket.socket()


#Connecting With Server
try:
    ClientSocket.connect(CONNECTIONOBJ)
except socket.error as SocketError:
    print(SocketError)

#Set Name
ClientName = input("ENTER YOUR NAME : ")

message = ClientSocket.recv(BUFFER)
print(message.decode())

connection = True
while connection:
    MessageToServer = input(f"[CLIENT @{ClientName}] ENTER YOUR MESSAGE TO SERVER - ")
    ClientSocket.send(bytes(f"[MESSAGE FROM CLIENT @{ClientName}] -- "+MessageToServer, FORMAT))
    print(f"[CLIENT @{ClientName}] WAITING FOR REPLY FROM SERVER...")
    MessageFromServer = ClientSocket.recv(BUFFER)
    print(MessageFromServer.decode())


