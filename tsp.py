import math, time, operator, csv

def distance(p1, p2): #return distance between two cartesian coordinates. Usage: distance((1,1),(2,2))
    a = abs(p1[0] - p2[0]) #horizontal displacement
    b = abs(p1[1] - p2[1]) #vertical displacement
    return math.sqrt(a*a + b*b)

def weightedGraph(cityArray):
    retMatrix = [[0.0 for _ in range(len(cityArray))] for _ in range(len(cityArray))] #build empty 2D matrix
    for i in range(0, len(cityArray)):
      for j in range(0, len(cityArray)):
        retMatrix[i][j] = distance(cityArray[i], cityArray[j]) #populate the 2D matrix with euclidean distances
    return retMatrix

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

def nearestNeighbor(graph, nameArray):
  startTime = time.time()
  cost = 0.0
  path = [0]
  wg = weightedGraph(graph)
  iterations = 0
  for i in range(1, len(graph)):
    min = 999999.9
    next = 0
    for node in range(1, len(graph)):
      iterations += 1
      prev = path[0]
      if path.count(node) == 0 and wg[prev][node] < min:
        next = node
        min = wg[prev][node]
    cost += min
    path = operator.iadd([next], path)
  
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

def main():
  print("""
EUCLIDEAN TSP SOLVER:

Author: Matt Houston
Last Edited: 29 AUGUST 2019
Filename: tsp.py
Input: CSV file, formatted in: City Name, Longitude, Latitude
Output: Optimal hamiltonian cycle and cost

Enter a CSV file ["example.csv"]: 
""")
  file = input()
  print("---------------------------------------------------------------------------------------------\n\n")
  print("""
1: Brute Force
2: Nearest Neighbor


Enter an algorithm by its number:
""")
  algo = input()
  coordPairs = []
  cityNames = []

  print("\n")
  print("---------------------------------------------------------------------------------------------\n\n")

  if algo == "1" or algo == "2":
    with open(file) as infile:
      csv_reader = csv.reader(infile, delimiter=',')
      for row in infile:
        print(row)
        rowArray = row.split(",")
        coordPairs.append([int(rowArray[1]), int(rowArray[2])])
        cityNames.append(rowArray[0])
      print("---------------------------------------------------------------------------------------------\n\n")
    if algo == "1":
      bruteForce(coordPairs, cityNames)
    elif algo == "2":
      nearestNeighbor(coordPairs, cityNames)
  else:
    print("Enter an algorithm number given by the list above")
if __name__ == "__main__":
  main()
  print("---------------------------------------------------------------------------------------------\n\n")
