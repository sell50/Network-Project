import socket
import os

#This program answers the first one-to-one job 

targetIP = input('Enter the host to be scanned: ')
targetAddress = socket.gethostbyname(targetIP)

print('Looking to see if host is online...')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket

rep = os.system('ping ' + targetAddress)
if rep == 0:
    print('')
    print(targetAddress, 'is online!')
else:
    print('')
    print(targetAddress, 'is not online!')
