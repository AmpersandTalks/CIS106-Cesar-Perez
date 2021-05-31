# This program asks for the amount of Years and converts into how many months,days,hours, minutes and seconds.
print("How old are you?")
year = float(input())
month = year * 12
day = year * 365
hour = year * 8760
seconds = year * 31536000
print(str(month) + " months " + str(day) + " days " + str(hour) + " hours " + str(seconds) + " seconds ")
