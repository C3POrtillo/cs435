class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.height = 1

def findMaxIter(root):
  curr = root
  while curr.right:
    curr = getRight(curr)
  return curr

def findMinIter(root):
  curr = root
  while curr.left:
    curr = getLeft(curr)
  return curr

def findNextIter(root, value):
  if root == None:
    return None
  curr, next = root, None
  while curr:
    if curr.value == value:
      break
    elif curr.value > value:
      next = curr
      curr = getLeft(curr)
    else:
      curr = getRight(curr)
  if curr.right:
    return findMinIter(curr.right)
  return next

def findPrevIter(root, value):
  if root == None:
    return None
  prev, curr = None, root
  while curr:
    if curr.value == value:
      break
    elif curr.value > value:
      curr = getLeft(curr)
    else:
      prev = root
      curr = getRight(curr)
  if curr.left:
    return findMaxIter(curr.left)
  return prev

def insertIter(root, node):
  if root == None:
    return node
  else:
    curr = root
    while curr != None:
      # increment node heights by 1 as needed as the to be inserted node is traveling that path
      prev = curr
      curr = getLeft(curr) if node.value < curr.value else curr.right
      if curr != None:
        curr.height += 1
    
    if node.value < prev.value:
      prev.left = node
    else:
      prev.right = node
  
  setHeight(root)
  return balanceTree(root, node.value)

def deleteIter(root, value):
  def deleteTwoChildren(node):
      temp = findMinIter(node.right)
      node.value = temp.value
      prev, toBeDeleted = None, node.right
      while True:
        if toBeDeleted.value == temp.value:
          break
        prev = toBeDeleted
        toBeDeleted.height -= 1
        toBeDeleted = getLeft(toBeDeleted)
      if prev:
        prev.left = None
      else:
        node.right = toBeDeleted.right if toBeDeleted.right else None
      setHeight(node.right)

  if root == None:
    return root

  prev, curr = None, root
  prevHasLeft = False
  while curr != None:
    # decrement node heights by 1 as needed as the to be deleted node is along this path
    if curr.value == value:
      break
    prev = curr
    prevHasLeft = value < prev.value 
    if value < curr.value:
      curr = getLeft(curr)
    else:
      curr = getRight(curr) 
    if curr != None:
      curr.height -= 1

  if curr == None:
    return root

  if prev:
    # No children
    if curr.left == getRight(curr) == None:
      if prevHasLeft:
        prev.left = None
      else:
        prev.right = None

    # 2 children 
    elif curr.left and curr.right:
      deleteTwoChildren(curr)
    
    # 1 child
    elif curr.left:
      if prevHasLeft:
        prev.left = getLeft(curr)
      else:
        prev.right = getLeft(curr)
    else:
      if prevHasLeft:
        prev.left = getRight(curr)
      else:
        prev.right = getRight(curr)

  else: # deleting root
    # No children
    if curr.left == getRight(curr) == None:
      return None
    # 2 children 
    elif curr.left and curr.right:
      deleteTwoChildren(curr)
    # 1 child
    elif curr.left:
      root = getLeft(curr)
    else:
      root = getRight(curr)

  setHeight(prev)
  setHeight(root)
  return balanceTree(root, value, deletion=True)   

  

def getHeight(root):
  return 0 if root == None else root.height

def setHeight(root):
  if root:
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

def getBalance(root):
  return 0 if root == None else (getHeight(root.left) - getHeight(root.right)) # positive if left taller, negative if right taller

def leftRotate(root):
  right = getRight(root)
  leftSubtree = getLeft(right)
  
  right.left = root
  root.right = leftSubtree

  setHeight(root)
  setHeight(right)

  return right

def rightRotate(root):
  left = getLeft(root)
  rightSubtree = getRight(left)
  
  left.right = root
  root.left = rightSubtree

  setHeight(root)
  setHeight(left)

  return left

def balanceTree(root, value, deletion=False):
  balanceFactor = getBalance(root)

  # LL
  if balanceFactor > 1 and ((deletion and getBalance(root.left) >= 0) or (not deletion and value < root.left.value)):
    return rightRotate(root)
  # RR
  if balanceFactor < -1 and ((deletion and getBalance(root.right) <= 0) or (not deletion and value > root.right.value)):
    return leftRotate(root)
  # LR
  if balanceFactor > 1 and ((deletion and getBalance(root.left) < 0) or (not deletion and value > root.left.value)):
    root.left = leftRotate(root.left)
    return rightRotate(root)
  # RL
  if balanceFactor < -1 and ((deletion and getBalance(root.right) > 0) or (not deletion and value < root.right.value)):
    root.right = rightRotate(root.right)
    return leftRotate(root)

  return root

def getLeft(node):
  node.visits += 1
  return node.left

def getRight(node):
  node.visits +=1
  return node.right