# https://dodona.ugent.be/nl/courses/414/series/4215/activities/1124537225
# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 5: Binary Boarding ---
# --- Part two ---


def seat_id(binarySeat):
    rownr = row(binarySeat)
    columnnr = column(binarySeat)
    seat_id = rownr * 8 + columnnr
    return seat_id


def row(binarySeat):
    nrRows = [0, 127]
    for c in binarySeat:
        if c == "F":
            nrRows[1] = int((nrRows[0] + nrRows[1]) / 2)
            rownr = nrRows[0]
        elif c == "B":
            nrRows[0] = int(1 + (nrRows[0] + nrRows[1]) / 2)
            rownr = nrRows[1]
    return rownr


def column(binarySeat):
    nrColumns = [0, 7]
    for c in binarySeat:
        if c == "R":
            nrColumns[0] = int(1 + (nrColumns[0] + nrColumns[1]) / 2)
            columnnr = nrColumns[1]
        elif c == "L":
            nrColumns[1] = int((nrColumns[0] + nrColumns[1]) / 2)
            columnnr = nrColumns[0]
    return columnnr


def missing_seat_id(boardinglist):
    boardingpasses = open(boardinglist, "r")
    occupiedSeats = []
    for boardingpass in boardingpasses:
        occupiedSeats.append(seat_id(boardingpass))
    occupiedSeats.sort()
    previousSeatId = occupiedSeats[0]
    for seatId in occupiedSeats:
        if seatId == previousSeatId + 2:
            missingSeatId = seatId - 1
        previousSeatId = seatId
    return missingSeatId

print(missing_seat_id("boarding_list"))