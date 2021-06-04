# This program converts the unit miles in to yards, feet, and inches.
# Reference:https://www.mathsisfun.com/measure/us-standard-length.html
#  https://en.wikibooks.org/wiki/JavaScript

print('Enter miles distance')
miles = float(input())

yards = miles * 1760
feet = miles * 5280
inches = miles * 63360

print(str(miles) + " miles is " +
      str(yards) + " yards " + str(feet) +
      " feet " + str(inches) +  " inches ")
