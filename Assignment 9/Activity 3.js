function main() {
    // this program that asks the user to enter an amount of hours worked to calculate weekly until user enters time that is higher than 40 hours.
    var rateperhour;
    
    rateperhour = getValue("rateperhour");
    doLoop(rateperhour);
}

function doLoop(rateperhour) {
    var hours;
    var sum;
    var increment;
    
    increment = 0;
    sum = 0;
    do {
        hours = getValue("hours");
        if (hours <= 40) {
            sum = rateperhour * hours;
            window.alert(sum);
            increment = increment + 1;
        } else {
            window.alert("please input a value under 40");
        }
    } while (hours <= 40);
    var average;
    
    average = (double) sum / increment;
    window.alert(average);
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}
