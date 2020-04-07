from DirectedGraph import DirectedGraph
from Graph import Graph
from GraphSearch import GraphSearch
from WeightedGraph import WeightedGraph
from TopSort import TopSort
from Node import Node
from random import sample, randint
from sys import argv
from math import inf

maxWeight = 100 # for weighted graphs (inclusive)
# Graph sizes for demo's
tiny = 10 
small = 100
medium = 1000
large = 10000

def populateGraph(g : Graph, n : int) -> Graph:
  def addRandomEdges(g : Graph) -> Graph:
    isDAG = isinstance(g, DirectedGraph)
    isWG = isinstance(g, WeightedGraph)

    nodes = sample(g.getAllNodes(), len(g))

    while len(nodes) > 1:
      curr = nodes.pop()

      if isWG:
        for node in g.getAllNodes():
          if node == curr:
            continue
          g.addWeightedEdge(curr, node, randint(1, maxWeight))

      else:
        sampleSet = g.getAllNodes() if not isDAG else nodes
        random_nodes = sample(sampleSet, randint(0, len(sampleSet)))
        for node in random_nodes:
          if isDAG and curr == node:
            continue
          
          if isDAG:
            g.addDirectedEdge(curr, node)
          else:
            g.g.addUndirectedEdge(curr, node)

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
  prev = nodes.pop(0)
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

def dijkstras(start : Node) -> dict:
  def minDist(distances: dict, visited:set) -> Node:
    ans = None
    m = inf
    for curr in distances.keys():
      if curr not in visited and distances[curr] <= m:
        m = distances[curr]
        ans = curr
    return ans

  distanceMap = {start: 0}
  visited = set()
  curr = start
  while curr != None and distanceMap[curr] != inf:
    visited.add(curr)
    
    for neighbor in curr.neighbors:
      distanceMap[neighbor] = distanceMap[curr] + curr.neighbors[neighbor]

    curr = minDist(distanceMap, visited)
  return distanceMap

if __name__ == "__main__":
  try:
    argv[1] = argv[1].lower()
    visualize = False if len(argv) < 3 else argv[2].lower() == "true"
  except:
    print("Missing argument")
    exit()

  if argv[1] == "graph":
    l_10000 = createLinkedList(large, Graph())
    l_100 = createLinkedList(small, Graph())

    print(BFTRecLinkedList(l_10000), end = "\n\n")
    print(BFTRecLinkedList(l_100), end = "\n\n")
    print(BFTIterLinkedList(l_10000))
  elif argv[1] == "directed":
    g = createRandomDAGIter(medium)
    if visualize:
      print(g)
    for func in [TopSort.Kahns, TopSort.mDFS]:
      arr = func(g)
      print(" Node Count: {} | {}".format(len(arr), arr))
  elif argv[1] == "weighted":
    for g in [createLinkedList(small, WeightedGraph()), createRandomCompleteWeightedGraph(small)]:
      if visualize:
        print(g)
      n = g.getNode(str(randint(0, small-1)))
      print("Dijkstras Map for Node {}: {}".format(n, dijkstras(n)))
      print()
  else:
    print("Invalid argument")
