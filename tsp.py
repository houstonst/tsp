import csv
from bruteForce import *
from nearestNeighbor import *
from farthestInsertion import *
from tkinter import *

def main():
  # root = Tk()
  # canvas_height = 700
  # canvas_width = 1200
  # root.title("Euclidean TSP Solver")
  # w = Canvas(root, width = canvas_width, height = canvas_height)
  # w.pack(expand = YES, fill=BOTH)
  # message = Label(root, text = "Example text")
  # message.pack(side=BOTTOM)

  print("""
EUCLIDEAN TSP SOLVER:

Author: Matt Houston
Last Edited: 16 SEPTEMBER 2019
Filename: tsp.py
Input: CSV file, formatted in: City Name, Longitude, Latitude
Output: A hamiltonian cycle and complexity data

Enter a CSV file ["example.csv"]: 
""")
  file = input()
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
    # for pair in coords:
    #   w.create_oval((pair[0], pair[1], pair[0] + 5, pair[1] + 5), fill = "red")
    print("---------------------------------------------------------------------------------------------\n\n")
    print("""
1: Brute Force
2: Nearest Neighbor
3: Farthest Insertion


Enter an algorithm by its number:
""")
    algo = input()

    print("\n")
    print("---------------------------------------------------------------------------------------------\n\n")

    if algo == "1" or algo == "2" or algo == "3":
      if algo == "1":
        path = bruteForce(coords, cityNames) # path is the same as the path variable in the algorithm's file
        last = coords[path[len(path)-1]] # the last node touched in the path
        for i in range(len(path)-1):
          node = path[i]
          nxt = path[i+1]
          w.create_line(coords[node][0], coords[node][1], coords[nxt][0], coords[nxt][1])
        w.create_line(coords[path[0]][0], coords[path[0]][1], last[0], last[1]) # routes back to the beginning of the path
      elif algo == "2":
        nearestNeighbor(coords, cityNames) # path is the same as the path variable in the algorithm's file
        # last = coords[path[len(path)-1]] # the last node touched in the path
        # for i in range(len(path)-1):
        #   node = path[i]
        #   nxt = path[i+1]
        #   w.create_line(coords[node][0], coords[node][1], coords[nxt][0], coords[nxt][1])
        # w.create_line(coords[path[0]][0], coords[path[0]][1], last[0], last[1]) # routes back to the beginning of the path
      elif algo == "3":
        path = farthestInsertion(coords, cityNames) # path is the same as the path variable in the algorithm's file
        last = coords[path[len(path)-1]] # the last node touched in the path
        for i in range(len(path)-1):
          node = path[i]
          nxt = path[i+1]
          w.create_line(coords[node][0], coords[node][1], coords[nxt][0], coords[nxt][1])
        w.create_line(coords[path[0]][0], coords[path[0]][1], last[0], last[1]) # routes back to the beginning of the path
    else:
      print("Enter an algorithm number given by the list above")

  #root.mainloop()
  
if __name__ == "__main__":
  main()
  print("---------------------------------------------------------------------------------------------\n\n")


# GUI References:
# https://stackoverflow.com/questions/39888580/how-can-i-draw-a-point-with-canvas-in-tkinter
# https://tkdocs.com/tutorial/canvas.html#creating
