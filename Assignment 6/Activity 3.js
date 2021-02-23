// This program converts the unit miles in to yards, feet, and inches.
//
// Reference:
//  https://www.mathsisfun.com/measure/us-standard-length.html
//  https://en.wikibooks.org/wiki/JavaScript

function main() {
    var miles;
    var yards;
    var feet;
    var inches;
    
    miles = getmiles();
    yards = calculateyards(miles);
    feet = calculatefeet(miles);
    inches = calculateinches(miles);
    displayResult(yards, feet, inches);
}

function calculatefeet(miles) {
    var feet;
    
    feet = miles * 5280;
    
    return feet;
}

function calculateinches(miles) {
    var inches;
    
    inches = miles * 63360;
    
    return inches;
}

function calculateyards(miles) {
    var yards;
    
    yards = miles * 1760;
    
    return yards;
}

function displayResult(yards, feet, inches) {
    window.alert(yards.toString() + " yards " + feet + " feet " + inches + " inches ");
}

function getmiles() {
    var miles;
    
    window.alert("Enter a value for miles");
    miles = window.prompt('Enter a value for miles');
    
    return miles;
}

if (typeof alert === "undefined") {
    global.alert = function(message) {
        console.log(message);
    };
}

if (typeof prompt === "undefined") {
    global.prompt = function(message) {
        var fs = require("fs");
        var result = "";
        var buffer = Buffer.alloc(1);

        console.log(message);
        for(;;){
            fs.readSync(0, buffer, 0, 1);
            if(buffer[0] === 10){
                break;
            }else if(buffer[0] !== 13){
                result += buffer.toString();
            }
        }

        return result;
    }
}

if (typeof window === "undefined") {
    global.window = {
        alert : global.alert,
        prompt : global.prompt
    };
}

main();
