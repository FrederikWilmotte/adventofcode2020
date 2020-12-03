# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 3: Toboggan Trajectory ---
# --- Part Two ---

import math


def checkTree(rowTree, realPosition):
    rowLength = len(rowTree)
    rowPosition = calculatePosition(realPosition, rowLength)
    if rowTree[rowPosition - 1:rowPosition] == "#":
        return True


def calculatePosition(realPosition, rowLength):
    rowPosition = realPosition
    while rowPosition > rowLength:
        rowPosition -= rowLength
    return rowPosition


def countTrees(right, down):
    forest = open("toboggan_forest", "r")
    positionNumber = 1
    rowNumber = 1
    nrTrees = 0
    for rowTree in forest:
        rowTree = rowTree.rstrip("\n")
        if (rowNumber == 1) or ((rowNumber - 1) % down == 0):
            if checkTree(rowTree, positionNumber):
                nrTrees += 1
            positionNumber += right
        rowNumber += 1
    return nrTrees


slopes = [countTrees(1, 1), countTrees(3, 1), countTrees(5, 1), countTrees(7, 1), countTrees(1, 2)]
multipleTrees = math.prod(slopes)

print("Number of trees:", multipleTrees)
