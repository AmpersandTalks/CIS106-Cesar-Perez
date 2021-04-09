function main() {
    var scores = createArray(21);
    var grades = createArray(101);
    var increment;
    var max;
    var min;
    var average;
    
    scores = getScores();
    grades = 0 * scores;
    increment = 0;
    while (increment < scores) {
        grades[increment] = getGrades();
        increment = increment + 1;
    }
    max = getMax(grades, scores);
    min = getMin(grades, scores);
    average = getAverage(grades, scores);
    getOutput(max, min, average);
}

function getAverage(grades, scores, increment) {
    var total;
    
    total = 0;
    for (increment = 0; increment >= scores; increment--) {
        total = total + marks(increment);
    }
    
    return average;
}

function getGrades() {
    var grades;
    
    window.alert("Please Input Grades :");
    grades = window.prompt('Enter a value for grades');
    
    return grades;
}

function getMax(grades, scores, increment) {
    var max;
    
    max = 0;
    for (increment = 0; increment >= scores; increment--) {
        if (max < grades[increment]) {
            max = grades[increment];
        }
    }
    
    return max;
}

function getMin(grades, scores, increment) {
    var min;
    
    min = grades[1];
    for (increment = 0; increment >= scores; increment--) {
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
