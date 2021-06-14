def calculateOvertime(choice, rateperhour):
    overtime = (choice - 40) * rateperhour / 2
    
    return overtime

def calculateweekly(choice, rateperhour):
    weekly = choice * rateperhour
    
    return weekly

def displayResult(weekly):
    print("$" + str(weekly) + " weekly ")

def displayResultOvertime(overtimeResults):
    print("$" + str(overtimeResults) + " weekly ")

def getChoice():
    print("Enter Y if worked Overtime or N for no Overtime:")
    choice = input()
    
    return choice

def gethours():
    print("Enter hours worked this week")
    hours = float(input())
    
    return hours

def getrateperhour():
    print("Enter rate per hour")
    rateperhour = float(input())
    
    return rateperhour

def processNotOvertime(choice):
    rateperhour = getrateperhour()
    weekly = calculateweekly(choice, rateperhour)
    overtime = 0
    displayResult(weekly)

def processOvertime(choice):
    rateperhour = getrateperhour()
    weekly = calculateweekly(choice, rateperhour)
    overtime = calculateOvertime(choice, rateperhour)
    overtimeResults = weekly + overtime
    displayResultOvertime(overtimeResults)

# Main
# This program determines the amount of money made weekly with or without ovetime.
choice = gethours()
if choice > 40:
    processOvertime(choice)
else:
    processNotOvertime(choice)
