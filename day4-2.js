// https://adventofcode.com/2018/day/4

const allRecords = [];

function findMostSleeptMinuteByGuard() {
    const sleepingRecords = {};
    let guardId;
    let minuteFalls;
    let minuteWakes;
    let resultRepeatMinutes = 0;
    let resultMinute;
    let resultGuard;

    for (let i = 0; i < allRecords.length; i++) {
        const r = allRecords[i];
        if (r.type === 'Guard') {
            guardId = r.guard;
            r.guard = guardId;
        } else if (r.type === 'falls') {
            minuteFalls = r.minute;
            r.guard = guardId;
        } else if (r.type === 'wakes') {
            minuteWakes = r.minute;

            const record = sleepingRecords[guardId] = sleepingRecords[guardId] | [];
            for (let j = minuteFalls; j < minuteWakes; j++) {
                record[j]++;
                if (resultRepeatMinutes < record[j]) {
                    resultRepeatMinutes = record[j];
                    resultMinute = j;
                    resultGuard = guardId;
                }
            }
        }
    }

    return { resultMinute, resultGuard };
}

function processRecords() {
    allRecords.sort((r1, r2) => r1.record > r2.record ? 1 : -1 );

    const mostSleptMinuteByGuard = findMostSleeptMinuteByGuard();
    // const result = mostSleptMinute * mostSleepingGuard;
    console.log(`Most slept minute by guard: ${JSON.stringify(mostSleptMinuteByGuard)}`);
    // console.log(`Result: ${result}`);
}

var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('day4input.1.txt')
});

lineReader.on('line', function (line) {
    const splitRecord = line.split(' ');
    const timeSplit = splitRecord[1].substring(0, splitRecord[1].length - 1).split(':');
    
    const result = {
        date: splitRecord[0].substring(1),
        hour: Number.parseInt(timeSplit[0]),
        minute: Number.parseInt(timeSplit[1]),                                               
        type: splitRecord[2],
        guard: splitRecord[2] === 'Guard' ? splitRecord[3].replace('#', '') : undefined,
        record: line
    };

    allRecords.push(result);
});

lineReader.on('close', function () {
    processRecords();
});