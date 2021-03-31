function main() {
    // this program that asks the user to enter grade scores and calculates the average of the entered scores.
    var total;
    
    doLoop();
}

function doLoop() {
    var score;
    var sum;
    var increment;
    
    increment = 0;
    sum = 0;
    do {
        score = getValue("score");
        score = Number(score);
        if (score >= 0) {
            sum = sum + score;
            window.alert(sum);
            increment = increment + 1;
        }
    } while (score >= 0);
    var average;
    
    average = sum / increment;
    window.alert(average);
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
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
