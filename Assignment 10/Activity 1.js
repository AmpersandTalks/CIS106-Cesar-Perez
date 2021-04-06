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
        window.alert(number.ToString() + " * " + increment + " = " + product);
    }
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}
