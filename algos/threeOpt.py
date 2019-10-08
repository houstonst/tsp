import operator, time, math
from algos.euclidean import *
from tkinter import *
from tsp import *

def step(wg, path, cost, unchanged, i, j, k, lineList, wndw, graph):
  pathCopy = path
  costCopy = cost

  if i < j and (i != j-1 or i != j+1):
    if j < k and (j != k-1 or j != k+1):
      a = pathCopy[i]
      b = pathCopy[i+1]
      m = pathCopy[j]
      n = pathCopy[j+1]
      r = pathCopy[k]
      s = pathCopy[k+1]

      oCost = wg[a][b] + wg[m][n]
      cost1 = wg[a][m] + wg[b][n] + wg[r][s]
      cost2 = wg[a][b] + wg[m][r] + wg[n][s]
      cost3 = wg[a][r] + wg[m][n] + wg[b][s]
      cost4 = wg[a][m] + wg[b][r] + wg[n][s]
      cost5 = wg[a][r] + wg[n][b] + wg[m][s]
      cost6 = wg[a][n] + wg[r][m] + wg[b][s]
      cost7 = wg[a][n] + wg[r][b] + wg[m][s]
      pCostList = [cost1, cost2, cost3, cost4, cost5, cost6, cost7]


