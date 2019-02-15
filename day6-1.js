// https://adventofcode.com/2018/day/5

const INPUT_FILE = 'day6input.1.txt';

let coordinates = [];

function processCoordinates() {
    const limits = {
        xMin: Math.min(...coordinates.map(v => v.x)),
        xMax: Math.max(...coordinates.map(v => v.x)),
        yMin: Math.min(...coordinates.map(v => v.y)),
        yMax: Math.max(...coordinates.map(v => v.y)),
    };
    coordinates.forEach(c => {
        // if ()
    });
    console.log(limits)
}

var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream(INPUT_FILE)
});

lineReader.on('line', function (line) {
    const coords = line.split(', ').map(v => parseInt(v));
    coordinates.push({x: coords[0], y: coords[1]});
});

lineReader.on('close', function () {
    console.log(coordinates)
    processCoordinates();
});