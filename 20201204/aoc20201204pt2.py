# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 4: Passport Processing ---
# --- Part Two ---

import string

batch = open("passport_batch", "r")

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def splitPassEntry(passEntry):
    split = passEntry.split(":")
    passField = split[0]
    passValue = split[1]
    return passField, passValue


def byrCheck(passValue):
    if "1920" <= passValue <= "2002":
        return True


def iyrCheck(passValue):
    if "2010" <= passValue <= "2020":
        return True


def eyrCheck(passValue):
    if "2020" <= passValue <= "2030":
        return True


def hgtCheck(passValue):
    if passValue[-2:] == "cm":
        if len(passValue) == 5 and passValue[:3].isdigit():
            if "150" <= passValue[:3] <= "193":
                return True
    elif passValue[-2:] == "in":
        if len(passValue) == 4 and passValue[:2].isdigit():
            if "59" <= passValue[:2] <= "76":
                return True


def hclCheck(passValue):
    if len(passValue) == 7:
        if passValue[:1] == "#":
            if all(c in string.hexdigits for c in passValue[-6:]):
                return True


def eclCheck(passValue):
    eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for ecl in eyeColor:
        if ecl == passValue:
            return True


def pidCheck(passValue):
    if len(passValue) == 9 and passValue.isdigit():
        return True


def checkPassEntry(passField, passValue):
    if passField == "byr":
        if byrCheck(passValue):
            return True
    elif passField == "iyr":
        if iyrCheck(passValue):
            return True
    elif passField == "eyr":
        if eyrCheck(passValue):
            return True
    elif passField == "hgt":
        if hgtCheck(passValue):
            return True
    elif passField == "hcl":
        if hclCheck(passValue):
            return True
    elif passField == "ecl":
        if eclCheck(passValue):
            return True
    elif passField == "pid":
        if pidCheck(passValue):
            return True
    else:
        return True


def checkPassportFields(batchline, fields):
    returnedFields = fields.copy()
    for field in fields:
        if field in batchLine:
            returnedFields.remove(field)
    return returnedFields


validPassports = 0
validationError = False
checkedFields = requiredFields.copy()
for batchLine in batch:
    if batchLine != "\n":
        checkedFields = checkPassportFields(batchLine, checkedFields)
        passEntries = batchLine.split()
        for passEntry in passEntries:
            (passField, passValue) = splitPassEntry(passEntry)
            if not checkPassEntry(passField, passValue):
                validationError = True
    else:
        if not checkedFields and not validationError:
            validPassports += 1
        checkedFields = requiredFields.copy()
        validationError = False
if not checkedFields and not validationError:
    validPassports += 1

print("Valid Passports", validPassports)