import { sum } from "../utils/math.ts";

function parseRules(rawRules: string){
    const lines = rawRules.split('\n');
    return lines;
}

function parseUpdates(rawUpdates: string){
    return rawUpdates.split('\n').map(updates => updates.split(',').map(update => parseInt(update)));
}


// Should next come before?
function checkPageUpdate(update: number[], page1: number, page2: number, rules: string[]) {
    // update includes page1 and page 2
    const includesBothPages = update.includes(page1) && update.includes(page2);
    if(!includesBothPages){
        return true;
    }
    
    const rule1 = rules.find(item => item === `${page1}|${page2}`);
    const rule2 = rules.find(item => item === `${page2}|${page1}`);

    if(rule1){
        return update.indexOf(page1) < update.indexOf(page2);
    }

    if(rule2){
        return update.indexOf(page2) < update.indexOf(page1);
    }

    return true;
}

function checkOkayUpdate(update: number[], rules: string[]){
    let counter = 0;
    for(let i = 0; i < update.length; i++){
        const page1 = update[i];
        let page2 = update[i+1];
        if(i === update.length - 1){
            page2 = update[i-1]; 
        }
        counter += checkPageUpdate(update, page1, page2, rules) ? 1 : 0 
    }
    return counter === update.length ? update : null;
}


async function main() {
    const input = 'input.txt';
    const file = await Deno.readTextFile(input);
    const [rawRules, rawUpdates] = file.split('\n\n');

    const rules = parseRules(rawRules)
    const updates = parseUpdates(rawUpdates);
    
    const okayUpdates = updates.map(update => checkOkayUpdate(update, rules)).filter(update => update !== null);
    const middleNumbers = okayUpdates.map(update => update ? update[(update?.length-1)/2] : 0);
    const result = sum(middleNumbers);
    console.log(result);
}

try {
    await main();
} catch (error) {
    console.error(error);
}
