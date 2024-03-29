import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

def step(wg, path, cost, unchanged, i, j, lineList, wndw, graph, option):
  pathCopy = path
  costCopy = cost

  if i < j and (i != j-1 or i != j+1):
    a = pathCopy[i]
    b = pathCopy[i+1]
    m = pathCopy[j]
    n = pathCopy[j+1]
    oCost = wg[a][b] + wg[m][n]
    pCost = wg[a][m] + wg[b][n]
    
    if pCost < oCost:
      if option == "1":
        if (a, b) in lineList.keys():
          wndw.delete(lineList[(a, b)])
          del lineList[(a, b)]
        elif (b, a) in lineList.keys():
          wndw.delete(lineList[(b, a)])
          del lineList[(b, a)]
        if (m, n) in lineList.keys():
          wndw.delete(lineList[(m, n)])
          del lineList[(m, n)]
        elif (n, m) in lineList.keys():
          wndw.delete(lineList[(n, m)])
          del lineList[(n, m)] 
        x = wndw.create_line(graph[a][0], graph[a][1], graph[m][0], graph[m][1])
        y = wndw.create_line(graph[b][0], graph[b][1], graph[n][0], graph[n][1])
        lineList.update({(a, m): x})
        lineList.update({(b, n): y})

      pathCopySlice = pathCopy[i+1:j]
      pathCopy = pathCopy[0:i+1] + [pathCopy[j]] + pathCopySlice[::-1] + pathCopy[j+1:]

      costCopy = costCopy - oCost + pCost
      unchanged = False

  return pathCopy, costCopy, unchanged, lineList

def twoOpt(initCoords, graph, nameArray, path, cost, height, width, option):
  if option == "1":
    # TKINTER #
    root = Tk()
    canvas_height = height
    canvas_width = width
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

  wg = weightedGraph(initCoords)
  pathCopy = path
  costCopy = cost
  unchanged = True
  endWhile = False
  runtime = 0.0
  lineList = {}
  i = 0
  j = 2

  if option == "1":
    last = graph[path[len(path)-1]] #the last node touched in the path
    for z in range(len(path)-1):
      node = path[z]
      nxt = path[z+1]
      a = w.create_line(graph[node][0], graph[node][1], graph[nxt][0], graph[nxt][1], fill = "black")
      lineList.update({(node, nxt): a})
    a = w.create_line(graph[path[0]][0], graph[path[0]][1], last[0], last[1], fill = "black")
    lineList.update({(path[0], path[len(path)-1])})

    w.itemconfig(lineList[(path[i], path[i+1])], fill = "red")
    w.itemconfig(lineList[(path[j], path[j+1])], fill = "red")
  
  def stepper(): #need to return for entire file
    nonlocal i, j, pathCopy, costCopy, unchanged, graph, lineList, w, endWhile

    if i == len(graph)-4 and j == len(graph)-1 and unchanged == True:
      endWhile = True
      return pathCopy, costCopy

    if j < len(graph):
      if option == "1":
        a = pathCopy[i]
        b = pathCopy[i+1]
        c = pathCopy[j]
        d = pathCopy[j+1]
        if (a, b) in lineList.keys():
          w.itemconfig(lineList[(a, b)], fill = "black")
        elif (b, a) in lineList.keys():
          w.itemconfig(lineList[(b, a)], fill = "black")
        if (c, d) in lineList.keys():
          w.itemconfig(lineList[(c, d)], fill = "black")
        elif (d, c) in lineList.keys():
          w.itemconfig(lineList[(d, c)], fill = "black")

      pathCopy, costCopy, unchanged, lineList = step(wg, pathCopy, costCopy, unchanged, i, j, lineList, w, graph, option)

      j += 1
    elif j == len(graph) and i < len(graph)-3:
      i += 1
      j = i + 2
      
      if option == "1":
        a = pathCopy[i]
        b = pathCopy[i+1]
        c = pathCopy[j]
        d = pathCopy[j+1]
        if (a, b) in lineList.keys():
          w.itemconfig(lineList[(a, b)], fill = "black")
        elif (b, a) in lineList.keys():
          w.itemconfig(lineList[(b, a)], fill = "black")
        if (c, d) in lineList.keys():
          w.itemconfig(lineList[(c, d)], fill = "black")
        elif (d, c) in lineList.keys():
          w.itemconfig(lineList[(d, c)], fill = "black")

      pathCopy, costCopy, unchanged, lineList = step(wg, pathCopy, costCopy, unchanged, i, j, lineList, w, graph, option)
    if i == len(graph)-3:
      unchanged = True
      i = 0
      j = 2

      if option == "1":
        a = pathCopy[i]
        b = pathCopy[i+1]
        c = pathCopy[j]
        d = pathCopy[j+1]
        if (a, b) in lineList.keys():
          w.itemconfig(lineList[(a, b)], fill = "black")
        elif (b, a) in lineList.keys():
          w.itemconfig(lineList[(b, a)], fill = "black")
        if (c, d) in lineList.keys():
          w.itemconfig(lineList[(c, d)], fill = "black")
        elif (d, c) in lineList.keys():
          w.itemconfig(lineList[(d, c)], fill = "black")

      pathCopy, costCopy, unchanged, lineList = step(wg, pathCopy, costCopy, unchanged, i, j, lineList, w, graph, option)
    
    if option == "1":
      u = i
      v = j

      if v == len(graph) and u < len(graph)-3:
        u += 1
        v = u + 2
      if u == len(graph):
        u = 0
        v = 2
      
      a = pathCopy[u]
      b = pathCopy[u+1]
      c = pathCopy[v]
      d = pathCopy[v+1]

      if (a, b) in lineList.keys():
        w.itemconfig(lineList[(a, b)], fill = "red")
      elif (b, a) in lineList.keys():
        w.itemconfig(lineList[(b, a)], fill = "red")
      if (c, d) in lineList.keys():
        w.itemconfig(lineList[(c, d)], fill = "red")
      elif (d, c) in lineList.keys():
        w.itemconfig(lineList[(d, c)], fill = "red")

  if option == "1":
    # TKINTER #
    stepButton = Button(root, text = "Step", command = stepper)
    stepButton.pack(side = BOTTOM)

    root.mainloop()
    # TKINTER #
    print("Two Optimal Tour: {} at Cost: {}".format(pathCopy, costCopy))

  else:
    startTime = time.time()
    while endWhile == False:
      w = 0
      stepper()

    runtime = time.time() - startTime
    print("Two Optimal Tour: {} at Cost: {} in {} Seconds".format(pathCopy, costCopy, runtime))
  
  
  return pathCopy, costCopy, runtime