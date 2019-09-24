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

def step(graph, path, lineList, cost, itr, wndw):
  wg = weightedGraph(graph)

  if itr == 1: #handles the very first button press
    iCost, iPath = initTour(wg)
    iPath.append(iPath[0]) #path is now a tour between the two furthest points
    fst = iPath[0]
    snd = iPath[1]
    thd = iPath[2]
    a = wndw.create_line(graph[fst][0], graph[fst][1], graph[snd][0], graph[snd][1])
    b = wndw.create_line(graph[snd][0], graph[snd][1], graph[thd][0], graph[thd][1])
    lineList.update({(fst, snd): a})
    lineList.update({(snd, fst): b})
    return (iPath, iCost, lineList)

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
      if deletedEdge in lineList.keys(): #delete replaced edges from the GUI
        wndw.delete(lineList[deletedEdge])
        del lineList[deletedEdge] #update the list of GUI line IDs
      else:
        wndw.delete(lineList[(deletedEdge[1], deletedEdge[0])]) #delete replaced edges from the GUI
        del lineList[(deletedEdge[1], deletedEdge[0])] 
      a = wndw.create_line(graph[nodeOne][0], graph[nodeOne][1], graph[nextNode][0], graph[nextNode][1]) #create the new edges that include the new node
      b = wndw.create_line(graph[nodeTwo][0], graph[nodeTwo][1], graph[nextNode][0], graph[nextNode][1])
      lineList.update({(nodeOne, nextNode): a}) #update the list of GUI line IDs
      lineList.update({(nodeTwo, nextNode): b})
      path.insert(markerOne + 1, nextNode)
      return (path, cost, lineList)
    
    elif markerOne == markerTwo + 1:
      nodeTwo = path[markerOne]
      nodeOne = path[markerTwo]
      if deletedEdge in lineList.keys():
        wndw.delete(lineList[deletedEdge])
        del lineList[deletedEdge]
      else:
        wndw.delete(lineList[(deletedEdge[1], deletedEdge[0])])
        del lineList[(deletedEdge[1], deletedEdge[0])]
      a = wndw.create_line(graph[nodeOne][0], graph[nodeOne][1], graph[nextNode][0], graph[nextNode][1])
      b = wndw.create_line(graph[nodeTwo][0], graph[nodeTwo][1], graph[nextNode][0], graph[nextNode][1])
      lineList.update({(nodeOne, nextNode): a})
      lineList.update({(nodeTwo, nextNode): b})
      path.insert(markerOne, nextNode)
      return (path, cost, lineList)

    elif path[len(path)-1] == deletedEdge[0] and path[len(path)-2] == deletedEdge[1]:
      nodeOne = path[len(path)-2]
      nodeTwo = path[len(path)-1]
      if deletedEdge in lineList.keys():
        wndw.delete(lineList[deletedEdge])
        del lineList[deletedEdge]
      else:
        wndw.delete(lineList[(deletedEdge[1], deletedEdge[0])])
        del lineList[(deletedEdge[1], deletedEdge[0])]
      a = wndw.create_line(graph[nodeOne][0], graph[nodeOne][1], graph[nextNode][0], graph[nextNode][1])
      b = wndw.create_line(graph[nodeTwo][0], graph[nodeTwo][1], graph[nextNode][0], graph[nextNode][1])
      lineList.update({(nodeOne, nextNode): a})
      lineList.update({(nodeTwo, nextNode): b})
      path.insert(len(path) - 1, nextNode)
      return (path, cost, lineList)

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
  for pair in graph:
    index = graph.index(pair)
    name = nameArray[index]
    w.create_oval((pair[0]-3, pair[1]-3, pair[0] + 3, pair[1] + 3), fill = "red")
    w.create_text(pair[0], pair[1] - 12, fill = "black", font = "Times 10 bold", text = name)
  # TKINTER #

  startTime = time.time()
  path = []
  cost = 0.0
  lineList = {}
  wg = weightedGraph(graph)
  i = 1

  def stepper(): #callable function for the step button
    nonlocal i, path, lineList, cost, graph
    if i < len(graph):
      path, cost, lineList = step(graph, path, lineList, cost, i, w)
      i += 1

  # TKINTER #
  stepButton = Button(root, text = "Step", command = stepper)
  stepButton.pack(side = BOTTOM)

  root.mainloop()
  # TKINTER #

  return path