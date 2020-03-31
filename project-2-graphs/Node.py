class Node:

  def __init__(self, val):
    self.val = str(val)

  def __lt__(self, other):
    return self.val < other.val

  def __le__(self, other):
    return self.val <= other.val

  def __gt__(self, other):
    return self.val > other.val

  def __ge__(self, other):
    return self.val >= other.val

