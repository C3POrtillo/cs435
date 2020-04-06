from Node import Node
class Graph:

  def __init__(self):
    self.vertices = {}

  def __len__(self):
    return len(self.vertices)

  def addNode(self, node):
    if not isinstance(node, Node):
      node = Node(node)
    self.vertices[node] = node.neighbors = set()

  def addUndirectedEdge(self, first : Node, second : Node):

    if first not in self.vertices:
      self.addNode(first)
    if second not in self.vertices:
      self.addNode(second)

    self.vertices[first].add(second)
    self.vertices[second].add(first)

  def removeUndirectedEdge(self, first : Node, second : Node):
    if first in self.vertices and second in self.vertices[first]:
      self.vertices[first].remove(second)

    if second in self.vertices and first in self.vertices[second]:
      self.vertices[second].remove(first)

  def getAllNodes(self) -> set:
    return set(self.vertices.keys())

  def getNode(self, nodeVal) -> Node:
    for node in self.vertices:
      if node.val == str(nodeVal):
        return node

  def __str__(self) -> str:
    """Creates a JSON string representation of vertices and their edges"""
    def iterToJSONStringify(x) -> str:
      """Convert an array to a JSON parseable value"""
      try:
        x = list(x)
        ret = "["
        prev = x[0]
        for curr in x[1:]:
          ret += "\"{}\",".format(prev)
          prev = curr
        if curr:
          ret += "\"{}\"".format(curr)
        ret += "]"
        return ret
      except:
        return []

    sortedNodes = sorted(self.getAllNodes())
    nodeFormat = "\t\"{}\": {}"
    ret = "{\n"
    prev = sortedNodes[0]
    for curr in sortedNodes[1:]:
      ret += nodeFormat.format(prev, iterToJSONStringify(self.vertices[prev]))
      ret += ",\n"
      prev = curr
    if curr:
     ret += nodeFormat.format(curr, iterToJSONStringify(self.vertices[prev]))
    ret += "\n}"
    return ret

  def __repr__(self) -> str:
    return "".join(self.__str__().split())