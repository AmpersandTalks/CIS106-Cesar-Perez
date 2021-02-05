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

if (typeof alert === "undefined") {
    global.alert = function(message) {
        console.log(message);
    };
}

if (typeof prompt === "undefined") {
    global.prompt = function(message) {
        var fs = require("fs");
        var result = "";
        var buffer = Buffer.alloc(1);

        console.log(message);
        for(;;){
            fs.readSync(0, buffer, 0, 1);
            if(buffer[0] === 10){
                break;
            }else if(buffer[0] !== 13){
                result += buffer.toString();
            }
        }

        return result;
    }
}

if (typeof window === "undefined") {
    global.window = {
        alert : global.alert,
        prompt : global.prompt
    };
}

main();
