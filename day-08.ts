import { readFileSync } from "fs";

const debug = true;
const fileName = `day-08${debug ? ".test" : ".input"}`;

const data: Array<string> = readFileSync(fileName, "utf8")
  .trim()
  .split(/\n/)
  .filter(x => x);

const instructions: Array<number> = data[0].split("").map(x => x === "L" ? 0 : 1);
const map: { [key: string]: Array<string> } = {};

data.forEach((x, i) => {
    if (i >= 1) {
        const s: Array<string> = x.split(" = (");
        const LR = s[1].replace(/[()]/g, '').split(", ");
        map[s[0]] = [LR[0], LR[1]]; 
    }
});

function runMap() {
    let i: number = 0;
    let location = 'AAA';
    while (location !== "ZZZ") {
        const nextInstruction = instructions.shift();
        if (typeof(nextInstruction) === "undefined") {
            return;
        }
        location = getDestination(location, nextInstruction);
        i++;
        instructions.push(nextInstruction);
        
    }
    return i;
}

function getDestination(mapIndex: string, instruction: number) {
    return map[mapIndex][instruction];
}

console.log(`Part 1: ${runMap()} steps`);
