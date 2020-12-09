# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 9: Encoding Error ---
# --- Part One ---

def find_xmas_output_error(xmas_file):
    xmas_output = open(xmas_file, "r")
    xmas = []
    preamble = 5
    position = preamble
    error_found = False
    for xmas_line in xmas_output:
        xmas.append(int(xmas_line.replace("\n", "")))
    while not error_found:
        if check_sum(xmas, preamble, position):
            position += 1
        else:
            error_found = True
    return xmas[position]


def check_sum(xmas, preamble, position):
    sum_found = False
    stop_searching = False
    position_1 = position - preamble
    position_2 = position_1 + 1
    while not sum_found and not stop_searching:
        if xmas[position_1] + xmas[position_2] == xmas[position]:
            sum_found = True
        else:
            if position_1 == position - 2 and position_2 == position - 1:
                stop_searching = True
            else:
                if position_2 == position - 1:
                    position_1 += 1
                    position_2 = position_1 + 1
                else:
                    position_2 += 1
    return sum_found


print(find_xmas_output_error("port_output"))
