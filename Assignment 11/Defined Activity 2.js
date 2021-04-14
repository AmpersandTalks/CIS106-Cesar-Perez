// This activity FInds the day of the birthday the person inputs.
    // 
    // Refrences: https://en.wikipedia.org/wiki/Zeller%27s_congruence
    // https://www.geeksforgeeks.org/zellers-congruence-find-day-date/

function main() {
    var year = getvalue("year");
    var month = getvalue("month");
    var day = getvalue("day");
    
    
    var dayofweek = calculatedayofweek(year,month, day);
    displayresults(dayofweek);
    window.alert("day of week:" + dayofweek);
}

function calculatedayofweek(year, month, day) {
    var j = math.floor(year / 100);
    var k = year % 100;
    var m = month;
    var q = day;
    
    if (m < 3) {
        m += 12;
        y -= 1;
    }
    
    var h = q + (13 * (m + 1)) / 5 + k +  k / 4 + j / 4 + 5 * j;
    h = math.floor(h % 7);
    
    return h;
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return Number(value);
}

function getvalue(dayofweek) {
    var days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"];
    window.alert("That day is a " + days[dayofweek]);
}
