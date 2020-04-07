from Main import createRandomCompleteWeightedGraph, createLinkedList
from WeightedGraph import WeightedGraph

ignore = True # To ignore invalid paths where a node does not exist

graphs = [createLinkedList(1000, WeightedGraph()), createRandomCompleteWeightedGraph(1000)]

if __name__ == "__main__":
  for g in graphs:
    print(g)