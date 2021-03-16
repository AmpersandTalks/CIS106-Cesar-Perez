function main() {
    // this program that asks the user to enter grade scores and calculates the average of the entered scores.
    var scores;
    var total;
    var increment;
    var average;
    
    increment = 1;
    total = getValue("total");
    scores = getValue("scores");
    average = (double) scores / total;
    doLoop(scores, total, increment);
}

function doLoop(scores, increment, total, average) {
    window.alert("Do loop counting from " + scores + " to " + total + " by " + increment + ":");
    var count;
    
    count = scores;
    do {
        window.alert(count);
        count = count + scores;
        increment = increment + 1;
    } while (increment <= total);
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}
