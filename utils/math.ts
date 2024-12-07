export function absDelta(a: number, b: number): number {
    return Math.abs(a - b);
}

export function sum(array: number[] | undefined): number {
    if (!array) {
        return 0;
    }

    return array.reduce((prev, curr) => prev + curr);
}
