from slurmcontrol.slurmconnections import Partitions
from pyslurm import create_partition_dict, slurm_update_partition, slurm_create_partition, slurm_delete_partition

class PartitionConfigurations(Partitions):

    def __init__(self):
        Partitions.__init__(self)

    def __CreateDictionary(self, partitionName=str, rangePartition=str):
        partition = create_partition_dict()
        partition['Name'] = partitionName
        partition['Nodes'] = rangePartition
        return partition

    def ChangePartitionNodes(self, partitionName=str, listNodes=list):
        if partitionName in self.partitions:
            slurm_update_partition(self.__CreateDictionary(partitionName, self.RangeNodes(listNodes)))

    def CreatePartition(self, partitionName=str, rangePartition=str):
        if not partitionName in self.partitions:
            partition = self.__CreateDictionary(partitionName, rangePartition)
            slurm_create_partition(partition)
            slurm_update_partition(partition)
            self.SearchPartitions()

    def DeletePartition(self, partitionName=str):
        if partitionName in self.partitions: slurm_delete_partition(partitionName)
        self.SearchPartitions()

    def RenamePartition(self, partitionName=str, newPartition=str):
        if partitionName in self.partitions and newPartition not in self.partitions:
            self.SelectPartition(partitionName)
            self.DeletePartition(partitionName)
            self.CreatePartition(partitionName, self.rangeNodes)
            self.SearchPartitions()

    def AddNodesInPartition(self, partitionName=str, listNodes=list):
        if partitionName in self.partitions:
            self.SelectPartition(partitionName)
            self.ChangePartitionNodes(partitionName, sorted(list(set(self.nodeList + listNodes))))


if __name__ == '__main__':
    PartitionConfigurations().AddNodesInPartition('hold', ['farm001', 'farm002', 'farm003','farm043'])