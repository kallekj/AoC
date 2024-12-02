import { stringArrayToInt } from '../utils/array.ts';
import { sum } from '../utils/math.ts';

function isSafe(report: number[]) {
    const deltas = report
        .map((value, index) => {
            if (index !== report.length - 1) {
                const compValue = report[index + 1];
                return value - compValue;
            }

            return NaN;
        })
        .filter((delta) => !isNaN(delta));

    const allPositiveAndLessThanThree = deltas.every(
        (delta) => delta > 0 && delta <= 3
    );
    const allNegativeAndGreaterThanThree = deltas.every(
        (delta) => delta < 0 && delta >= -3
    );

    return allPositiveAndLessThanThree || allNegativeAndGreaterThanThree
        ? 1
        : 0;
}

async function main() {
    const input = 'input.txt';
    const file = await Deno.readTextFile(input);
    const reports = file.split('\n');
    const reportWithLevels = reports.map((report) =>
        stringArrayToInt(report.split(/\s{1}/))
    );
    const safeReports = sum(reportWithLevels.map((report) => isSafe(report)));
    console.log(safeReports);
}

try {
    await main();
} catch (error) {
    console.error(error);
}
