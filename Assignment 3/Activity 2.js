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
    window.alert(months.toString() + " months " + days + " days " + minutes + " minutes " + seconds + " seconds ");
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
