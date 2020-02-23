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
  else:
    root = node

def deleteIter(root, value):
  if root == None:
    return root
  else:
    prev, curr = None, root
    while True:
      if curr.value > value:
        prev = curr
        curr = curr.left
      elif curr.value < value:
        prev = curr
        curr = curr.right
      else:
        if curr.left == curr.right == None:
          if prev == None:
            root = None
          elif prev.left.value == curr.value:
            prev.left = None
          else:
            prev.right = None
        elif curr.left == None:
          if prev == None:
            root = curr.right
          elif prev.left.value == curr.value:
            prev.left = curr.right
          else:
            prev.right = curr.right
        elif curr.right == None:
          if prev == None:
            root = curr.left
          elif prev.left.value == curr.value:
            prev.left = curr.left
          else:
            prev.right = curr.left
        else:
          temp = findMinIter(curr.right)
          curr.value = temp.value
          deleteIter(root, temp.value)
          


def inOrder(root):
  def helper(root):
    if root:
      helper(root.left)
      print(root.value, end= " ")
      helper(root.right)
  helper(root)
  print()

