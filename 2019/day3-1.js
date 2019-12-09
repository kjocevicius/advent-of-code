/*
https://adventofcode.com/2019/day/3


*/

const lineReader = require('readline').createInterface({
    // input: require('fs').createReadStream('day3-1.input')
    // input: require('fs').createReadStream('day3-1.longer.135.input')
    input: require('fs').createReadStream('day3-1.longer.159.input')
    // input: require('fs').createReadStream('day3-1.simple.input')
});

let wires = [];

lineReader.on('line', function (line) {
    wires.push(
        line.split(",")
            .map(turn => ({
                direction: turn.charAt(0),
                steps: Number.parseInt(turn.substring(1))
            }))
    );
});

lineReader.on('close', function () {
    findResult();
});

function findResult() {
    const intersectionDistances = findIntersections(wires[0], wires[1]);
    console.log(intersectionDistances);

    let shortestDist;
    intersectionDistances
        .map(c => c.distance)
        .forEach(c => {
            if (shortestDist === undefined || c < shortestDist) {
                shortestDist = c;
            }
        });
    console.log(shortestDist);
}

function findIntersections(wireSteps1, wireSteps2) {
    let currentCoord1 = coord(0, 0);
    let intersections = [];
    wireSteps1.forEach(turn => {

        for (let turnStep = 0; turnStep <= turn.steps; turnStep++) {
            advanceTurn(currentCoord1, turn.direction);

            let currentCoord2 = coord(0, 0);
            for (let j = 0; j < wireSteps2.length; j++) {
                const innerTurn = wireSteps2[j];

                for (let innerTurnStep = 0; innerTurnStep <= innerTurn.steps; innerTurnStep++) {
                    advanceTurn(currentCoord2, innerTurn.direction);

                    if (currentCoord1.x === currentCoord2.x && currentCoord1.y === currentCoord2.y) {
                        intersections.push({
                            distance: calculateDistance(0, 0, currentCoord1.x, currentCoord1.y),
                            coord: coord(currentCoord1.x, currentCoord1.y)
                        });
                    }
                }
            }

        }
    });
    return intersections;
}

function advanceTurn(coords, direction) {
    switch (direction) {
        case 'U':
            nextPoint = coords.y++;
            break;
        case 'D':
            nextPoint = coords.y--;
            break;
        case 'R':
            nextPoint = coords.x++;
            break;
        case 'L':
            nextPoint = coords.x--;
            break;
    }
}

const coord = (x, y) => ({ x, y });

function calculateDistance(x1, y1, x2, y2) {
    return Math.abs(x1 - x2) + Math.abs(y1 - y2);
}
