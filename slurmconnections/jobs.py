from pyslurm import job
from pwd import getpwuid
from re import findall

class Jobs(job):

    def __init__(self):
        job.__init__(self)
        self.jobs = ''
        self.workStationSend = ''
        self.timeRunning = ''
        self.startRender = ''
        self.jobsFound = {}
        self.userGroup = ''
        self.partition = ''
        self.endRender = ''
        self.command = ''
        self.jobName = ''
        self.jobId = ''
        self.state = ''
        self.nodes = ''
        self.node = ''
        self.send = ''
        self.user = ''
        self.log = ''

    # Searchs
    def SearchJobsInFarm(self):
        for jobId, values in self.get().iteritems(): self.__AddJobValues(jobId, values)

    def SearchJobId(self, jobId=int):
        try:
            self.jobsFound = {}
            self.__AddJobValues(jobId, self.find_id(str(jobId))[0])
            self.SelectJobId(jobId)
        except: pass

    def SearchJobRunning(self):
        self.jobsFound = {}
        for jobId in self.find('job_state', 'RUNNING'): self.__AddJobValues(jobId, self.find_id(jobId)[0])

    def SearchJobPending(self):
        self.jobsFound = {}
        for jobId in self.find('job_state', 'PENDING'): self.__AddJobValues(jobId, self.find_id(jobId)[0])

    def SearchByPartition(self, partition=str):
        self.jobsFound = {}
        for jobId in self.find('partition', partition): self.__AddJobValues(jobId, self.find_id(jobId)[0])

    def SearchByUser(self, user=str):
        self.jobsFound = {}
        for jobId, values in self.find_user(user).iteritems(): self.__AddJobValues(jobId, values)

    def __AddJobValues(self, jobId, values):
        self.jobsFound[jobId] = {'jobId': values.get('job_id'),
                                 'jobName': values.get('name'),
                                 'state': values.get('job_state'),
                                 'log': values.get('std_out'),
                                 'command': values.get('command'),
                                 'userGroup': values.get('group_id'),
                                 'node': values.get('alloc_node'),
                                 'send': values.get('submit_time'),
                                 'startRender': values.get('start_time'),
                                 'endRender': values.get('end_time'),
                                 'user': getpwuid(values.get('user_id'))[0],
                                 'workStationSend': values.get('work_dir'),
                                 'timeRunning': values.get('run_time_str'),
                                 'partition': values.get('partition'),
                                 'nodes': values.get('partition')}

    # Filter searches
    def SearchByName(self, name=str):
        return self.FilterJobsFoundBy(name, 'jobName')

    def FilterJobsFoundBy(self, whatDoSearch, whereDoSearch):
        if not self.jobsFound: self.SearchJobsInFarm()
        result = {}
        ids = [jobId for jobId, values in self.jobsFound.iteritems() if findall(whatDoSearch, values.get(whereDoSearch))]
        for id in ids: result[id] = self.jobsFound.get(id)
        return result

    def SelectJobId(self, jobId=int):
        if self.jobsFound.has_key(jobId):
            jobInfo = self.jobsFound.get(jobId)
            self.workStationSend = jobInfo.get('workStationSend')
            self.timeRunning = jobInfo.get('timeRunning')
            self.startRender = jobInfo.get('startRender')
            self.partition = jobInfo.get('partition')
            self.endRender = jobInfo.get('endRender')
            self.userGroup = jobInfo.get('userGroup')
            self.command = jobInfo.get('command')
            self.jobName = jobInfo.get('jobName')
            self.jobId = jobInfo.get('jobId')
            self.state = jobInfo.get('state')
            self.nodes =jobInfo.get('nodes')
            self.node = jobInfo.get('node')
            self.send = jobInfo.get('send')
            self.user = jobInfo.get('user')
            self.log = jobInfo.get('log')

if __name__ == '__main__':
    jb = Jobs()
    # jb.SearchJobsInFarm()
    # jb.SearchJobId('6422523')

    # jb.SearchJobRunning()
    # jb.SearchJobPending()ss
    # jb.SearchByUser('jlasa')
    #jb.SearchByPartition('renderFarm')
    # print jb.GetTotalJobsFound()

    # for job, values in jb.jobsFound.iteritems():
    #     print job, values

    # print jb.GetTotalJobsFound()

    print jb.SearchByName('106')
    # for idj, value in jb.jobsFilter.iteritems():
    #     print idj, value.get('jobName'), value.get('user')
    # print jb.GetJobsFound()

    # jb.SelectJobId(6425091)
    # print jb.log

