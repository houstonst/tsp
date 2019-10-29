import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

def initTour(weightedGraph): #finds initial tour and cost between the two furthest away points
  maxVal = 0                 
  r = 0
  c = 0
  for row in weightedGraph:
    if max(row) > maxVal:
      maxVal = max(row)
      r = weightedGraph.index(row)
      c = row.index(maxVal)
  return (maxVal*2, [r, c])

def step(graph, path, cost, itr):
  wg = weightedGraph(graph)

  if itr == 1: #handles the very first button press
    iCost, iPath = initTour(wg)
    iPath.append(iPath[0]) #path is now a tour between the two furthest points
    fst = iPath[0]
    snd = iPath[1]
    thd = iPath[2]
    return (iPath, iCost)

  elif itr < len(graph) + 1: #itr simultaneously represents the path length. Handles all remaining button presses
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
    for r in range(len(wg)):
      for c in range(len(wg)):
        if r in path and c in path and r != c: #consider edges that exist in the subtour and are not self-directed
          if abs(path.index(r) - path.index(c)) == 1:
            edgeList.append((wg[r][c], r, c)) #create a list of edges and the incident nodes that exist in the subtour
          elif path[len(path)-1] == r and path[len(path)-2] == c:
            edgeList.append((wg[r][c], r, c))
    minDamage = 999999
    deletedEdge = (-1, -1)
    addedEdge1 = -1
    addedEdge2 = -1
    for edge in edgeList: #does not seem to correctly assess damages
      pEdge1 = wg[nextNode][edge[1]]
      pEdge2 = wg[nextNode][edge[2]]
      damage = cost - edge[0] + pEdge1 + pEdge2 #calculates the cost that would result from insertion
      if damage < minDamage:
        minDamage = damage
        deletedEdge = (edge[1], edge[2]) #edge in the node-pair form
        addedEdge1 = (nextNode, edge[1])
        addedEdge2 = (nextNode, edge[2])

    #remove and add the appropriate edges to include the new node. Adjust path and cost.
    cost = minDamage
    markerOne = path.index(deletedEdge[0]) #markerOne is the index of a node in the path that is incident to the edge being removed
    markerTwo = path.index(deletedEdge[1]) #markerTwo is the index of the node that is connected to the markerOne node. Its edge is being removed
    if markerOne == markerTwo - 1: #ensures that the edge being deleted is actually represented by the path list
      nodeOne = path[markerOne]
      nodeTwo = path[markerTwo]
      path.insert(markerOne + 1, nextNode)
      return (path, cost)
    
    elif markerOne == markerTwo + 1:
      nodeTwo = path[markerOne]
      nodeOne = path[markerTwo]
      path.insert(markerOne, nextNode)
      return (path, cost)

    elif path[len(path)-1] == deletedEdge[0] and path[len(path)-2] == deletedEdge[1]:
      nodeOne = path[len(path)-2]
      nodeTwo = path[len(path)-1]
      path.insert(len(path) - 1, nextNode)
      return (path, cost)

    else:
      print("error")

def farthestInsertion_NG(graph, nameArray):

  startTime = time.time()
  path = []
  cost = 0.0
  lineList = {}
  wg = weightedGraph(graph)
  i = 1

  def stepper(): #callable function for the step button
    nonlocal i, path, lineList, cost, graph
    while i < len(graph):
      path, cost = step(graph, path, cost, i)
      i += 1

  stepper()

  return path, cost