import operator, time, math
from euclidean import *
from tkinter import *
from tsp import *

def twoOpt(graph, nameArray, path, cost): #run until no improvement is made
  # TKINTER #
  root = Tk()
  canvas_height = 750
  canvas_width = 1200
  root.title("Euclidean TSP Solver")
  root.iconbitmap('favicon.ico')
  w = Canvas(root, width = canvas_width, height = canvas_height)
  w.pack(expand = YES, fill=BOTH)
  for pair in graph:
    index = graph.index(pair)
    name = nameArray[index]
    w.create_oval((pair[0]-3, pair[1]-3, pair[0] + 3, pair[1] + 3), fill = "red")
    w.create_text(pair[0], pair[1] - 12, fill = "black", font = "Times 10 bold", text = name)
  # TKINTER #

  wg = weightedGraph(graph)
  pathCopy = path
  costCopy = cost
  unchanged = False

  print(path)
  print(cost)
  
  while (unchanged == False):
    unchanged = True
    for i in range(0, (len(pathCopy)-1)//2):
      for j in range(0, len(pathCopy)-1):
        if i != j and (i != j-1 or i != j+1):
          a = pathCopy[i]
          b = pathCopy[i+1]
          m = pathCopy[j]
          n = pathCopy[j+1]
          oCost = wg[a][b] + wg[m][n]
          pCost = wg[a][m] + wg[b][n]
          if pCost < oCost:
            pathCopySlice = pathCopy[i+1:j]
            pathCopy = pathCopy[0:i+1] + [pathCopy[j]] + pathCopySlice[::-1] + pathCopy[j+1:]
            costCopy = costCopy - oCost + pCost
            #unchanged = False

  print(pathCopy)
  print(costCopy)

  last = graph[pathCopy[len(pathCopy)-1]] # the last node touched in the pathCopy
  for i in range(len(pathCopy)-1):
    node = pathCopy[i]
    nxt = pathCopy[i+1]
    w.create_line(graph[node][0], graph[node][1], graph[nxt][0], graph[nxt][1])
  w.create_line(graph[pathCopy[0]][0], graph[pathCopy[0]][1], last[0], last[1]) # routes back to the beginning of the path

  # TKINTER #
  root.mainloop()
  # TKINTER #

  return pathCopy, costCopy