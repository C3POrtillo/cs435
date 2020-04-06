from DirectedGraph import DirectedGraph
from Graph import Graph
from GraphSearch import GraphSearch
from GraphConversion import nodes_to_val
from random import sample, randint
from sys import argv

def populateGraph(g : Graph, n : int) -> Graph:
  def randomEdges(g : Graph) -> Graph:
    if isinstance(g, DirectedGraph):
      addEdge = g.addDirectedEdge
    else:
      addEdge = g.addUndirectedEdge

    n = len(g)
    nodes = sample(g.getAllNodes(), n) # randomize input

    while len(nodes) > 1:
      curr = nodes.pop()
      random_nodes = sample(g.getAllNodes(), randint(0, n)) # random sample of 0 to n nodes
      for node in random_nodes:
        addEdge(curr, node)
        
    return g

  if g == None:
    g = Graph()

  for i in range(n):
    g.addNode(i)

  g = randomEdges(g)
  return g


def createRandomUnewightedGraphIter(n : int) -> Graph:
  return populateGraph(Graph(), n)

def createRandomDAGIter(n : int) -> DirectedGraph:
  return populateGraph(DirectedGraph(), n)

def createLinkedList(n : int) -> Graph:
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

def BFTRecLinkedList(graph : Graph) -> list:
  try:
    return GraphSearch.BFTRec(graph)
  except Exception as e:
    return e

def BFTIterLinkedList(graph : Graph) -> list:
  try:
    return GraphSearch.BFTIter(graph)
  except Exception as e:
    return e

if __name__ == "__main__":
  try:
    argv[1] = argv[1].lower()
    if argv[1] == "graph":
      l_10000 = createLinkedList(10000)
      l_100 = createLinkedList(100)

      print(nodes_to_val(BFTRecLinkedList(l_10000)), end = "\n\n")
      print(nodes_to_val(BFTRecLinkedList(l_100)), end = "\n\n")
      print(nodes_to_val(BFTIterLinkedList(l_10000)))
    elif argv[1] == "directed":
      pass
    else:
      print("Invalid argument")
  except:
    print("Missing argument")
