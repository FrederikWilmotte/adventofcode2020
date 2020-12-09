# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 9: Encoding Error ---
# --- Part Two ---

def find_encryption_weakness(xmas_file):
    xmas = read_xmas(xmas_file)
    xmas_output_error = find_xmas_output_error(xmas)
    (position_1, position_2) = search_sum(xmas, xmas_output_error)
    encryption_weakness = min(xmas[position_1:position_2 + 1]) + max(xmas[position_1:position_2 + 1])
    return encryption_weakness


def read_xmas(xmas_file):
    xmas_output = open(xmas_file, "r")
    xmas = []
    for xmas_line in xmas_output:
        xmas.append(int(xmas_line.replace("\n", "")))
    return xmas


def find_xmas_output_error(xmas):
    preamble = 25
    position = preamble
    error_found = False
    while not error_found:
        if check_sum(xmas, preamble, position):
            position += 1
        else:
            error_found = True
    return xmas[position]


def search_sum(xmas, xmas_output_error):
    sum_found = False
    position_1 = 0
    position_2 = position_1 + 1
    while not sum_found:
        sum_output = sum(xmas[position_1:position_2 + 1])
        if sum_output == xmas_output_error:
            sum_found = True
        else:
            if sum_output > xmas_output_error:
                position_1 += 1
                position_2 = position_1 + 1
            else:
                position_2 += 1
    return position_1, position_2


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


print(find_encryption_weakness("port_output"))
