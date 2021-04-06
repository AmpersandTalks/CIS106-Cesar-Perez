// this program uses a loop to generate a list of multiplication expressions for a given value

function main() {
    let question = "";

    do {
        let number = getValue("number");
        let factor = getValue("factor");
        displayExpressions(number, factor);
        question = window.prompt("Do you want to continue (y/N)?");
    } while (question == "y");
}

function displayExpressions(number, factor) {
    for (let increment = 1; increment <= factor; increment++)
    {
        product = number * increment;
        window.alert(number.toString() + " * " + increment + " = " + product);
    }
}

function getValue(name) {
    let value = window.prompt(" Enter " + name + " value:");    
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
