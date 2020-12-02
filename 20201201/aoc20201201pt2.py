# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 1: Report Repair ---
# --- Part Two ---

expenseReport = open("expense_report", "r")
expenses = []
address1 = 0
address2 = 1
address3 = 2

# Load expenses in array
for expense in expenseReport:
    expenses.append(int(expense))

expenseSum = expenses[address1] + expenses[address2] + expenses[address3]
while expenseSum != 2020:
    address3 += 1
    if address3 == len(expenses):
        address2 += 1
        if address2 == len(expenses) - 1:
            address1 += 1
            address2 = address1 + 1
        address3 = address2 + 1
    expenseSum = expenses[address1] + expenses[address2] + expenses[address3]

expenseMultiply = expenses[address1] * expenses[address2] * expenses[address3]

print("expenseMultiply:", expenseMultiply)
