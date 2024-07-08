#!/usr/bin/node

const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  const newList = args.sort((a, b) => b - a);
  console.log(newList[1]);
}
