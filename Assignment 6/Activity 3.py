
function calculatefeet(miles) {
    let feet = miles * 5280;
    return feet;
}

function calculateinches(miles) {
    let inches = miles * 63360;
    return inches;
}

function calculateyards(miles) {
    let yards = miles * 1760;    
    return yards;
}

function Displayresult(yards, feet, inches) {
    window.alert(yards.toString() + " yards " + feet + " feet " + inches + " inches ");
}

function getmiles() {
    window.alert("Enter a value for miles");
    let miles = window.prompt('Enter a value for miles');
    return miles;



# This program converts the unit miles in to yards, feet, and inches.
# Reference: https://www.mathsisfun.com/measure/us-standard-length.html
# https://en.wikibooks.org/wiki/JavaScript

function main() {
    miles = getmiles();
    yards = calculateyards(miles);
    feet = calculatefeet(miles);
    inches = calculateinches(miles);
    
    Displayresult(yards, feet, inches);
}