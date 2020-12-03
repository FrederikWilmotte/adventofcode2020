# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 3: Toboggan Trajectory ---
# --- Part Two ---

import math

forest = open("toboggan_forest", "r")

def checkTree(rowTree, position):
    rowPosition = position % len(rowTree)
    if rowTree[rowPosition:rowPosition+1] == "#":
        return True

def countTrees(right, down):
    forest.seek(0)
    position = 0
    row = 1
    nrTrees = 0
    for rowTree in forest:
        rowTree = rowTree.rstrip("\n")
        if (row == 1) or ((row - 1) % down == 0):
            if checkTree(rowTree, position):
                nrTrees += 1
            position += right
        row += 1
    return nrTrees


slopes = [countTrees(1, 1), countTrees(3, 1), countTrees(5, 1), countTrees(7, 1), countTrees(1, 2)]
multipleTrees = math.prod(slopes)

print("Number of trees:", multipleTrees)
