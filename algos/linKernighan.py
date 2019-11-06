import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

bestTour = [[], 0.0]
added = set()
addedCost = 0.0
removed = set()
removedCost = 0.0
untested = set() #in the form (node, edge)

### BEST COST ISSUE. THE BEST COST IS PREVENTING ANY ADVANCES ###

def linKernighan(graph, nameArray, initPath, initCost, height, width):
  wg = weightedGraph(graph)
  "TEST SETS"
  
  "TEST SETS"

  # TKINTER #
  root = Tk() #GUI for the starting path
  canvas_height = height
  canvas_width = width
  root.title("Euclidean TSP Solver")
  root.iconbitmap('./graphics/favicon.ico')
  wndw = Canvas(root, width = canvas_width, height = canvas_height)
  wndw.pack(expand = YES, fill=BOTH)
  for pair in graph:
    index = graph.index(pair)
    name = nameArray[index]
    wndw.create_oval((pair[0]-3, pair[1]-3, pair[0] + 3, pair[1] + 3), fill = "red")
    wndw.create_text(pair[0], pair[1] - 12, fill = "black", font = "Times 10 bold", text = name)
  # TKINTER #

  # STEP FUNCTIONALITY #

  lineList = {}
  bestTour = [initPath, initCost]
  resultList = [bestTour]
  resultList += [outerLoop(graph, initPath, initCost, wndw, lineList)]
  result = bestTour
  s = 0
  t = 1
  print(bestTour)

  def stepper():
    nonlocal s, t, initPath, initCost, graph, wndw, resultList, lineList

    print("next step\n")
    if resultList[s] == resultList[t] and len(untested) == 0:
      for key in lineList.keys(): #clean up window before populating
        wndw.delete(lineList[key])
      
      lineList = {}

      tour = resultList[len(resultList)-1][0]
      for i in range(0, len(bestTour[0])-2): #display bestTour
        a = tour[i]
        b = tour[i+1]
        line = wndw.create_line(graph[a][0], graph[a][1], graph[b][0], graph[b][1])
        lineList.update({(a, b): line})
      first = tour[0]
      last = tour[len(tour)-2]
      line = wndw.create_line(graph[first][0], graph[first][1], graph[last][0], graph[last][1])
      lineList.update({(first, last): line})
      
      print("Initial Tour: {}, Initial Cost: {}".format(initPath, initCost))
      print("Lin-Kernighan Result: {}, Cost: {}".format(resultList[len(resultList)-1][0], resultList[len(resultList)-1][1]))
      print(untested)
      return
    else:
      resultList += [outerLoop(graph, resultList[t][0], resultList[t][1], wndw, lineList)]

      for key in lineList.keys(): #clean up window before populating
        wndw.delete(lineList[key])
      
      lineList = {}

      for i in range(0, len(bestTour[0])-2): #display bestTour
        tour = resultList[len(resultList)-1][0]
        a = tour[i]
        b = tour[i+1]
        line = wndw.create_line(graph[a][0], graph[a][1], graph[b][0], graph[b][1])
        lineList.update({(a, b): line})
      first = tour[0]
      last = tour[len(tour)-2]
      line = wndw.create_line(graph[first][0], graph[first][1], graph[last][0], graph[last][1])
      lineList.update({(first, last): line})

      s += 1
      t += 1
  # STEP FUNCTIONALITY #

  for i in range(0, len(initPath)-2): #display initPath
    a = initPath[i]
    b = initPath[i+1]
    line = wndw.create_line(graph[a][0], graph[a][1], graph[b][0], graph[b][1])
    lineList.update({(a, b): line})
  first = initPath[0]
  last = initPath[len(initPath)-2]
  line = wndw.create_line(graph[first][0], graph[first][1], graph[last][0], graph[last][1])
  lineList.update({(first, last): line})

  # TKINTER #
  stepButton = Button(root, text = "Step", command = stepper)
  stepButton.pack(side = BOTTOM)

  root.mainloop()
  # TKINTER #

def outerLoop(graph, initPath, initCost, wndw, lineList): #step 1
  global bestTour, added, addedCost, removed, removedCost, untested
  wg = weightedGraph(graph)
  bestTour = [initPath, initCost] #FIXES IN PART
  added = set()
  addedCost = 0.0
  removed = set()
  removedCost = 0.0
  untested = set()

  for i in range(0, len(initPath)-2):
    for j in range(0, len(initPath)-1):
      if i != j:
        untested.add((i, j))
  
  scan1 = [[], 9999999]
  scan2 = [[], 9999999]

  for v in range(0, len(initPath)-2): #for each node v of G. Do not evaluate last path value since it's the same as path[0]
    u0 = 0 #initialize
    u1 = 0
    if v == 0: #special case since initPath[0] == initPath[last]
      u0 = len(initPath)-2 #first edge incident with v
      u1 = 1 #second edge incident with v
    else:
      u0 = v-1 #first edge incident with v
      u1 = v+1 #second edge incident with v

    newScan1 = edgeScan(v, u0, graph, initPath, wg, wndw, lineList)
    newScan2 = edgeScan(v, u1, graph, initPath, wg, wndw, lineList)

    if newScan1[1] < scan1[1]:
      scan1 = newScan1
    if newScan2[1] < scan2[1]:
      scan2 = newScan2

  bestScan = min(scan1[1], scan2[1])
  if bestScan == scan1[1]:
    return scan1
  else:
    return scan2

def edgeScan(v, u, graph, path, wg, wndw, lineList): #step 2
  global bestTour, added, removed, addedCost, removedCost, untested
  u0 = u
  origPath = path
  u0val = path[u0] #make these since they'll be deleted immediately below
  vval = path[v]

  #set checks
  if (u0val, vval) in added or (u0val, vval) in removed:
    return bestTour
  elif (vval, u0val) in added or (vval, u0val) in removed:
    return bestTour
  #set checks
  else:
    rmCost = wg[u0val][vval]
    if u0 == len(path)-2 and v == 0:
      path = path[:len(path)-1]
      removed.add((u0val, vval))
      removedCost += rmCost
    elif u0 == len(path)-2 and v == len(path)-3:
      sec = path[:u0]
      path = sec[::-1] + [path[u0]]
      removed.add((vval, u0val))
      removedCost += rmCost
    elif u0 < v: #delete edge (u0, v)
      sec1 = path[1:v]
      sec2 = path[v:]
      path = sec2 + sec1
      removed.add((u0val, vval))
      removedCost += rmCost
    else:
      sec1 = path[1:u0]
      sec2 = path[u0:]
      path = sec1[::-1] + sec2[::-1] #reversed so that v's corresponding node is still at the start of the path
      removed.add((vval, u0val))
      removedCost += rmCost

    dPath = []
    remaining = []

    for w0 in range(0, len(origPath)-1): #add edge (w0, u0)

      isUntested = (v, w0) in untested

      if w0 != v and w0 != u0 and w0 != u0+1 and w0 != u0-1 and isUntested: #new edge cannot be self-directed, back to v, or to a node that's already adjacent
        print("checked edges: {}, {}".format((origPath[w0], u0val), (vval, u0val)))
        
        untested.remove((v, w0))

        if wg[origPath[w0]][u0val] <= wg[vval][u0val]: #if cost condition met, add the edge
          newEdge = [origPath[w0], u0val]
          if (newEdge[0], newEdge[1]) in removed or (newEdge[1], newEdge[0]) in removed or (removedCost - addedCost) < 0:
            continue
          elif (newEdge[0], newEdge[1]) in added or (newEdge[1], newEdge[0]) in added:
            continue
          else:
            added.add((origPath[w0], u0val))
            addedCost += wg[origPath[w0]][u0val]

            #add edge (w0, u0). Find u0's position then insert w0 immediately before.
            #The nodes before w0 appears must be symmetrical with those after the second w0 in path:
            dPath = path + [origPath[w0]]
            remaining = [num for num in range(w0+1, len(origPath)-1)]
            break

    # print("remaining: {}, remaining length: {}".format(untested, len(untested)))

    if len(dPath) > 0:
      return testTour(graph, path, dPath, wg, v, dPath.index(u0val), dPath.index(dPath[len(dPath)-1]), newEdge, wndw, lineList)
    else:
      return bestTour

def testTour(graph, path, dPath, wg, v, u, w, newEdge, wndw, lineList): #step 3
  global bestTour
  r = w + 1
  sec = dPath[r:len(dPath)-1]
  tour = dPath[:w+1] + sec[::-1] + [dPath[0]] #creates tour that breaks the cycle and returns to start

  cost = 0.0
  for i in range(0, len(tour)-1):
    cost += wg[tour[i]][tour[i+1]]

  if cost <= bestTour[1]:
    bestTour[0] = tour
    bestTour[1] = cost

  return nextDelta(graph, path, dPath, tour, cost, wg, v, u, w, newEdge, wndw, lineList) #performing step 4 on delta path, not the tour

def nextDelta(graph, path, dPath, tour, tourCost, wg, v, u, w, newEdge, wndw, lineList): #step 4
  global bestTour, added, removed, addedCost, removedCost
  un = w + 1
  wVal = dPath[w]
  unVal = dPath[un]
  vval = path[v]
  
  if [wVal, unVal] == newEdge or [unVal, wVal] == newEdge:
    return bestTour

  else:
    #set checks
    if (wVal, unVal) in added or (wVal, unVal) in removed:
      return bestTour
    elif (unVal, wVal) in added or (unVal, wVal) in removed:
      return bestTour
    #set checks

    else: # ERROR. CREATING DELTA SETS THAT REVISIT MORE THAN ONE NODE. Likely in the slicing
      #remove (w_i, u_i+1)
      sec = dPath[un:u+1]
      dPath = dPath[:w+1] + sec[::-1]
      removed.add((wVal, unVal))
      removedCost += wg[wVal][unVal]

      for wn in range(1, len(tour)-1): #evaluate every node, so use tour since dPath has been shortened
        wnVal = tour[wn]
        wnInd = tour.index(wnVal)
        unInd = tour.index(unVal)
        if wnInd == unInd + 1 or wnInd == unInd - 1: #ensures that wn and un are not adjacent in the tour transformation
          continue
        elif wVal == wnVal or wnVal == vval or dPath[len(dPath)-1] == wnVal or (removedCost - addedCost) < 0:
          continue
        elif (dPath[len(dPath)-1], wnVal) in removed or (dPath[len(dPath)-1], wnVal) in added:
          continue
        elif (wnVal, dPath[len(dPath)-1]) in removed  or (wnVal, dPath[len(dPath)-1]) in added:
          continue
        else: #perform (u_i+1, w_i+1) switch; removed (w_i, u_i+1), now add (u_i+1, w_i+1)
          dPath = dPath + [dPath[wn]]
          edge = [dPath[len(dPath)-2], dPath[wn]]
          added.add((edge[0], edge[1]))
          addedCost += wg[edge[0]][edge[1]]

          testTour(graph, path, dPath, wg, v, dPath.index(unVal), dPath.index(wnVal), edge, wndw, lineList)
          break
    
    return bestTour