
function calculatefeet(miles):
    feet = miles * 5280
    
    return feet


function calculateinches(miles):
    inches = miles * 63360
    
    return inches


function calculateyards(miles):
    yards = miles * 1760   
    
    return yards


function Displayresult(yards, feet, inches):
    print(Str(yards) + " yards " + feet + " feet " + inches + " inches ")


function getmiles():
    print("Enter a value for miles")
    miles = float(input())
    
    return miles



# This program converts the unit miles in to yards, feet, and inches.
# Reference: https://www.mathsisfun.com/measure/us-standard-length.html
# https://en.wikibooks.org/wiki/JavaScript

    miles = getmiles();
    yards = calculateyards(miles);
    feet = calculatefeet(miles);
    inches = calculateinches(miles);
    Displayresult(yards, feet, inches);
