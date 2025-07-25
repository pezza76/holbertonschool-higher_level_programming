#!/usr/bin/node

const c = 'C is fun';
const arg = Number(process.argv[2]);

if (!Number.isInteger(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log(c);
  }
}
