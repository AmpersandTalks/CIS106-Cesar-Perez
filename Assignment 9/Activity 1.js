function main() {
    // this program that asks the user to enter grade scores and calculates the average of the entered scores.
    var total;
    
    total = getValue("total");
    var increment;
    
    increment = 1;
    doLoop(total, increment);
}

function doLoop(increment, total) {
    var score;
    
    score = getValue("score");
    var sum;
    
    sum = score;
    do {
        var score2;
        
        score2 = getValue("score2");
        sum = sum + score2;
        window.alert(sum);
        increment = increment + 1;
    } while (increment >= total);
    var average;
    
    average = (double) sum / total;
    window.alert(average);
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}
