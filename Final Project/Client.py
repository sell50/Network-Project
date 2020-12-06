import pickle
import socket
from IPOnlineDetection import *
from SpecificPortDetection import *
from UDPFloodAttack import *
from TCPFloodAttack import *
from NodeLocation import *

'''
After Client runs Job Specific Program (EX: UDP Flood Attack)
Send Message to Server to tell Job Creator the job is complete
'''


class Client(object):

    def __init__(self):
        """
        Name: Client Constructor
        Type: void
        Description: This constructor will save all the necessary variables that will be used
                    in the other class functions
        """

        # Server Information
        self.SERVER = "127.0.0.1"
        self.PORT = 1233

        # Target Information
        self.targetIP = "1.1.1.1"
        self.targetPort = 25565

        #One-to-One Job Objects
        self.ipDetection = IPOnlineDetection()
        self.portDetection = SpecificPortDetection()

        #One-to-Many Job Objects
        self.udpAttack = UDPFloodAttack()
        self.tcpAttack = TCPFloodAttack()

        #Final Project Job Objects
        self.nodeLocation = NodeLocation()

        #Needed Variables
        self.in_data = ''

        self.HOSTNAME = socket.gethostname()

        self.seekerIP = socket.gethostbyname(self.HOSTNAME)

        #Creating Client Socket Object
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connecting Client--->Server
        self.client.connect((self.SERVER, self.PORT))

        print(self.seekerIP)

    '''
    HELPER Functions
    '''

    # Handles and Chooses Right Path For Server Messages
    def serverMessageHandler(self):

        # When True The Client Can Send and Receive Messages
        while True:
            # Refresh Buffer For New Server Message
            self.resetServerMessage()

            # For Closing Connection To Server
            self.closeConnection(self.in_data)

            # For Displaying Messages From The Server
            self.normalCommunication(self.in_data)

            # For Displaying the List to Client
            self.obtainList(self.in_data)

            # For Setting the Target Credentials
            self.setTargetCredentials(self.in_data)

            # For Running Specific Job
            self.jobPrograms()

            # Gathering Input From Client to send to Server
            out_data = input()

            # Sending Message To Server
            self.client.send(pickle.dumps(out_data))

    # Takes in Server Message to Run Specific Job
    def jobPrograms(self):
        if self.in_data == "IPOnlineDetection":

            self.resetServerMessage()
            self.targetIP = self.in_data

            self.resetServerMessage()
            self.targetPort = self.in_data

            self.ipDetection.detectIPStatus(self.targetIP)

        elif self.in_data == "SpecificPortDetection":

            self.resetServerMessage()
            self.targetIP = self.in_data

            self.resetServerMessage()
            self.targetPort = int(self.in_data)

            self.portDetection.checkPort(self.targetIP, self.targetPort)

        elif self.in_data == "TCPFloodAttack":

            self.resetServerMessage()
            self.targetIP = self.in_data

            self.resetServerMessage()
            self.targetPort = int(self.in_data)

            self.tcpAttack.sendTCPPackets(self.targetIP, self.targetPort)

        elif self.in_data == "UDPFloodAttack":

            self.resetServerMessage()
            self.targetIP = self.in_data

            self.resetServerMessage()
            self.targetPort = int(self.in_data)

            self.udpAttack.sendUDPPackets(self.targetIP, self.targetPort)

        elif self.in_data == "NodeLocation":

            self.resetServerMessage()
            self.targetIP = self.in_data

            self.resetServerMessage()
            self.targetPort = int(self.in_data)

            self.nodeLocation.DistanceEquation(self.targetIP, self.seekerIP)

        elif self.in_data == "NodeLANScan":

            self.resetServerMessage()
            self.targetIP = self.in_data

            self.resetServerMessage()
            self.targetPort = int(self.in_data)

            print("Job 6")

    #Prints List Messages From Server
    def obtainList(self, in_data):
        count = 1

        # If JobList is sent from Server Print the Job List
        if type(in_data) == list:
            for job in in_data:
                print(str(count) + ":", end=" ")
                count += 1
                for element in job:
                    if len(element) == 1:
                        print(element, end="")
                    else:
                        print(element, end=" ")
                print()

    # Prints Single Lined Messages From Server
    def normalCommunication(self, in_data):
        if type(in_data) != list:
            print(in_data)

    # Sets The Global Target Credentials (Job Seeker)
    def setTargetCredentials(self, in_data):

        if in_data == "Target Credentials":
            print("Obtaining Target Information")

            # Refresh Buffer For New Server Message
            self.resetServerMessage()

            # Setting Global targetIP
            self.targetIP = str(in_data)
            print(self.targetIP)

            # Refresh Buffer For New Server Message
            self.resetServerMessage()

            # Setting Global targetPort
            self.targetPort = int(in_data)
            print(self.targetPort)

            # Skip Blank Space
            print("Press Enter to Continue")

    # Refresh Buffer For New Server Message
    def resetServerMessage(self):
        # Limiting to 1024 bytes
        self.in_data = self.client.recv(2048)

        # Sets in_data to what is sent from the Server
        self.in_data = pickle.loads(self.in_data)

    # Closes Connection to Server
    def closeConnection(self, in_data):
        if in_data == 'exit':
            self.client.close()

    # Main Function
    def main(self):
        self.serverMessageHandler()


# Start Main Function
if __name__ == "__main__":
    s = Client()
    s.main()