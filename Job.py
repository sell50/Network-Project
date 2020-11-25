
class Job(object):

    def __init__(self, jobCreator, jobName, numOfSeekers):

        self.JobCreator = jobCreator
        self.JobName = jobName
        self.NumOfSeekers = numOfSeekers

    def __iter__(self):
        yield self.JobCreator
        yield self.JobName
        yield self.NumOfSeekers