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

    constructor(guardMap: string[][], pos: number[], dir: { name: Directions, value: number[]}){
        this.map = guardMap;
        this.limits = { minCol: 0, minRow: 0, maxRow: this.map.length - 1, maxCol: this.map[0].length - 1 };
        this.visited = new Set();
        this.pos = pos;
        this.direction = dir;
        this.debugMap = Array.from(this.map);
    }

    public get numVisited(){
        return this.visited.size;
    }

    public get currentPos() {
        return this.pos;
    }

    public get currentDir() {
        return this.direction;
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
                return;
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
                return;
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
                return;
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
            // console.log('Outside!');
            throw new Error('Outside!');
        }
        const entry = `${newPos[0]},${newPos[1]},${this.currentDir.name}`;

        if(this.visited.has(entry)) {
            throw new Error('loop');
        }

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
        if(newPos[0] > this.limits.maxRow || newPos[0] < this.limits.minRow || newPos[1] > this.limits.maxCol || newPos[1] < this.limits.minCol){
            throw new Error('Outside!');
        }
        return false;
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