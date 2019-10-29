import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

def bruteForce(graph, nameArray, height, width): #return the optimal hamiltonian cycle of a complete graph in O(n!) time
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
  iterations = 0

  def minBranch(graph, traversed): #traverses all paths that branch from the root city
    nonlocal iterations
    prev = traversed[0]            #finds least expensive branch from root
    if (len(traversed) == len(graph)):
      iterations += 1
      retTraversed = operator.iadd([0], traversed)
      return (graph[prev][0], retTraversed)
    else:
      min = 9999999.9
      p = []
      for potential in range(1, len(graph)):
        if traversed.count(potential) == 0:
          altTraversed = operator.iadd([potential], traversed)
          (branchVal, branchPath) = minBranch(graph, altTraversed)
          branchVal += graph[prev][potential]
          if branchVal < min:
            p = branchPath
            min = branchVal
      return (min, p)

  (cost, path) = minBranch(weightedGraph(graph), [0])
  endTime = time.time() - startTime
  adjCost = cost
  pathString = ""
  graphSize = len(graph)
  for i in range(0, len(path)-1):
    pathString += nameArray[path[i]] + " -> "
  pathString += nameArray[path[len(path)-1]]

  line1 = "\n\nThe optimal path in this {}-city instance using Brute Force is: \n{}\n\n".format(graphSize, pathString)
  line2 = "This path costs {} units, and required {} iterations in {} seconds \n(running in (n - 1)! = n! time, where n is the number of cities)\n\n".format(cost, iterations, endTime)
  print(line1 + line2)

  # TKINTER #
  last = graph[path[len(path)-1]] # the last node touched in the path
  for i in range(len(path)-1):
    node = path[i]
    nxt = path[i+1]
    w.create_line(graph[node][0], graph[node][1], graph[nxt][0], graph[nxt][1])
  w.create_line(graph[path[0]][0], graph[path[0]][1], last[0], last[1]) # routes back to the beginning of the path

  root.mainloop()
  # TKINTER #

  return path