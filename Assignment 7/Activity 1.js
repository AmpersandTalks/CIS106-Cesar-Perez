function main() {
    // This program determines the amount of money made weekly with or without Ovetime.
    var choice;
    
    choice = gethours();
    if (choice > 40) {
        processOvertime(choice);
    } else {
        processNotOvertime(choice);
    }
}

function calculateOvertime(choice, rateperhour) {
    var overtime;
    
    overtime = (choice - 40) * rateperhour / 2;
    
    return overtime;
}

function calculateweekly(choice, rateperhour) {
    var weekly;
    
    weekly = choice * rateperhour;
    
    return weekly;
}

function displayResult(weekly) {
    window.alert("$" + weekly + " weekly ");
}

function displayResultOvertime(overtimeResults) {
    window.alert("$" + overtimeResults + " weekly ");
}

function getChoice() {
    var choice;
    
    window.alert("Enter Y if worked Overtime or N for no Overtime:");
    choice = window.prompt('Enter a value for choice');
    
    return choice;
}

function gethours() {
    var hours;
    
    window.alert("Enter hours worked this week");
    hours = window.prompt('Enter a value for hours');
    
    return hours;
}

function getrateperhour() {
    var rateperhour;
    
    window.alert("Enter rate per hour");
    rateperhour = window.prompt('Enter a value for rateperhour');
    
    return rateperhour;
}

function processNotOvertime(choice) {
    var rateperhour;
    var weekly;
    var overtime;
    
    rateperhour = getrateperhour();
    weekly = calculateweekly(choice, rateperhour);
    overtime = 0;
    displayResult(weekly);
}

function processOvertime(choice) {
    var rateperhour;
    var overtime;
    var weekly;
    var overtimeResults;
    
    rateperhour = getrateperhour();
    weekly = calculateweekly(choice, rateperhour);
    overtime = calculateOvertime(choice, rateperhour);
    overtimeResults = weekly + overtime;
    displayResultOvertime(overtimeResults);
}
