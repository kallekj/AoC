import { stringArrayToInt } from "../utils/array.ts";
import { GuardMap } from './guardMap.ts'
import { ObstacleMab } from "./obstacleMap.ts";

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

    let obstacles = 0;
    guard.visitedNodes.forEach((node) => {
        const [i,j] = stringArrayToInt(node.split(','));
        if(i === guard.guardPosition[0] && j === guard.guardPosition[1]){
            return;
        }
        const newMap = JSON.parse(JSON.stringify(guard.mapMatrix))
        newMap[i][j] = '#';
        const obstacleMap = new ObstacleMab(newMap, guard.guardPosition, { name: 'UP', value: [-1, 0] });
        
        while(true){
            try {
                obstacleMap.visitNextNode();
            } catch (e) {
                if(e instanceof Error && e.message === 'loop'){
                    obstacles += 1;
                }
                break;
            }
        }
    })

    console.log(obstacles)

}

try {
    await main();
} catch (error) {
    console.error(error);
}
