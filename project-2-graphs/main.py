from DirectedGraph import DirectedGraph
from Graph import Graph
from GraphSearch import GraphSearch
from GridGraph import GridGraph
from WeightedGraph import WeightedGraph
from TopSort import TopSort
from Nodes import Node, GridNode
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

    def addWeightedEdges(curr, g : Graph):
      for node in g.getAllNodes():
        if node == curr:
          continue
        g.addWeightedEdge(curr, node, randint(1, maxWeight))

    def addUnweightedEdges(curr, g : Graph, isDAG):
      sampleSet = g.getAllNodes() if not isDAG else nodes
      random_nodes = sample(sampleSet, randint(0, len(sampleSet)))
      for node in random_nodes:
        if isDAG:
          if curr == node:
            continue
          g.addDirectedEdge(curr, node)

        else:
          g.g.addUndirectedEdge(curr, node)

    isWG = isinstance(g, WeightedGraph)
    isDAG = isinstance(g, DirectedGraph)
    nodes = g.getAllNodes()

    while len(nodes) > 1:
      curr = nodes.pop()

      if isWG:
        addWeightedEdges(curr, g)
      else:
        addUnweightedEdges(curr, g, isDAG)

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

def createRandomGridGraph(n : int) -> GridGraph:
  g = GridGraph()
  for row in range(n):
    for col in range(n):
      g.addGridNode(col, row, "{},{}".format(col, row))
  nodes = g.getAllNodes()
  while len(nodes) > 1:
    curr = nodes.pop()
    sampleSet = g.getAllNodes()
    for node in sampleSet:
      if not g.isNeighbor(curr, node):
        continue
      coin = randint(0,1)
      if coin == 1:
        g.addUndirectedEdge(curr, node)

  return g
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
    for curr in distances:
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
      if neighbor not in visited:
        if neighbor in distanceMap:
          g = distanceMap[curr] + curr.neighbors[neighbor]
          if  g < distanceMap[neighbor]:
            distanceMap[neighbor] = g
        else:
          distanceMap[neighbor] = distanceMap[curr] + curr.neighbors[neighbor]

    curr = minDist(distanceMap, visited)
  return distanceMap

def astar(sourceNode : GridNode, destNode : GridNode) -> list:
  def manhattan(curr : GridNode, destNode : GridNode):
    xDist = abs(curr.x - destNode.x)
    yDist = abs(curr.y - destNode.y)
    return xDist + yDist

  def minDist(distances: dict, visited:set) -> Node:
    ans = None
    m = inf

    for curr in distances:
      if curr not in visited and sum(distances[curr]) <= m:
        m = sum(distances[curr])
        ans = curr
    return ans

  distanceMap = {sourceNode : (0, manhattan(sourceNode, destNode))}
  visited = []
  curr = sourceNode

  while curr != None and curr != destNode:
    if curr not in visited:
      visited.append(curr)

    for neighbor in curr.neighbors:
      if neighbor not in visited:
        if neighbor in distanceMap:
          g = distanceMap[curr][0] + 1
          if g < distanceMap[neighbor][0]:
            distanceMap[neighbor][0] = g
        else:
          g = distanceMap[curr][0] + 1
          h = manhattan(neighbor, destNode)
          distanceMap[neighbor] = [g, h]

    curr = minDist(distanceMap, visited)
  visited.append(curr)
  return visited

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
  elif argv[1] == "grid":
    dim = small
    g = createRandomGridGraph(dim)
    if visualize:
      print(g)
    sourceNode = g.graphToArr()[0][0]
    destNode = g.graphToArr()[dim-1][dim-1]
    print(astar(sourceNode, destNode))
  else:
    print("Invalid argument")
