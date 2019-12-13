import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

def step(initCoords, graph, path, cost, iterations, i, wndw, option):
  wg = weightedGraph(initCoords)
  min = 999999.9
  next = 0

  for node in range(0, len(graph)):
    iterations += 1
    prev = path[0]
    if path.count(node) == 0 and wg[prev][node] < min and node != path[len(path)-1]:
      next = node
      min = wg[prev][node]
    elif node == path[len(path)-1] and len(path) == len(graph):
      next = node
      min = wg[prev][node]

  cost += min
  if option == "1":
    wndw.create_line(graph[next][0], graph[next][1], graph[path[0]][0], graph[path[0]][1])
  path = operator.iadd([next], path)
  return path, cost, 0

def nearestNeighbor(initCoords, graph, nameArray, height, width, option):
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

  startTime = time.time()
  path = [0]
  cost = 0.0
  iterations = 0
  i = 1

  def stepper(): #callable function for the step button
    nonlocal i, path, cost, iterations, graph, w
    if option == "1":
      if i <= len(graph):
        path, cost, iterations = step(initCoords, graph, path, cost, iterations, i, w, option)
        i += 1
      else:
        print("Nearest Neighbor Tour: {}, Cost: {}".format(path, cost))
        return path, cost, 0
    elif option == "2":
      while i <= len(graph):
        w = 0
        path, cost, iterations = step(initCoords, graph, path, cost, iterations, i, w, option)
        i += 1
      
      runTime = time.time() - startTime
      print("Nearest Neighbor Tour: {}, Cost: {}, Running Time: {}".format(path, cost, runTime))
      return path, cost, runTime
      
  if option == "1":
    # TKINTER #
    stepButton = Button(root, text = "Step", command = stepper)
    stepButton.pack(side = BOTTOM)

    root.mainloop()
    # TKINTER #
  
  else:
    path, cost, runtime = stepper()
    return path, cost, runtime