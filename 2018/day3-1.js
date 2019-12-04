// https://adventofcode.com/2018/day/3

var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('day3input.txt')
});

const cuts = [];
const usedCoordinates = new Set();
const overlappingCoordinates = new Set();

function processCut(cut) {
    for (let x = cut.x; x < cut.x + cut.w; x++) {
        for (let y = cut.y; y < cut.y + cut.h; y++) {
            const coordString = `${x}:${y}`;
            if (usedCoordinates.has(coordString)) {
                overlappingCoordinates.add(coordString);
            } else {
                usedCoordinates.add(coordString);
            }
        }   
    }
}

function calculateOverlaps() {
    cuts.forEach(processCut);
    return overlappingCoordinates.size;
}

lineReader.on('line', function (line) {
    const split1 = line.split(' ');
    const coordinatesSplit = split1[2].slice(0, split1[2].length - 1).split(',');
    const sizeSplit = split1[3].split('x');
    cuts.push({
        id: split1[0].slice(1),
        x: Number.parseInt(coordinatesSplit[0]),
        y: Number.parseInt(coordinatesSplit[1]),
        w: Number.parseInt(sizeSplit[0]),
        h: Number.parseInt(sizeSplit[1]),
    });
});

lineReader.on('close', function () {
    var overlaps = calculateOverlaps();
    console.log('Result: ', overlaps);
});