from Main import createRandomCompleteWeightedGraph, createLinkedList
from WeightedGraph import WeightedGraph
from Node import Node

ignore = True # To ignore invalid paths where a node does not exist

graphs = [createLinkedList(25, WeightedGraph()), createRandomCompleteWeightedGraph(10)]

if __name__ == "__main__":
  for g in graphs:
    print(g)