# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 13: Shuttle Search ---
# --- Part One ---
# Dodona submission

def bus_multiplication(bus_notes_file):
    bus_notes = read_bus_notes(bus_notes_file)
    bus_answer = departure(int(bus_notes[0]), bus_notes[1])
    return bus_answer


def departure(timestamp_arrival, busses):
    active_busses = get_active_busses(busses)
    waiting_minutes = 0
    bus_id = 0
    for active_bus in active_busses:
        if bus_id == 0:
            waiting_minutes = waiting_time(timestamp_arrival, active_bus)
            bus_id = active_bus
        elif waiting_time(timestamp_arrival, active_bus) < waiting_minutes:
            waiting_minutes = waiting_time(timestamp_arrival, active_bus)
            bus_id = active_bus
    bus_answer = bus_id * waiting_minutes
    return bus_answer


def waiting_time(timestamp, bus_id):
    waiting_minutes = bus_id - (timestamp % bus_id)
    if waiting_minutes == bus_id:
        waiting_minutes = 0
    return waiting_minutes


def get_active_busses(busses):
    active_busses = busses.split(",")
    while "x" in active_busses:
        active_busses.remove("x")
    active_busses = [int(x) for x in active_busses]
    return active_busses


def read_bus_notes(bus_notes_file):
    bus_notes_output = open(bus_notes_file, "r")
    bus_notes = []
    for bus_note in bus_notes_output:
        bus_notes.append(bus_note.replace("\n", ""))
    return bus_notes
