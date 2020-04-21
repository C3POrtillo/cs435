from DirectedGraph import DirectedGraph

class TopSort:

  @staticmethod
  def initializeInDegreeMap(graph : DirectedGraph) -> dict:
    inDegree = {}
    for node in graph.getAllNodes():
      inDegree[node] = 0
    
    for node in graph.getAllNodes():
      for neighbor in node.neighbors:
        inDegree[neighbor] += 1

    return inDegree

  @staticmethod
  def addNodesWithoutDependencies(inDegree: dict, queue):
    for node in inDegree:
      if inDegree[node] == 0:
        queue.append(node)
        inDegree[node] -= 1

  @staticmethod
  def Kahns(graph : DirectedGraph) -> list:
    
    inDegree = TopSort.initializeInDegreeMap(graph)
    topSort = []

    queue = []
    TopSort.addNodesWithoutDependencies(inDegree, queue)
    while len(queue) > 0:
      curr = queue.pop(0)
      topSort.append(curr)
      
      for neighbor in curr.neighbors:
        inDegree[neighbor] -= 1
      TopSort.addNodesWithoutDependencies(inDegree, queue)

    return topSort

  @staticmethod
  def mDFS(graph: DirectedGraph) ->list:
    topSort = []
    visited = set()
    
    for node in graph.getAllNodes():
      stack = [node]
      while len(stack) != 0:
        curr = stack.pop()

        if curr not in visited:
          visited.add(curr)

        n = len(stack)
        for neighbor in node.neighbors:
          if neighbor not in visited:
            stack.insert(n, neighbor)

      topSort.append(node)

    return topSort[::-1]