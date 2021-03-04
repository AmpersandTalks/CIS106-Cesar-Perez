function main() {
    // This program coverts the distance in miles into either the US system yards or metric system kilometers.
    var choice;
    
    choice = getChoice();
    if (choice == "Y" || choice == "y") {
        processUs();
    } else {
        if (choice == "N" || choice == "n") {
            processMetric();
        } else {
            window.alert("Please enter Y to use the US measurement system or N to use the  metric measurement system !");
        }
    }
}

function calculatecentimeters(miles) {
    var centimeters;
    
    centimeters = miles * 160934;
    
    return centimeters;
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

function calculatekilometers(miles) {
    var kilometers;
    
    kilometers = miles * 1.60934;
    
    return kilometers;
}

function calculatemeters(miles) {
    var meters;
    
    meters = miles * 1609.34;
    
    return meters;
}

function calculateyards(miles) {
    var yards;
    
    yards = miles * 1760;
    
    return yards;
}

function getChoice() {
    var choice;
    
    window.alert("Would you like to use the US measurement system? Y or N ");
    choice = window.prompt('Enter a value for choice');
    
    return choice;
}

function getMiles() {
    var miles;
    
    window.alert("Enter a value for miles");
    miles = window.prompt('Enter a value for miles');
    
    return miles;
}

function metricDisplayResults(kilometers, meters, centimeters) {
    window.alert(kilometers.ToString() + " kilometers " + meters + " meters " + centimeters + " centimeter ");
}

function processMetric() {
    var miles;
    var kilometers;
    var meters;
    var centimeters;
    
    miles = getMiles();
    kilometers = calculatekilometers(miles);
    meters = calculatemeters(miles);
    centimeters = calculatecentimeters(miles);
    metricDisplayResults(kilometers, meters, centimeters);
}

function processUs() {
    var miles;
    var yards;
    var feet;
    var inches;
    
    miles = getMiles();
    yards = calculateyards(miles);
    feet = calculatefeet(miles);
    inches = calculateinches(miles);
    usDisplayResults(yards, feet, inches);
}

function usDisplayResults(yards, feet, inches) {
    window.alert(yards.ToString() + " yards " + feet + " feet " + inches + " inches ");
}
