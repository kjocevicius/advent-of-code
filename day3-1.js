//Incomplete


var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('day3input.txt')
});

var result = 0;
var cuts = [];

function calculateOverlaps() {
    //TODO
}

lineReader.on('line', function (line) {
    const split1 = line.split(' ');
    const coordinatesSplit = split1[2].slice(0, split1[2].length - 1).split(',');
    const sizeSplit = split1[3].split('x');
    cuts.push({
        id: split1[0].slice(1),
        x: coordinatesSplit[0],
        y: coordinatesSplit[1],
        w: sizeSplit[0],
        h: sizeSplit[1],
    });
});

lineReader.on('close', function (line) {
    var overlaps = calculateOverlaps();
    console.log(cuts[0]);
    console.log(overlaps);
});