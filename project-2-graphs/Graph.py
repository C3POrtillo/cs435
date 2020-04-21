from Nodes import Node
class Graph:

  def __init__(self):
    self.vertices = {}

  def addNode(self, nodeVal):
    if not isinstance(nodeVal, Node):
      nodeVal = Node(nodeVal)
    self.vertices[nodeVal] = nodeVal.neighbors = set()

  def addUndirectedEdge(self, first : Node, second : Node):
    if not self.nodeExists(first):
      self.addNode(first)
    if not self.nodeExists(second):
      self.addNode(second)
    self.vertices[first].add(second)
    self.vertices[second].add(first)

  def removeUndirectedEdge(self, first : Node, second : Node):
    if self.nodeExists(first) and self.nodeExists(second) and second in self.vertices[first]:
      self.vertices[first].remove(second)
      self.vertices[second].remove(first)

  def getAllNodes(self) -> set:
    return set(self.vertices.keys())

  def getNode(self, nodeVal) -> Node:
    for node in self.vertices:
      if node.val == str(nodeVal):
        return node

  def nodeExists(self, n : Node) -> bool:
    return n in self.vertices

  @staticmethod
  def iterToJSONStringify(x) -> str:
    """Convert an iterable to a JSON parseable value"""
    if not isinstance(x, dict):
      if len(x) == 0:
        return []
      ret = "["
      x = list(x)
      prev = None
      for curr in x:
        if prev:
          ret += "\"{}\",".format(prev)
        prev = curr
      if curr:
        ret += "\"{}\"".format(curr)
      ret += "]"
      return ret
    else:
      if len(x) == 0:
        return {}
      ret = "{"
      prev = None
      weightedStr = "\"{}\": {}"
      for key in sorted(x.keys()):
        if prev:
          ret += weightedStr.format(prev, x[prev])
          ret += ", "
        prev = key
      if key:
        ret += weightedStr.format(key, x[key])
      ret += "}"
      return ret

  def __str__(self) -> str:
    """Creates a JSON string representation of vertices and their edges"""

    sortedNodes = sorted(self.getAllNodes())
    nodeFormat = "\t\"{}\": {}"
    ret = "{\n"
    prev = sortedNodes[0]
    for curr in sortedNodes[1:]:
      ret += nodeFormat.format(prev, Graph.iterToJSONStringify(self.vertices[prev]))
      ret += ",\n"
      prev = curr
    if curr:
     ret += nodeFormat.format(curr, Graph.iterToJSONStringify(self.vertices[prev]))
    ret += "\n}"
    return ret

  
  def __repr__(self) -> str:
    return "".join(self.__str__().split())

  def __len__(self):
    return len(self.vertices)