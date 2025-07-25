#!/usr/bin/node

const num = Number(process.argv[2]);

if (!Number.isInteger(num)) {
  console.log(1);
} else {
  function factorial (num) {
    if (num === 0) {
      return 1;
    }
    return num * factorial(num - 1);
  }
  console.log(factorial(num));
}
