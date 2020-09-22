from slurmcontrol.slurmconnections import Jobs

class JobsControl(Jobs):

    def GetTotalJobsFound(self):
        return len(self.jobsFound.keys())

    def GetIdsListFound(self):
        return self.jobsFound.keys()

    def UserSubSearch(self, user=str):
        return self.FilterJobsFoundBy(user, 'user')

    def PartitionSubSearch(self, partition):
        return self.FilterJobsFoundBy(partition, 'partition')

    def RenderRunningSubSearch(self):
        return self.FilterJobsFoundBy('RUNNING', 'state')

    def RenderPendingSubSearch(self):
        return self.FilterJobsFoundBy('PENDING', 'state')

if __name__ == '__main__':
    jc = JobsControl()
    jc.SearchJobsInFarm()

    # jc.SearchJobRunning()
    # print jc.UserSubSearch('fapodaca')
    # print jc.PartitionSubSearch('renderFarm')
    # print jc.RenderRunningSubSearch()
    print jc.RenderPendingSubSearch()
    # print jc.jobsFound