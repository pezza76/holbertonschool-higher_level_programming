#!/usr/bin/node
const sizeOfSquare = Number(process.argv[2]);

if (!Number.isInteger(sizeOfSquare)) {
  console.log('Missing size');
}
for (let i = 0; i < sizeOfSquare; i++) {
  console.log('X'.repeat(sizeOfSquare));
}
