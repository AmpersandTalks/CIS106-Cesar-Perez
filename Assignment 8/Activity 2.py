# this program uses a loop to generate a list of multiplication expressions for a given value


def get_average(total_scores, total):
    average = float(total_scores) / total
    return average


def get_scores():
    print(" Enter score value: ")
    scores = int(input())
    return scores


def get_total(scores, total, average):
    print(" The avergae of all these score is " + str(average))

    
def get_total_scores(total_scores, scores):
    sum_scores = total_scores + scores
    return sum_scores


def get_value(name):
    print(" Enter " + name + " value: ")
    value = int(input())
    return value


def main():
    total = get_value("total")
    total_scores = 0
    for counter in range(1, total + 1, 1):
        scores = get_scores()
        total_scores = get_total_scores(total_scores, scores)
        
    average = get_average(total_scores, total)
    get_total(scores, total, average)
    
    
main()
