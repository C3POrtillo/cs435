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
  def delete(node):
    def inOrderHelper(node):
      prev, curr = node, node.right
      while curr.left:
        prev = curr
        curr = curr.left
      if node.left:
        prev.right = curr.right
      else:
        prev.left = curr.right
      node.right = None
      return node

    if node:
      if node.left == node.right == None:
        return None
      if node.left and node.right:
        temp = inOrderHelper(node)
        node.value = temp.value
      elif node.left:
        node = node.left
      else:
        node = node.right
    return node
  if root == None:
    return root
  else:
    prev, curr = None, root
    while True:
      if curr.value == value:
        break

      prev = curr
      if curr.value > value:
        curr = curr.left
      elif curr.value < value:
        curr = curr.right
      
    if prev == None:
      return delete(curr)
    if prev.left:
      prev.left = delete(curr)
    else:
      prev.right = delete(curr)
    return root


def inOrder(root):
  def helper(root):
    if root:
      helper(root.left)
      print(root.value, end= " ")
      helper(root.right)
  helper(root)
  print()

