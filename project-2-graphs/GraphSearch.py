from Nodes import Node
from Graph import Graph

class GraphSearch:

  @staticmethod
  def DFSRec(start : Node, end : Node) -> list:
    def helper(start : Node, end : Node, visited : list) -> list:
      
      visited.append(start)

      if end in visited:
        return visited

      for node in start.neighbors:
        if node not in visited:
          if helper(node, end, visited):
            return visited

    if start == None or end == None:
      return None

    return helper(start, end, [])

  @staticmethod
  def DFSIter(start : Node, end : Node) -> list:

    if start == None or end == None:
      return None

    visited = []
    stack = [start]

    while len(stack) != 0:

      curr = stack.pop()
      if curr not in visited:
        visited.append(curr)

      if end in visited:
        return visited

      n = len(stack)
      for node in curr.neighbors:
        if node not in visited:
          stack.insert(n, node)

  @staticmethod
  def BFTRec(graph: Graph) -> list:
    def helper(queue : list, visited : list) -> list:

      if len(queue) == 0:
        return visited

      curr = queue.pop(0)

      exhaust = True
      for node in curr.neighbors:
        if node not in visited:
          queue.append(node)
          visited.append(node)
          if node in nodes:
            nodes.remove(node)
          exhaust = False

      # Graph is disconnected and unvisited nodes exist
      if exhaust and len(nodes) != 0 and len(visited) < len(graph):
        queue.append(nodes.pop())

      return helper(queue, visited)

    nodes = graph.getAllNodes()
    start = nodes.pop()
    return helper([start], [start])

  @staticmethod
  def BFTIter(graph : Graph) -> list:

    nodes = graph.getAllNodes()
    start = nodes.pop()
    queue = [start]
    visited = [start]

    while len(queue) != 0:

      curr = queue.pop(0)

      exhaust = True
      for node in curr.neighbors:
        if node not in visited:
          queue.append(node)
          visited.append(node)
          if node in nodes:
            nodes.remove(node)
          exhaust = False

      # Graph is disconnected and unvisited nodes exist
      if exhaust and len(nodes) != 0 and len(visited) < len(graph):
        queue.append(nodes.pop())

    return visited