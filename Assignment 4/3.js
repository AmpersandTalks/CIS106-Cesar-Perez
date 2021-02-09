function main() {
  // This program converts the unit miles in to yards, feet, and inches.
  // Reference:
  // https://www.mathsisfun.com/measure/us-standard-length.html
  // https://en.wikibooks.org/wiki/JavaScript
  var miles;
  var yards;
  var feet;
  var inches;

  window.alert('Enter miles distance');
  miles = window.prompt('Enter a value for miles');
  yards = miles * 1760;
  feet = miles * 5280;
  inches = miles * 63360;
  window.alert(
    miles.toString() + ' miles is ' + yards + ' yards ' + feet + ' feet ' + inches + ' inches ');
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
