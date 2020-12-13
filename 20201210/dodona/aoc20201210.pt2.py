# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 10: Adapter Array ---
# --- Part Two ---
# Dodona submission

def arrangements(joltage_adapters_in_bag):
    adapters = read_joltage_adapters(joltage_adapters_in_bag)
    charging_outlet = 0  # charging outlet
    adapters.append(charging_outlet)
    adapters.sort()
    paths = [0 for _ in range(max(adapters)+1)]
    paths[0] = 1
    for adapter in adapters:
        paths = determine_number_of_paths(adapter, paths)
    return paths[len(paths)-1]


def determine_number_of_paths(adapter, paths):
    prev_adapter = adapter - 1
    while prev_adapter >= 0 and adapter <= prev_adapter + 3:
        paths[adapter] += paths[prev_adapter]
        prev_adapter -= 1
    return paths


def read_joltage_adapters(joltage_adapters):
    adapters_output = open(joltage_adapters, "r")
    adapters = []
    for adapter_line in adapters_output:
        adapters.append(int(adapter_line.replace("\n", "")))
    return adapters
