// https://adventofcode.com/2018/day/5

const INPUT_FILE = 'day5input.txt';

let polymers;

function processPolymers() {
    let reset = true;
    while (reset) {
        for (let i = 0; i < polymers.length -1; i++) {
            c1 = polymers[i];
            c2 = polymers[i + 1];
            if (c1 !== c2 && c1.toLowerCase() === c2.toLowerCase()) {
                reset = true;
                // console.log(polymers + `, remove ${c1}, ${c2}`);
                polymers = polymers.substring(0, i) + polymers.substring(i + 2, polymers.length);
                break;
            }
            reset = false;
        }
    }
    console.log(`Result:  ${polymers.length}`);
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