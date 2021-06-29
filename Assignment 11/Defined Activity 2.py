# This activity FInds the day of the birthday the person inputs. 
# Refrences: https://en.wikipedia.org/wiki/Zeller%27s_congruence
# https://www.geeksforgeeks.org/zellers-congruence-find-day-date/


def getValue(name):
    print(" Enter " + name + " value: ")
    value = int(input())
    return value


def calculateDayOfWeek(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    
    
    j = round(year / 100)
    k = year % 100
    m = month
    q = day
    y = year

    h = q + (13 * (m + 1)) / 5 + k +  k / 4 + j / 4 + 5 * j
    h = round(h % 7)
    return h


def displayResults(dayofweek):
     days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
     print("That day is a " + days[dayofweek])

    
    
def main():
     year = getValue("year")
     month = getValue("month")
     day = getValue("day")
    
     dayofweek = calculateDayOfWeek(year,month, day)
     displayResults(dayofweek)


main()
