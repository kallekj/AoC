type Direction = "TLDR" | "DRTL" | "TRDL" | "DLTR";
type CheckType = "SAM" | "MAS" | "SAM + MAS";

/**
 * Checks all combinations of SAM, MAS, or SAM + MAS for given directions.
 * 
 * @param directions - An array of direction identifiers (e.g., "TLDR", "DRTL").
 * @param isSAM - A function that checks if a combination is SAM.
 * @param isMAS - A function that checks if a combination is MAS.
 * @returns An array of objects representing the combinations and their results.
 */
function checkCombinations(
    directions: Direction[],
    isSAM: (dir1: Direction, dir2: Direction) => boolean,
    isMAS: (dir1: Direction, dir2: Direction) => boolean
): { pair: [Direction, Direction]; type: CheckType }[] {
    const results: { pair: [Direction, Direction]; type: CheckType }[] = [];

    for (let i = 0; i < directions.length; i++) {
        for (let j = i; j < directions.length; j++) {
            const dir1 = directions[i];
            const dir2 = directions[j];

            // Check for SAM
            if (isSAM(dir1, dir2)) {
                results.push({ pair: [dir1, dir2], type: "SAM" });
            }

            // Check for MAS
            if (isMAS(dir1, dir2)) {
                results.push({ pair: [dir1, dir2], type: "MAS" });
            }

            // Check for SAM + MAS
            if (isSAM(dir1, dir2) && isMAS(dir1, dir2)) {
                results.push({ pair: [dir1, dir2], type: "SAM + MAS" });
            }
        }
    }

    return results;
}

// Example usage:

const directions: Direction[] = ["TLDR", "DRTL", "TRDL", "DLTR"];

// Example implementations of isSAM and isMAS
function isSAM(dir1: Direction, dir2: Direction): boolean {
    // Example logic for SAM
    return (dir1 === "TLDR" && dir2 === "TRDL") || (dir1 === "DRTL" && dir2 === "DRTL");
}

function isMAS(dir1: Direction, dir2: Direction): boolean {
    // Example logic for MAS
    return (dir1 === "TLDR" && dir2 === "DRTL") || (dir1 === "DRTL" && dir2 === "TRDL");
}

const results = checkCombinations(directions, isSAM, isMAS);

console.log(results);
