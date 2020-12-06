# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 6: Custom Customs ---
# --- Part One ---
# Dodona submission

def group_count(answers):
    answers = answers.replace(" ", "")
    answers = set(answers)
    uniqueQuestions = len(answers)
    return uniqueQuestions


def plane_count(answerList):
    answer_list = open(answerList, "r")
    answer = ""
    sumOfCounts = 0
    for answerLine in answer_list:
        if answerLine != "\n":
            answerLine = answerLine.rstrip("\n")
            answer = answer + answerLine
        else:
            sumOfCounts += group_count(answer)
            answer = ""
    sumOfCounts += group_count(answer)
    return sumOfCounts
