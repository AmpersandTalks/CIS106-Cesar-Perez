# this program uses a for loop take grade scores from the user
# and averages out the grade score average


def get_value(name):
    print(" Enter " + name + " value: ")
    value = int(input())
    return value


def get_scores():
    print(" Enter score value: ")
    scores = int(input())
    return scores


def process_scores(total):
    total_scores = 0
    for counter in range(1, total + 1, 1):
        scores = get_scores()
        total_scores = total_scores + scores
    return total_scores


def calculate_average(total_scores, total):
    average = float(total_scores) / total
    return average


def display_average(average):
    print(" The average of all these score is " + str(average))


def main():
    total = get_value("scores")
    total_scores = process_scores(total)        
    average = calculate_average(total_scores, total)
    display_average(average)
    
    
main()
