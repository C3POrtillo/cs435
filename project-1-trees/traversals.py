def sorted(root):
  inOrder(root)

def inOrder(root, output=True):
  curr = root
  stack = []
  ret = 0
  while True:
    if curr:
      stack.append(curr)
      curr = curr.left
    elif stack:
      curr = stack.pop()
      if output:
        print(root.value, end=" ")
      ret += root.value
      curr = curr.right
    else:
      break
  if output:
    print()
  return ret