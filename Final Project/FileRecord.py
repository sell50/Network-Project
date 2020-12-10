class FileRecord(object):

    def recordOutput(self, clientOutput):

        outputFile = open("ClientOutput.txt", 'a+')
        outputFile.write(clientOutput)
        outputFile.close()

    def updateJobListBackup(self, Job):
        
        jobBackup = open("JobBackup.txt", 'a+')
        jobBackup.write(Job)
        jobBackup.close()

