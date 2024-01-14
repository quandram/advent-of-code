import { readFileSync } from "fs";

const debug = false;
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
    const instructions1 = instructions;
    let location = 'AAA';
    while (location !== "ZZZ") {
        const nextInstruction = instructions1.shift();
        if (typeof(nextInstruction) === "undefined") {
            return;
        }
        location = getDestination(location, nextInstruction);
        i++;
        instructions1.push(nextInstruction);
        
    }
    return i;
}

function getDestination(mapIndex: string, instruction: number) {
    return map[mapIndex][instruction];
}

console.log(`Part 1: ${runMap()} steps`);

// while not all is Ending node
// run next loop
//

function part2() {
    let i: number = 0;
    const instructions2 = instructions;
    console.log("a");
    let currentNodes = Object.keys(map).filter(x => x.slice(-1) === 'A');
    const endingNodes = Object.keys(map).filter(x => x.slice(-1) === "Z");
    currentNodes = currentNodes.filter((x, i) => i === 3);
    while(currentNodes.some(x => endingNodes.indexOf(x) === -1) && i < 4000000) {
        console.log("-----");
        console.log(i);
        console.log(currentNodes);
        const nextInstruction = instructions2.shift();
        if (typeof(nextInstruction) === "undefined") {
            return;
        }
        console.log("-----");
        currentNodes = currentNodes.map(x => getDestination(x, nextInstruction));
        console.log("-----");
        i++;
        instructions2.push(nextInstruction);
        if (i === 20777) {
            console.log(currentNodes);
            console.log(endingNodes);
        }
    }
    return i;
}
console.log(`Part 2: ${part2()}`);
