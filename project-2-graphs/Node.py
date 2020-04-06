class Node:

  def __init__(self, val):
    self.val = str(val)

  def __lt__(self, other) -> bool:
    return self.val < other.val

  def __le__(self, other) -> bool:
    return self.val <= other.val

  def __gt__(self, other) -> bool:
    return self.val > other.val

  def __ge__(self, other) -> bool:
    return self.val >= other.val

  def __str__(self) -> str:
    return str(self.val)

  def __repr__(self) -> str:
    return self.__str__()