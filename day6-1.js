// https://adventofcode.com/2018/day/5

const INPUT_FILE = 'day6input.1.txt';

let coordinates = [];
let areas = [];

function getLimits(coordinates) {
    const result = {
        xMin: Math.min(...coordinates.map(v => v.x)),
        xMax: Math.max(...coordinates.map(v => v.x)),
        yMin: Math.min(...coordinates.map(v => v.y)),
        yMax: Math.max(...coordinates.map(v => v.y)),
    };
    result.width = result.xMax - result.xMin + 1;
    result.height = result.yMax - result.yMin + 1;
    console.log('Limits: ',  result);
    return result;
}

function getAreasMap(coordinates, limits) {
    const areasMap = [];
    for (x = limits.xMin; x <= limits.xMax; x++) {
        for (y = limits.yMin; y <= limits.yMax; y++) {
            let minDistance = undefined;
            let minDistanceCoordinateId = undefined;
            coordinates.forEach((c, index) => {
                const distance = Math.abs(x - c.x) + Math.abs(y - c.y);
                if (minDistance === undefined || distance < minDistance) {
                    minDistance = distance;
                    minDistanceCoordinateId = index;
                } else if (distance === minDistance) {
                    minDistanceCoordinateId = undefined;
                }
            });
            if (areasMap[x - limits.xMin] === undefined) {
                areasMap[x - limits.xMin] = [];
            }
            areasMap[x - limits.xMin][y - limits.yMin] = minDistanceCoordinateId;
        }
    }
    console.log(areasMap);
    return areasMap;
}

function eliminateEdges(areasMap, limits) {

}

function processCoordinates() {
    const limits = getLimits(coordinates);
    const areasMap = getAreasMap(coordinates, limits);


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