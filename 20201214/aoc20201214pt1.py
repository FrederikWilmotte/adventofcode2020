# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 14: Docking Data ---
# --- Part One ---


def memory(program_file):
    program = read_program(program_file)
    mem = {}
    mask = ""
    sum_values = 0
    for program_line in program:
        program_line_split = program_line.split(" = ")
        if program_line_split[0] == "mask":
            mask = program_line_split[1]
        else:
            value = int(program_line_split[1])
            result = bitmask(value, mask)
            program_line_split[0] = program_line_split[0].replace("mem[", "")
            program_line_split[0] = program_line_split[0].replace("]", "")
            mem[int(program_line_split[0])] = result
    return sum(mem.values())


def bitmask(value, mask):
    value_bit = "{0:036b}".format(value)
    result_bit = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            result_bit = result_bit + value_bit[i]
        else:
            result_bit = result_bit + mask[i]
    result = int(result_bit, 2)
    return result


def read_program(program_file):
    program_output = open(program_file, "r")
    program = []
    for program_line in program_output:
        program.append(program_line.replace("\n", ""))
    return program


print(memory("program_test"))
print(memory("program"))
