# This program converts the unit miles in to yards, feet, and inches.
# Reference: https://www.mathsisfun.com/measure/us-standard-length.html
# https://en.wikibooks.org/wiki/JavaScript

def calculate_feet(miles):
    feet = miles * 5280    
    return feet


def calculate_inches(miles):
    inches = miles * 63360
    return inches


def calculate_yards(miles):
    yards = miles * 1760   
    return yards


def display_result(yards, feet, inches):
    print(str(yards) + " yards " + 
    str(feet) + " feet " + str(inches) + " inches ")


def get_miles():
    print("Enter a value for miles")
    miles = float(input())
    return miles

# main function starts here
def main():
    miles = get_miles()
    yards = calculate_yards(miles)
    feet = calculate_feet(miles)
    inches = calculate_inches(miles)
    display_result(yards, feet, inches)
    
main()
