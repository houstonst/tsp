import math

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