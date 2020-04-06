from Graph import Graph
from Node import Node

class DirectedGraph(Graph):

  def addDirectedEdge(self, first : Node, second : Node):
    if not self.nodeExists(first):
      self.addNode(first)
    if not self.nodeExists(second):
      self.addNode(second)
    self.vertices[first].add(second)

  def removeDirectedEdge(self, first : Node, second : Node):
    if self.nodeExists(first) and self.nodeExists(second) and second in self.vertices[first]:
      self.vertices[first].remove(second)