# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 17: Conway Cube ---
# --- Part Two ---
# Dodona submission

def active_cubes(cubes_file, cycles):
    cubes_lines = read_cubes_file(cubes_file)
    cubes = create_cubes(cubes_lines)
    for cycle in range(cycles):
        cubes = simulate_cycle(cubes)
    cubes_active_state = list(cubes.values()).count("#")
    return cubes_active_state


def simulate_cycle(old_cubes):
    new_cubes = {}
    for cube in old_cubes:
        active_neighbours = count_active_neighbours(cube, old_cubes)
        if old_cubes[cube] == "#":
            if active_neighbours == 2 or active_neighbours == 3:
                new_cubes[cube] = "#"
            else:
                new_cubes[cube] = "."
            neighbours = find_all_neighbours(cube)
            for neighbour in neighbours:
                if neighbour not in old_cubes:
                    active_neighbours = count_active_neighbours(neighbour, old_cubes)
                    if active_neighbours == 3:
                        new_cubes[neighbour] = "#"
        elif old_cubes[cube] == ".":
            if active_neighbours == 3:
                new_cubes[cube] = "#"
            else:
                new_cubes[cube] = "."
    return new_cubes


def count_active_neighbours(cube, cubes):
    active_neighbours = 0
    neighbours = find_all_neighbours(cube)
    for neighbour in neighbours:
        if cubes.get(neighbour) == "#":
            active_neighbours += 1
    return active_neighbours


def find_all_neighbours(cube):
    neighbours = [(cube[0] + x, cube[1] + y, cube[2] + z, cube[3] + w)
                  for x in range(-1, 2)
                  for y in range(-1, 2)
                  for z in range(-1, 2)
                  for w in range(-1, 2)]
    neighbours.remove((cube[0], cube[1], cube[2], cube[3]))
    return neighbours


def create_cubes(cubes_lines):
    cubes = {(x, y, 0, 0): cubes_lines[x][y] for x in range(len(cubes_lines)) for y in range(len(cubes_lines))}
    return cubes


def read_cubes_file(cubes_file):
    cubes_output = open(cubes_file, "r")
    cubes_lines = []
    for cubes_line in cubes_output:
        cubes_lines.append(cubes_line.replace("\n", ""))
    return cubes_lines
