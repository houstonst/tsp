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

      oCost = wg[a][b] + wg[m][n] + wg[r][s]
      cost1 = wg[a][m] + wg[b][n] + wg[r][s]
      cost2 = wg[a][b] + wg[m][r] + wg[n][s]
      cost3 = wg[a][r] + wg[m][n] + wg[b][s]
      cost4 = wg[a][m] + wg[b][r] + wg[n][s]
      cost5 = wg[a][r] + wg[n][b] + wg[m][s]
      cost6 = wg[a][n] + wg[r][m] + wg[b][s]
      cost7 = wg[a][n] + wg[r][b] + wg[m][s]
      pCostList = [oCost, cost1, cost2, cost3, cost4, cost5, cost6, cost7]

      bestCost = min(pCostList)
      if bestCost == cost1: #need to update paths appropriately
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

        costCopy = costCopy - oCost + cost1
      elif bestCost == cost2:
        if (r, s) in lineList.keys():
          wndw.delete(lineList[(r, s)])
          del lineList[(r, s)]
        elif (s, r) in lineList.keys():
          wndw.delete(lineList[(s, r)])
          del lineList[(s, r)]
        if (m, n) in lineList.keys():
          wndw.delete(lineList[(m, n)])
          del lineList[(m, n)]
        elif (n, m) in lineList.keys():
          wndw.delete(lineList[(n, m)])
          del lineList[(n, m)] 
        x = wndw.create_line(graph[m][0], graph[m][1], graph[r][0], graph[r][1])
        y = wndw.create_line(graph[n][0], graph[n][1], graph[s][0], graph[s][1])
        lineList.update({(m, r): x})
        lineList.update({(n, s): y})

        pathCopySlice = pathCopy[j+1:k]
        pathCopy = pathCopy[0:j+1] + [pathCopy[k]] + pathCopySlice[::-1] + pathCopy[k+1:]

        costCopy = costCopy - oCost + cost2
      elif bestCost == cost3:
        if (a, b) in lineList.keys():
          wndw.delete(lineList[(a, b)])
          del lineList[(a, b)]
        elif (b, a) in lineList.keys():
          wndw.delete(lineList[(b, a)])
          del lineList[(b, a)]
        if (r, s) in lineList.keys():
          wndw.delete(lineList[(r, s)])
          del lineList[(r, s)]
        elif (s, r) in lineList.keys():
          wndw.delete(lineList[(s, r)])
          del lineList[(s, r)] 
        x = wndw.create_line(graph[a][0], graph[a][1], graph[r][0], graph[r][1])
        y = wndw.create_line(graph[b][0], graph[b][1], graph[s][0], graph[s][1])
        lineList.update({(a, r): x})
        lineList.update({(b, s): y})

        pathCopySlice = pathCopy[j+1:k]
        pathCopy = pathCopy[0:i+1] + [pathCopy[k]] + pathCopySlice[::-1] + pathCopy[i+1]

        costCopy = costCopy - oCost + cost3     
      elif bestCost == cost4:
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
        if (r, s) in lineList.keys():
          wndw.delete(lineList[(r, s)])
          del lineList[(r, s)]
        elif (s, r) in lineList.keys():
          wndw.delete(lineList[(s, r)])
          del lineList[(s, r)] 
        x = wndw.create_line(graph[a][0], graph[a][1], graph[m][0], graph[m][1])
        y = wndw.create_line(graph[b][0], graph[b][1], graph[r][0], graph[r][1])
        z = wndw.create_line(graph[n][0], graph[n][1], graph[s][0], graph[s][1])
        lineList.update({(a, m): x})
        lineList.update({(b, r): y})
        lineList.update({(n, s): z})

        # pathCopySlice = pathCopy[i+1:j]
        # pathCopy = pathCopy[0:i+1] + [pathCopy[j]] + pathCopySlice[::-1] + pathCopy[j+1:]

        costCopy = costCopy - oCost + cost4
      elif bestCost == cost5:
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
        if (r, s) in lineList.keys():
          wndw.delete(lineList[(r, s)])
          del lineList[(r, s)]
        elif (s, r) in lineList.keys():
          wndw.delete(lineList[(s, r)])
          del lineList[(s, r)] 
        x = wndw.create_line(graph[a][0], graph[a][1], graph[r][0], graph[r][1])
        y = wndw.create_line(graph[n][0], graph[n][1], graph[b][0], graph[b][1])
        z = wndw.create_line(graph[m][0], graph[m][1], graph[s][0], graph[s][1])
        lineList.update({(a, r): x})
        lineList.update({(n, b): y})
        lineList.update({(m, s): z})

        # pathCopySlice = pathCopy[i+1:j]
        # pathCopy = pathCopy[0:i+1] + [pathCopy[j]] + pathCopySlice[::-1] + pathCopy[j+1:]

        costCopy = costCopy - oCost + cost5
      elif bestCost == cost6:
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
        if (r, s) in lineList.keys():
          wndw.delete(lineList[(r, s)])
          del lineList[(r, s)]
        elif (s, r) in lineList.keys():
          wndw.delete(lineList[(s, r)])
          del lineList[(s, r)] 
        x = wndw.create_line(graph[a][0], graph[a][1], graph[n][0], graph[n][1])
        y = wndw.create_line(graph[r][0], graph[r][1], graph[m][0], graph[m][1])
        z = wndw.create_line(graph[b][0], graph[b][1], graph[s][0], graph[s][1])
        lineList.update({(a, n): x})
        lineList.update({(r, m): y})
        lineList.update({(b, s): z})

        # pathCopySlice = pathCopy[i+1:j]
        # pathCopy = pathCopy[0:i+1] + [pathCopy[j]] + pathCopySlice[::-1] + pathCopy[j+1:]

        costCopy = costCopy - oCost + cost6
      elif bestCost == cost7:
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
        if (r, s) in lineList.keys():
          wndw.delete(lineList[(r, s)])
          del lineList[(r, s)]
        elif (s, r) in lineList.keys():
          wndw.delete(lineList[(s, r)])
          del lineList[(s, r)] 
        x = wndw.create_line(graph[a][0], graph[a][1], graph[n][0], graph[n][1])
        y = wndw.create_line(graph[r][0], graph[r][1], graph[b][0], graph[b][1])
        z = wndw.create_line(graph[m][0], graph[m][1], graph[s][0], graph[s][1])
        lineList.update({(a, n): x})
        lineList.update({(r, b): y})
        lineList.update({(m, s): z})

        # pathCopySlice = pathCopy[i+1:j]
        # pathCopy = pathCopy[0:i+1] + [pathCopy[j]] + pathCopySlice[::-1] + pathCopy[j+1:]

        costCopy = costCopy - oCost + cost7

def threeOpt(graph, nameArray, path, cost):
  return