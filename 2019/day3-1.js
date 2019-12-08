/*
https://adventofcode.com/2019/day/3


*/

const lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('day3-1.input')
});

let wires = [];

lineReader.on('line', function (line) {
    wires.push(line.split(","));
});

lineReader.on('close', function () {

});