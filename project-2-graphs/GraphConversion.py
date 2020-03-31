from Graph import Graph

def readable_edges(g : Graph):
  nodes = g.getAllNodes()
  ret = {}
  for key in sorted(nodes):
    ret[key.val] = nodes_to_val(key.neighbors)
  return ret

def nodes_to_val(nodes):
  try:
    return [node.val for node in nodes]
  except:
    return nodes
