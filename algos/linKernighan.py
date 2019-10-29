import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

bestTour = [[], 0.0]
deltaSet = set() #must store tuples, not lists

def linKernighan(graph, nameArray, initPath, initCost):
  # initPath = [3,2,0,5,4,1,3] #testing shortTest.csv
  # initPath = [5,3,2,1,4,0,5]
  # initPath = [0,1,5,3,4,2,0] #exceeds recursion

  # initPath = [0,3,7,5,4,9,8,2,6,1,10,0] #testing longTest.csv

  # TKINTER #
  startPath = Tk() #GUI for the starting path
  canvas_height = 750
  canvas_width = 1200
  startPath.title("Euclidean TSP Solver")
  startPath.iconbitmap('./graphics/favicon.ico')
  wndw = Canvas(startPath, width = canvas_width, height = canvas_height)
  wndw.pack(expand = YES, fill=BOTH)
  for pair in graph:
    index = graph.index(pair)
    name = nameArray[index]
    wndw.create_oval((pair[0]-3, pair[1]-3, pair[0] + 3, pair[1] + 3), fill = "red")
    wndw.create_text(pair[0], pair[1] - 12, fill = "black", font = "Times 10 bold", text = name)

  # initiate work
  print("Random Tour: {}, Cost: {}".format(initPath, initCost))

  lineList = {}
  result = outerLoop(graph, initPath, initCost, wndw, lineList)

  print("Best Tour: {}, Cost: {}".format(result[0], result[1]))
  # initiate work

  for i in range(0, len(initPath)-2): #display initPath
    a = initPath[i]
    b = initPath[i+1]
    line = wndw.create_line(graph[a][0], graph[a][1], graph[b][0], graph[b][1])
    lineList.update({(a, b): line})
  first = initPath[0]
  last = initPath[len(initPath)-2]
  line = wndw.create_line(graph[first][0], graph[first][1], graph[last][0], graph[last][1])
  lineList.update({(first, last): line})

  #### Second Window ####

  endPath = Tk() #GUI for the starting path
  canvas_height = 750
  canvas_width = 1200
  endPath.title("Euclidean TSP Solver")
  endPath.iconbitmap('./graphics/favicon.ico')
  wndw = Canvas(endPath, width = canvas_width, height = canvas_height)
  wndw.pack(expand = YES, fill=BOTH)
  for pair in graph:
    index = graph.index(pair)
    name = nameArray[index]
    wndw.create_oval((pair[0]-3, pair[1]-3, pair[0] + 3, pair[1] + 3), fill = "red")
    wndw.create_text(pair[0], pair[1] - 12, fill = "black", font = "Times 10 bold", text = name)

  for i in range(0, len(initPath)-2): #display bestTour
    tour = result[0]
    a = tour[i]
    b = tour[i+1]
    line = wndw.create_line(graph[a][0], graph[a][1], graph[b][0], graph[b][1])
    lineList.update({(a, b): line})
  first = tour[0]
  last = tour[len(tour)-2]
  line = wndw.create_line(graph[first][0], graph[first][1], graph[last][0], graph[last][1])
  lineList.update({(first, last): line})
  
  # TKINTER #
  startPath.mainloop()
  endPath.mainloop()
  # TKINTER #

def outerLoop(graph, initPath, initCost, wndw, lineList): #step 1
  global bestTour
  wg = weightedGraph(graph)
  bestTour = [initPath, initCost]
  
  scan1 = [[], 9999999]
  scan2 = [[], 9999999]
  # for v in range(3, 4): #testing
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

  bestScan = max(scan1[1], scan2[1])
  if bestScan == scan1[1]:
    return scan1
  else:
    return scan2


def edgeScan(v, u, graph, path, wg, wndw, lineList): #step 2
  global bestTour, deltaSet
  u0 = u
  origPath = path
  u0val = path[u0] #make these since they'll be deleted immediatley below
  vval = path[v]

  if u0 == len(path)-2 and v == 0:
    path = path[:len(path)-1]
  elif u0 == len(path)-2 and v == len(path)-3:
    sec = path[:u0]
    path = sec[::-1] + [path[u0]]
  elif u0 < v: #delete edge (u0, v)
    sec1 = path[1:v]
    sec2 = path[v:]
    path = sec2 + sec1
  else:
    sec1 = path[1:u0]
    sec2 = path[u0:]
    path = sec1[::-1] + sec2[::-1] #reversed so that v's corresponding node is still at the start of the path

  # if (u0val, vval) in lineList.keys():
  #   wndw.delete(lineList[(u0val, vval)])
  #   del lineList[(u0val, vval)]
  # elif (vval, u0val) in lineList.keys():
  #   wndw.delete(lineList[(vval, u0val)])
  #   del lineList[(vval, u0val)]
  
  dPath = []
  for w0 in range(0, len(origPath)-1): #add edge (w0, u0)
    if w0 != v and w0 != u0 and w0 != u0+1 and w0 != u0-1: #new edge cannot be self-directed, back to v, or to a node that's already adjacent
      if wg[origPath[w0]][u0val] <= wg[vval][u0val]: #if cost condition met, add the edge
        newEdge = [origPath[w0], u0val]

        #add edge (w0, u0). Find u0's position then insert w0 immediately before.
        #The nodes before w0 appears must be symmetrical with those after the second w0 in path:
        dPath = path + [origPath[w0]]
        deltaSet.add(tuple(dPath))
        # line = wndw.create_line(graph[u0val][0], graph[u0val][1], graph[origPath[w0]][0], graph[origPath[w0]][1])
        # lineList.update({(newEdge[0], newEdge[1]): line})
        break

  if len(dPath) > 0:
    return testTour(graph, dPath, wg, dPath.index(u0val), dPath.index(dPath[len(dPath)-1]), newEdge, wndw, lineList)
  else:
    return bestTour

def testTour(graph, dPath, wg, u, w, newEdge, wndw, lineList): #step 4
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

  return nextDelta(graph, dPath, tour, cost, wg, u, w, newEdge, wndw, lineList) #performing step 4 on delta path, not the tour

def nextDelta(graph, dPath, tour, tourCost, wg, u, w, newEdge, wndw, lineList): #step 4
  global bestTour, deltaSet
  un = w + 1
  wVal = dPath[w]
  unVal = dPath[un]
  
  if [wVal, unVal] == newEdge or [unVal, wVal] == newEdge:
    print("Go to step 5")
    return bestTour
  else:
    #remove (w_i, u_i+1)
    sec = dPath[un:u+1]
    dPath = dPath[:w+1] + sec[::-1]

    if tuple(dPath) not in deltaSet:

    # if (wVal, unVal) in lineList.keys():
    #   wndw.delete(lineList[(wVal, unVal)])
    #   del lineList[(wVal, unVal)]
    # elif (unVal, wVal) in lineList.keys():
    #   wndw.delete(lineList[(unVal, wVal)])
    #   del lineList[(unVal, wVal)]

      for wn in range(1, len(tour)-1): #evaluate every node, so use tour since dPath has been shortened
        wnVal = tour[wn]
        wnInd = tour.index(wnVal)
        unInd = tour.index(unVal)
        if wnInd == unInd + 1 or wnInd == unInd - 1: #ensures that wn and un are not adjacent in the tour transformation
          continue
        elif wVal == wnVal:
          continue
        else: #perform (u_i+1, w_i+1) switch; removed (w_i, u_i+1), now add (u_i+1, w_i+1)
          dPath = dPath + [dPath[wn]]
          deltaSet.add(tuple(dPath))

          dCost = 0.0
          for i in range(0, len(dPath)-1):
            dCost += wg[dPath[i]][dPath[i+1]]

          if dCost <= tourCost: #check the costs
            edge = [dPath[len(dPath)-2], dPath[len(dPath)-1]]

            # line = wndw.create_line(graph[edge[0]][0], graph[edge[0]][1], graph[edge[1]][0], graph[edge[1]][1])
            # lineList.update({(edge[0], edge[1]): line})
            testTour(graph, dPath, wg, dPath.index(unVal), dPath.index(wnVal), edge, wndw, lineList)

    return bestTour