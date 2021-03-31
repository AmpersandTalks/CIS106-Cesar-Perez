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
        if (score >= 0) {
            sum = sum + score;
            window.alert(sum);
            increment = increment + 1;
        }
    } while (score >= 0);
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
