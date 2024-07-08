#!/usr/bin/node
const arg = process.argv[2];

const x = parseInt(arg, 10);

function factorial (n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

const result = isNaN(x) ? 1 : factorial(x);

console.log(result);
