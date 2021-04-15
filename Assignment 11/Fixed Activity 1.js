// This program asks the user for grades and the calculates the highest, lowest and average of the scores
// Reference:
//https://www.mathsisfun.com/definitions/average.html

function main() {
    
    var scores = getScores();
    var grades = Array(scores);
    
    var increment = 0;
    while (increment < scores) {
        grades[increment] = getGrades();
        increment = increment + 1;
    }
    var max = getMax(grades, scores);
    var min = getMin(grades, scores);
    var average = getAverage(grades, scores);
    getOutput(max, min, average);
}

function getAverage(grades, scores) {
    
    var total = 0;
    for (increment = 1; increment < scores; increment++) {
        total = total + grades[increment];
    }
    average = calculate(total) / scores;
    
    return average;
}

function getGrades() {
    var grades;
    
    window.alert("Please Input Grades :");
    grades = window.prompt('Enter a value for grades');
    
    return grades;
}

function getMax(grades, scores) {
    
    var max = [0];
    for (increment = 1; increment < scores; increment++) {
        if (max < grades[increment]) {
            max = grades[increment];
        }
    }
    
    return max;
}

function getMin(grades, scores) {
    var increment;
    var min;
    
    min = grades[0];
    for (increment = 1; increment < scores; increment++) {
        if (min > grades[increment]) {
            min = grades[increment];
        }
    }
    
    return min;
}

function getOutput(max, min, average) {
    window.alert("Maximum Grade:" + max);
    window.alert("Minimum Grade :" + min);
    window.alert("Average Grade :" + average);
}

function getScores() {
    var scores;
    
    window.alert("Please enter how many scores you want to enter");
    scores = window.prompt('Enter a value for scores');
    
    return scores;
}

if (typeof window === "undefined") {
    global.window = {
        alert : global.alert,
        prompt : global.prompt
    };
}

main();
