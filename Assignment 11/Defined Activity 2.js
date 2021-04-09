function main() {
    // This activity FInds the day of the birthday the person inputs.
    // 
    // Refrences: https://en.wikipedia.org/wiki/Zeller%27s_congruence
    // https://www.geeksforgeeks.org/zellers-congruence-find-day-date/
    var h = createArray(6);
    var q;
    var m = createArray(14);
    var k;
    var j;
    var y;
    
    q = getValue("day");
    m = getValue("month");
    y = calculateYear(j, k);
    equation(q, m, k, j, y);
}

function calculateYear(k, j) {
    var y;
    
    k = getValue("decade");
    j = getValue("century") * 100;
    y = k + j;
    
    return y;
}

function equation(q, m, k, j, y) {
    var h = createArray(6);
    
    h = 0;
    if (m == 1) {
        m = 13;
        y = y - 1;
    }
    if (m == 2) {
        m = 14;
        y = y - 1;
    }
    h = q + (double) (13 * (m + 1)) / 5 + k + (double) k / 4 + (double) j / 4 + 5 * j;
    h = h % 7;
    
    return h;
}

function getValue(name) {
    var value;
    
    window.alert(" Enter " + name + " value: ");
    value = window.prompt('Enter a value for value');
    
    return value;
}
