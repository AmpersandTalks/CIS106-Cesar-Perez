def getScores(total):
    for counter in range(1, total + 1, 1):
        print(" Enter score value: ")
        scores = int(input())
    
    return scores

def getTotal(scores, total, average):
    print(" The avergae of all these score is " + str(average))

def getValue(name):
    print(" Enter " + name + " value: ")
    value = int(input())
    
    return value

# Main
# this program uses a loop to generate a list of multiplication expressions for a given value
total = getValue("total")
scores = getScores(total)
average = float(scores) / total
getTotal(scores, total, average)
