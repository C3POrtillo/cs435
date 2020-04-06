from Node import Node
class Graph:

  def __init__(self):
    self.graph = {}

  def addNode(self, node):
    if not isinstance(node, Node):
      node = Node(node)
    self.graph[node] = node.neighbors = set()

  def addUndirectedEdge(self, first : Node, second : Node):

    if first not in self.graph:
      self.addNode(first)
    if second not in self.graph:
      self.addNode(second)

    self.graph[first].add(second)
    self.graph[second].add(first)

  def removeUndirectedEdge(self, first : Node, second : Node):
    if first in self.graph and second in self.graph[first]:
      self.graph[first].remove(second)

    if second in self.graph and first in self.graph[second]:
      self.graph[second].remove(first)

  def getAllNodes(self) -> set:
    return set(self.graph.keys())

  def getNode(self, nodeVal) -> Node:
    for node in self.graph:
      if node.val == str(nodeVal):
        return node
