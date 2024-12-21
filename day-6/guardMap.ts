const directions = {
    UP: [-1, 0],
    DOWN: [1, 0],
    LEFT: [0, -1],
    RIGHT: [0, 1]
};

type Directions = keyof typeof directions;

export class GuardMap {
    private visited: Set<string>;
    private map: string[][];
    // public debugMap: string[][];
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

    constructor(input: string){
        const rows = input.split('\n');
        this.map = rows.map(row => row.split(''));
        this.limits = { minCol: 0, minRow: 0, maxRow: this.map.length - 1, maxCol: this.map[0].length - 1 };
        this.visited = new Set();
        this.pos = [0,0];
        this.direction = {
            name: 'UP',
            value: directions.UP
        };
        this.guardPos = this.pos;
        // this.debugMap = Array.from(this.map);
        
        rows.forEach((row, rowI) => {
            // Check up
            let colI = row.indexOf('^');
            if(colI !== -1){
                this.pos = [rowI, colI];
                this.direction = {
                    name: 'UP',
                    value: directions.UP
                };
                // this.addToDebugMap(rowI, colI);
                this.visited.add(`${rowI},${colI}`);
                this.guardPos = [rowI, colI];
                return;
            }
            
            // Check down
            colI = row.indexOf('v');
            if(colI !== -1){
                this.pos = [rowI, colI];
                this.direction = {
                    name: 'DOWN',
                    value: directions.DOWN
                };
                // this.addToDebugMap(rowI, colI);
                this.visited.add(`${rowI},${colI}`);
                this.guardPos = [rowI, colI];
                return;
            }

            // Check left
            colI = row.indexOf('<');
            if(colI !== -1){
                this.pos = [rowI, colI];
                this.direction = {
                    name: 'LEFT',
                    value: directions.LEFT
                };
                // this.addToDebugMap(rowI, colI);
                this.visited.add(`${rowI},${colI}`);
                this.guardPos = [rowI, colI];
                return;
            }

            // Check right
            colI = row.indexOf('>');
            if(colI !== -1){
                this.pos = [rowI, colI];
                this.direction = {
                    name: 'RIGHT',
                    value: directions.RIGHT
                };
                // this.addToDebugMap(rowI, colI);
                this.visited.add(`${rowI},${colI}`);
                this.guardPos = [rowI, colI];
                return;
            }
        });

        console.log('GuardMap Initialized - settings:');
        console.log(JSON.stringify({ visited: this.visited.entries(), pos: this.pos, direction: this.direction, limits: this.limits }));
    }

    public get visitedNodes(){
        return this.visited;
    }

    public get mapMatrix(){
        return this.map;
    }

    public get currentDirection(){
        return this.direction;
    }

    public get guardPosition(){
        return this.guardPos;
    }

    public get numNodes(){
        return this.map.length * this.map[0].length;
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
            // this.addToDebugMap(newPos[0], newPos[1]);
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
}