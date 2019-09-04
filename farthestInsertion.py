import operator, time, math
from euclidean import *

def farthestNeighbor(graph, nameArray):
  startTime = time.time()
  cost = 0.0
  wg = weightedGraph(graph)
  iterations = 0
