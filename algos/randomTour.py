import operator, time, math, random
from algos.euclidean import *

def randomTour(graph, nameArray):
  startTime = time.time()
  path = []
  cost = 0.0
  wg = weightedGraph(graph)
  nodes = []

  for i in range(0, len(graph)):
    nodes.append(i)
  
  for i in range(0, len(graph)):
    randNode = random.choice(nodes)
    path.append(randNode)
    nodes.remove(randNode)
  
  path.append(path[0])

  for i in range(0, len(path)-1):
    cost += wg[path[i]][path[i+1]]

  endTime = time.time()-startTime

  # print("Randomly Generated Tour: {} at cost: {}".format(path, cost))
  # print("Ran in {} sec".format(endTime))
  return path, cost, endTime