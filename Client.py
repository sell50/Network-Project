import socket
import sys

#Server Information
SERVER = "127.0.0.1"
PORT = 1233

#Creating Client Socket Object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting Client--->Server
client.connect((SERVER, PORT))

#When True The Client Can Send and Receive Messages
while True:

    #Blocking more than 1024 bytes
    in_data = client.recv(1024)

    #Displaying Message From Server
    print(in_data.decode())

    #Getting Message For Server
    out_data = input()

    #Sending Message To Server
    client.sendall(bytes(out_data, 'UTF-8'))

    #Exit if 'bye' is sent
    if out_data == 'bye':
        break

#Closing the Socket Connection
client.close()
