#!/usr/bin/node

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function add (a, b) {
  for (let i = 0; i < 1; i++) {
    console.log(a + b);
  }
}

add(a, b);
