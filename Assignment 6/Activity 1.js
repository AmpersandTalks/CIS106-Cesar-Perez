// This program calculates  their weekly, monthly, and annual gross pay.
//
// References:
//  https://en.wikibooks.org/wiki/JavaScript

function main() {
    
    let hours;
    let rateperhour;
    let weekly;
    let monthly;
    let annual;
    
    hours = gethours();
    rateperhour = getrateperhour();
    weekly = calculateweekly(rateperhour, hours);
    monthly = calculatemonthly(rateperhour, hours);
    annual = calculateannual(rateperhour, hours);
    displayResult(weekly, monthly, annual);
}

function calculatemonthly(hours, rateperhour) {
    let monthly;
    
    monthly = hours * rateperhour * 4;
    
    return monthly;
}

function calculateannual(hours, rateperhour) {
    let annual;
    
    annual = hours * rateperhour * 52;
    
    return annual;
}

function calculateweekly(hours, rateperhour) {
    let weekly;
    
    weekly = hours * rateperhour;
    
    return weekly;
}

function displayResult(weekly, monthly, annual) {
    window.alert(weekly.toString() + " weekly " + monthly + " monthly " + annual + " annually ");
}

function gethours() {
    let hours;
    
    window.alert("Enter hours worked this week");
    hours = window.prompt('Enter a value for hours');
    
    return hours;
}

function getrateperhour() {
    let rateperhour;
    
    window.alert("Enter rate per hour");
    rateperhour = window.prompt('Enter a value for rateperhour');
    
    return rateperhour;
}
