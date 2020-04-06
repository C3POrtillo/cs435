from Main import createRandomUnewightedGraphIter, createRandomDAGIter, GraphSearch
from DirectedGraph import DirectedGraph
from GraphConversion import *

ignore = True # To ignore invalid paths where a node does not exist
graphs = [createRandomDAGIter(10), createRandomUnewightedGraphIter(10)]

for g in graphs:
  edges = readable_edges(g)
  for node in sorted(edges.keys()):
    print("{} | {}".format(node, edges[node]))
  print()

  bft = GraphSearch.BFTRec(g)
  print("BFTRec()  :", nodes_to_val(bft))
  bft = GraphSearch.BFTIter(g)
  print("BFTIter() :", nodes_to_val(bft))
  print()

  for start in [0, 15, -1, "a", "c"]:
    start_node = g.getNode(start)
    if ignore and start_node == None:
      continue
    for end in [start, 7, 40, -1, "b", "d"]:
      end_node = g.getNode(end)
      if ignore and end_node == None:
        continue
      dfs = GraphSearch.DFSRec(start_node, end_node)
      print("DFSRec({}, {})  :".format(start, end), nodes_to_val(dfs))
      dfs = GraphSearch.DFSIter(start_node, end_node)
      print("DFSIter({}, {}) :".format(start, end), nodes_to_val(dfs))
    print()