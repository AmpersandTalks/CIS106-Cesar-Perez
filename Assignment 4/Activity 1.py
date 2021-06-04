# This program calculates  their weekly, monthly, and annual gross pay.
# References:https://en.wikibooks.org/wiki/JavaScript

print("Enter hours worked this week : ")
hours = float(input())
print("Enter rate per hour : ")
rate_per_hour = float(input())

weekly = hours * rate_per_hour
monthly = hours * rate_per_hour * 4
annual = hours * rate_per_hour * 52

print("$" + str(weekly) + " weekly " +
      "$" + str(monthly) + " monthly " +
      "$" + str(annual) + " annually ")
