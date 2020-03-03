import sys

from BBST import BBST
from BST import BST_Rec, BST_Iter, BST_Node

from arrays import *

input = getRandomArray(10000)
bbst = None
bst_rec = None
bst_iter = None
try:
  print("Inserting 10000 elements")

  for i in input:
    bbst = BBST.insertIter(bbst, BBST.Node(i))
    bst_rec = BST_Rec.insertRec(bst_rec, BST_Node.Node(i))
    bst_iter = BST_Iter.insertIter(bst_iter, BST_Node.Node(i))

except:
  bbst = None
  bst_rec = None
  bst_iter = None
  print("Error after inserting node with value: {}".format(i))
  print()
  print("Inserting 10 elements")
  for i in input[:10]:
    bbst = BBST.insertIter(bbst, BBST.Node(i))
    bst_rec = BST_Rec.insertRec(bst_rec, BST_Node.Node(i))
    bst_iter = BST_Iter.insertIter(bst_iter, BST_Node.Node(i))

print("Sorted Input (first 10 elements): ", end = "")
print(sorted(input[:10]))
print("BBST: ", end = "")
BBST.inOrder(bbst)
print("BST Rec: ", end = "")
BST_Rec.sort(bst_rec)
print("BST Iter: ", end = "")
BST_Iter.sort(bst_iter)