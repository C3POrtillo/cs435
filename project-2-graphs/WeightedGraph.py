from Graph import Graph
from DirectedGraph import DirectedGraph
from Node import Node

class WeightedGraph(DirectedGraph):

  def addNode(self, node):
    if not isinstance(node, Node):
      node = Node(node)
    self.vertices[node] = node.neighbors = {}

  def addWeightedEdge(self, first : Node, second : Node, edgeWeight : int):
    if first not in self.vertices:
      self.addNode(first)
    if second not in self.vertices:
      self.addNode(second)
    self.vertices[first][second] = edgeWeight

  def removeDirectedEdge(self, first : Node, second : Node):
    if first in self.vertices and second in self.vertices[first]:
      self.vertices[first].pop(second)
    