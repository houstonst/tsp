import tsp
from euclidean import *
from nearestNeighbor import *

def genPath(algo):
  coords = tsp.main().coords
  cityNames = tsp.main().cityNames
  w = tsp.main().coords
  if algo == "2":
    path = nearestNeighbor(coords, cityNames) # path is the same as the path variable in the algorithm's file
    last = coords[path[len(path)-1]] # the last node touched in the path
    for i in range(len(path)-1):
      node = path[i]
      nxt = path[i+1]
      w.create_line(coords[node][0], coords[node][1], coords[nxt][0], coords[nxt][1])
    w.create_line(coords[path[0]][0], coords[path[0]][1], last[0], last[1]) # routes back to the beginning of the path