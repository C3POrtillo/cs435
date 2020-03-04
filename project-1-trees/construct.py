from BBST import BBST
from BST import BST_Rec, BST_Iter
from Node import Node
from arrays import getRandomArray, getSortedArray
from traversals import *

random_input = getRandomArray(10000)
sorted_input = getSortedArray(10000)

bbst = None
bst_rec = None
bst_iter = None
try:
  print("Inserting 10000 elements")

  for i in range(len(random_input)):
    val = random_input[i]
    bbst = BBST.insertIter(bbst, Node(val))
    bst_rec = BST_Rec.insertRec(bst_rec, Node(val))
    bst_iter = BST_Iter.insertIter(bst_iter, Node(val))

except:
  pass

bbst = None
bst_rec = None
bst_iter = None
print("Error after inserting {} nodes".format(i))
print()
print("Inserting 10 elements from random")
for i in random_input[:10]:
  bbst = BBST.insertIter(bbst, Node(i))
  bst_rec = BST_Rec.insertRec(bst_rec, Node(i))
  bst_iter = BST_Iter.insertIter(bst_iter, Node(i))

print("BBST {} traversals: ".format(countTraversals(bbst)), end = "")
preOrder(bbst, debug=True)

print("BST {} traversals: ".format(countTraversals(bst_iter)), end = "")
preOrder(bst_iter, debug=True )



bbst = None
bst_rec = None
bst_iter = None
print()
print("Inserting 10 elements from sorted")
for i in sorted_input[:10]:
  bbst = BBST.insertIter(bbst, Node(i))
  bst_iter = BST_Iter.insertIter(bst_iter, Node(i))

print("BBST {} traversals: ".format(countTraversals(bbst)), end = "")
preOrder(bbst, debug=True)

print("BST {} traversals: ".format(countTraversals(bst_iter)), end = "")
preOrder(bst_iter, debug=True )



