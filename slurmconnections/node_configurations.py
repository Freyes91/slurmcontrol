from slurmcontrol.slurmconnections import Nodes
from pyslurm import NODE_STATE_IDLE, NODE_STATE_DOWN, node

class NodeConfigurations(Nodes):

    def __init__(self):
        Nodes.__init__(self)
        self.__node = node()

    def DownNode(self, node=str, reason=str):
        if node in self.nodes and reason != '':
            downDict = {'node_names': node, 'node_state': NODE_STATE_DOWN, 'reason': reason}
            self.__node.update(downDict)

    def IdleNode(self, node=str):
        if node in self.nodes:
            actNode = {'node_names': node, 'node_state': NODE_STATE_IDLE}
            self.__node.update(actNode)

    def UndrainNode(self, node):
        if node in self.nodes:
            self.SelectNode(node)
            if self.state == 'DRAIN':
                self.DownNode(node, 'undrain node')
                self.IdleNode(node)
