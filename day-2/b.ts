import { stringArrayToInt } from '../utils/array.ts';
import { sum } from '../utils/math.ts';

function isSafe(report: number[]) {
    const deltas = report
        .map((value, index) => {
            if (index !== report.length - 1) {
                const compValue = report[index + 1];
                return value - compValue;
            }

            if (index === report.length - 1) {
                const compValue = report[index - 1];
                return compValue - value;
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

    return {
        safe: allPositiveAndLessThanThree || allNegativeAndGreaterThanThree,
        report,
    };
}

function faultDampener(input: {
    safe: boolean;
    report: number[];
}) {
    const { safe, report } = input;
    if (!safe) {
        const newTests = report.map((_, index) => {
            let newReport: number[] = [];
            if (index === report.length - 1) {
                newReport = report.slice(0, report.length - 1);
            } else {
                newReport = report
                    .slice(0, index)
                    .concat(report.slice(index + 1));
            }

            const newIsSafe = isSafe(newReport);
            return newIsSafe;
        });
        return (
            newTests.find((test) => test.safe) || { safe: false, report: [] }
        );
    }

    return input;
}

async function main() {
    const input = 'input.txt';
    const file = await Deno.readTextFile(input);
    const reports = file.split('\n');
    const reportWithLevels = reports.map((report) =>
        stringArrayToInt(report.split(/\s{1}/))
    );
    const safeReports = sum(
        reportWithLevels.map((report) => {
            return faultDampener(isSafe(report)).safe ? 1 : 0;
        })
    );
    console.log(safeReports);
}

try {
    await main();
} catch (error) {
    console.error(error);
}
