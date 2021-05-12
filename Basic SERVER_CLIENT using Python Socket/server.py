#from client import BUFFER
#from client import MessageToServer
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555
BUFFER = 1024
CONNECTIONOBJ = (HOST,PORT)
WELCOME_MESSAGE = "Welcome To Server [Server IP -> "+ str(HOST)+"]"
FORMAT = 'utf-8'


#Creating Socket 
ServerSocket = socket.socket()

#Binding Socket
try:
    ServerSocket.bind((HOST,PORT))
except socket.error as SocketError:
    print(str(SocketError))

#Set Name
ServerName = input("ENTER YOUR NAME : ")

#Listening for request
print(f"[SERVER STARTED @{ServerName}] : ACTIVELY LISTINING FOR CONNECTIONS")
ServerSocket.listen()

#Handling Each Client
def HandleClient(ClientSocket, address):
    print(f"[JOINED] : {address}")
    ClientSocket.send(bytes(f"[MESSAGE FROM SERVER @{ServerName}]" + WELCOME_MESSAGE,FORMAT))
    
    Connected = True
    while Connected:
        print(f"[SERVER @{ServerName}] WAITING FOR REPLY FROM CLIENT...")
        MessageFromClient = ClientSocket.recv(BUFFER)
        MessageFromClient = MessageFromClient.decode()
        print(MessageFromClient)
        MessageToClient = input(f"[SERVER @{ServerName}] ENTER YOUR MESSAGE TO CLIENT - ")
        ClientSocket.send(bytes(f"[MESSAGE FROM SERVER @{ServerName}] -- "+MessageToClient,FORMAT))
        
        


#Accepting Client Requests
ActiveConnection = 0
while True:
    ClientSocket, address = ServerSocket.accept()
    #ClientThread = threading.Thread(target=HandleClient, args=(ClientSocket, address))
    HandleClient(ClientSocket, address)
    # ClientThread.start()
    # ActiveConnection += 1
    # print(f"[ACTIVE CONNECTIONS] : {ActiveConnection}")