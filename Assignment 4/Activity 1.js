function main() {
    // This program calculates  their weekly, monthly, and annual gross pay.
    // References:
    // https://en.wikibooks.org/wiki/JavaScript
    var hours;
    var rateperhour;
    var weekly;
    var monthly;
    var annual;
    
    window.alert("Enter hours worked this week");
    hours = window.prompt('Enter a value for hours');
    window.alert("Enter rate per hour");
    rateperhour = window.prompt('Enter a value for rateperhour');
    weekly = hours * rateperhour;
    monthly = hours * rateperhour * 4;
    annual = hours * rateperhour * 52;
    window.alert("$" + weekly + " weekly " + "$" + monthly + " monthly " + "$" + annual + " annually ");
}
if (typeof alert === 'undefined') {
  global.alert = function (message) {
    console.log(message);
  };
}

if (typeof prompt === 'undefined') {
  global.prompt = function (message) {
    var fs = require('fs');
    var result = '';
    var buffer = Buffer.alloc(1);

    console.log(message);
    for (;;) {
      fs.readSync(0, buffer, 0, 1);
      if (buffer[0] === 10) {
        break;
      } else if (buffer[0] !== 13) {
        result += buffer.toString();
      }
    }

    return result;
  };
}

if (typeof window === 'undefined') {
  global.window = {
    alert: global.alert,
    prompt: global.prompt,
  };
}

main();