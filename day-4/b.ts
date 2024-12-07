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

function isLetterX<T>(matrix: T[][], i: number, j: number, char: string): boolean {
    return isInside(matrix, i, j) ? matrix[i][j] === char : false;
}

async function main() {
    const input = 'input.txt';
    const file = await Deno.readTextFile(input);
    const data = file.split('\n');

    // Split chars
    const matrix = data.map((line) => line.split(''));

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; i < matrix[0].length; j++) {
            /**
             *  X (i-1,j-1) . (i-1,j) X (i-1,j+1)
             *  . (i  ,j-1) X (i , j) . (i  ,j+1)
             *  X (i+1,j-1) . (i+1,j) X (1+i,j+1)
             */
            const isLetterA = matrix[i][j] === 'A';
            if(isLetterA){
                // Check top left (i-1,j-1)
                const isTopLeftLetterSM = isLetterX(matrix, i-1, j-1, 'S') || isLetterX(matrix, i-1, j-1, 'M');
                if(isTopLeftLetterSM){
                    const isTopLeftLetterS = isLetterX(matrix, i-1, j-1, 'S');

                    // Is S
                    if(isTopLeftLetterS){
                        const isDownRightLetterM = isLetterX(matrix, i+1, j+1, 'M');
                        if(isDownRightLetterM){
                            const isTopRightLetterSM = isLetterX(matrix, i-1, j-1, 'S') || isLetterX(matrix, i-1, j-1, 'M');
                        } 
                    }

                    // else is M

                }
            }
        }
    }
}

try {
    await main();
} catch (error) {
    console.error(error);
}
