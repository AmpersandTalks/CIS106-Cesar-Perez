# This program calculates  their weekly, monthly, and annual gross pay.
# References:https://en.wikibooks.org/wiki/JavaScript

print("Enter hours worked this week : ")
hours = float(input())
print("Enter rate per hour : ")
ratePerHour = float(input())

weekly = hours * ratePerHour
monthly = hours * ratePerHour * 4
annual = hours * ratePerHour * 52

print("$" + str(weekly) + " weekly " +
    "$" + str(monthly) + " monthly " +
    "$" + str(annual) + " annually ")


