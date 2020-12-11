class FileRecord(object):

    def recordOutput(self, clientOutput):
        """
        Input: clientOutput (String)
        Description: This function checks for 'ClientOutput.txt', if not found
                    it will create this file and append the given input to this file.
                    After all is done, the stream to the file is closed ensuring the
                    file gets saved
        """
        outputFile = open("ClientOutput.txt", 'a+')
        outputFile.write(clientOutput)
        outputFile.close()

    def updateJobListBackup(self, jobList):
        """
        Input: Job (String)
        Description: This function checks for 'JobBackup.txt', if not found
                    it will create this file and append the given input to this file.
                    After all is done, the stream to the file is closed ensuring the
                    file gets saved
        """
        try:
            jobBackup = open("JobBackup.txt", 'w+')
        except IOError:
            jobBackup = open("JobBackup.txt", 'w+')

        for Jobs in jobList:
            jobBackup.write(Jobs.FullJob)

        jobBackup.close()