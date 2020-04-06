from Graph import Graph
from Node import Node

class DirectedGraph(Graph):

  def addDirectedEdge(self, first : Node, second : Node):
    
    if first not in self.graph:
      self.addNode(first)
    if second not in self.graph:
      self.addNode(second)
    
    self.graph[first].add(second)


  def removeDirectedEdge(self, first : Node, second : Node):
    if first in self.graph and second in self.graph[first]:
      self.graph[first].remove(second)