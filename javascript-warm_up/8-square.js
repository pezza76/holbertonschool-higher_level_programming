#!/usr/bin/node
sizeOfSquare = Number(process.argv[2]);

if (sizeOfSquare) {
  for (let i = 0; i < sizeOfSquare; i++) {
    console.log('x'.repeat(sizeOfSquare));
  }
}
