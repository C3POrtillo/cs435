from Main import createRandomDAGIter
from DirectedGraph import DirectedGraph
from Node import Node
from TopSort import *

ignore = True # To ignore invalid paths where a node does not exist

x = DirectedGraph()
for char in "ABCDEFGH":
  x.addNode(char)

x.addDirectedEdge(x.getNode("A"), x.getNode("B"))
x.addDirectedEdge(x.getNode("A"), x.getNode("D"))

x.addDirectedEdge(x.getNode("C"), x.getNode("D"))
x.addDirectedEdge(x.getNode("C"), x.getNode("G"))
x.addDirectedEdge(x.getNode("C"), x.getNode("H"))

x.addDirectedEdge(x.getNode("D"), x.getNode("G"))

x.addDirectedEdge(x.getNode("H"), x.getNode("E"))
x.addDirectedEdge(x.getNode("H"), x.getNode("F"))

graphs = [createRandomDAGIter(5), createRandomDAGIter(50), x]

if __name__ == "__main__":
  for g in graphs:
    print(g)
    print()
    for func in [TopSort.Kahns, TopSort.mDFS]:
      arr = func(g)
      print("Node Count: {} | {}".format(len(arr), arr))
    print()