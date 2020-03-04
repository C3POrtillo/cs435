def inOrder(root, debug=False, levels=False):
  def helper(root, str):
    if root:
      helper(root.left, str + "l")
      print("{} {}".format(root.value, str if debug else ""), end = " | " if debug else " ")
      helper(root.right, str + "r")
  helper(root, "h")
  print()

def preOrder(root, debug=False): 
  def helper(root, str):
    if root:
      print("{} {}".format(root.value, str if debug else ""), end = " | " if debug else " ")
      helper(root.left, str + "l")
      helper(root.right, str + "r")
  helper(root, "h")
  print()

def countTraversals(root):
  if root:
    ret = root.visits
    ret += countTraversals(root.left)
    ret += countTraversals(root.right)
    return ret
  return 0
