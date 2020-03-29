from BBST import BBST
from BST import BST_Iter
from Node import Node
from Arrays import getRandomArray, getSortedArray
from time import time

random_input = getRandomArray(10000)
sorted_input = getSortedArray(10000)
def insert(root, arr_input, balanced=False):
  for i in arr_input:
    if balanced:
      root = BBST.insertIter(root, Node(i))
    else:
      root = BST_Iter.insertIter(root, Node(i))
  return root

def deletion(root, arr_input, balanced=False):
  for i in arr_input:
    if balanced:
      root = BBST.deleteIter(root, i)
    else:
      root = BST_Iter.deleteIter(root, i)
  return root

s = ["random", "sorted"]
x = [random_input, sorted_input]

for i in range(2):
  bbst = None
  bst = None
  storage = [ [bbst, True], [bst, False] ]
  print("Inserting 10000 elements from {}".format(s[i]))
  for data in storage:
    start = time()
    data[0] = insert(data[0], x[i], balanced=data[1])
    end = time()
    struct = "BBST" if data[1] else "BST"
    print("{} Elapsed Time: {}".format(struct, end - start))

  print("Deleting 10000 elements from {}".format(s[i]))
  for data in storage:
    start = time()
    data[0] = deletion(data[0], x[i], balanced=data[1])
    end = time()
    struct = "BBST" if data[1] else "BST"
    print("{} Elapsed Time: {}".format(struct, end - start))

