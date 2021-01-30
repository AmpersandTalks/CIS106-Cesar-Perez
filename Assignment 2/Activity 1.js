function main() {
    // This Program displays "Hello Cesar!"
    window.alert("Hello Cesar!");
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
