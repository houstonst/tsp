import operator, time, math
from euclidean import *
from tkinter import *
from tsp import *

def twoOpt(graph, nameArray, path, cost):
  wg = weightedGraph(graph)
  newPath = []
  newCost = 0.0

  print(path)
  print(cost)

  for i in range(0, len(path)-1):
    for j in range(0, len(path)-1):
      if i != j and (i != j-1 or i != j+1):
        a = path[i]
        b = path[i+1]
        m = path[j]
        n = path[j+1]
        oCost = wg[a][b] + wg[m][n]
        pCost = wg[a][m] + wg[b][n]
        if pCost < oCost:
          revSection = path[i+1:j+1].reverse()
          #newPath = path[0:i+1] + [path[j]] + path[j+1:]
          newCost = cost - oCost + pCost

  print(newPath)
  print(newCost)
  return newPath, newCost