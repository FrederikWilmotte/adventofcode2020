# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 14: Docking Data ---
# --- Part Two ---
# Dodona submission

from itertools import product


def memory(program_file):
    program = read_program(program_file)
    mem = {}
    mask = ""
    for program_line in program:
        program_line_split = program_line.split(" = ")
        if program_line_split[0] == "mask":
            mask = program_line_split[1]
        else:
            value = int(program_line_split[1])
            program_line_split[0] = program_line_split[0].replace("mem[", "")
            program_line_split[0] = program_line_split[0].replace("]", "")
            address = int(program_line_split[0])
            floating_bits = bitmask_address(address, mask)
            for address_bit in floating_bits:
                address_value = int(address_bit, 2)
                mem[address_value] = value
    return sum(mem.values())


def bitmask_address(address, mask):
    address_bit = "{0:036b}".format(address)
    floating_bit = ""
    for i in range(len(mask)):
        if mask[i] == "X" or mask[i] == "1":
            floating_bit = floating_bit + mask[i]
        else:
            floating_bit = floating_bit + address_bit[i]
    floating_bits = expand_floating_bit(floating_bit)
    return floating_bits


def expand_floating_bit(floating_bit):
    floating_bits = []
    count_floating_bits = 0
    for c in floating_bit:
        if c == "X":
            count_floating_bits += 1
    bit_list = product([0, 1], repeat=count_floating_bits)
    for combo in bit_list:
        floating_bit_entry = floating_bit
        for bit in combo:
            floating_bit_entry = floating_bit_entry.replace("X", str(bit), 1)
        floating_bits.append(floating_bit_entry)
    return floating_bits


def read_program(program_file):
    program_output = open(program_file, "r")
    program = []
    for program_line in program_output:
        program.append(program_line.replace("\n", ""))
    return program
