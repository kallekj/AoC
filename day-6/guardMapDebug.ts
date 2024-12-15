const directions = {
    UP: [-1, 0],
    DOWN: [1, 0],
    LEFT: [0, -1],
    RIGHT: [0, 1]
};

type Directions = keyof typeof directions;

export class ObstacleMab {
    private map: string[][];
    private visited: Set<string>;
    public debugMap: string[][];
    private limits: {
        minRow: number;
        minCol: number;
        maxRow: number;
        maxCol: number; 
    }
    private pos: number[];
    private direction: {
        name: Directions;
        value: number[]
    };
    private guardPos: number[];

    constructor(guardMap: string[][], endPos: number[], endDirection: { name: Directions, value: number[]}, guardPos: number[]){
        this.map = guardMap;
        this.limits = { minCol: 0, minRow: 0, maxRow: this.map.length - 1, maxCol: this.map[0].length - 1 };
        this.visited = new Set<string>();
        this.pos = endPos;
        this.direction = {
            name: 'UP',
            value: directions.UP
        };
        this.guardPos = guardPos;
        this.debugMap = Array.from(this.map);
        

        // Check up
        if(endDirection.name === 'UP'){
            this.direction = {
                name: 'DOWN',
                value: directions.DOWN
            };
        }
        
        // Check down
        if(endDirection.name === 'DOWN'){
            this.direction = {
                name: 'UP',
                value: directions.UP
            };
        }

        // Check left
        if(endDirection.name === 'LEFT'){
            this.direction = {
                name: 'RIGHT',
                value: directions.RIGHT
            };
        }

        // Check right
        if(endDirection.name === 'RIGHT'){
            this.direction = {
                name: 'LEFT',
                value: directions.LEFT
            };
        }

        console.log('GuardMap Initialized - settings:');
        console.log(JSON.stringify({ visited: this.visited.entries(), pos: this.pos, direction: this.direction, limits: this.limits }));
    }

    public get numVisited(){
        return this.visited.size;
    }

    public visitNextNode(){
        // If dir UP
        if(this.direction.name === 'UP'){
            const newPos = this.getNewPos();
            const valAtNewPos = this.getValAtNewPos(newPos);
            if(valAtNewPos === '#'){
                this.direction = {
                    name: 'RIGHT',
                    value: directions.RIGHT,
                };
            } else {
                return this.visit(newPos);
            }
        }

        // If dir DOWN
        if(this.direction.name === 'DOWN'){
            const newPos = this.getNewPos();
            const valAtNewPos = this.getValAtNewPos(newPos);
            if(valAtNewPos === '#'){
                this.direction = {
                    name: 'LEFT',
                    value: directions.LEFT,
                };
            } else {
                return this.visit(newPos);
            }  
        }

        // If dir LEFT
        if(this.direction.name === 'LEFT'){
            const newPos = this.getNewPos();
            const valAtNewPos = this.getValAtNewPos(newPos);
            if(valAtNewPos === '#'){
                this.direction = {
                    name: 'UP',
                    value: directions.UP,
                };
            } else {
                return this.visit(newPos);
            }  
        }

        const newPos = this.getNewPos();
        const valAtNewPos = this.getValAtNewPos(newPos);
        if(valAtNewPos === '#'){
            this.direction = {
                name: 'DOWN',
                value: directions.DOWN,
            };
        } else {
            return this.visit(newPos);
        }

        return !this.isOutside();
    
    }

    private visit(newPos: number[]): boolean {
        if(this.isNewOutside(newPos)){
            throw new Error('Outside!');
        }
        const entry = `${newPos[0]},${newPos[1]}`;
        if(!this.visited.has(entry)){
            this.addToDebugMap(newPos[0], newPos[1]);
            this.visited.add(entry);
        }
        this.pos = newPos;
        return true;
    }

    public isOutside(): boolean {
        return this.isNewOutside(this.pos);
    }

    private isNewOutside(newPos: number[]): boolean {
        return newPos[0] > this.limits.maxRow || newPos[0] < this.limits.minRow || newPos[1] > this.limits.maxCol || newPos[1] < this.limits.minCol;
    }

    private getNewPos(){
        return [this.pos[0] + this.direction.value[0], this.pos[1] + this.direction.value[1]];
    }

    private getValAtNewPos(newPos: number[]){
        if(this.isNewOutside(newPos)){
            throw new Error('Outside!');
        }
        return this.map[newPos[0]][newPos[1]];
    }

    public printMap(map: string[][]){
        map.forEach(row => console.log(row.join('')));
    }

    private addToDebugMap(i: number, j: number){
        this.debugMap[i][j] = 'X';
    }
}