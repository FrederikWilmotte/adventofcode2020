# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 3: Toboggan Trajectory ---
# --- Part One ---
# Dodona submission

def count_trees(slopesFile):
    forest = open(slopesFile, "r")
    nrTrees = 0
    position = 0
    row = 1
    right = 3
    down = 1
    for rowTree in forest:
        rowTree = rowTree.rstrip("\n")
        if (row == 1) or ((row - 1) % down == 0):
            if checkTree(rowTree, position):
                nrTrees += 1
            position += right
        row += 1
    return nrTrees

def checkTree(rowTree, position):
    rowPosition = position % len(rowTree)
    if rowTree[rowPosition:rowPosition+1] == "#":
        return True