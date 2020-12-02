# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 1: Report Repair ---
# --- Part One ---

expenseReport = open("expense_report", "r")
expenses = []
address1 = 0
address2 = 1

# Load expenses in array
for expense in expenseReport:
    expenses.append(int(expense))

expenseSum = expenses[address1] + expenses[address2]
while expenseSum != 2020:
    address2 += 1
    if address2 == len(expenses):
        address1 += 1
        address2 = address1 + 1
    expenseSum = expenses[address1] + expenses[address2]

expenseMultiply = expenses[address1] * expenses[address2]

print("expenseMultiply:", expenseMultiply)