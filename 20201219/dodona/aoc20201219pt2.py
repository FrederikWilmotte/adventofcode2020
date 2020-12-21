# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 19: Monster Messages ---
# --- Part Two ---
# Dodona submission


def matches(messages_file, rules_file):
    correct_messages = 0
    messages = read_messages_file(messages_file)
    for message in messages:
        if match(message, rules_file):
            correct_messages += 1
    return correct_messages


def match(message, rules_file):
    rules_lines = read_rules_file(rules_file)
    rules = translate_rules(rules_lines)
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    return message_match_rules(message, list(reversed(rules[0][0])), rules)


def message_match_rules(message, stack, rules):
    if len(stack) > len(message):
        return False
    elif len(stack) == 0 or len(message) == 0:
        return len(stack) == 0 and len(message) == 0

    check_rule = stack.pop()
    if isinstance(check_rule, str):
        if message[0] == check_rule:
            return message_match_rules(message[1:], stack.copy(), rules)
    else:
        for rule in rules[check_rule]:
            if message_match_rules(message, stack + list(reversed(rule)), rules):
                return True
    return False


def translate_rules(rules_lines):
    rules = {}
    for line in rules_lines:
        index, value = line.split(": ")
        if value.find('"') >= 0:
            rules[int(index)] = value.replace('"', '')
        else:
            temp_values = value.split(" | ")
            values = []
            for temp_value in temp_values:
                values.append([int(v) for v in temp_value.split(" ")])
            rules[int(index)] = values
    return rules


def read_messages_file(messages_file):
    messages_output = open(messages_file, "r")
    messages_lines = []
    for messages_line in messages_output:
        messages_lines.append(messages_line.replace("\n", ""))
    return messages_lines

def read_rules_file(rules_file):
    rules_output = open(rules_file, "r")
    rules_lines = []
    for rules_line in rules_output:
        rules_lines.append(rules_line.replace("\n", ""))
    return rules_lines
