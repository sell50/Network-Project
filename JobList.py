from Job import *

class JobList(object):

    listofjobs = []

    def updateJobList(self, creatorName, jobName, numofSeekers):

        job = Job(creatorName, jobName, numofSeekers)
        self.listofjobs.append(job)

    def printJobList(self):
        for obj in self.listofjobs:
            for job in obj:
                print(job, end=", ")
            print()

