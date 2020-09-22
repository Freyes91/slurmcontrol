from pyslurm import node, hostlist
from re import findall

class Nodes():

    def __init__(self):
        self.noFarm = ['slurmweb', 'huematrix']
        self.nodeInformations = {}
        self.__hosts = hostlist()
        self.__node = node()
        self.SearchNodes()
        self.nodes = sorted(self.nodeInformations.keys())
        self.state = ''
        self.node = ''

    def __AddNodeValues(self, node, value):
        self.nodeInformations[node] = {'state': value.get('state')}

    def ListNodes(self, hosts):
        self.__hosts.create(hosts)
        nodes = self.__hosts.get_list()
        self.__hosts.destroy()
        return sorted(nodes)

    def RangeNodes(self, hosts=list):
        self.__hosts.create(','.join(hosts))
        nodes = self.__hosts.ranged_string()
        self.__hosts.destroy()
        return nodes

    def __SearchByState(self, state):
        return sorted([node for node in self.nodes if findall(state, self.GetStateNode(node))])

    def SearchNodes(self):
        for node, value in self.__node.get().iteritems():
            if not node in self.noFarm: self.__AddNodeValues(node, value)

    def GetStateNode(self, node):
        if self.nodeInformations.has_key(node): return self.nodeInformations.get(node).get('state')

    def GetListOfDownNodes(self):
        return self.__SearchByState('DOWN')

    def GetListOfBusyNodes(self):
        return self.__SearchByState('ALLOCATED')

    def GetListOfAvailableNodes(self):
        return self.__SearchByState('IDLE')

    def GetListOfDrainNodes(self):
        return self.__SearchByState('DRAIN')

    def SelectNode(self, node=str):
        if self.nodeInformations.has_key(node):
            self.node = node
            self.state = self.nodeInformations.get(node).get('state')
