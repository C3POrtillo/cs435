from Main import createRandomCompleteWeightedGraph, createLinkedList, dijkstras
from WeightedGraph import WeightedGraph

graphs = [createLinkedList(100, WeightedGraph()), createRandomCompleteWeightedGraph(100)]

if __name__ == "__main__":
  for g in graphs:
    for val in ["0", "50", "99"]:
      n = g.getNode(val)
      print("Dijkstras Map for Node {}: {}".format(n, dijkstras(n)))
      print()