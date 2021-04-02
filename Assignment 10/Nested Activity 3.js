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
    window.alert(" Enter value 1 for Yes or 2 for no. ");
    var question;
    
    do {
        question = getValue("question");
        if (question == 1) {
            product = number * increment;
            window.alert(number.ToString() + " * " + increment + " = " + product);
            increment = increment + 1;
        } else {
            window.alert("Pleas input value 1 for yes or 2 for no.");
        }
    } while (increment <= factor);
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}
