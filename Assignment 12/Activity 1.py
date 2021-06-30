# This program takes grades from user stores it in dynamic array 
# until a negative score is input.
# the program also dislays highest , lowest and average grade.


def get_average(grades):
    total = sum(grades)
    average = float(total) / len(grades)
    return average


def get_scores():
    print("Please enter Grade :")
    grades = float(input())
    return grades


def get_grades():
    grades = []
    print("Please enter a negative number to stop input grades")
    while True:
        scores = get_scores()
        if scores <= 0:
            break
        grades.append(scores)
    return grades


def display_output(maximum, minimum, average):
    print("Maximum Grade : " + str(maximum))
    print("Minimum Grade : " + str(minimum))
    print("Average Grade : " + str(average))


def main():
    grades = get_grades()
    average = get_average(grades)
    display_output(max(grades), min(grades), average)


main()
