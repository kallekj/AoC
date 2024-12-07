import {
    getDiagonals,
    transpose,
} from '../utils/array.ts';
import { sum } from '../utils/math.ts';

const XMAS = /XMAS/g;
const SAMX = /SAMX/g;

function readXMAS(lines: string[]) {
    const hits = lines.map((line) => Array.from(line.matchAll(XMAS)).length);
    return sum(hits);
}

function readSAMX(lines: string[]) {
    const hits = lines.map((line) => Array.from(line.matchAll(SAMX)).length);
    return sum(hits);
}

async function main() {
    const input = 'input.txt';
    const file = await Deno.readTextFile(input);
    const data = file.split('\n');

    const xmas = readXMAS(data);
    console.log(xmas);
    const samx = readSAMX(data);
    console.log(samx);

    // Split chars
    const splitted = data.map((line) => line.split(''));

    const transposed = transpose(splitted).map((line) => ''.concat(...line));
    // console.log(transposed.join('\n'));
    // Will check up/down and down/up
    const xmasDtu = readXMAS(transposed);
    console.log(xmasDtu);
    const samxDtd = readSAMX(transposed);
    console.log(samxDtd);

    // Get diagonals
    const diagonalsTopDown = getDiagonals(splitted).map((diagonal) =>
        ''.concat(...diagonal)
    );

    // console.log(diagonalsTopDown.join('\n'));
    const xmasDiagonal = readXMAS(diagonalsTopDown);
    console.log(xmasDiagonal);
    const samxDiagonal = readSAMX(diagonalsTopDown);
    console.log(samxDiagonal);

    const result = sum([
        xmas,
        samx,
        xmasDtu,
        samxDtd,
        xmasDiagonal,
        samxDiagonal,
    ]);
    console.log(result);
}

try {
    await main();
} catch (error) {
    console.error(error);
}
