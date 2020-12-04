# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 4: Passport Processing ---
# --- Part Two ---
# Dodona Submission

import string


def is_valid_field(passField, passValue):
    passportValid = False
    if passField == "byr":
        if byrCheck(passValue):
            passportValid = True
    elif passField == "iyr":
        if iyrCheck(passValue):
            passportValid = True
    elif passField == "eyr":
        if eyrCheck(passValue):
            passportValid = True
    elif passField == "hgt":
        if hgtCheck(passValue):
            passportValid = True
    elif passField == "hcl":
        if hclCheck(passValue):
            passportValid = True
    elif passField == "ecl":
        if eclCheck(passValue):
            passportValid = True
    elif passField == "pid":
        if pidCheck(passValue):
            passportValid = True
    else:
        passportValid = True
    return passportValid

def count_valid_passports(passport_batch):
    batch = open(passport_batch, "r")
    validPassports = 0
    passport = ""
    for batchLine in batch:
        if batchLine != "\n":
            batchLine = batchLine.rstrip("\n")
            passport = passport + " " + batchLine
        else:
            if is_valid_passport(passport):
                validPassports += 1
            passport = ""
    if is_valid_passport(passport):
        validPassports += 1
    return validPassports


def is_valid_passport(passport):
    passportFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    checkedFields = passportFields.copy()
    passEntries = passport.split()
    validationError = False
    for field in passportFields:
        if field in passport:
            checkedFields.remove(field)
    for passEntry in passEntries:
        (passField, passValue) = splitPassEntry(passEntry)
        if not is_valid_field(passField, passValue):
            validationError = True
    if not checkedFields and not validationError:
        return True
    else:
        return False



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

print(count_valid_passports("../passport_batch"))