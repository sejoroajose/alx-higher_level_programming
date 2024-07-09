#!/usr/bin/node
const square = require('./5-square.js');

const Square = class extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
};

module.exports = Square;
