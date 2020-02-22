class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class CompleteTree:
  
  def __init__(self, root):
    self.root = root
    
  def fromArray(self, aList):
    def helper(self, aList, root, i, size):
      if i < size:
        node = Node(aList[i])
        root = node
        root.left = helper(arr, root.left, 2 * i + 1, size)
        root.right = helper(arr, node.left, 2 * i + 2, size)

    # TODO
    
  def isBST(self):
    # TODO
    return True
    
  def preOrder(self):
    def helper(node, ret):
      return ret + [node.value, helper(node.left, []), helper(node.right, [])]
    return helper(self.root, [])
    
  def postOrder(self):
    def helper(self, node, ret):
      return ret + [helper(node.left, []), helper(node.right, []), node.value]
    return helper(rself.oot, [])
    
  def numNodesInLookup(self, value):
    def helper(self, node, value, count):
      if node.value == value:
        return count
      
      if(node.left):
        helper(node.left, value, count + 1)

      if(node.right):
        helper(node.right, value, count + 1)
        
      return -1
    return helper(value, root, 0)
