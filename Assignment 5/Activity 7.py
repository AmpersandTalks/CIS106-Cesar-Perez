def calculatedogyears(humanyear):
    dogyears = humanyear * 7
    
    return dogyears

def displayResult(dogname, dogyears):
    print(dogname + " is " + str(dogyears) + " Dog Years")

def getdogname():
    print("Enter Dog's Name")
    dogname = input()
    
    return dogname

def gethumanyear():
    print("Enter dogs age is in human years")
    humanyear = float(input())
    
    return humanyear

# Main
# This program converts Human years to Dog years.
# Reference:
# https://en.wikipedia.org/wiki/Aging_in_dogs
dogname = getdogname()
humanyear = gethumanyear()
dogyears = calculatedogyears(humanyear)
displayResult(dogname, dogyears)
