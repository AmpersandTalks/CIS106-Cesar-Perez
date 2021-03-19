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
    do {
        product = number * increment;
        window.alert(number.ToString() + " * " + increment + " = " + product);
        increment = increment + 1;
    } while (increment <= factor);
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}
