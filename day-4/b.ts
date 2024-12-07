import { transpose } from '../utils/array.ts';

function isInside<T>(matrix: T[][], row: number, col: number): boolean {
    const maxRow = matrix.length - 1;
    const maxCol = transpose(matrix).length - 1;
    const minRow = 0;
    const minCol = 0;

    if (row > maxRow || row < minRow) {
        return false;
    }
    if (col > maxCol || col < minCol) {
        return false;
    }

    return true;
}

function getLetter<T>(matrix: T[][], i: number, j: number): T | null {
    if (isInside(matrix, i, j)) {
        return matrix[i][j];
    }
    return null;
}

function isLetterX<T>(matrix: T[][], i: number, j: number, char: string): boolean {
    return isInside(matrix, i, j) ? matrix[i][j] === char : false;
}

async function main() {
    const input = 'input.txt';
    const file = await Deno.readTextFile(input);
    const data = file.split('\n');

    // Split chars
    const matrix = data.map((line) => line.split(''));
    let counter = 0;
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            /**
             *  X (i-1,j-1) . (i-1,j) X (i-1,j+1)
             *  . (i  ,j-1) X (i , j) . (i  ,j+1)
             *  X (i+1,j-1) . (i+1,j) X (1+i,j+1)
             */
            const center = getLetter(matrix, i, j) ?? '';
            const isCenterLetterA = center === 'A';
            if (isCenterLetterA) {
                
                if(isLetterX(matrix, i-1, j-1, 'M') && isLetterX(matrix, i+1, j+1, 'S')){
                    if((isLetterX(matrix, i-1, j+1, 'M') && isLetterX(matrix, i+1, j-1, 'S')) || (isLetterX(matrix, i-1, j+1, 'S') && isLetterX(matrix, i+1, j-1, 'M'))){
                        counter += 1;
                    }
                }

                if(isLetterX(matrix, i-1, j-1, 'S') && isLetterX(matrix, i+1, j+1, 'M')){
                    if((isLetterX(matrix, i-1, j+1, 'M') && isLetterX(matrix, i+1, j-1, 'S')) || (isLetterX(matrix, i-1, j+1, 'S') && isLetterX(matrix, i+1, j-1, 'M'))){
                        counter += 1;
                    }
                }

            }
        }
    }
    console.log(counter);
}

try {
    await main();
} catch (error) {
    console.error(error);
}
