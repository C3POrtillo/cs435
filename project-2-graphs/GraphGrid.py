from Graph import Graph
from Nodes import GridNode

class GraphGrid(Graph):

  def __init__(self):
    super().__init__()
    self.minX = self.maxX = 0
    self.minY = self.maxY = 0

  def addNode(self, nodeVal):
    self.addGridNode(0, 0, nodeVal)

  def addGridNode(self, x : int, y : int, nodeVal):
    if not isinstance(nodeVal, GridNode):
      nodeVal = GridNode(x, y, nodeVal)
    self.updateSize(x, y)
    self.vertices[nodeVal] = nodeVal.neighbors = set()

  def addUndirectedEdge(self, first : GridNode, second : GridNode):
    if self.isNeighbor(first, second):
      super().addUndirectedEdge(first, second)

  def removeUndirectedEdge(self, first : GridNode, second : GridNode):
    super().removeUndirectedEdge(first, second)

  def isNeighbor(self, first : GridNode, second : GridNode):
    if self.nodeExists(first) and self.nodeExists(second):
      xDist = abs(first.x - second.x)
      yDist = abs(first.y - second.y)
      return (xDist**2 + yDist**2) == 1 # a^2 + b^2 = c^2, valid only for 1 + 0 or 0 + 1
    else:
      return False

  def updateSize(self, x, y):
    if x < self.minX:
      self.minX = x
    elif x > self.maxX:
      self.maxX = x
    
    if y < self.minY:
      self.minY = y
    elif y > self.maxY:
      self.maxY = y

  def __str__(self):
    """Creates a string representation of the grid with paths"""
    sortedNodes = sorted(self.getAllNodes())
    xlen = abs(self.maxX - self.minX) + 1
    ylen = abs(self.maxY - self.minY) + 1
    graphArr = [["" for col in range(xlen)] for row in range(ylen)]
    pad = 3
    for node in sortedNodes:
      graphArr[node.y][node.x] = node
      l = len(str(node))
      if l > pad:
        pad = l

    ret = []
    horiF = "{} {} {}"
  
  
    for row in range(xlen):
      hori = ""
      vert = ""
      for curr in graphArr[row]:
        left = " "
        up = " "
        right = " "
        for neighbor in curr.neighbors:
          xDist = curr.x - neighbor.x
          yDist = abs(curr.y - neighbor.y)
          if yDist == 1:
            up = "|"
          elif xDist == 1:
            left = "-"
          elif xDist == -1:
            right = "-"
        hori += horiF.format(left, str(curr).center(pad), right)
        vert += up.center(pad + 4)
      ret.append(hori)
      if(row < xlen - 1):
        ret.append(vert)
    return "\n".join(ret[::-1])
    
  def __repr__(self):
    return "".join(super().__str__().split())
      