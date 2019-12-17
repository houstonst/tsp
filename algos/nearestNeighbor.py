import operator, time, math, random
from algos.euclidean import *
from tkinter import *
from tsp import *

def step(initCoords, graph, paths, iterations, i, wndw, option):
  wg = weightedGraph(initCoords)

  for ind in range(len(paths)):
    min = 999999.9
    next = 0
    for node in range(0, len(graph)):
      iterations += 1
      prev = paths[ind][0]
      if paths[ind].count(node) == 0 and wg[prev][node] < min and node != paths[ind][len(paths[ind])-1]:
        next = node
        min = wg[prev][node]
      elif node == paths[ind][len(paths[ind])-1] and len(paths[ind]) == len(graph):
        next = node
        min = wg[prev][node]

    if option == "1":
      wndw.create_line(graph[next][0], graph[next][1], graph[paths[ind][0]][0], graph[paths[ind][0]][1])

    paths[ind] = operator.iadd([next], paths[ind])
  
  return paths

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
  paths = []
  iterations = 0
  i = 1
  wg = weightedGraph(initCoords)

  while len(paths) < 5: #build paths
    temp = random.randrange(len(graph))
    if [temp] not in paths:
      paths += [[temp]]

  def stepper(): #callable function for the step button
    nonlocal i, paths, iterations, graph, w, wg
    if option == "1":
      if i <= len(graph):
        paths = step(initCoords, graph, paths, iterations, i, w, option)
        i += 1
      else:
        bestPath = [[], 999999999.9]
        for path in paths:
          cost = 0.0
          for i in range(0, len(path)-1):
            cost += wg[path[i]][path[i+1]]
          if cost < bestPath[1]:
            bestPath = [path, cost]

        print("Nearest Neighbor Tour: {}, Cost: {}".format(bestPath[0], bestPath[1]))
        return path, cost, 0
    elif option == "2":
      while i <= len(graph):
        w = 0
        paths = step(initCoords, graph, paths, iterations, i, w, option)
        i += 1
      
      worstCost = 0.0
      bestPath = [[], 999999999.9]
      avg = 0.0
      for path in paths:
        cost = 0.0
        for i in range(0, len(path)-1):
          cost += wg[path[i]][path[i+1]]
        avg += cost
        if cost < bestPath[1]:
          bestPath = [path, cost]
        if cost > worstCost:
          worstCost = cost
      avg = avg/5

      runTime = time.time() - startTime
      print("Nearest Neighbor -- Worst Cost: {}, Average Cost: {}, Best Cost: {}, Running Time: {}".format(worstCost, avg, bestPath[1], runTime))
      return bestPath[0], bestPath[1], runTime
      
  if option == "1":
    # TKINTER #
    stepButton = Button(root, text = "Step", command = stepper)
    stepButton.pack(side = BOTTOM)

    root.mainloop()
    # TKINTER #
  
  else:
    path, cost, runtime = stepper()
    return path, cost, runtime