import operator, time, math
from euclidean import *
from tkinter import *
from tsp import *

def initTour(weightedGraph): # Finds initial tour and cost between the two furthest away points
  maxVal = 0                 
  r = 0
  c = 0
  for row in weightedGraph:
    if max(row) > maxVal:
      maxVal = max(row)
      r = weightedGraph.index(row)
      c = row.index(maxVal)
  return (maxVal*2, [r, c])

def step(graph, path, cost, itr, wndw):
  wg = weightedGraph(graph)

  if itr == 1:
    iCost, iPath = initTour(wg)
    iPath.append(iPath[0]) #path is now a tour between the two furthest points
    fst = iPath[0]
    snd = iPath[1]
    thd = iPath[2]
    wndw.create_line(graph[fst][0], graph[fst][1], graph[snd][0], graph[snd][1])
    wndw.create_line(graph[snd][0], graph[snd][1], graph[thd][0], graph[thd][1])
    print("in if")
    return (iPath, iCost)

  elif itr < len(graph) + 1: #itr simultaneously represents the path length
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
          if abs(path.index(r) - path.index(c)) == 1:
            edgeList.append((wg[r][c], r, c)) #create a list of edges and the incident nodes that exist in the subtour
    minDamage = 999999
    deletedEdge = (-1, -1)
    addedEdge1 = -1
    addedEdge2 = -1
    for edge in edgeList:
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
    leftMarker = path.index(deletedEdge[0]) #leftMarker is the index of the first node in the path that is incident to the edge being removed
    rightMarker = path.index(deletedEdge[1]) #rightMarker is the index of the node that is connected to the leftMarker node. Its edge is being removed
    #print("Old path: {}.".format(path))
    if leftMarker == rightMarker - 1: #ensures that the edge being deleted is actually represented by the path list
      leftNode = path[leftMarker]
      rightNode = path[rightMarker]
      wndw.create_line(graph[leftNode][0], graph[leftNode][1], graph[nextNode][0], graph[nextNode][1])
      wndw.create_line(graph[rightNode][0], graph[rightNode][1], graph[nextNode][0], graph[nextNode][1])
      path.insert(leftMarker + 1, nextNode)
      print("in elif")
      return (path, cost)
      # print("The edge {} can be deleted and edges {}, {} can be added for a new cost of {} in place of the former cost {}.".format(deletedEdge, addedEdge1, addedEdge2, minDamage, cost))
      # print("The path is now {}.".format(path))
    else:
      print("error")


def farthestInsertion(graph, nameArray):
  # TKINTER #
  root = Tk()
  canvas_height = 800
  canvas_width = 1200
  root.title("Euclidean TSP Solver")
  w = Canvas(root, width = canvas_width, height = canvas_height)
  w.pack(expand = YES, fill=BOTH)
  message = Label(root, text = "Farthest Insertion")
  message.pack(side=TOP)
  for pair in graph:
    w.create_oval((pair[0], pair[1], pair[0] + 5, pair[1] + 5), fill = "red")
  # TKINTER #


  startTime = time.time()
  path = []
  cost = 0.0
  wg = weightedGraph(graph)
  i = 1

  def stepper():
    nonlocal i, path, cost, graph
    path, cost = step(graph, path, cost, i, w)
    i += 1

  stepButton = Button(root, text = "Step", command = stepper)
  stepButton.pack(side = BOTTOM)

  # pathString = ""
  # adjCost = cost + wg[path[0]][0]
  # endTime = time.time() - startTime
  # for i in range(0, len(path)-1):
  #   pathString += nameArray[path[i]] + " -> "
  # pathString += nameArray[path[len(path)-1]]
  # graphSize = len(graph)
  # line1 = "\n\nThe optimal path in this {}-city instance using Farthest Insertion is: \n{}\n\n".format(graphSize, pathString)
  # line2 = "This path costs {} units, and required {} iterations in {} seconds \n(running in ????????? time, where n is the number of cities)\n\n".format(adjCost, iterations, endTime)
  # print(line1 + line2)

  root.mainloop()

  return path