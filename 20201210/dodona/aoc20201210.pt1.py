# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 10: Adapter Array ---
# --- Part One ---
# Dodona submission

def differences(joltage_adapters_in_bag):
    adapters = read_joltage_adapters(joltage_adapters_in_bag)
    adapters.append(0)  # add charging outlet
    adapters.append(max(adapters)+3)  # add built-in adapter
    adapters.sort()
    position = 1
    difference_1 = 0
    difference_3 = 0
    while position < len(adapters):
        if adapters[position] - adapters[position - 1] == 1:
            difference_1 += 1
        elif adapters[position] - adapters[position - 1] == 3:
            difference_3 += 1
        position += 1
    differences_1_and_3 = difference_1 * difference_3
    return differences_1_and_3


def read_joltage_adapters(joltage_adapters):
    adapters_output = open(joltage_adapters, "r")
    adapters = []
    for adapter_line in adapters_output:
        adapters.append(int(adapter_line.replace("\n", "")))
    return adapters
