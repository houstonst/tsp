import csv
from algos.bruteForce import *
from algos.nearestNeighbor import *
from algos.farthestInsertion import *
from algos.randomTour import *
from algos.twoOpt import *
from algos.linKernighan import *
from tkinter import *

def main():
  print("""
EUCLIDEAN TSP SOLVER:

Author: Matt Houston
Last Edited: 08 OCTOBER 2019
Filename: tsp.py
Input: CSV file, formatted in: City Name, Longitude, Latitude
Output: A hamiltonian cycle and complexity data

Enter a CSV file ["example.csv"]: 
""")
  inp = "./tests/" + input()
  file = inp
  cityNames = []
  coords = []
  print("---------------------------------------------------------------------------------------------\n\n")
  with open(file) as infile:
    csv_reader = csv.reader(infile, delimiter=',')
    for row in infile:
      print(row)
      rowArray = row.split(",")
      coords.append([int(rowArray[1]), int(rowArray[2])])
      cityNames.append(rowArray[0])
    print("---------------------------------------------------------------------------------------------\n\n")
    print("""
1: Brute Force
2: Nearest Neighbor
3: Farthest Insertion
4: Two Opt Interchange
5: Lin-Kernighan


Enter an algorithm by its number:
""")
    algo = input()
    algoPicks = "12345"

    print("\n")
    print("---------------------------------------------------------------------------------------------\n\n")

    if algo in algoPicks:
      if algo == "1":
        path = bruteForce(coords, cityNames) # path is the same as the path variable in the algorithm's file
        last = coords[path[len(path)-1]] # the last node touched in the path
        for i in range(len(path)-1):
          node = path[i]
          nxt = path[i+1]
          w.create_line(coords[node][0], coords[node][1], coords[nxt][0], coords[nxt][1])
        w.create_line(coords[path[0]][0], coords[path[0]][1], last[0], last[1]) # routes back to the beginning of the path
      elif algo == "2":
        nearestNeighbor(coords, cityNames)
      elif algo == "3":
        farthestInsertion(coords, cityNames)
      elif algo == "4":
        randPath, randCost = randomTour(coords, cityNames)
        twoOpt(coords, cityNames, randPath, randCost)
      elif algo == "5":
        initPath, initCost = randomTour(coords, cityNames)
        linKernighan(coords, cityNames, initPath, initCost)
    else:
      print("Exiting. Must enter an algorithm number given by the list above")
if __name__ == "__main__":
  main()
  print("---------------------------------------------------------------------------------------------\n\n")


# GUI References:
# https://stackoverflow.com/questions/39888580/how-can-i-draw-a-point-with-canvas-in-tkinter
# https://tkdocs.com/tutorial/canvas.html#creating
# https://stackoverflow.com/questions/42333288/how-to-delete-lines-using-tkinter
# https://stackoverflow.com/questions/17736967/python-how-to-add-text-inside-a-canvas

# Algorithm References:
# https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
