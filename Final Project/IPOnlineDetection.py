import socket
import os

#This program answers the first one-to-one job
class IPOnlineDetection(object):

    def __init__(self):
        print()

    def detectIPStatus(self, targetIP):

        rep = os.system('ping ' + targetIP)

        if rep == 0:
            print('')
            print(targetIP, 'is online')
        else:
            print('')
            print(targetIP, 'is Offline')