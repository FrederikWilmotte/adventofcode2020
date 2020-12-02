# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 2: Password Philosophy ---
# --- Part Two ---

passwordList = open("password_list", "r")
passwordLines = []


# Process Password line
def splitPasswordLine(passwordLine):
    passwordLineSplit = passwordLine.split()
    positions = passwordLineSplit[0].split("-")
    position1 = int(positions[0])
    position2 = int(positions[1])
    character = passwordLineSplit[1][0:1]
    password = passwordLineSplit[2]
    return position1, position2, character, password

def checkPasswordPolicyNew(pos1, pos2, character, password):
    if password[(pos1-1):pos1] == character or password[(pos2-1):pos2] == character:
        if not (password[(pos1-1):pos1] == character and password[(pos2-1):pos2] == character):
            return True

# Proccess Password List
nrCorrectPasswords = 0
for passwordline in passwordList:
    (pos1, pos2, character, password) = splitPasswordLine(passwordline)
    if checkPasswordPolicyNew(pos1, pos2, character, password):
        nrCorrectPasswords += 1

print("Number of correct passwords:", nrCorrectPasswords)
