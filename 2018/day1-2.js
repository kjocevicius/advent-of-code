// https://adventofcode.com/2018/day/1

var result = 0;
var frequencies = [];
var firstRepeatedFrequency = undefined;

function startReading() {
    var lineReader = require('readline').createInterface({
        input: require('fs').createReadStream('day1input.txt')
    });

    lineReader.on('line', function (line) {
        if (!firstRepeatedFrequency) {
            frequencies.push(result);
        }

        const nextNumber = Number.parseInt(line);
        result += nextNumber;

        if (!firstRepeatedFrequency && frequencies.indexOf(result) > -1) {
            firstRepeatedFrequency = result;
            lineReader.close();
        }
    });

    lineReader.on('close', function (line) {
        if (firstRepeatedFrequency) {
            console.log('First repeated frequency:', firstRepeatedFrequency);
        } else {
            startReading();
        }
    })

    return lineReader;
}

startReading();