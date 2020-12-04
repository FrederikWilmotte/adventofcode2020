# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 4: Passport Processing ---
# --- Part One ---

batch = open("passport_batch", "r")

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def checkPassportFields(batchline, fields):
    returnedFields = fields.copy()
    for field in fields:
        if field in batchLine:
            returnedFields.remove(field)
    return returnedFields

validPassports = 0
checkedFields = requiredFields.copy()
for batchLine in batch:
    if batchLine != "\n":
        checkedFields = checkPassportFields(batchLine, checkedFields)
    else:
        if not checkedFields:
            validPassports += 1
        checkedFields = requiredFields.copy()
if not checkedFields:
    validPassports += 1

print("Valid Passports", validPassports)
