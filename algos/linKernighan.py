import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

bestTour = []

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

  print(initPath)
  outerLoop(graph, initPath, w)

  # TKINTER #
  root.mainloop()
  # TKINTER #

def outerLoop(graph, initPath, w): #step 1
  wg = weightedGraph(graph)
  bestTour = initPath
  for v in range(0, len(graph)-1): #for each node v of G. Do not evaluate last path value since it's the same as path[0]
    u0 = 0 #initialize
    u1 = 0
    if v == 0: #special case since initPath[0] == initPath[last]
      u0 = len(initPath)-2 #first edge incident with v
      u1 = 1 #second edge incident with v
    else:
      u0 = v-1 #first edge incident with v
      u1 = v+1 #second edge incident with v

    edgeScan(v, u0, graph, initPath, wg, w)
    edgeScan(v, u1, graph, initPath, wg, w)

def edgeScan(v, u, graph, path, wg, w): #step 2
  u0 = u

  origPath = path
  u0val = path[u0] #make these since they'll be deleted immediatley below
  vval = path[v]

  if u0 < v: #delete edge (u0, v)
    path = path[:u0] + path[v+1:]
  else:
    path = path[:v] + path[u0+1:]
  
  dPath = []
  for w0 in range(0, len(origPath)-1): #add edge (w0, u0)
    if w0 != v and w0 != u0 and w0 != u0+1 and w0 != u0-1: #new edge cannot be self-directed, back to v, or to a node that's already adjacent
      if wg[origPath[w0]][u0val] <= wg[vval][u0val]: #if met, add the edge
        edge = [origPath[w0], u0val]
        print("edge: {}".format(edge))
        #add edge (w0, u0). Find u0's position then insert w0 immediately before.
        #The nodes before w0 appears must be symmetrical with those after the second w0 in path:
        symSlice = origPath[:u0]
        dPath = symSlice + edge + path[u0+1:w0+1] + symSlice[::-1]
        w.create_line(graph[u0val][0], graph[u0val][1], graph[origPath[w0]][0], graph[origPath[w0]][1])
        break
  print("dPath: {}".format(dPath))

