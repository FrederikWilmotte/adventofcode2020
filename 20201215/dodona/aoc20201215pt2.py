# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 15: Rambunctious Recitation ---
# --- Part Two ---
# Dodona submission


def recitation(starting_numbers_string, number):
    starting_numbers = starting_numbers_string.split(',')
    for index in range(0, len(starting_numbers)):
        starting_numbers[index] = int(starting_numbers[index])
    # Put the starting numbers in a list that will keep the last time said
    lts_list = {starting_numbers[x]: x + 1 for x in range(len(starting_numbers))}
    last_spoken_number = starting_numbers[-1]
    for turn in range(len(starting_numbers), number):
        current_spoken_number = 0
        if last_spoken_number in lts_list:
            current_spoken_number = turn - lts_list[last_spoken_number]
        lts_list[last_spoken_number] = turn
        last_spoken_number = current_spoken_number
    return last_spoken_number
