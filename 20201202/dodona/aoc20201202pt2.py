# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 2: Password Philosophy ---
# --- Part Two ---
#Dodona submission

def is_valid_password(password, policy):
    (minAppear, maxAppear, character) = splitPolicy(policy)
    if checkPasswordPolicyNew(minAppear, maxAppear, character, password):
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

def checkPasswordPolicyNew(pos1, pos2, character, password):
    if password[(pos1-1):pos1] == character or password[(pos2-1):pos2] == character:
        if not (password[(pos1-1):pos1] == character and password[(pos2-1):pos2] == character):
            return True
