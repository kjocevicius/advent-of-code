// https://adventofcode.com/2018/day/4

const allRecords = [];
const sleepingRecords = {};

function findMostSleepingGuardId() {
    let guardId;
    let minuteFalls;
    let minuteWakes;

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
            if (!sleepingRecords[guardId]) {
                sleepingRecords[guardId] = {
                    minutesSlept: 0,
                    minutes: []
                };
            }

            const record = sleepingRecords[guardId];
            record.minutesSlept += (minuteWakes - minuteFalls);
            for (let j = minuteFalls; j < minuteWakes; j++) {
                if (!record.minutes[j]) {
                    record.minutes[j] = 0;
                }
                record.minutes[j]++;
            }
        }
    }

    const ids = Object.keys(sleepingRecords);
    ids.sort((r1, r2) => sleepingRecords[r1].minutesSlept < sleepingRecords[r2].minutesSlept ? 1 : -1 );
    return ids[0]
}

function findMostSleeptMinuteByGuard(guardId) {
    const record = sleepingRecords[guardId];
    let maxMinutes = 0;
    let maxMinutesIndex = 0;
    for (let i = 0; i < record.minutes.length; i++) {
        if (record.minutes[i] > maxMinutes) {
            maxMinutes = record.minutes[i];
            maxMinutesIndex = i;
        }
    }
    return maxMinutesIndex;
}

function processRecords() {
    allRecords.sort((r1, r2) => r1.record > r2.record ? 1 : -1 );

    const mostSleepingGuard = findMostSleepingGuardId();
    const mostSleptMinute = findMostSleeptMinuteByGuard(mostSleepingGuard);
    const result = mostSleptMinute * mostSleepingGuard;
    console.log(`Most sleeping guard: ${mostSleepingGuard}, most slept minute: ${mostSleptMinute}`);
    console.log(`Result: ${result}`);
}

var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('day4input.txt')
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