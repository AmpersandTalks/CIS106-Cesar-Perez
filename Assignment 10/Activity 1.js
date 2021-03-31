function main() {
    // this program uses a loop to generate a list of multiplication expressions for a given value
    var number;
    var factor;
    var increment;
    
    number = getValue("number");
    factor = getValue("factor");
    increment = 1;
    forLoop(number, factor, increment);
}

function forLoop(number, factor, increment) {
    window.alert(" While loop multiplication from " + number + " to " + factor + " by " + increment + " : ");
    var product;
    
    product = number;
    for (increment = increment; increment <= factor; increment++) {
        product = number * increment;
        window.alert(number.ToString() + " * " + increment + " = " + product);
    }
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}
