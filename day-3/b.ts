import { sum } from '../utils/math.ts';

enum Types {
    DO = 'do()',
    DONT = "don't()",
}

function sequenceParser(sequence: string) {
    const regex = /mul\(\d{1,3},\d{1,3}\)/gm;
    const mulSequences = sequence.match(regex);
    const sumSequences = mulSequences?.map((mul) => {
        const values = mul.match(/\d{1,3}/g)?.map((match) => parseInt(match));
        if (!values) {
            return 0;
        }
        return values[0] * values[1];
    });
    return sum(sumSequences);
}

function removeRanges(input: string, ranges: number[][]): string {
    let result = '';
    let lastIndex = 0;
    for (const [start, end] of ranges) {
        result += input.slice(lastIndex, start);
        lastIndex = end;
    }

    result += input.slice(lastIndex);

    return result;
}

function findValidSequences(sequence: string) {
    const doDontRegex = /don't\(\)|do\(\)/gm;
    const dosAndDonts = sequence.matchAll(doDontRegex);
    const dosAndDontsIndexes = Array.from(
        dosAndDonts.map((seq) => {
            if (seq[0].includes(Types.DO)) {
                return {
                    type: Types.DO,
                    index: seq.index,
                };
            }

            return {
                type: Types.DONT,
                index: seq.index,
            };
        })
    );
    let prevType = Types.DO[0];
    const removeBetween: number[][] = [];
    for (let i = 0; i < dosAndDontsIndexes.length; i++) {
        const current = dosAndDontsIndexes[i];
        if (current.type === Types.DONT && prevType !== Types.DONT) {
            prevType = Types.DONT;
            const nextDo = dosAndDontsIndexes
                .slice(i)
                .findIndex((next) => next.type === Types.DO);
            const startIndex = current.index;
            const endIndex = dosAndDontsIndexes.slice(i)[nextDo].index;
            removeBetween.push([startIndex, endIndex]);
        }

        if (current.type === Types.DO) {
            prevType = Types.DO;
        }
    }

    const correctSequences = removeRanges(sequence, removeBetween);

    return correctSequences;
}

async function main() {
    const input = 'input.txt';
    const sequence = await Deno.readTextFile(input);
    const validSequences = findValidSequences(sequence);
    const sum = sequenceParser(validSequences);
    console.log(sum);
}

try {
    await main();
} catch (error) {
    console.error(error);
}
