# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 3: Toboggan Trajectory ---
# --- Part One ---

forest = open("toboggan_forest", "r")

def checkTree(rowTree, realPosition):
    rowLength = len(rowTree)
    rowPosition = calculatePosition(realPosition, rowLength)
    if rowTree[rowPosition-1:rowPosition] == "#":
        return True

def calculatePosition(realPosition, rowLength):
    rowPosition = realPosition
    while rowPosition > rowLength:
        rowPosition -= rowLength
    return rowPosition

nrTrees = 0
positionNumber = 1
rowNumber = 1
countPosition = 3
countRow = 1
for rowTree in forest:
    rowTree = rowTree.rstrip("\n")
    if (rowNumber == 1) or ((rowNumber-1) % countRow == 0):
        if checkTree(rowTree, positionNumber):
            nrTrees += 1
        positionNumber += countPosition
    rowNumber += 1

print("Number of trees:",nrTrees)