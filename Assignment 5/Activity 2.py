def calculatedays(years):
    days = years * 365
    
    return days

def calculatehours(years):
    hours = years * 8760
    
    return hours

def calculatemonths(years):
    months = years * 12
    
    return months

def calculateseconds(years):
    seconds = years * 31536000
    
    return seconds

def displayResult(years, months, days, hours, seconds):
    print(str(years) + " years " + str(months) + " months " + str(days) + " days " + str(hours) + " hours " + str(seconds) + " seconds ")

def getyears():
    print("How old are you?")
    years = float(input())
    
    return years

# Main
# This program converts the unit of Years into months, days, hours, and seconds.
years = getyears()
months = calculatemonths(years)
days = calculatedays(years)
hours = calculatehours(years)
seconds = calculateseconds(years)
displayResult(years, months, days, hours, seconds)
