# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 4: Passport Processing ---
# --- Part One ---

batch = open("passport_batch", "r")

def checkPassportFields(passport):
    passportFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    checkedFields = passportFields.copy()
    for field in passportFields:
        if field in passport:
            checkedFields.remove(field)
    if not checkedFields:
        return True

validPassports = 0
passport = ""
for batchLine in batch:
    if batchLine != "\n":
        batchLine = batchLine.rstrip("\n")
        passport = passport + " " + batchLine
    else:
        if checkPassportFields(passport):
            validPassports += 1
        passport = ""
if checkPassportFields(passport):
    validPassports += 1

print("Valid Passports", validPassports)
