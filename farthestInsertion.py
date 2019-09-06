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
  return (maxVal, [r, c])

def farthestNeighbor(graph, nameArray):
  startTime = time.time()
  cost = 0.0
  wg = weightedGraph(graph)
  iterations = 0
  cost, path = initTour(wg)
  path.append(path[0])

  #see which node not in the subtour has the greatest minimum distance to a node in the subtour
  legList = []
  for i in range(len(graph)): #iterate through nodes
    minLeg = 999999
    if i not in path: #consider node n if not in subtour
      for c in range(len(wg[i])): #look at distances from node n to any other node
        if c in path and wg[i][c] < minLeg: #consider only edges that go from n to a subtour node that are less than the current minLeg
          minLeg = wg[i][c]
      legList.append((minLeg, i))
  return legList



  #return (cost, path)