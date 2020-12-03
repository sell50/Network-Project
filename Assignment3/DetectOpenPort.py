import socket

class DetectOpenPort(object):

    def __init__(self):
        print()


    def checkPort(self, targetIP, targetPort):
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        location = (targetIP, targetPort)
        result_of_check = a_socket.connect_ex(location)

        if result_of_check == 0:
            print("Port: OPEN")
        else:
            print("Port: CLOSED")

        a_socket.close()
