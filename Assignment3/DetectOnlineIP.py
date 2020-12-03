import socket
import os

#This program answers the first one-to-one job
class DetectOnlineIP(object):

    def __init__(self):
        print()

    def detect(self, ipaddress):

        targetip = input('Enter the host to be scanned: ')
        targetaddress = socket.gethostbyname(targetip)

        print('Looking to see if host is online...')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket

        rep = os.system('ping ' + targetaddress)
        if rep == 0:
            print('')
            print(targetaddress, 'is online!')
        else:
            print('')
            print(targetaddress, 'is not online!')