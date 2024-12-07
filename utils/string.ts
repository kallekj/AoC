export function isEmptyString(str: string): boolean {
    if (!str) {
        return true;
    }

    return str.length === 0;
}

export function replaceBetween(
    origin: string,
    startIndex: number,
    endIndex: number,
    insertion: string
) {
    return ''.concat(
        origin.substring(0, startIndex),
        insertion,
        origin.substring(endIndex),
    );
}


export function repeat(char: string, times: number): string {
    ''.padStart(times, char);
    return ''.padStart(times, char);
}

export function joinStringArray(strings: string[]): string {
    return ''.concat(...strings);
}

export function reverse(input: string): string {
    const chars = [];
    for(let i = input.length - 1; i >= 0; i--) {
        chars.push(input[i]);
    }
    return ''.concat(...chars);
}