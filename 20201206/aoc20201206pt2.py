# Advent of Code 2020
# Author: Frederik Wilmotte
# --- Day 6: Custom Customs ---
# --- Part Two ---

def unique_questions(answers, nrAnswers):
    uniquelist = set(answers)
    uniqueQuestions = 0
    for c in uniquelist:
        count = answers.count(c)
        if count == nrAnswers:
            uniqueQuestions += 1
    return uniqueQuestions


def sum_of_counts(answerList):
    answer_list = open(answerList, "r")
    answer = ""
    nrAnswer = 0
    sumOfCounts = 0
    for answerLine in answer_list:
        if answerLine != "\n":
            answerLine = answerLine.rstrip("\n")
            answer = answer + answerLine
            nrAnswer += 1
        else:
            sumOfCounts += unique_questions(answer, nrAnswer)
            answer = ""
            nrAnswer = 0
    sumOfCounts += unique_questions(answer, nrAnswer)
    return sumOfCounts


print(sum_of_counts("answer_list"))