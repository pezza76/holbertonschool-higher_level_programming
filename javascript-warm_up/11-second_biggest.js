#!/usr/bin/node

const nums = process.argv.slice(2).map(Number);
const sort = nums.sort((a, b) => a - b);
console.log(sort[sort.length - 2]);
