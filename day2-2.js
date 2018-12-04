// https://adventofcode.com/2018/day/2

const tolerance = 1;
const ids = [];

function compareStrings(str1, str2, tolerance) {
    if (str1.length !== str2.length) {
        return false;
    }
    var diff = 0;
    var diffIndex = false;

    for (var i = 0; i < str1.length; i++) {
        if (str1.charAt(i) !== str2.charAt(i)) {
            diff++;
            diffIndex = i;
            if (diff > tolerance) {
                return false;
            }
        }
    }
    return diffIndex;
}

function findID() {
    var id1, id2;
    var validationResult = false;
    for (var i = 0; i < ids.length; i++ ) {
        id1 = ids[i];
        for (var j = 0; j < ids.length; j++ ) {
            if (i === j) {
                continue;
            }

            id2 = ids[j];
            validationResult = compareStrings(id1, id2, tolerance);
            if (validationResult !== false) {
                break;
            }
        }

        if (validationResult !== false) {
            break;
        }
    }
    return validationResult !== false ? id2.slice(0, validationResult) + id2.slice(validationResult + 1) : undefined;
}

const lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('day2input.txt')
});

lineReader.on('line', function (line) {
    ids.push(line);
});

lineReader.on('close', function (line) {
    const result = findID();
    console.log(result);
});