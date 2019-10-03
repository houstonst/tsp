import operator, time, math
from algos.euclidean import *

def bruteForce(graph, nameArray): #return the optimal hamiltonian cycle of a complete graph in O(n!) time
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

  return path