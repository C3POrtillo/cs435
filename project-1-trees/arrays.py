import random

def getRandomArray(n):
  ret = []
  while len(ret) < n:
    rand = random.randint(-n, n)
    if rand not in ret:
      ret.append(rand)
  return ret

def getSortedArray(n):
  return [x for x in range(n, 0, -1)]

if __name__ == "__main__":
  print(getSortedArray(10))
  print(getRandomArray(10))