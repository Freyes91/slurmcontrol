from slurmcontrol.slurmconnections import Nodes
from pyslurm import partition
from re import findall

class Partitions(partition, Nodes):

    def __init__(self):
        Nodes.__init__(self)
        partition.__init__(self)

        self.partitionsInformations = {}
        self.SearchPartitions()
        self.partitions = self.partitionsInformations.keys()
        self.namePartition = ''
        self.totalNodes = 0
        self.nodeList = []
        self.rangeNodes = ''

    def __AddPartitionValues(self, node, value):
        self.partitionsInformations[node] = {'nodes': value.get('nodes'),
                                             'listNodes': self.ListNodes(value.get('nodes')),
                                             'totalNodes': value.get('total_nodes')}

    def __SearchNodesInPartition(self, state):
        return [node for node in self.nodeList if findall(state, self.GetStateNode(node))]

    def SearchPartitions(self):
        for partition, values in self.get().iteritems(): self.__AddPartitionValues(partition, values)

    def SelectPartition(self, partition=str):
        if self.partitionsInformations.has_key(partition):
            self.namePartition = partition
            self.totalNodes = self.partitionsInformations.get(partition).get('totalNodes')
            self.nodeList = self.partitionsInformations.get(partition).get('listNodes')
            self.rangeNodes = self.partitionsInformations.get(partition).get('nodes')

    def GetValueFromPartition(self, partition, whatValue):
        if self.partitionsInformations.has_key(partition):
            return self.partitionsInformations.get(partition, whatValue)

    def GetListDownNodes(self):
        return self.__SearchNodesInPartition('DOWN') if self.namePartition else self.GetListOfDownNodes()

    def GetListBusyNodes(self):
        return self.__SearchNodesInPartition('ALLOCATED') if self.namePartition else self.GetListOfBusyNodes()

    def GetListAvailableNodes(self):
        return self.__SearchNodesInPartition('IDLE') if self.namePartition else self.GetListOfAvailableNodes()

    def GetListDrainNodes(self):
        return self.__SearchNodesInPartition('DRAIN') if self.namePartition else self.GetListOfDrainNodes()
