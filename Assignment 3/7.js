function main() {
    // This program converts the unit of Human Years into dog years.
    var dogname;
    var hy;
    var dy;
    
    window.alert("Enter Dog's Name");
    dogname = window.prompt('Enter a value for dogname');
    window.alert("Enter Human Years");
    hy = window.prompt('Enter a value for hy');
    dy = hy * 7;
    window.alert(dogname + " is " + dy + " Dog Years");
}
