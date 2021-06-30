# This program asks the user for grades and
# then calculates the highest, lowest and average of the scores
# Reference:
# https://www.mathsisfun.com/definitions/average.html


def get_grade():
    print("Please Input Grades :")
    grade = int(input())
    return grade


def get_grades(scores):
    grades = [None] * (scores)

    increment = 0
    while increment < scores:
        grades[increment] = get_grade()
        increment = increment + 1

    return grades


def calculate_average(grades):
    total = 0
    for increment in range(0, len(grades)):
        total = total + grades[increment]
    average = total / len(grades)
    return average


def calculate_maximum(grades):
    max = grades[0]
    for increment in range(1, len(grades)):
        if max < grades[increment]:
            max = grades[increment]
    return max


def calculate_minimum(grades):
    min = grades[0]
    for increment in range(1, len(grades)):
        if min > grades[increment]:
            min = grades[increment]
    return min


def display_output(maximum, minimum, average):
    print("Maximum Grade: " + str(maximum))
    print("Minimum Grade: " + str(minimum))
    print("Average Grade: " + str(average))


def get_scores():
    print("Please enter how many scores you want to enter")
    scores = int(input())
    return scores


def main():
    scores = get_scores()
    grades = get_grades(scores)
    maximum = calculate_maximum(grades)
    minimum = calculate_minimum(grades)
    average = calculate_average(grades)
    display_output(maximum, minimum, average)


main()
