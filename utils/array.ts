export function stringArrayToInt(content: string[]): number[] {
    return content.map((val) => parseInt(val));
}

export function transpose<T>(matrix: T[][]): T[][] {
    return matrix[0].map((_, colIndex) => matrix.map((row) => row[colIndex]));
}

export function isEmptyArray<T>(array: T[] | undefined | null): boolean {
    if (!array) {
        return true;
    }

    return array.length === 0;
}

export function shearCCW<T>(matrix: T[][]): T[][] {
    const rows = matrix.length;
    const cols = matrix[0].length;

    // Calculate the size of the new matrix
    const newSize = rows + cols - 1;
    const result: T[][] = Array.from({ length: newSize }, () => []);

    // Fill the new matrix
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const newRow = i + j;
            result[newRow].push(matrix[i][j]);
        }
    }

    // Pad the result rows to ensure it's a proper "matrix" shape
    const maxRowLength = Math.max(...result.map((row) => row.length));
    return result.map((row) => {
        const padStart = Math.floor((maxRowLength - row.length) / 2);
        const padEnd = maxRowLength - row.length - padStart;
        return Array(padStart)
            .fill(null)
            .concat(row)
            .concat(Array(padEnd).fill(null));
    });
}

export function shearCW<T>(matrix: T[][]): T[][] {
    const rows = matrix.length;
    const cols = matrix[0].length;

    // Calculate the size of the new matrix
    const newSize = rows + cols - 1;
    const result: T[][] = Array.from({ length: newSize }, () => []);

    // Fill the new matrix
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const newRow = rows - 1 - i + j;
            result[newRow].push(matrix[i][j]);
        }
    }

    // Pad the result rows to ensure it's a proper "matrix" shape
    const maxRowLength = Math.max(...result.map((row) => row.length));
    return result.map((row) => {
        const padStart = Math.floor((maxRowLength - row.length) / 2);
        const padEnd = maxRowLength - row.length - padStart;
        return Array(padStart)
            .fill(null)
            .concat(row)
            .concat(Array(padEnd).fill(null));
    });
}

export function flipMatrix<T>(
    matrix: T[][],
    orientation: 'row' | 'col' = 'row'
): T[][] {
    if (orientation === 'row') {
        return matrix.map((row) => row.reverse());
    }
    return transpose(transpose(matrix).map((row) => row.reverse()));
}

export function getDiagonals<T>(matrix: T[][]): T[][] {
    const rows = matrix.length;
    const cols = matrix[0].length;
    const diagonals: T[][] = [];

    // Top-left to bottom-right diagonals
    for (let d = 0; d < rows + cols - 1; d++) {
        const diagonal: T[] = [];
        for (let i = 0; i < rows; i++) {
            const j = d - i; // Column index
            if (j >= 0 && j < cols) {
                diagonal.push(matrix[i][j]);
            }
        }
        diagonals.push(diagonal);
    }

    // Top-right to bottom-left diagonals
    for (let d = 0; d < rows + cols - 1; d++) {
        const diagonal: T[] = [];
        for (let i = 0; i < rows; i++) {
            const j = i + (cols - 1 - d); // Column index
            if (j >= 0 && j < cols) {
                diagonal.push(matrix[i][j]);
            }
        }
        diagonals.push(diagonal);
    }

    return diagonals;
}
