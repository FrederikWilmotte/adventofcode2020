# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 10: Adapter Array ---
# --- Part Two ---

def compute_distinct_connections(joltage_adapters_in_bag):
    adapters = read_joltage_adapters(joltage_adapters_in_bag)
    charging_outlet = 0  # charging outlet
    adapters.sort()
    arrangements_old = [charging_outlet]
    arrangements_new = []
    distinct_connections = 1
    while adapters:
        while arrangements_old:
            i = 0
            while i < len(adapters):
                if adapters[i] <= arrangements_old[0]:
                    if adapters[i] == adapters[-1]:
                        distinct_connections += 1
                    i += 1
                elif adapters[i] - arrangements_old[0] <= 3:
                    arrangements_new.append(adapters[i])
                    i += 1
                else:
                    i += len(adapters)
            arrangements_old.pop(0)
        arrangements_old = arrangements_new.copy()
        arrangements_new = []
        adapters.pop(0)
    return distinct_connections


def check_adapter_combination(adapter_combination, charging_outlet, build_in_adapter):
    if adapter_combination[0] - charging_outlet > 3 or build_in_adapter - adapter_combination[-1] > 3:
        correct_combination = False
    else:
        correct_combination = True
    position = 1
    while position < len(adapter_combination) and correct_combination:
        if adapter_combination[position] - adapter_combination[position - 1] > 3:
            correct_combination = False
        position += 1
    return correct_combination


def read_joltage_adapters(joltage_adapters):
    adapters_output = open(joltage_adapters, "r")
    adapters = []
    for adapter_line in adapters_output:
        adapters.append(int(adapter_line.replace("\n", "")))
    return adapters


print(compute_distinct_connections("joltage_adapters"))
