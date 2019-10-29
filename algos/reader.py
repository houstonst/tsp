import csv, re
from tsp import *

def reader(file):
  cityNames = []
  coords = []

  with open(file) as infile:
    csv_reader = csv.reader(infile, delimiter = ',')
    for row in infile:
      rowArray = re.split(",\s*", row)
      coords.append([int(float(rowArray[1])), int(float(rowArray[2]))]) #python cannot convert from string representation
      cityNames.append(rowArray[0])                                     #of a float to an int. Convert to float first.
  
  return cityNames, coords