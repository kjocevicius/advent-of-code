// https://adventofcode.com/2018/day/5

const INPUT_FILE = 'day6input.txt';

let coordinates = [];

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
    // console.log('areasMap', areasMap);
    return areasMap;
}

function findEdgeAreas(areasMap, limits) {
    const edgeIds = new Set();
    for (let x = 0; x < limits.width; x++) {
        edgeIds.add(areasMap[x][0]);
    }
    for (let y = 0; y < limits.width; y++) {
        edgeIds.add(areasMap[0][y]);
    }

    const result = [...edgeIds].filter(v => v !== undefined);
    console.log('Edges: ', result);
    return result;
}

function calculateAreasSizes(areasMap, limits) {
    for (let x = 0; x < limits.width; x++) {
        for (let y = 0; y < limits.height; y++) {
            const areaId = areasMap[x][y];
            if (areaId !== undefined) {
                coordinates[areaId].size++;
            }
        }
    }
}

function processCoordinates() {
    const limits = getLimits(coordinates);
    const areasMap = getAreasMap(coordinates, limits);
    const edgeIds = findEdgeAreas(areasMap, limits);
    calculateAreasSizes(areasMap, limits);
    const nonEdgeSizes = coordinates
        .filter((v, i) => !edgeIds.includes(i))
        .map(v => v.size);
    const largestSize = Math.max(...nonEdgeSizes);

    console.log(largestSize);
}

var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream(INPUT_FILE)
});

lineReader.on('line', function (line) {
    const coords = line.split(', ').map(v => parseInt(v));
    coordinates.push({x: coords[0], y: coords[1], size: 0});
});

lineReader.on('close', function () {
    processCoordinates();
});