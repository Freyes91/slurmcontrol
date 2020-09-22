from slurmcontrol.slurmconnections import Partitions

class PartitionNodesControl(Partitions):

    def __init__(self):
        Partitions.__init__(self)

    def GetRangeDownNodes(self):
        return self.RangeNodes(self.GetListDownNodes())

    def GetRangeBusyNodes(self):
        return self.RangeNodes(self.GetListBusyNodes())

    def GetRangeAvailableNodes(self):
        return self.RangeNodes(self.GetListAvailableNodes())

    def GetRangeDrainNodes(self):
        return self.RangeNodes(self.GetRangeDrainNodes())

    def GetSharedNodes(self):
        shared ={}
        for node in self.nodes:
            share = [p for p in self.partitions if node in self.partitionsInformations.get(p).get('listNodes')]
            if len(share) > 1: shared['_'.join(share)] = node

        return shared

if __name__ == '__main__':
    pnc = PartitionNodesControl()
    # print pnc.partitions
    # pnc.SelectPartition('renderFarm')
    # print pnc.nodeList
    # print pnc.GetRangeAvailableNodes()
    # print pnc.GetRangeBusyNodes()
    # print pnc.GetRangeDownNodes()
    # print pnc.partitions



    # print pnc.totalNodes
    # print pnc.nodeList
    # print pnc.rangeNodes

    print pnc.GetListAvailableNodes()
    print pnc.GetListBusyNodes()
    print pnc.GetListDownNodes()
    print pnc.GetListDrainNodes()

    # print pnc.GetSharedNodes()