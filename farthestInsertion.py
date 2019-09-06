import operator, time, math
from euclidean import *

def initTour(weightedGraph): # Finds initial tour and cost between the two furthest away points
  maxVal = 0                 # Works.
  r = 0
  c = 0
  for row in weightedGraph:
    if max(row) > maxVal:
      maxVal = max(row)
      r = weightedGraph.index(row)
      c = row.index(maxVal)
  return (maxVal, (r, c))

def farthestNeighbor(graph, nameArray):
  startTime = time.time()
  cost = 0.0
  wg = weightedGraph(graph)
  iterations = 0
  return 0