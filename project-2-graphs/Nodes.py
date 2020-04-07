class Node:

  def __init__(self, val):
    self.val = str(val)

  def __lt__(self, other) -> bool:
    try:
      return int(self.val) < int(other.val)
    except:
      return self.val < other.val

  def __le__(self, other) -> bool:
    try:
      return int(self.val) <= int(other.val)
    except:
      return self.val <= other.val

  def __gt__(self, other) -> bool:
    try:
      return int(self.val) > int(other.val)
    except:
      return self.val > other.val

  def __ge__(self, other) -> bool:
    try:
      return int(self.val) >= int(other.val)
    except:
      return self.val >= other.val

  def __str__(self) -> str:
    return str(self.val)

  def __repr__(self) -> str:
    return self.__str__()

class GridNode(Node):
  def __init__(self, x, y, val):
    super().__init__(val)
    self.x = x
    self.y = y