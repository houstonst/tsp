from win32.win32api import GetSystemMetrics
from algos.reader import *
from algos.bruteForce import *
from algos.nearestNeighbor import *
from algos.farthestInsertion import *
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
Last Edited: 18 NOVEMBER 2019
Filename: tsp.py
Input: .csv or .txt file, formatted in: City Name, Longitude, Latitude
Output: A hamiltonian cycle and complexity data

Enter a .csv or .txt file name ["example.csv or example.txt"]: 
""")
  fileList = ["6.csv", "11.csv", "14.csv", "26.csv", "29.csv", "48.csv", "52.csv", "76.csv", "100.csv", "105.csv", "107.csv", "120.csv", "152.txt", "195.csv", "200.txt", "225.txt", "280.txt", "299.txt", "318.txt", "439.txt"]
  # fileList = ["6.csv", "11.csv", "26.csv", "29.csv", "48.csv", "52.csv", "76.csv", "100.csv", "105.csv", "120.csv", "152.txt", "195.csv", "200.txt", "225.txt", "280.txt", "299.txt", "318.txt", "439.txt"]

  # inp = "./tests/" + input()
  # file = inp
  print("---------------------------------------------------------------------------------------------\n\n")
  # cityNames, coords, newCoords = reader(file, height, width)
  print("---------------------------------------------------------------------------------------------\n\n")
  print("""
1: Brute Force
2: Nearest Neighbor
3: Farthest Insertion
4: Two Opt Interchange
5: Three Opt Interchange (In Progress)
6: Lin-Kernighan


Enter an algorithm by its number:
""")
  algo = input()
  algoPicks = "1234567"

  print("\n")
  print("---------------------------------------------------------------------------------------------\n\n")

  if algo in algoPicks:
    if algo == "1":
      for f in fileList:
        file = "./tests/" + f
        cityNames, coords, newCoords = reader(file, height, width)
        bruteForce(coords, newCoords, cityNames, height, width) #path is the same as the path variable in the algorithm's file
    elif algo == "2":
      print("\n")
      print("---------------------------------------------------------------------------------------------\n\n")
      print("""
1: Run Graphics
2: Run Without Graphics

Enter whether or not to run with GUI
""")
      option = input()
      for f in fileList:
        file = "./tests/" + f
        print("--------------------------------------------------------------------------------------------\n")
        print("\n{}: \n\n".format(file))
        cityNames, coords, newCoords = reader(file, height, width)
        nearestNeighbor(coords, newCoords, cityNames, height, width, option)
    elif algo == "3":
      print("\n")
      print("---------------------------------------------------------------------------------------------\n\n")
      print("""
1: Run Graphics
2: Run Without Graphics

Enter whether or not to run with GUI
""")
      option = input()
      for f in fileList:
        file = "./tests/" + f
        print("--------------------------------------------------------------------------------------------\n")
        print("\n{}: \n\n".format(file))
        cityNames, coords, newCoords = reader(file, height, width)
        farthestInsertion(coords, newCoords, cityNames, height, width, option)
    elif algo == "4":
      print("\n")
      print("---------------------------------------------------------------------------------------------\n\n")
      print("""
1: Run Graphics
2: Run Without Graphics

Enter whether or not to run with GUI
""")
      option = input()
      for f in fileList:
        avgCost = 0.0
        avgTime = 0.0
        file = "./tests/" + f
        print("--------------------------------------------------------------------------------------------\n")
        print("\n{}: \n\n".format(file))
        for i in range(10):
          cityNames, coords, newCoords = reader(file, height, width)
          randPath, randCost, randTime = randomTour(coords, cityNames)          
          path, cost, runtime = twoOpt(coords, newCoords, cityNames, randPath, randCost, height, width, option)
          avgCost += cost
          avgTime += runtime
        avgCost = avgCost/10
        avgTime = avgTime/10
        print("Average cost and time over 10 trials: {}, {}".format(avgCost, avgTime))
    
    elif algo == "5":
      randPath, randCost = randomTour(coords, cityNames)
      threeOpt(coords, cityNames, randPath, randCost, height, width)
    elif algo == "6":
      print("""
1: Random Tour
2: Nearest Neighbor Tour
3: Farthest Insertion Tour

Enter the initial tour constructor by its number:
""")
      constructor = input()
      constPicks = "12"

      print("\n")
      print("---------------------------------------------------------------------------------------------\n\n")
      print("""
1: Run Graphics
2: Run Without Graphics

Enter whether or not to run with GUI
""")
      option = input()
      for f in fileList:
        file = "./tests/" + f
        print("--------------------------------------------------------------------------------------------\n")
        print("\n{}: \n\n".format(file))
        cityNames, coords, newCoords = reader(file, height, width)

        if constructor in constPicks:
          if constructor == "1":
            initPath, initCost, runtime = randomTour(coords, cityNames)
            linKernighan(coords, newCoords, cityNames, initPath, initCost, height, width, option)
          elif constructor == "2":
            initPath, initCost, runtime = nearestNeighbor(coords, newCoords, cityNames, height, width, option)
            linKernighan(coords, newCoords, cityNames, initPath, initCost, height, width, option)
          elif constructor == "3":
            initPath, initCost, runtime = farthestInsertion(coords, newCoords, cityNames, height, width, option)
            linKernighan(coords, newCoords, cityNames, initPath, initCost, height, width, option)
        else:
          print("Exiting. Must enter a constructor number given by the list above")
      
    elif algo == "7":
      for f in fileList:
        avgCost = 0.0
        avgTime = 0.0
        file = "./tests/" + f
        print("--------------------------------------------------------------------------------------------\n")
        print("\n{}: \n\n".format(file))
        for i in range(10):
          cityNames, coords, newCoords = reader(file, height, width)
          path, cost, runtime = randomTour(coords, cityNames)
          avgCost += cost
          avgTime += runtime
        avgCost = avgCost/10
        avgTime = avgTime/10
        print("Average cost and time over 10 trials: {}, {}".format(avgCost, avgTime))
        
        print("-----------------------------------------------------------------\n")
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