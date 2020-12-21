# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 19: Monster Messages ---
# --- Part One ---


def matches(messages_file):
    correct_messages = 0
    messages_lines = read_messages_file(messages_file)
    (rules, messages) = create_messages_and_rules(messages_lines)
    for message in messages:
        if message_match_rules(message, list(reversed(rules[0][0])), rules):
            correct_messages += 1
    return correct_messages


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


def create_messages_and_rules(messages_lines):
    process_rules = True
    messages = []
    rules = {}
    for line in messages_lines:
        if line == "":
            process_rules = False
        elif process_rules:
            index, value = line.split(": ")
            if value.find('"') >= 0:
                rules[int(index)] = value.replace('"', '')
            else:
                temp_values = value.split(" | ")
                values = []
                for temp_value in temp_values:
                    values.append([int(v) for v in temp_value.split(" ")])
                rules[int(index)] = values
        else:
            messages.append(line)
    return rules, messages


def read_messages_file(messages_file):
    messages_output = open(messages_file, "r")
    messages_lines = []
    for messages_line in messages_output:
        messages_lines.append(messages_line.replace("\n", ""))
    return messages_lines


print(matches("messages"))
