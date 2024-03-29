#!/usr/bin/node

const argv = process.argv;
const n = parseInt(argv[2]);

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(n));
