// https://adventofcode.com/2018/day/1

var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('day1input.txt')
});

var result = 0;

lineReader.on('line', function (line) {
    const nextNumber = Number.parseInt(line);
    result += nextNumber;
});

lineReader.on('close', function (line) {
    console.log('Result:', result);
});