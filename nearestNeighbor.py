import operator, time, math
from euclidean import *

def nearestNeighbor(graph, nameArray):
  startTime = time.time()
  cost = 0.0
  path = [0]
  wg = weightedGraph(graph)
  iterations = 0
  for i in range(1, len(graph)):
    min = 999999.9
    next = 0
    for node in range(1, len(graph)):
      iterations += 1
      prev = path[0]
      if path.count(node) == 0 and wg[prev][node] < min:
        next = node
        min = wg[prev][node]
    cost += min
    path = operator.iadd([next], path)
  
  pathString = ""
  pathString += nameArray[path[len(path)-1]] + " -> "
  adjCost = cost + wg[path[0]][0]
  endTime = time.time() - startTime
  for i in range(0, len(path)-1):
    pathString += nameArray[path[i]] + " -> "
  pathString += nameArray[path[len(path)-1]]
  graphSize = len(graph)
  line1 = "\n\nThe optimal path in this {}-city instance using Nearest Neighbor is: \n{}\n\n".format(graphSize, pathString)
  line2 = "This path costs {} units, and required {} iterations in {} seconds \n(running in (n - 1)^2 = n^2 time, where n is the number of cities)\n\n".format(adjCost, iterations, endTime)
  print(line1 + line2)
  
  return path