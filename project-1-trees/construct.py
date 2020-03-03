import sys

from BBST import BBST
from BST import BST_Rec, BST_Node

from arrays import getRandomArray

input = getRandomArray(10000)

bbst = None
bst = None
for i in input:
  bbst = BBST.insertIter(bbst, BBST.Node(i))
  BST_Rec.insertRec(bst, BST_Node.Node(i))
