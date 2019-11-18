import csv, re
from tsp import *

def reader(file, height, width):
  cityNames = []
  coords = []
  newCoords = []

  with open(file) as infile:
    # csv_reader = csv.reader(infile, delimiter = ',')
    for row in infile:
      rowArray = re.split(",*\s*", row)
      coords.append([int(float(rowArray[1])), int(float(rowArray[2]))])    #python cannot convert from string representation
      newCoords.append([int(float(rowArray[1])), int(float(rowArray[2]))]) #of a float to an int. Convert to float first.
      cityNames.append(rowArray[0])                                     
  
  newCoords = fitter(newCoords, height, width)
  return cityNames, coords, newCoords


def fitter(coords, GUIheight, GUIwidth): #force coordinates to fit GUI window size
  maxX = 0
  maxY = 0
  minX = 999999
  minY = 999999
  origin = (100, GUIheight-100)
  multiplier = 1
  expand = False
  shrink = False

  #find the node furthest left, right, up, and down
  for coord in coords:
    if coord[0] > maxX:
      maxX = coord[0]
    if coord[0] < minX:
      minX = coord[0]
    if coord[1] > maxY:
      maxY = coord[1]
    if coord[1] < minY:
      minY = coord[1]

  #shrink or expand the size of the graph based on the window size, not the GUI itself
  arbitraryXstart = minX + GUIwidth - 200
  arbitraryYstart = minY + GUIheight - 200
  arbitraryXdiff = maxX - arbitraryXstart
  arbitraryYdiff = maxY - arbitraryYstart

  if arbitraryXdiff > 0 and arbitraryXdiff > arbitraryYdiff:
    #shrink on x
    multiplier = (GUIwidth - 200)/(maxX - minX)
  elif arbitraryXdiff < 0 and arbitraryXdiff > arbitraryYdiff:
    #expand on x
    multiplier = (GUIwidth - 200)/(maxX - minX)
  elif arbitraryYdiff > 0 and arbitraryYdiff > arbitraryXdiff:
    #shrink on y
    multiplier = (GUIheight - 200)/(maxY - minY)
  elif arbitraryYdiff < 0 and arbitraryYdiff > arbitraryXdiff:
    #expand on y
    multiplier = (GUIheight - 200)/(maxY - minY)

  for coord in coords:
    coord[0] = coord[0]*multiplier
    coord[1] = coord[1]*multiplier

  #reset the min and max values
  maxX = 0
  maxY = 0
  minX = 999999
  minY = 999999

  for coord in coords:
    if coord[0] > maxX:
      maxX = coord[0]
    if coord[0] < minX:
      minX = coord[0]
    if coord[1] > maxY:
      maxY = coord[1]
    if coord[1] < minY:
      minY = coord[1]

  #rerun expansion/shrinking in case a dimension continues
  #to expand beyond GUI
  multiplier = 1
  arbitraryXstart = minX + GUIwidth - 200
  arbitraryYstart = minY + GUIheight - 200
  arbitraryXdiff = maxX - arbitraryXstart
  arbitraryYdiff = maxY - arbitraryYstart

  if arbitraryXdiff > 0 and arbitraryXdiff > arbitraryYdiff:
    #shrink on x
    multiplier = (GUIwidth - 200)/(maxX - minX)
  elif arbitraryXdiff < 0 and arbitraryXdiff > arbitraryYdiff:
    #expand on x
    multiplier = (GUIwidth - 200)/(maxX - minX)
  elif arbitraryYdiff > 0 and arbitraryYdiff > arbitraryXdiff:
    #shrink on y
    multiplier = (GUIheight - 200)/(maxY - minY)
  elif arbitraryYdiff < 0 and arbitraryYdiff > arbitraryXdiff:
    #expand on y
    multiplier = (GUIheight - 200)/(maxY - minY)

  for coord in coords:
    coord[0] = coord[0]*multiplier
    coord[1] = coord[1]*multiplier

  #reset the min and max values
  maxX = 0
  maxY = 0
  minX = 999999
  minY = 999999

  for coord in coords:
    if coord[0] > maxX:
      maxX = coord[0]
    if coord[0] < minX:
      minX = coord[0]
    if coord[1] > maxY:
      maxY = coord[1]
    if coord[1] < minY:
      minY = coord[1]

  #furthest left node shifted to be directly over origin.
  #furthest down node shifted to be directly besides origin.
  #all other nodes shifted by the same constants.
  xDiff = minX - origin[0]
  yDiff = maxY - origin[1]

  for coord in coords:
    coord[0] -= xDiff
    coord[1] -= yDiff

  return coords