/*
https://adventofcode.com/2019/day/2

Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. 
What value is left at position 0 after the program halts?
*/

var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('day2-1.input')
});

var data;

lineReader.on('line', function (line) {
    data = line
        .split(',')
        .map(v => Number.parseInt(v));
});

lineReader.on('close', function () {
    // console.log(data)

    // 1202 alarm state:
    data[1] = 12;
    data[2] = 2;

    computer(data);
    // console.log(data)

    // 1202 alarm - position 0
    console.log(data[0]);
});

function computer() {
    for (let head = 0; head < data.length; head++) {
        const opcode = data[head];
        switch (opcode) {
            case 1:
                data[data[head + 3]] = data[data[head + 1]] + data[data[head + 2]];
                break;
            case 2:
                data[data[head + 3]] = data[data[head + 1]] * data[data[head + 2]];
                break;
            case 99:
                console.log(`step ${head} : 99)`)
                return;
            default:
                throw Error(`Bad opcode: ${opcode}`)
        }
        head += 3;
        console.log(`step ${head} : ${data[head + 3]} = ${opcode} ( ${data[head + 1]}, ${data[head + 2]} )`);
    }
}