# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 3: Toboggan Trajectory ---
# --- Part Two ---
# Dodona submission

def count_trees(right, down, slopesFile):
    forest = open(slopesFile, "r")
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

def checkTree(rowTree, position):
    rowPosition = position % len(rowTree)
    if rowTree[rowPosition:rowPosition+1] == "#":
        return True
