from win32.win32api import GetSystemMetrics
from algos.reader import *
from algos.bruteForce import *
from algos.nearestNeighbor import *
from algos.farthestInsertion import *
from algos.farthestInsertion_NG import *
from algos.randomTour import *
from algos.twoOpt import *
from algos.threeOpt import *
from algos.linKernighan import *
from tkinter import *

def main():
  height = GetSystemMetrics(1) - 200
  width = GetSystemMetrics(0) - 200

  print("""
EUCLIDEAN TSP SOLVER:

Author: Matt Houston
Last Edited: 29 OCTOBER 2019
Filename: tsp.py
Input: CSV file, formatted in: City Name, Longitude, Latitude
Output: A hamiltonian cycle and complexity data

Enter a CSV file ["example.csv"]: 
""")
  inp = "./tests/" + input()
  file = inp
  print("---------------------------------------------------------------------------------------------\n\n")
  cityNames, coords = reader(file, height, width)
  print("---------------------------------------------------------------------------------------------\n\n")
  print("""
1: Brute Force
2: Nearest Neighbor
3: Farthest Insertion
4: Two Opt Interchange
5: Three Opt Interchange (In Progress)
6: Lin-Kernighan (In Progress)


Enter an algorithm by its number:
""")
  algo = input()
  algoPicks = "123456"

  print("\n")
  print("---------------------------------------------------------------------------------------------\n\n")

  if algo in algoPicks:
    if algo == "1":
      bruteForce(coords, cityNames, height, width) #path is the same as the path variable in the algorithm's file
    elif algo == "2":
      nearestNeighbor(coords, cityNames, height, width)
    elif algo == "3":
      farthestInsertion(coords, cityNames, height, width)
    elif algo == "4":
      randPath, randCost = randomTour(coords, cityNames)
      twoOpt(coords, cityNames, randPath, randCost, height, width)
    elif algo == "5":
      randPath, randCost = randomTour(coords, cityNames)
      threeOpt(coords, cityNames, randPath, randCost, height, width)
    elif algo == "6":
      print("""
1: Random Tour
2: Farthest Insertion Tour

Enter the initial tour constructor by its number:
""")
      constructor = input()
      constPicks = "12"

      print("\n")
      print("---------------------------------------------------------------------------------------------\n\n")

      if constructor in constPicks:
        if constructor == "1":
          initPath, initCost = randomTour(coords, cityNames)
          linKernighan(coords, cityNames, initPath, initCost, height, width)
        elif constructor == "2":
          initPath, initCost = farthestInsertion_NG(coords, cityNames)
          linKernighan(coords, cityNames, initPath, initCost, height, width)
      else:
        print("Exiting. Must enter a constructor number given by the list above")
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