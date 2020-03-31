from Graph import Graph
from GraphSearch import GraphSearch
from GraphConversion import nodes_to_val
from random import sample, randint

def createRandomUnewightedGraphIter(n : int):
  g = Graph()
  for i in range(n):
    g.addNode(i)

  nodes = sample(g.getAllNodes(), n)

  prev = None
  while len(nodes) > 1:
    curr = nodes.pop()
    if prev:
      g.addUndirectedEdge(prev, curr)
    
    node_count = randint(1, len(nodes))
    random_nodes = sample(nodes, node_count)

    for node in random_nodes:
      g.addUndirectedEdge(curr, node)
    random_nodes.append(curr)

    prev = random_nodes[randint(0, node_count)]
  return g

def createLinkedList(n : int):
  g = Graph()
  for i in range(n):
    g.addNode(i)
  nodes = g.getAllNodes()
  prev = nodes.pop()
  while len(nodes) != 0:
    curr = nodes.pop()
    g.addUndirectedEdge(prev, curr)
    prev = curr
  return g

def BFTRecLinkedList(graph : Graph):
  try:
    return GraphSearch.BFTRec(graph)
  except Exception as e:
    return e

def BFTIterLinkedList(graph : Graph):
  try:
    return GraphSearch.BFTIter(graph)
  except Exception as e:
    return e

if __name__ == "__main__":
  l_10000 = createLinkedList(10000)
  l_100 = createLinkedList(100)

  print(nodes_to_val(BFTRecLinkedList(l_10000)), end = "\n\n")
  print(nodes_to_val(BFTRecLinkedList(l_100)), end = "\n\n")
  print(nodes_to_val(BFTIterLinkedList(l_10000)))
