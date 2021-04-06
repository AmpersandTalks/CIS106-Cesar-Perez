function main() {
    // this program uses a loop to generate a list of multiplication expressions for a given value
    var number;
    var factor;
    var increment;
    
    number = getValue("number");
    factor = getValue("factor");
    increment = 1;
    doLoop(number, factor, increment);
}

function doLoop(number, factor, increment) {
    window.alert(" While loop multiplication from " + number + " to " + factor + " by " + increment + " : ");
    var product;
    
    product = number;
    window.alert(" Enter value y for Yes or n for no. ");
    var question;
    
    do {
        do {
            question = getValue2("question");
            product = number * increment;
            window.alert(number.ToString() + " * " + increment + " = " + product);
            increment = increment + 1;
        } while (question == "y");
    } while (increment <= factor);
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}

function getValue2(name) {
    var value2;
    
    window.alert(" Enter " + name + " value: ");
    value2 = window.prompt('Enter a value for value2');
    
    return value2;
}
