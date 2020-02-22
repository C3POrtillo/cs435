class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def findMaxRec(root):
  if root.right == None:
    return root
  return findMaxRec(root.right)

def findMinRec(root):
  if root.left == None:
    return root
  return findMinRec(root.left)
  
def findNextRec(root, value):
  def findNext(root, succ, value):
    if root == None:
      return None
    if root.value == value:
      if root.right:
        return findMinRec(root.right)
    elif root.value > value:
      return findNext(root.left, root, value)
    else:
      return findNext(root.right, succ, value)
    return succ
  return findNext(root, None, value)

def findPrevRec(root, value):
  def findPrev(root, pred, value):
    if root == None:
      return None
    if root.value == value:
      if root.left:
        return findMaxRec(root.left)
    elif root.value > value:
      return findPrev(root.left, pred, value)
    else:
      return findPrev(root.right, root, value)
    return pred
  return findPrev(root, None, value)

def insert(root, node):
  if root:
    if root.value < node.value:
      if root.right: 
        insert(root.right, node)
      else:
        root.right = node
    else:
      if root.left:
        insert(root.left, node)
      else:
        root.left = node
  else:
    root = node

def delete(root, value):
  if root == None:
    return root
  if value < root.value:
    root.left = delete(root.left, value)
  elif value > root.value:
    root.right = delete(root.right, value)
  else:
    if root.left == None:
      root = root.right
      return root
    elif root.right == None:
      root = root.left
      return root
    temp = findMinRec(root.right)
    root.key = temp.key
    root.right = delete(root.right, temp.key)
  return root

def inOrder(root):
  if root:
    inOrder(root.left)
    print(root.value, end= " ")
    inOrder(root.right)

