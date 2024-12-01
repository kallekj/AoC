import { stringArrayToInt, transpose } from "../utils/array.ts";


function getSimilarity(a: number[], b: number[]){
    return a.map(left => b.filter(right => left === right).length * left)
}

async function main(){
    const input = 'input.txt';
    const file =  await Deno.readTextFile(input);
    const lines = file.split('\n');
    const [a, b] = transpose(lines.map(line => line.split(/\s{3}/)));
    const result = getSimilarity(stringArrayToInt(a), stringArrayToInt(b));

    console.log(result.reduce((prev, curr) => prev += curr))
}

try {
    await main();   
} catch (error) {
    console.error(error);
}