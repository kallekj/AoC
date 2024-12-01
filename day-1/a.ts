import zip from 'https://deno.land/x/stdlib_utils_zip/mod.js';
import { stringArrayToInt, transpose } from "../utils/array.ts";


function sortListsAndGetDistance(a: number[], b: number[]){
    const aSorted = a.sort();
    const bSorted = b.sort();
    return zip(aSorted, bSorted).map(([first, second]) => Math.abs(first-second));
}

async function main(){
    const input = 'input.txt';
    const file =  await Deno.readTextFile(input);
    const lines = file.split('\n');
    const [a, b] = transpose(lines.map(line => line.split(/\s{3}/)));
    const result = sortListsAndGetDistance(stringArrayToInt(a), stringArrayToInt(b));

    console.log(result.reduce((prev, curr) => prev += curr))
}

try {
    await main();   
} catch (error) {
    console.error(error);
}