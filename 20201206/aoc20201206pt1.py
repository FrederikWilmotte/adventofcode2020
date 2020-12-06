# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 6: Custom Customs ---
# --- Part One ---

def unique_questions(answers):
    answers = set(answers)
    uniqueQuestions = len(answers)
    return uniqueQuestions


def sum_of_counts(answerList):
    answer_list = open(answerList, "r")
    answer = ""
    sumOfCounts = 0
    for answerLine in answer_list:
        if answerLine != "\n":
            answerLine = answerLine.rstrip("\n")
            answer = answer + answerLine
        else:
            sumOfCounts += unique_questions(answer)
            answer = ""
    sumOfCounts += unique_questions(answer)
    return sumOfCounts


print(sum_of_counts("answer_list"))
