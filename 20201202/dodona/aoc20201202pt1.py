# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 2: Password Philosophy ---
# --- Part One ---
# Dodona submission

def is_valid_password(password, policy):
    (minAppear, maxAppear, character) = splitPolicy(policy)
    if checkPasswordPolicy(minAppear, maxAppear, character, password):
        return True
    else:
        return False

def splitPolicy(policy):
    policySplit = policy.split()
    positions = policySplit[0].split("-")
    position1 = int(positions[0])
    position2 = int(positions[1])
    character = policySplit[1][0:1]
    return position1, position2, character

def checkPasswordPolicy(minAppear, maxAppear, character, password):
    realAppear = password.count(character)
    if minAppear <= realAppear <= maxAppear:
        return True