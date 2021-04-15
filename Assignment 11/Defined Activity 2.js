// This activity FInds the day of the birthday the person inputs.
    // 
    // Refrences: https://en.wikipedia.org/wiki/Zeller%27s_congruence
    // https://www.geeksforgeeks.org/zellers-congruence-find-day-date/

function main() {
    var year = getValue("year");
    var month = getValue("month");
    var day = getValue("day");
    
    var dayofweek = calculateDayOfWeek(year,month, day);
    displayResults(dayofweek);
}

function calculateDayOfWeek(year, month, day) {
    if (month < 3) {
        month += 12;
        year -= 1;
    }
    
    var j = Math.floor(year / 100);
    var k = year % 100;
    var m = month;
    var q = day;
    var y = year;
    
    var h = q + (13 * (m + 1)) / 5 + k +  k / 4 + j / 4 + 5 * j;
    h = Math.floor(h % 7);
    
    return h;
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return Number(value);
}

function displayResults(dayofweek) {
    var days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"];
    window.alert("That day is a " + days[dayofweek]);
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
