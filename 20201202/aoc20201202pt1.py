# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 2: Password Philosophy ---
# --- Part One ---

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

# Check Password Policy
def checkPasswordPolicy(minAppear, maxAppear, character, password):
    realAppear = password.count(character)
    if realAppear >= minAppear and realAppear <= maxAppear:
        return True

# Proccess Password List
nrCorrectPasswords = 0
for passwordline in passwordList:
    (minAppear, maxAppear, character, password) = splitPasswordLine(passwordline)
    if checkPasswordPolicy(minAppear, maxAppear, character, password):
        nrCorrectPasswords += 1

print("Number of correct passwords:", nrCorrectPasswords)