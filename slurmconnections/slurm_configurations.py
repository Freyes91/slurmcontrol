import pyslurm as slurm

class SlurmConfiguration(object):

    def GetSlurmServer(self):
        return slurm.get_controllers()[0]

    def SlurmReconfigure(self):
        slurm.slurm_reconfigure()

    def CancelJob(self, jobId=int):
        slurm.slurm_kill_job(jobId, 9, 0)

    def SuspendJob(self, jobId=int):
        slurm.slurm_suspend(jobId)

    def ActivateJob(self, jobId=int):
        slurm.slurm_resume(jobId)

    def RequeueJob(self, jobId=int):
        slurm.slurm_requeue(jobId)