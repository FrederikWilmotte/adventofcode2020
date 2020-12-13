# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 13: Shuttle Search ---
# --- Part Two ---

from sympy.ntheory.modular import crt


def get_earliest_timestamp(bus_notes_file):
    bus_notes = read_bus_notes(bus_notes_file)
    active_busses = get_active_busses(bus_notes[1])
    numbers = active_busses
    remainders = []
    index = 0
    for busses in active_busses:
        if busses == 1:
            remainders.append(0)
        else:
            remainders.append(-index % busses)
        index += 1
    print(remainders)
    earliest_timestamp = crt(numbers, remainders)[0]
    return earliest_timestamp


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


print(get_earliest_timestamp("bus_notes_test"))
print(get_earliest_timestamp("bus_notes_test2"))
print(get_earliest_timestamp("bus_notes_test3"))
print(get_earliest_timestamp("bus_notes_test4"))
print(get_earliest_timestamp("bus_notes_test5"))
print(get_earliest_timestamp("bus_notes_test6"))
print(get_earliest_timestamp("bus_notes"))