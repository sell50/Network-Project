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

    def updateJobListBackup(self, Job):
        """
        Input: Job (String)
        Description: This function checks for 'JobBackup.txt', if not found
                    it will create this file and append the given input to this file.
                    After all is done, the stream to the file is closed ensuring the 
                    file gets saved
        """
        jobBackup = open("JobBackup.txt", 'a+')
        jobBackup.write(Job)
        jobBackup.close()

