from Main import createLinkedList, createRandomUnewightedGraphIter, GraphSearch
from GraphConversion import *

ignore = True # To ignore invalid paths where a node does not exist

r = createRandomUnewightedGraphIter(50) # random
l = createLinkedList(25) # worst case
x = Graph() # disconnected

x.addNode("a")
x.addNode("b")
x.addNode("c")
x.addNode("d")
x.addUndirectedEdge(x.getNode("a"), x.getNode("b"))
x.addUndirectedEdge(x.getNode("c"), x.getNode("d"))

for g in [r, l, x]:
  
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