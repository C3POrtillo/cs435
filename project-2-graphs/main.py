from DirectedGraph import DirectedGraph
from Graph import Graph
from GraphSearch import GraphSearch
from WeightedGraph import WeightedGraph
from TopSort import TopSort
from random import sample, randint
from sys import argv

maxWeight = 100 # for weighted graphs (inclusive)

def populateGraph(g : Graph, n : int) -> Graph:
  def addRandomEdges(g : Graph) -> Graph:
    isDAG = isinstance(g, DirectedGraph)
    isWG = isinstance(g, WeightedGraph)

    if isDAG:
      addEdge = g.addDirectedEdge
    else:
      addEdge = g.addUndirectedEdge

    n = len(g)
    nodes = sample(g.getAllNodes(), n)

    while len(nodes) > 1:
      curr = nodes.pop()
      sampleSet = g.getAllNodes() if not isDAG else nodes
      random_nodes = sample(sampleSet, randint(0, len(sampleSet)))
      for node in random_nodes:
        if (isDAG) and curr == node:
          continue
        if isWG:
          g.addWeightedEdge(curr, node, randint(1, maxWeight))
        else:
          addEdge(curr, node)


  if g == None:
    g = Graph()

  for i in range(n):
    g.addNode(i)

  addRandomEdges(g)
  return g

def createRandomUnewightedGraphIter(n : int) -> Graph:
  return populateGraph(Graph(), n)

def createRandomDAGIter(n : int) -> DirectedGraph:
  return populateGraph(DirectedGraph(), n)

def createRandomCompleteWeightedGraph(n : int) -> Graph:
  return populateGraph(WeightedGraph(), n)

def createLinkedList(n : int, g : Graph) -> Graph:
  isWG = isinstance(g, WeightedGraph)
  if len(g) != 0: # Create new graph if input is not empty
    g = WeightedGraph() if isWG else Graph()

  for i in range(n):
    g.addNode(i)

  nodes = sorted(g.getAllNodes())
  prev = nodes.pop()
  while len(nodes) != 0:
    curr = nodes.pop()
    if isWG:
      g.addWeightedEdge(prev, curr, 1)
    else:
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
  except:
    print("Missing argument")
    exit()

  if argv[1] == "graph":
    l_10000 = createLinkedList(10000, Graph())
    l_100 = createLinkedList(100, Graph())

    print(BFTRecLinkedList(l_10000), end = "\n\n")
    print(BFTRecLinkedList(l_100), end = "\n\n")
    print(BFTIterLinkedList(l_10000))
  elif argv[1] == "directed":
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
    print(x)
    print()
    for func in [TopSort.Kahns, TopSort.mDFS]:
      arr = func(x)
      print("Node Count: {} | {}".format(len(arr), arr))
    print()
  elif argv[1] == "weighted":
    x = createLinkedList(10, WeightedGraph())
    print(x)
  else:
    print("Invalid argument")
