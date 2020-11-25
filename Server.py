import socket
import sys
import os
import pickle
from _thread import *
from JobList import *


class Server(object):

    def __init__(self):

        self.ServerSocket = socket.socket()
        self.host = '127.0.0.1'
        self.port = 1233
        self.ThreadCount = 0
        self.jobList = JobList()

        # Bind socket to port
        try:
            self.ServerSocket.bind((self.host, self.port))

        except socket.error as e:
            print(str(e))

        print('Waiting for a Connection..')
        self.ServerSocket.listen(5)

    def main(self):
        while True:
            Client, address = self.ServerSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.threadedClient, (Client,))
            self.ThreadCount += 1
            print('Thread Number: ' + str(self.ThreadCount))

    def threadedClient(self, connection):
        connection.send(str.encode("Welcome, Are You A Job Seeker or A Job Creator?\n"
                                +"Enter JS for Job Seeker, JC for Job Creator or Exit to quit","UTF-8"))
        while True:
            #Limiting to 2048 Bytes
            data = connection.recv(2048)

            #Receiving Message From Client
            roleSelection = data.decode()

            #Job Creator Condition
            if roleSelection.upper() == 'JC':
                self.FoundJobCreator(connection)

            #Job Seeker Condition
            if roleSelection.upper() == 'JS':
                self.FoundJobSeeker(connection)

            #Exit Program Condition
            if roleSelection.upper() == 'EXIT':
                sys.exit(0)

            #Base Condition
            if roleSelection.upper() != 'JC' and roleSelection.upper() != 'JS' and roleSelection.upper() != 'EXIT':
                connection.send(bytes("Not a Valid Input...Try Again", 'UTF-8'))

        connection.close()


    def FoundJobSeeker(self, connection):
        print("In Function")
        # Sending Job Seeker Options
        connection.send(bytes("1.View Jobs\n2.Current Jobs\n3.Exit\n", 'UTF-8'))

        while True:
            # Receiving Message From Client
            data = connection.recv(2048)
            optionSelection = data.decode()

            # View Jobs Condition
            if optionSelection == '1':
   
                print("Job Seeker Views Job")
                connection.send(bytes("Job Seeker: Viewing Jobs", 'UTF-8'))

            # Current Job Condition
            if optionSelection == '2':
 
                print("Job Seeker Viewing Current Jobs")
                connection.send(bytes("Job Seeker Viewing Current Jobs", 'UTF-8'))

            # Exit Condition
            if optionSelection == '3':
                sys.exit(0)

            # Base Case Condition
            if optionSelection != '1' and optionSelection != '2' and optionSelection != '3':
                connection.send(bytes("Not a Valid Input...Try Again", 'UTF-8'))

    def FoundJobCreator(self, connection):

        """
        :Description: This Function will Run when the Client identifies themselves as a Job Creator.
                        It will then send the Client a list of options to choose from, when one of these
                        choices are picked it will run another function to fulfil the job requested from
                        the Job Creator Client
        :param connection: This is the Socket which is used to send and receive message from the Client
        :return: VOID
        """

        # Sending Job Creator Options to Client
        connection.send(bytes("1.View Jobs\n2.Create Job\n3.Exit\n", 'UTF-8'))

        while True:
            # Receiving Message From Client
            data = connection.recv(2048)
            optionSelection = data.decode()

            # View Jobs Condition
            if optionSelection == '1':

                print("Client Views Job")
                self.jobListView(connection)

            # Create Job Condition
            if optionSelection == '2':

                self.jobCreationItems(connection)

            # Exit Condition
            if optionSelection == '3':
                sys.exit(0)

            # Base Case Condition
            if optionSelection != '1' and optionSelection != '2' and optionSelection != '3':
                connection.send(bytes("Not a Valid Input...Try Again", 'UTF-8'))

    def jobCreationItems(self, connection):

        # Sending Job Creator Options to Client
        connection.send(bytes("Enter name of Job Creator:", 'UTF-8'))
        data = connection.recv(2048)
        creatorsName = data.decode()

        connection.send(bytes("Enter the job name:", 'UTF-8'))
        data = connection.recv(2048)
        jobName = data.decode()

        connection.send(bytes("Enter number of job seekers:", 'UTF-8'))
        data = connection.recv(2048)
        numofSeekers = data.decode()

        self.jobList.updateJobList(creatorsName, jobName, numofSeekers)
        self.jobList.printJobList()

        #Sending Job Creator Options to Client
        connection.send(bytes("1.View Jobs\n2.Create Job\n3.Exit\n", 'UTF-8'))

    def jobListView(self, connection):

        #Condition for No Jobs In Job List
        if len(self.jobList.listofjobs) == 0:
            connection.send(bytes("No Jobs Posted", 'UTF-8'))
        else:

            jobNum = 0

            for obj in self.jobList.listofjobs:

                connection.send(bytes(self.jobList.listofjobs[jobNum].FullJob, 'UTF-8'))

                jobNum+=1


if __name__ == "__main__":
    s = Server()
    s.main()
