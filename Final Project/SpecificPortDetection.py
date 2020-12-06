import socket

class SpecificPortDetection(object):

    def __init__(self):
        print()


    def checkPort(self, targetIP, targetPort):
        checkerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        targetLocation = (targetIP, targetPort)
        portStatus = checkerSocket.connect_ex(targetLocation)

        if portStatus == 0:
            print("Port: OPEN")
        else:
            print("Port: CLOSED")

        checkerSocket.close()