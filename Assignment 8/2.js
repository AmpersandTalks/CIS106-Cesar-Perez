function main() {
    // this program that asks the user to enter grade scores and calculates the average of the entered scores.
    var scores;
    var total;
    var average;
    var score;
    
    total = getValue("total");
    scores = getScores(total);
    average = (double) scores / total;
    getTotal(scores, total, average);
}

function getScores(total) {
    var value;
    var counter;
    
    counter = 1;
    while (counter <= total) {
        window.alert(" Enter score value: ");
        value = window.prompt('Enter a value for value');
        counter = counter + 1;
    }
    
    return value;
}

function getTotal(scores, total, average) {
    window.alert(" The avergae of all these score is " + average);
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}
