export function absDelta(a: number, b: number): number {
    return Math.abs(a - b);
}

export function sum(array: number[]): number {
    return array.reduce((prev, curr) => prev + curr);
}
