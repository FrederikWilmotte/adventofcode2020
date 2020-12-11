# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 10: Adapter Array ---
# --- Part Two ---

def compute_distinct_connections(joltage_adapters_in_bag):
    adapters = read_joltage_adapters(joltage_adapters_in_bag)
    charging_outlet = 0  # charging outlet
    adapters.sort()
    distinct_connections = 1
    previous_adapter = [charging_outlet]
    while adapters:




        previous_adapter = adapters[0]
        adapters.pop(0)
    return distinct_connections


def read_joltage_adapters(joltage_adapters):
    adapters_output = open(joltage_adapters, "r")
    adapters = []
    for adapter_line in adapters_output:
        adapters.append(int(adapter_line.replace("\n", "")))
    return adapters


print(compute_distinct_connections("joltage_adapters_test"))
