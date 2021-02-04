function main() {
    // This program converts the unit of Years into months,days,hours, minutes and seconds.
    var years;
    var months;
    var days;
    var minutes;
    var seconds;
    
    window.alert("How old are you?");
    years = window.prompt('Enter a value for years');
    months = years * 12;
    days = years * 365;
    minutes = years * 525600;
    seconds = years * 31536000;
    window.alert(months.ToString() + " months " + days + " days " + minutes + " minutes " + seconds + " seconds ");
}
