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
  if root:
    curr = root
    while True:
      prev = curr
      if node.value < curr.value:
        curr = getLeft(curr)
        if curr == None:
          prev.left = node
          break
      else:
        curr = getRight(curr)
        if curr == None:
          prev.right = node
          break
    return root
  else:
    return node

def deleteIter(root, value):
  def deleteTwoChildren(node):
      temp = findMinIter(node.right)
      node.value = temp.value
      prev, toBeDeleted = None, node.right
      while True:
        if toBeDeleted.value == temp.value:
          break
        prev = toBeDeleted
        toBeDeleted = getLeft(toBeDeleted)
      if prev:
        prev.left = None
      else:
        node.right = getRight(toBeDeleted) if toBeDeleted.right else None

  if root == None:
    return root

  prev, curr = None, root
  prevHasLeft = False
  while curr != None:
    if curr.value == value:
      break
    prev = curr
    prevHasLeft = value < prev.value 
    if value < curr.value:
      curr = getLeft(curr)
    else:
      curr = getRight(curr) 

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
  
  return root

def getLeft(node):
  node.visits += 1
  return node.left

def getRight(node):
  node.visits += 1
  return node.right