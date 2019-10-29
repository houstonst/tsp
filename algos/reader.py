import csv, re
from tsp import *

def reader(file, height, width):
  cityNames = []
  coords = []

  with open(file) as infile:
    csv_reader = csv.reader(infile, delimiter = ',')
    for row in infile:
      rowArray = re.split(",\s*", row)
      coords.append([int(float(rowArray[1])), int(float(rowArray[2]))]) #python cannot convert from string representation
      cityNames.append(rowArray[0])                                     #of a float to an int. Convert to float first.
  
  coords = fitter(coords, height, width)
  return cityNames, coords


def fitter(coords, height, width): #force coordinates to fit GUI window size
  maxWidth = 0
  maxHeight = 0
  widthMult = 1
  heightMult = 1

  for coord in coords:
    if coord[0] > maxWidth:
      maxWidth = coord[0]
    if coord[1] > maxHeight:
      maxHeight = coord[1]

  if maxWidth >= width - 100:
    widthMult = (width-100)/maxWidth
  if maxHeight >= height - 100:
    heightMult = (height-100)/maxHeight

  for coord in coords:
    coord[0] = coord[0]*widthMult
    coord[1] = coord[1]*heightMult
  
  return coords