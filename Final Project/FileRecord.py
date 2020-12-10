class FileRecord(object):

    def recordOutput(self, clientOutput):

        outputFile = open("ClientOutput.txt", 'a+')
        outputFile.write(clientOutput)
        outputFile.close()

    def updateJobListBackup(self):
        print()

    def readJobListBack(self):
        print()

