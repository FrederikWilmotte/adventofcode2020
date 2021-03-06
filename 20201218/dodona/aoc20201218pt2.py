# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 18: Operation Order ---
# --- Part Two ---
# Dodona submission

def homework(homework_file):
    homework_lines = read_homework_file(homework_file)
    sum_results = 0
    for homework_line in homework_lines:
        result = evaluate(homework_line)
        sum_results += result
    return sum_results


def evaluate(homework_line):
    while homework_line.find(")") >= 0:
        pos_close = homework_line.find(")")
        pos_open = homework_line[0:pos_close].rfind("(")
        result = calculate_clean_string(homework_line[pos_open+1:pos_close])
        homework_line = homework_line.replace(homework_line[pos_open:pos_close+1], str(result), 1)
    result = calculate_clean_string(homework_line)
    return result


def calculate_clean_string(expression):
    result = 1
    expression_split = expression.split()
    while "+" in expression_split:
        index_plus = expression_split.index("+")
        add = int(expression_split[index_plus - 1]) + int(expression_split[index_plus + 1])
        expression_split[index_plus - 1] = add
        expression_split.pop(index_plus)
        expression_split.pop(index_plus)
    for element in expression_split:
        if not element == "*":
            result *= int(element)
    return result


def read_homework_file(homework_file):
    homework_output = open(homework_file, "r")
    homework_lines = []
    for homework_line in homework_output:
        homework_lines.append(homework_line.replace("\n", ""))
    return homework_lines
