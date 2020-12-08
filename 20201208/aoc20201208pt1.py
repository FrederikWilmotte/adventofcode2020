# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 8: Handheld Halting ---
# --- Part One ---


def run_boot_code(boot_code):
    boot_code_instructions = open(boot_code, "r")
    instructions = []
    code_executed = []
    for boot_code_instruction in boot_code_instructions:
        instructions.append(boot_code_instruction)
        code_executed.append(False)
    acc = 0
    pos = 0
    while not code_executed[pos]:
        code_executed[pos] = True
        (operation, argument) = read_instruction(instructions[pos])
        (acc, pos) = process_instruction(acc, pos, operation, argument)
    return acc


def read_instruction(instruction):
    split_instruction = instruction.split()
    operation = split_instruction[0]
    argument = int(split_instruction[1])
    return operation, argument


def process_instruction(acc, pos, operation, argument):
    if operation == "nop":
        pos += 1
    elif operation == "acc":
        pos += 1
        acc += argument
    elif operation == "jmp":
        pos += argument
    return acc, pos


print(run_boot_code("boot_code"))
