function main() {
    // this program uses a loop to generate a list of multiplication expressions for a given value
    var number;
    var factor;
    
    number = getValue("number");
    factor = getValue("factor");
    forLoop(number, factor);
}

function forLoop(number, factor) {
    window.alert(" While loop multiplication from " + number + " to " + factor + " by 1 :");
    var product;
    var increment;
    
    increment = 1;
    product = number;
    for (increment = increment; increment <= factor; increment++) {
        product = number * increment;
        window.alert(number.toString() + " * " + increment + " = " + product);
    }
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
