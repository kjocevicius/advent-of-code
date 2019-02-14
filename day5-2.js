// https://adventofcode.com/2018/day/5

const INPUT_FILE = 'day5input.txt';

let polymers;

function makeUniqueLower(str) {
    return String.prototype.concat(...new Set(str.toLowerCase()))
}

function reactPolymers(polymersString) {
    let reset = true;
    while (reset) {
        for (let i = 0; i < polymersString.length -1; i++) {
            c1 = polymersString[i];
            c2 = polymersString[i + 1];
            if (c1 !== c2 && c1.toLowerCase() === c2.toLowerCase()) {
                reset = true;
                // console.log(polymersString + `, remove ${c1}, ${c2}`);
                polymersString = polymersString.substring(0, i) + polymersString.substring(i + 2, polymersString.length);
                break;
            }
            reset = false;
        }
    }
    return polymersString.length;
}

function processPolymers() {
    let uniquePolymers = makeUniqueLower(polymers);
    let bestResultIndex;
    let bestResult;
    for (let i = 0; i < uniquePolymers.length; i++) {
        const charToRemove = uniquePolymers[i];
        const modifiedPolymers = polymers
            .replace(new RegExp(charToRemove, 'g'), '')
            .replace(new RegExp(charToRemove.toUpperCase(), 'g'), '');
        // console.log(modifiedPolymers, charToRemove)
        const length = reactPolymers(modifiedPolymers);
        if (bestResultIndex === undefined || bestResult > length) {
            bestResult = length;
            bestResultIndex = i;
        }
    }
    
    console.log(`Result:  ${bestResult}`);
}

var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream(INPUT_FILE)
});

lineReader.on('line', function (line) {
    polymers = line;
});

lineReader.on('close', function () {
    processPolymers();
});