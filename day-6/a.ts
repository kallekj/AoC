import { GuardMap } from './guardMap.ts'

async function main() {
    const input = '/home/kj/Documents/programming/AoC/day-6/input.txt';
    const file = await Deno.readTextFile(input);
    const guard = new GuardMap(file);

    let isDone = true
    while(isDone){
        try{
            isDone = guard.visitNextNode();
        } catch(e) {
            if(e instanceof Error && e.message === 'Outside!'){
                break;
            }
        }
    }

    console.log(guard.numVisited);
}

try {
    await main();
} catch (error) {
    console.error(error);
}
