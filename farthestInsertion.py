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
  maxMinLeg = -1
  nextNode = -1
  for pair in legList:
    if pair[0] > maxMinLeg:
      maxMinLeg = pair[0]
      nextNode = pair[1]
  
  #see which edge can be broken and connected to this farthest node in the cheapest manner
  edgeList = []
  for r in range(len(wg)//2):
    for c in range(len(wg)):
      if r in path and c in path and r != c: #consider edges that exist in the subtour and are not self-directed
        edgeList.append((wg[r][c], r, c)) #create a list of edges and the incident nodes that exist in the subtour
  minDamage = 999999
  deletedEdge = (-1, -1)
  addedEdge1 = -1
  addedEdge2 = -1
  for edge in edgeList:
    pEdge1 = wg[nextNode][edge[1]]
    pEdge2 = wg[nextNode][edge[2]]
    damage = cost - edge[0] + pEdge1 + pEdge2
    if damage < minDamage:
      minDamage = damage
      deletedEdge = (edge[1], edge[2])
      addedEdge1 = (nextNode, edge[1])
      addedEdge2 = (nextNode, edge[2])
  print("The edge {} can be deleted and edges {}, {} can be added for a new cost of {} in place of the former cost {}".format(deletedEdge, addedEdge1, addedEdge2, minDamage, cost))





  #return (cost, path)