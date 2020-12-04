# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 4: Passport Processing ---
# --- Part One ---
# Dodona submission


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
            passport = " "
    if is_valid_passport(passport):
        validPassports += 1
    return validPassports


def is_valid_passport(passport):
    passportFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    checkedFields = passportFields.copy()
    for field in passportFields:
        if field in passport:
            checkedFields.remove(field)
    if not checkedFields:
        return True
    else:
        return False
