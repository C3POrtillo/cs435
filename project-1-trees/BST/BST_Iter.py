def findMaxIter(root):
  curr = root
  while curr.right:
    curr = curr.right
  return curr

def findMinIter(root):
  curr = root
  while curr.left:
    curr = curr.left
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
      curr = curr.left
    else:
      curr = curr.right
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
      curr = curr.left
    else:
      prev = root
      curr = curr.right
  if curr.left:
    return findMaxIter(curr.left)
  return prev

def insertIter(root, node):
  if root:
    curr = root
    while True:
      prev = curr
      if node.value < curr.value:
        curr = curr.left
        if curr == None:
          prev.left = node
          break
      else:
        curr = curr.right
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
        toBeDeleted = toBeDeleted.left
      if prev:
        prev.left = None
      else:
        node.right = toBeDeleted.right if toBeDeleted.right else None

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
      curr = curr.left
    else:
      curr = curr.right 

  if curr == None:
    return root

  if prev:
    # No children
    if curr.left == curr.right == None:
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
        prev.left = curr.left
      else:
        prev.right = curr.left
    else:
      if prevHasLeft:
        prev.left = curr.right
      else:
        prev.right = curr.right

  else: # deleting root
    # No children
    if curr.left == curr.right == None:
      return None
    # 2 children 
    elif curr.left and curr.right:
      deleteTwoChildren(curr)
    # 1 child
    elif curr.left:
      root = curr.left
    else:
      root = curr.right
  
  return root

def sort(root):
  def helper(root):
    if root:
      helper(root.left)
      print(root.value, end= " ")
      helper(root.right)
  helper(root)
  print()

