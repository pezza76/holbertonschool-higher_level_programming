#!/usr/bin/node

const nums = process.argv.slice(2).map(Number);

if (process.argv[2] === undefined) {
    console.log(0);
} else {
const sort = nums.sort((a, b) => a - b);
console.log(sort[sort.length - 2]);
}