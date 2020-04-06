from Node import Node
from Graph import Graph
from DirectedGraph import DirectedGraph

class TopSort:

  @staticmethod
  def Kahns(g : DirectedGraph) -> list:
    def initializeInDegreeMap(g : DirectedGraph) -> dict:
      inDegree = {}
      for node in g.vertices:
        inDegree[node] = 0
      
      for node in g.vertices:
        for neighbor in node.neighbors:
          inDegree[neighbor] += 1

      return inDegree

    def addNodesWithoutDependenciesToQueue(inDegree: dict, queue):
      for node in inDegree:
        if inDegree[node] == 0:
          queue.append(node)
          inDegree[node] -= 1
      print(inDegree)

    inDegree = initializeInDegreeMap(g)
    print(inDegree)
    topSort = []
    queue = []
    addNodesWithoutDependenciesToQueue(inDegree, queue)

    while len(queue) > 0:
      curr = queue.pop(0)
      topSort.append(curr)
      for neighbor in curr.neighbors:
        inDegree[neighbor] -= 1
      addNodesWithoutDependenciesToQueue(inDegree, queue)

    return topSort