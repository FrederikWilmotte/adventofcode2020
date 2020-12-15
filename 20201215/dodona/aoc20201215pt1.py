# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 15: Rambunctious Recitation ---
# --- Part One ---
# Dodona submission


def recitation(starting_numbers_string, number):
    starting_numbers = starting_numbers_string.split(',')
    for index in range(0, len(starting_numbers)):
        starting_numbers[index] = int(starting_numbers[index])
    turn = 0
    spoken_numbers = [0]
    while turn < number:
        turn += 1
        if turn <= len(starting_numbers):
            spoken_numbers.append(starting_numbers[turn-1])
        else:
            lts = last_time_spoken(spoken_numbers)
            spoken_numbers.append(lts)
    return spoken_numbers[number]


def last_time_spoken(spoken_numbers):
    turn = 0
    for index in range(len(spoken_numbers)-2, 0, -1):
        if spoken_numbers[index] == spoken_numbers[len(spoken_numbers)-1]:
            turn = len(spoken_numbers) - 1 - index
            break
    return turn
