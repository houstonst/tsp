import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

def step(graph, path, cost, iterations, i, wndw):
  wg = weightedGraph(graph)
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
  return (path, cost, iterations)

def nearestNeighbor(graph, nameArray, height, width):
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
  wg = weightedGraph(graph)
  i = 1

  def stepper(): #callable function for the step button
    nonlocal i, path, cost, iterations, graph
    if i <= len(graph):
      path, cost, iterations = step(graph, path, cost, iterations, i, w)
      i += 1

  # TKINTER #
  stepButton = Button(root, text = "Step", command = stepper)
  stepButton.pack(side = BOTTOM)

  root.mainloop()
  # TKINTER #
  
  return path