import csv
from bruteForce import *
from nearestNeighbor import *
from farthestInsertion import *
from tkinter import *

def main():
  root = Tk()
  canvas_height = 800
  canvas_width = 1200
  root.title("Euclidean TSP Solver")
  w = Canvas(root, width = canvas_width, height = canvas_height)
  w.pack(expand = YES, fill=BOTH)
  message = Label(root, text = "Example text")
  message.pack(side=BOTTOM)


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
3: Farthest Insertion


Enter an algorithm by its number:
""")
  algo = input()
  cityNames = []
  coordPairs = []

  print("\n")
  print("---------------------------------------------------------------------------------------------\n\n")

  if algo == "1" or algo == "2" or algo == "3":
    with open(file) as infile:
      csv_reader = csv.reader(infile, delimiter=',')
      for row in infile:
        print(row)
        rowArray = row.split(",")
        coordPairs.append([int(rowArray[1]), int(rowArray[2])])
        cityNames.append(rowArray[0])
      for pair in coordPairs:
        w.create_oval((pair[0], pair[1], pair[0] + 5, pair[1] + 5), fill = "red")

      print("---------------------------------------------------------------------------------------------\n\n")
    if algo == "1":
      bruteForce(coordPairs, cityNames)
    elif algo == "2":
      nearestNeighbor(coordPairs, cityNames)
    elif algo == "3":
      farthestInsertion(coordPairs, cityNames)
  else:
    print("Enter an algorithm number given by the list above")


  root.mainloop()
  
if __name__ == "__main__":
  main()
  print("---------------------------------------------------------------------------------------------\n\n")


# GUI References:
# https://stackoverflow.com/questions/39888580/how-can-i-draw-a-point-with-canvas-in-tkinter
# https://tkdocs.com/tutorial/canvas.html#creating
