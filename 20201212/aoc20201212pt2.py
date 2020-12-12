# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 12: Rain Risk ---
# --- Part Two ---


def calculate_manhattan_distance(navigation_instructions_file):
    ew_ship = 0
    ns_ship = 0
    ew_way = 10
    ns_way = 1
    navigation_instructions = read_navigation_instructions(navigation_instructions_file)
    for navigation_instruction in navigation_instructions:
        (ew_ship, ns_ship, ew_way, ns_way) = navigate(navigation_instruction, ew_ship, ns_ship, ew_way, ns_way)
    distance = abs(ew_ship) + abs(ns_ship)
    return distance


def navigate(navigation_instruction, ew_ship, ns_ship, ew_way, ns_way):
    if navigation_instruction[0] == "L" or navigation_instruction[0] == "R":
        (ew_way, ns_way) = change_facing(navigation_instruction[0], int(navigation_instruction[1:]), ew_way, ns_way)
    elif navigation_instruction[0] == "F":
        (ew_ship, ns_ship) = move_ship(int(navigation_instruction[1:]), ew_ship, ns_ship, ew_way, ns_way)
    else:
        (ew_way, ns_way) = move_waypoint(navigation_instruction[0], int(navigation_instruction[1:]), ew_way, ns_way)
    return ew_ship, ns_ship, ew_way, ns_way


def move_ship(steps, ew_ship, ns_ship, ew_way, ns_way):
    ew_ship += ew_way * steps
    ns_ship += ns_way * steps
    return ew_ship, ns_ship


def move_waypoint(direction, steps, ew_way, ns_way):
    if direction == "W" or direction == "S":
        steps = -steps
    if direction == "N" or direction == "S":
        ns_way += steps
    elif direction == "E" or direction == "W":
        ew_way += steps
    return ew_way, ns_way


def change_facing(direction, degrees, ew_way_old, ns_way_old):
    ew_way = ew_way_old
    ns_way = ns_way_old
    turns = degrees / 90
    turns = int(turns % 4)
    for i in range(turns):
        if direction == "L":
            ew_way = -ns_way_old
            ns_way = ew_way_old
            ew_way_old = ew_way
            ns_way_old = ns_way
        else:
            ew_way = ns_way_old
            ns_way = -ew_way_old
            ew_way_old = ew_way
            ns_way_old = ns_way
    return ew_way, ns_way


def read_navigation_instructions(navigation_instructions_file):
    navigation_instructions_output = open(navigation_instructions_file, "r")
    navigation_instructions = []
    for navigation_instruction in navigation_instructions_output:
        navigation_instructions.append(navigation_instruction.replace("\n", ""))
    return navigation_instructions


print(calculate_manhattan_distance("navigation_instructions_test"))
print(calculate_manhattan_distance("navigation_instructions"))
