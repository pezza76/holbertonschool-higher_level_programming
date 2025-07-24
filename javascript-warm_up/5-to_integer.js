#!/usr/bin/node

const int = process.argv[2];
const num = parseInt(int);

if (isNaN(num)) {
    console.log('Not a number');
} else {
    console.log(num);
}
