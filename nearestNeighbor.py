import operator, time, math
from euclidean import *
from tkinter import *
from tsp import *

def step(graph, path, cost, iterations, i, wndw):
  wg = weightedGraph(graph)

  # for i in range(1, len(graph)):
  min = 999999.9
  next = 0
  for node in range(1, len(graph)):
    iterations += 1
    prev = path[0]
    if path.count(node) == 0 and wg[prev][node] < min:
      next = node
      min = wg[prev][node]
  cost += min
  wndw.create_line(graph[next][0], graph[next][1], graph[path[0]][0], graph[path[0]][1])
  path = operator.iadd([next], path)

def nearestNeighbor(graph, nameArray):
  # TKINTER #
  root = Tk()
  canvas_height = 800
  canvas_width = 1200
  root.title("Euclidean TSP Solver")
  w = Canvas(root, width = canvas_width, height = canvas_height)
  w.pack(expand = YES, fill=BOTH)
  message = Label(root, text = "Example text")
  message.pack(side=BOTTOM)
  for pair in graph:
    w.create_oval((pair[0], pair[1], pair[0] + 5, pair[1] + 5), fill = "red")
  # TKINTER #

  startTime = time.time()
  path = [0]
  cost = 0.0
  iterations = 0
  wg = weightedGraph(graph)
  i = 1
  def stepper(i):
    step(graph, path, cost, iterations, i, w)
    i += 1

  stepButton = Button(root, text = "Step", command = print("hello"))
  stepButton.pack(side = BOTTOM)
  # cost = 0.0
  # path = [0]
  # wg = weightedGraph(graph)
  # iterations = 0
  # for i in range(1, len(graph)):
  #   min = 999999.9
  #   next = 0
  #   for node in range(1, len(graph)):
  #     iterations += 1
  #     prev = path[0]
  #     if path.count(node) == 0 and wg[prev][node] < min:
  #       next = node
  #       min = wg[prev][node]
  #   cost += min
  #   path = operator.iadd([next], path)
  
  pathString = ""
  pathString += nameArray[path[len(path)-1]] + " -> "
  adjCost = cost + wg[path[0]][0]
  endTime = time.time() - startTime
  for i in range(0, len(path)-1):
    pathString += nameArray[path[i]] + " -> "
  pathString += nameArray[path[len(path)-1]]
  graphSize = len(graph)
  line1 = "\n\nThe optimal path in this {}-city instance using Nearest Neighbor is: \n{}\n\n".format(graphSize, pathString)
  line2 = "This path costs {} units, and required {} iterations in {} seconds \n(running in (n - 1)^2 = n^2 time, where n is the number of cities)\n\n".format(adjCost, iterations, endTime)
  print(line1 + line2)

  # TKINTER #
  root.mainloop()
  # TKINTER #
  
  return path