#!/usr/bin/node
const [firstArg] = process.argv.slice(2);
console.log(firstArg || 'No argument');
