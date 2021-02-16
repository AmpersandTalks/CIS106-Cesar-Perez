function main() {
    // This program converts Human years to Dog years.
    // Reference:
    // https://en.wikipedia.org/wiki/Aging_in_dogs
    var dogname;
    var humanyears;
    var dogyears;
    
    dogname = getdogname();
    dogyears = calculatedogyears();
    displayResult(dogname, dogyears);
}

function calculatedogyears() {
    var dogyears;
    var humanyears;
    
    window.alert("Enter dogs age is in human years");
    humanyears = window.prompt('Enter a value for humanyears');
    dogyears = humanyears * 7;
    
    return dogyears;
}

function displayResult(dogname, dogyears) {
    window.alert(dogname + " is " + dogyears + " Dog Years");
}

function getdogname() {
    var dogname;
    
    window.alert("Enter Dog's Name");
    dogname = window.prompt('Enter a value for dogname');
    
    return dogname;
}
