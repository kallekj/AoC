import { sum } from '../utils/math.ts';

function sequenceParser(sequence: string) {
    const regex = /mul\(\d{1,3},\d{1,3}\)/gm;
    const mulSequences = sequence.match(regex);
    const sumSequences = mulSequences?.map((mul) => {
        const values = mul.match(/\d{1,3}/g)?.map(match => parseInt(match))
        if(!values) {
            return 0;
        }
        return values[0] * values[1];
    });
    return sum(sumSequences);
}

async function main() {
    const input = 'input.txt';
    const sequence = await Deno.readTextFile(input);
    const sum = sequenceParser(sequence);
    console.log(sum);
}

try {
    await main();
} catch (error) {
    console.error(error);
}
