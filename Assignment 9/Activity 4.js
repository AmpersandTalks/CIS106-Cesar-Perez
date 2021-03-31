// This program that asks the user to enter an amount of hours worked 
// to calculate weekly until user enters time that is higher than 40 hours.

function main() {
    var rateperhour;
    var hours;
    
    rateperhour = getRate();
    hours = getHours()
    sum = rateperhour * hours;
    window.alert("Your pay is: " + sum);
}

function getHours() {
    var hours;

    do {
        hours = window.prompt("Enter hours: ");
        if (hours < 0 || hours > 40) {
            window.alert("please input a value under 40");
        }
    } while (hours < 0 || hours > 40);

    return hours; 
}

function getRate() {
    var rate;

    do {
        rate = window.prompt("Enter rate: ");
        if (rate < 0) {
            window.alert("please input a value greater than or equal to 0");
        }
    } while (rate < 0);

    return rate; 
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
