
def get_scores(total):
    counter = 1
    while counter <= total:
        print(" Enter score value: ")
        scores = int(input())
        counter = counter + 1
      
    return scores

def get_value(name): 
    print(" Enter " + name + " value: ")
    value = int(input())

    return value


def get_total(scores, total, average):
    print(" The avergae of all these score is " + str(average))


# this program that asks the user to enter grade scores and calculates the average of the entered scores.
def main():
    total = get_value("total")
    scores = get_scores(total)
    average = float(scores) / total
    get_total(scores, total, average)


main()