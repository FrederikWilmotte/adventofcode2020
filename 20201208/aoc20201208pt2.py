# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 8: Handheld Halting ---
# --- Part One ---


def run_boot_code(boot_code):
    boot_code_instructions = open(boot_code, "r")
    instructions = []
    code_executed = []
    for boot_code_instruction in boot_code_instructions:
        instructions.append(boot_code_instruction.replace("\n", ""))
        code_executed.append(False)
    code_executed.append(True)
    acc = 0
    pos = 0
    last_switch = -1
    while pos < len(instructions):
        acc = 0
        pos = 0
        code_executed_temp = code_executed.copy()
        while not code_executed_temp[pos]:
            code_executed_temp[pos] = True
            (operation, argument) = read_instruction(instructions[pos])
            (acc, pos) = process_instruction(acc, pos, operation, argument)
        if pos < len(instructions):
            (instructions, last_switch) = switch_next_operation(instructions, last_switch)
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


def switch_next_operation(instructions, last_switch):
    switched = False
    next_switch = 0
    if last_switch >= 0:
        switch_instruction(instructions, last_switch)
        last_switch += 1
    else:
        last_switch = 0
    while not switched:
        switched = switch_instruction(instructions, last_switch)
        if switched:
            next_switch = last_switch
        else:
            last_switch += 1
    return instructions, next_switch


def switch_instruction(instructions, switch_position):
    switched = False
    (switch_operation, switch_argument) = read_instruction(instructions[switch_position])
    if switch_operation == "nop":
        instructions[switch_position] = instructions[switch_position].replace("nop", "jmp")
        switched = True
    elif switch_operation == "jmp":
        instructions[switch_position] = instructions[switch_position].replace("jmp", "nop")
        switched = True
    return switched


print(run_boot_code("boot_code"))
