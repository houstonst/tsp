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
  w = Canvas(root, width = canvas_width, height = canvas_height)
  w.pack(expand = YES, fill=BOTH)
  for pair in graph:
    index = graph.index(pair)
    name = nameArray[index]
    w.create_oval((pair[0]-3, pair[1]-3, pair[0] + 3, pair[1] + 3), fill = "red")
    w.create_text(pair[0], pair[1] - 12, fill = "black", font = "Times 10 bold", text = name)
  # TKINTER #

  lineList = {}

  for i in range(0, len(initPath)-2): #display initPath
    a = initPath[i]
    b = initPath[i+1]
    line = w.create_line(graph[a][0], graph[a][1], graph[b][0], graph[b][1])
    lineList.update({(a, b): line})
  first = initPath[0]
  last = initPath[len(initPath)-2]
  line = w.create_line(graph[first][0], graph[first][1], graph[last][0], graph[last][1])
  lineList.update({(first, last): line})

  print("starting path: {}".format(initPath))
  outerLoop(graph, initPath, w, lineList)

  # TKINTER #
  root.mainloop()
  # TKINTER #

def outerLoop(graph, initPath, w, lineList): #step 1
  wg = weightedGraph(graph)
  bestTour = initPath

  for v in range(0, 1): #for each node v of G. Do not evaluate last path value since it's the same as path[0]
    u0 = 0 #initialize
    u1 = 0
    if v == 0: #special case since initPath[0] == initPath[last]
      u0 = len(initPath)-2 #first edge incident with v
      u1 = 1 #second edge incident with v
    else:
      u0 = v-1 #first edge incident with v
      u1 = v+1 #second edge incident with v

    #edgeScan(v, u0, graph, initPath, wg, w, lineList)
    edgeScan(v, u1, graph, initPath, wg, w, lineList)

def edgeScan(v, u, graph, path, wg, w, lineList): #step 2
  u0 = u

  origPath = path
  u0val = path[u0] #make these since they'll be deleted immediatley below
  vval = path[v]

  if u0 < v: #delete edge (u0, v)
    path = path[:u0] + path[v:]
  else:
    path = path[:v] + path[u0:]
    path = path[::-1] #reversed so that v's corresponding node is still at the start of the path

  print("path after deletion: {}".format(path))

  if (u0val, vval) in lineList.keys():
    print("here")
    w.delete(lineList[(u0val, vval)])
    del lineList[(u0val, vval)]
  elif (vval, u0val) in lineList.keys():
    print("stillHere")
    w.delete(lineList[(vval, u0val)])
    del lineList[(vval, u0val)]
  
  dPath = []
  for w0 in range(0, len(origPath)-1): #add edge (w0, u0)
    print("w0: {}, u0: {}".format(origPath[w0], u0val))
    if w0 != v and w0 != u0 and w0 != u0+1 and w0 != u0-1: #new edge cannot be self-directed, back to v, or to a node that's already adjacent
      print("entered edge condition")
      if wg[origPath[w0]][u0val] <= wg[vval][u0val]: #if cost condition met, add the edge
        print("entered cost condition")
        newEdge = [origPath[w0], u0val]
        print("newEdge: {}".format(newEdge))
        #add edge (w0, u0). Find u0's position then insert w0 immediately before.
        #The nodes before w0 appears must be symmetrical with those after the second w0 in path:
        dpath = path + [origPath[w0]]
        w.create_line(graph[u0val][0], graph[u0val][1], graph[origPath[w0]][0], graph[origPath[w0]][1])
        break
  print("dPath: {}".format(dPath))

