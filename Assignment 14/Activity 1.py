# This program displays maximum, minimum, and average scores 
# based on input file 'scores.txt'.

def check_file(filename):
    try:
        file = open(filename, "r")
        file.close()
        message = "Success"
    except:
        message = "Error"
    return message


def read_file(filename):
    file = open(filename, "r")
    file_data = []
    for line in file:
        line = line.replace("\n", "")
        file_data.append(line)
    file.close()
    return file_data


def get_score(file_data):
    score = []
    increment = 1
    while increment < len(file_data):
        score.append(int(file_data[increment][file_data[increment].find(",") + 1: len(file_data[increment])]))
        increment = increment + 1
    return score


def get_name(file_data):
    name = []
    increment = 1
    while increment < len(file_data):
        name.append(file_data[increment][0:file_data[increment].find(",")])
        increment = increment + 1
    return name


def get_average(score):
    total_score = 0
    for increment in range(0, len(score), 1):
        total_score = total_score + score[increment]

    average = float(total_score / len(score))
    return average


def display_output(file_data):
    print("Content of File :")
    for increment in range(0, len(file_data), 1):
        print(file_data[increment])


def display_maximum(name, score, maximum_score):
    print("Maximum Score Result board")
    for increment in range(0, len(score) - 1, 1):
        if(score[increment] == maximum_score):
            print( "Maximum Score is : " + str(maximum_score) + " , achieve by  " + name[increment])


def display_minimum(name, score, minimum_score):
    print("Minimum Score Result board")
    for increment in range(0, len(score) - 1, 1):
        if(score[increment] == minimum_score):
            print("Manimum Score is : " + str(minimum_score) + " , achieve by  " + name[increment])


def display_average(average):
    print(f"Average score  : {average:.2f}")


def main():
    filename = "scores.txt"
    file_status = check_file(filename)
    if file_status == "Success":
        file_data = read_file(filename)
        display_output(file_data)
        name = get_name(file_data)
        score = get_score(file_data)
        display_maximum(name, score, max(score))
        display_minimum(name, score, min(score))
        average = get_average(score)
        display_average(average)
    else:
        print("File does not exist, create file first")


main()
