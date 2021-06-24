# this program that asks the user to enter grade scores and calculates the average of the entered scores.

def displayAverage(average):
    print(" The avergae of all these score is " + str(average))

    
def processScores():
    increment = 0
    sum = 0
    while True:    #This simulates a Do Loop
        score = getValue("score")
        if score >= 0:
            sum = sum + score
            print(sum)
            increment = increment + 1
        if not(score >= 0): break   #Exit loop
    average = float(sum) / increment
    return average

def getValue(name):
    print(" Enter " + name + " value: ")
    value = int(input())
    return value

def main():
    average = processScores()
    displayAverage(average)

    
main()
