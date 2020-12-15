# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 15: Rambunctious Recitation ---
# --- Part One ---


def find_spoken_number(starting_numbers, number):
    turn = 0
    spoken_numbers = [0]
    while turn < number:
        turn += 1
        if turn <= len(starting_numbers):
            spoken_numbers.append(starting_numbers[turn-1])
        else:
            lts = last_time_spoken(spoken_numbers)
            spoken_numbers.append(lts)
    print(spoken_numbers)
    return spoken_numbers[number]


def last_time_spoken(spoken_numbers):
    turn = 0
    for index in range(len(spoken_numbers)-2, 0, -1):
        if spoken_numbers[index] == spoken_numbers[len(spoken_numbers)-1]:
            turn = len(spoken_numbers) - 1 - index
            break
    return turn


starting_numbers = [5, 1, 9, 18, 13, 8, 0]
number = 2020
print(find_spoken_number(starting_numbers, number))
