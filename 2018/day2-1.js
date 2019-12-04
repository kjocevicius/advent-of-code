// https://adventofcode.com/2018/day/2

var twoOfAnyCount = 0;
var threeOfAnyCount = 0;

function countLetters(line) {
    const result = {};
    for (var i = 0; i < line.length; i++) {
        const char = line.charAt(i);
        if (!result[char]) {
            result[char] = 0;
        }
        result[char]++;
    }
    return result;
}

var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('day2input.txt')
});

lineReader.on('line', function (line) {
    const letterCounts = countLetters(line);
    const counts = Object.keys(letterCounts)
        .map(k => letterCounts[k]);
    if (counts.indexOf(2) > -1) {
        twoOfAnyCount++;
    }
    if (counts.indexOf(3) > -1) {
        threeOfAnyCount++;
    }
});

lineReader.on('close', function (line) {
    console.log('twoOfAnyCount:', twoOfAnyCount);
    console.log('threeOfAnyCount:', threeOfAnyCount);
    console.log('Result:', twoOfAnyCount * threeOfAnyCount);
});