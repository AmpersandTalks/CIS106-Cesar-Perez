function main() {
    // this program uses a loop to generate a list of multiplication expressions for a given value
    var number;
    var var_input;
    var increment;
    
    number = getValue("number");
    var_input = getValue("input");
    increment = 1;
    whileLoop(number, var_input, increment);
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}

function whileLoop(number, var_input, increment) {
    window.alert(" While loop multiplication from " + number + " to " + var_input + " by " + increment + " : ");
    var product;
    
    product = number;
    while (increment <= var_input) {
        product = number * increment;
        window.alert(number.ToString() + " * " + increment + " = " + product);
        increment = increment + 1;
    }
}
