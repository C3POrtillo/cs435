def findMaxRec(root):
  if root.right == None:
    return root
  return findMaxRec(root.right)

def findMinRec(root):
  if root.left == None:
    return root
  return findMinRec(root.left)
  
def findNextRec(root, value):
  def findNext(root, next, value):
    if root == None:
      return None
    if root.value == value:
      if root.right:
        return findMinRec(root.right)
    elif root.value > value:
      return findNext(root.left, root, value)
    else:
      return findNext(root.right, next, value)
    return next
  return findNext(root, None, value)

def findPrevRec(root, value):
  def findPrev(root, prev, value):
    if root == None:
      return None
    if root.value == value:
      if root.left:
        return findMaxRec(root.left)
    elif root.value > value:
      return findPrev(root.left, prev, value)
    else:
      return findPrev(root.right, root, value)
    return prev
  return findPrev(root, None, value)

def insertRec(root, node):
  if root:
    if root.value < node.value:
      if root.right: 
        insertRec(root.right, node)
      else:
        root.right = node
    else:
      if root.left:
        insertRec(root.left, node)
      else:
        root.left = node
  else:
    root = node

def deleteRec(root, value):
  if root == None:
    return root
  if root.value > value:
    root.left = deleteRec(root.left, value)
  elif root.value < value:
    root.right = deleteRec(root.right, value)
  else:
    if root.right == None:
      return root.left
    if root.left == None:
      return root.right
    temp = findMinRec(root.right)
    root.value = temp.value
    root.right = deleteRec(root.right, temp.value)
  return root

def inOrder(root):
  def helper(root):
    if root:
      helper(root.left)
      print(root.value, end= " ")
      helper(root.right)
  helper(root)
  print()

