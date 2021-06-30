# This program asks the user for grades and 
# then calculates the highest, lowest and average of the scores
# Reference:
# https://www.mathsisfun.com/definitions/average.html


def get_average(grades, scores):
    total = 0
    for increment in range(0, len(grades)):
        total = total + grades[increment]
    average = total / scores
    return average


def get_grades():
    print("Please Input Grades :")
    grades = int(input())
    return grades


def get_max(grades, scores):
    max = grades[0]
    for increment in range(1, len(grades)):
        if max < grades[increment]:
            max = grades[increment]
    return max


def get_min(grades, scores):
    min = grades[0]
    for increment in range(1, len(grades)):
        if min > grades[increment]:
            min = grades[increment]
    return min


def get_output(max, min, average):
    print("Maximum Grade: " + str(max))
    print("Minimum Grade: " + str(min))
    print("Average Grade: " + str(average))


def get_scores():
    print("Please enter how many scores you want to enter")
    scores = int(input())
    return scores


def main(): 
    scores = get_scores()
    grades = [0] * (scores)
    
    increment = 0
    while increment < scores:
        grades[increment] = get_grades()
        increment = increment + 1
    max = get_max(grades, scores)
    min = get_min(grades, scores)
    average = get_average(grades, scores)
    get_output(max, min, average)


main()
