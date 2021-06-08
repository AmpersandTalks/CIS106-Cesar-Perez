def calculatedays(year):
    days = year * 365
    
    return days

def calculatehours(year):
    hours = year * 8760
    
    return hours

def calculatemonths(year):
    months = year * 12
    
    return months

def calculateseconds(year):
    seconds = year * 31536000
    
    return seconds

def displayResult(year, months, days, hours, seconds):
    print(str(year) + " year(s) " + str(months) + " months " + str(days) + " days " + str(hours) + " hours " + str(seconds) + " seconds ")

def getyear():
    print("How old are you?")
    year = float(input())
    
    return year

# Main
# This program converts the unit of Years into months, days, hours, and seconds.
year = getyear()
months = calculatemonths(year)
days = calculatedays(year)
hours = calculatehours(year)
seconds = calculateseconds(year)
displayResult(year, months, days, hours, seconds)
