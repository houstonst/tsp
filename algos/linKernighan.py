import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

bestTour = [] #tracking the best tour seen

def linKernighan(graph, nameArray, initPath, initCost):
  # TKINTER #
  root = Tk()
  canvas_height = 750
  canvas_width = 1200
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

  lineList = {}

  for i in range(0, len(initPath)-2): #display initPath
    a = initPath[i]
    b = initPath[i+1]
    line = wndw.create_line(graph[a][0], graph[a][1], graph[b][0], graph[b][1])
    lineList.update({(a, b): line})
  first = initPath[0]
  last = initPath[len(initPath)-2]
  line = wndw.create_line(graph[first][0], graph[first][1], graph[last][0], graph[last][1])
  lineList.update({(first, last): line})

  print("starting path: {}".format(initPath))
  outerLoop(graph, initPath, wndw, lineList)

  # TKINTER #
  #root.mainloop()
  # TKINTER #

def outerLoop(graph, initPath, wndw, lineList): #step 1
  wg = weightedGraph(graph)
  bestTour = initPath
  
  #for v in range(1, 2): #testing
  for v in range(0, len(initPath)-2): #for each node v of G. Do not evaluate last path value since it's the same as path[0]
    u0 = 0 #initialize
    u1 = 0
    if v == 0: #special case since initPath[0] == initPath[last]
      u0 = len(initPath)-2 #first edge incident with v
      u1 = 1 #second edge incident with v
    else:
      u0 = v-1 #first edge incident with v
      u1 = v+1 #second edge incident with v

    edgeScan(v, u0, graph, initPath, wg, wndw, lineList)
    edgeScan(v, u1, graph, initPath, wg, wndw, lineList)

def edgeScan(v, u, graph, path, wg, wndw, lineList): #step 2
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

  if (u0val, vval) in lineList.keys():
    wndw.delete(lineList[(u0val, vval)])
    del lineList[(u0val, vval)]
  elif (vval, u0val) in lineList.keys():
    wndw.delete(lineList[(vval, u0val)])
    del lineList[(vval, u0val)]
  
  dPath = []
  for w0 in range(0, len(origPath)-1): #add edge (w0, u0)
    if w0 != v and w0 != u0 and w0 != u0+1 and w0 != u0-1: #new edge cannot be self-directed, back to v, or to a node that's already adjacent
      if wg[origPath[w0]][u0val] <= wg[vval][u0val]: #if cost condition met, add the edge
        newEdge = [origPath[w0], u0val]

        #add edge (w0, u0). Find u0's position then insert w0 immediately before.
        #The nodes before w0 appears must be symmetrical with those after the second w0 in path:
        dPath = path + [origPath[w0]]
        wndw.create_line(graph[u0val][0], graph[u0val][1], graph[origPath[w0]][0], graph[origPath[w0]][1])
        break

  if len(dPath) > 0:
    print("dPath: {}".format(dPath))
    testTour(graph, dPath, wg, dPath.index(u0val), dPath.index(dPath[len(dPath)-1]), newEdge)
  else:
    print("No delta path produced")

def testTour(graph, dPath, wg, u, w, newEdge): #step 4
  r = w + 1

  sec = dPath[r:len(dPath)-1]
  tour = dPath[:w+1] + sec[::-1] + [dPath[0]] #creates tour that breaks the cycle and returns to start

  cost = 0.0
  for i in range(0, len(tour)-1):
    cost += wg[tour[i]][tour[i+1]]

  print("new tour: {}, new cost: {}".format(tour, cost))

  nextDelta(graph, dPath, tour, wg, u, w, newEdge) #performing step 4 on delta path, not the tour

def nextDelta(graph, dPath, tour, wg, u, w, newEdge): #step 4
  un = -1
  if u == w + 1: #identify u_i+1
    un = dPath[len(dPath)-2]
  elif u == len(dPath)-2:
    un = w + 1
  else:
    print("Cannot ID u_i+1")
  
  print("u: {}, w: {}, un: {}\n".format(u, w, un))
  # unVal = dPath[un]
  
  # if [w, un] == newEdge or [un, w] == newEdge:
  #   print("Go to step 5")
  # else:
  #   for wn in range(0, len(dPath)-1):
  #     wnInd = tour.index(wn)
  #     unInd = tour.index(un)
  #     if wnInd == unInd + 1 or wnInd == unInd - 1:
  #       print("here")