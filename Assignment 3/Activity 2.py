# This program asks for the amount of Years and converts into how many months,days,hours, and seconds.
print("What is your age in years?")
year = float(input())
month = year * 12
day = year * 365
hour = year * 8760
seconds = year * 31536000
print(str(month) + " months " + str(day) + " days " + str(hour) + " hours " + str(seconds) + " seconds ")
