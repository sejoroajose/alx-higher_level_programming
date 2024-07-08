#!/usr/bin/node

const arg = process.argv[2];

const x = parseInt(arg);

if (isNaN(x) || x <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
