# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 5: Binary Boarding ---
# --- Part One ---

def boarding_pass(binarySeat):
    nrRows = [0, 127]
    nrColumns = [0, 7]
    for c in binarySeat:
        if c == "F":
            nrRows[1] = int((nrRows[0] + nrRows[1]) / 2)
            row = nrRows[0]
        elif c == "B":
            nrRows[0] = int(1 + (nrRows[0] + nrRows[1]) / 2)
            row = nrRows[1]
        elif c == "R":
            nrColumns[0] = int(1 + (nrColumns[0] + nrColumns[1]) / 2)
            column = nrColumns[1]
        elif c == "L":
            nrColumns[1] = int((nrColumns[0] + nrColumns[1]) / 2)
            column = nrColumns[0]
    seatId = row * 8 + column
    return row, column, seatId


def highest_seatId(boardingpasses):
    highestSeatId = 0
    for boardingpass in boardingpasses:
        (row, column, seatId) = boarding_pass(boardingpass)
        if seatId > highestSeatId:
            highestSeatId = seatId
    return highestSeatId


boarding_list = open("boarding_list", "r")

boardingpasses = []
for boarding in boarding_list:
    boardingpasses.append(boarding)

print(highest_seatId(boardingpasses))