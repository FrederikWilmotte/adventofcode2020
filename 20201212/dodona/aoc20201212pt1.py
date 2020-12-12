# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 12: Rain Risk ---
# --- Part One ---
# Dodona submission


def distance(navigation_instructions_file):
    ew_pos = 0
    ns_pos = 0
    facing = "E"
    navigation_instructions = read_navigation_instructions(navigation_instructions_file)
    for navigation_instruction in navigation_instructions:
        (facing, ew_pos, ns_pos) = navigate(navigation_instruction, facing, ew_pos, ns_pos)
    distance = abs(ew_pos) + abs(ns_pos)
    return distance


def navigate(navigation_instruction, facing, ew_pos, ns_pos):
    if navigation_instruction[0] == "L" or navigation_instruction[0] == "R":
        facing = change_facing(navigation_instruction[0], int(navigation_instruction[1:]), facing)
    elif navigation_instruction[0] == "F":
        (ew_pos, ns_pos) = go_forward(int(navigation_instruction[1:]), facing, ew_pos, ns_pos)
    else:
        (ew_pos, ns_pos) = go_forward(int(navigation_instruction[1:]), navigation_instruction[0], ew_pos, ns_pos)
    return facing, ew_pos, ns_pos


def go_forward(steps, facing, ew_pos, ns_pos):
    if facing == "W" or facing == "S":
        steps = -steps
    if facing == "N" or facing == "S":
        ns_pos += steps
    elif facing == "E" or facing == "W":
        ew_pos += steps
    return ew_pos, ns_pos


def change_facing(direction, degrees, current_facing):
    axe = ["E", "S", "W", "N"]
    turns = degrees / 90
    turns = turns % 4
    if direction == "L":
        turns = -turns
    position = axe.index(current_facing)
    position = int(position + turns)
    if position > 3:
        position = position - 4
    elif position < 0:
        position = position + 4
    facing = axe[position]
    return facing


def read_navigation_instructions(navigation_instructions_file):
    navigation_instructions_output = open(navigation_instructions_file, "r")
    navigation_instructions = []
    for navigation_instruction in navigation_instructions_output:
        navigation_instructions.append(navigation_instruction.replace("\n", ""))
    return navigation_instructions
