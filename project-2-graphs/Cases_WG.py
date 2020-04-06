from Main import createRandomCompleteWeightedGraph
from Node import Node

ignore = True # To ignore invalid paths where a node does not exist

graphs = [createRandomCompleteWeightedGraph(10)]

if __name__ == "__main__":
  for g in graphs:
    print(g)