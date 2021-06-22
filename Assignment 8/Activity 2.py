# this program uses a loop to generate a list of multiplication expressions for a given value


def getAverage(totalScores, total):
    average = float(totalScores) / total
    return average


def getScores():
    print(" Enter score value: ")
    scores = int(input())
    return scores


def getTotal(scores, total, average):
    print(" The avergae of all these score is " + str(average))

    
def getTotalScores(totalScores, scores):
    sumScores = totalScores + scores
    return sumScores


def getValue(name):
    print(" Enter " + name + " value: ")
    value = int(input())
    return value


def main():
    total = getValue("total")
    totalScores = 0
    for counter in range(1, total + 1, 1):
        scores = getScores()
        totalScores = getTotalScores(totalScores, scores)
        
    average = getAverage(totalScores, total)
    getTotal(scores, total, average)
    
    
main()
