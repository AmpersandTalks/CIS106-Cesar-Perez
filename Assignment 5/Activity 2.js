function main() {
    // This program converts the unit of Years into months,days,hours, minutes and seconds.
    var years;
    var months;
    var days;
    var hours;
    var seconds;
    
    years = getyears();
    months = calculatemonths(years);
    days = calculatedays(years);
    hours = calculatehours(years);
    seconds = calculateseconds(years);
    displayResult(months, days, hours, seconds);
}

function calculatedays(years) {
    var days;
    
    days = years * 365;
    
    return days;
}

function calculatehours(years) {
    var hours;
    
    hours = years * 8760;
    
    return hours;
}

function calculatemonths(years) {
    var months;
    
    months = years * 12;
    
    return months;
}

function calculateseconds(years) {
    var seconds;
    
    seconds = years * 31536000;
    
    return seconds;
}

function displayResult(months, days, hours, seconds) {
    window.alert(months.ToString() + " months " + days + " days " + hours + " hours " + seconds + " seconds ");
}

function getyears() {
    var years;
    
    window.alert("How old are you?");
    years = window.prompt('Enter a value for years');
    
    return years;
}
