from Graph import Graph
from Node import Node

class DirectedGraph(Graph):

  def addDirectedEdge(self, first : Node, second : Node):
    
    if first not in self.vertices:
      self.addNode(first)
    if second not in self.vertices:
      self.addNode(second)
    
    self.vertices[first].add(second)


  def removeDirectedEdge(self, first : Node, second : Node):
    if first in self.vertices and second in self.vertices[first]:
      self.vertices[first].remove(second)