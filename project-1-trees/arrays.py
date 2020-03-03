import random
import sys
def getRandomArray(n):
  ret = []
  while len(ret) < n:
    rand = random.randint(-sys.maxsize, sys.maxsize)
    if rand not in ret:
      ret.append(rand)
  return ret

def getSortedArray(n):
  return [x for x in range(n, 0, -1)]

print(getSortedArray(10))
print(getRandomArray(10))