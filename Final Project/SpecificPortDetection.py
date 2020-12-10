import socket

class SpecificPortDetection(object):

    def checkPort(self, targetIP, targetPort):
        checkerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        targetLocation = (targetIP, targetPort)
        portStatus = checkerSocket.connect_ex(targetLocation)

        if portStatus == 0:
            return "Target IP Address: "+targetIP +" Target Port: "+ str(targetPort) +": "+ " Open\n"
        else:
            return "Target IP Address: "+targetIP +" Target Port: "+ str(targetPort) +": "+ " Closed\n"

        checkerSocket.close()