# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 13: Shuttle Search ---
# --- Part Two ---
# Dodona submission


def get_earliest_timestamp(bus_notes_file):
    bus_notes = read_bus_notes(bus_notes_file)
    timestamp = earliest_timestamp(bus_notes[1])
    return timestamp


def earliest_timestamp(bus_notes):
    active_busses = get_active_busses(bus_notes)
    numbers = active_busses
    remainders = []
    index = 0
    for busses in active_busses:
        if busses == 1:
            remainders.append(0)
        else:
            remainders.append(-index % busses)
        index += 1
    timestamp = chinese_remainder_theorum(numbers, remainders, len(numbers))
    return timestamp


def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 = x1 + m0
    return x1


def chinese_remainder_theorum(num, rem, k):
    prod = 1
    for i in range(0, k):
        prod = prod * num[i]
    result = 0
    for i in range(0, k):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp
    return result % prod


def get_active_busses(busses):
    active_busses = busses.split(",")
    active_busses = [1 if x == "x" else x for x in active_busses]
    active_busses = [int(x) for x in active_busses]
    return active_busses


def read_bus_notes(bus_notes_file):
    bus_notes_output = open(bus_notes_file, "r")
    bus_notes = []
    for bus_note in bus_notes_output:
        bus_notes.append(bus_note.replace("\n", ""))
    return bus_notes
