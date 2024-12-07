import { transpose } from '../utils/array.ts';
import { sum } from '../utils/math.ts';

function isMAS(line: string) {
    const MAS = /MAS/g;
    return line.match(MAS);
}

function isSAM(line: string) {
    const SAM = /SAM/g;
    return line.match(SAM);
}

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
    const input = 'test.txt';
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
                const [TL, DR] = [
                    getLetter(matrix, i - 1, j - 1) ?? '',
                    getLetter(matrix, i + 1, j + 1) ?? '',
                ];
                const [TR, DL] = [
                    getLetter(matrix, i - 1, j - 1) ?? '',
                    getLetter(matrix, i + 1, j + 1) ?? '',
                ];

                const TLDR = ''.concat(...[TL, center, DR]);
                const DRTL = ''.concat(...[DR, center, TL]);
                const TRDL = ''.concat(...[TR, center, DL]);
                const DLTR = ''.concat(...[DL, center, TR]);

                // Check Top Left
                if(isLetterX(matrix, i-1, j-1, 'S')){
                    if(isSAM(TLDR)){
                        // Check Top Right
                        const isSamOrMas = isSAM(TRDL) || isMAS(TRDL);
                        if(isSamOrMas){
                            counter += 1;
                        }
                    }
                }

                if(isLetterX(matrix, i-1, j-1, 'M')){
                    if(isMAS(TLDR)){
                        // Check Top Right
                        const isSamOrMas = isSAM(TRDL) || isMAS(TRDL);
                        if(isSamOrMas){
                            counter += 1;
                        }
                    }
                }

                // if (isSAM(TLDR)) {
                //     counter =
                //         isSAM(TRDL) || isMAS(TRDL) ? (counter += 1) : counter;
                //     continue;
                // }

                // if (isMAS(TLDR)) {
                //     counter =
                //         isSAM(TRDL) || isMAS(TRDL) ? (counter += 1) : counter;
                //     continue;
                // }


                // if(isSAM(DRTL)){
                //     xCounter = isSAM(DRTL) || isSAM(T) ? xCounter += 1 : xCounter;
                // }

                // Check SAM
                // if TLDR + TRDL == SAM

                // if DRTL + DRTL == SAM

                // if TLDR + DRTL == SAM

                // if DRTL + TRDL == SAM

                // Check MAS
                // if TLDR + TRDL == MAS

                // if DRTL + DRTL == MAS

                // if TLDR + DRTL == MAS

                // if DRTL + TRDL == MAS

                // Check SAM + MAS
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
