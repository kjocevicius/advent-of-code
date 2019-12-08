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

var program;

lineReader.on('line', function (line) {
    program = line
        .split(',')
        .map(v => Number.parseInt(v));
});

lineReader.on('close', function () {
    const result = findArguments(program, 19690720);
    console.log(result);
    console.log(100 * result[0] + result[1]);
});

function findArguments(program, requiredInput) {
    for (let arg1 = 0; arg1 < 100; arg1++) {
        for (let arg2 = 0; arg2 < 100; arg2++) {
            program[1] = arg1;
            program[2] = arg2;
            const result = computer(program);
            if (result === 19690720) {
                return [arg1, arg2];
            }
        }
    }
}

function computer(program) {
    const memory = [];
    memory.push(...program);

    for (let head = 0; head < memory.length; head++) {
        const opcode = memory[head];
        switch (opcode) {
            case 1:
                memory[memory[head + 3]] = memory[memory[head + 1]] + memory[memory[head + 2]];
                break;
            case 2:
                memory[memory[head + 3]] = memory[memory[head + 1]] * memory[memory[head + 2]];
                break;
            case 99:
                console.log(`step ${head} : 99, result : ${memory[0]}`)
                return memory[0];
            default:
                throw Error(`Bad opcode: ${opcode}`)
        }
        head += 3;
    }
}