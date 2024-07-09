#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('X');
        }
        process.stdout.write('\n');
      }
    }
  }

  rotate () {
    if (this.width && this.height) {
      const newW = this.height;
      const newH = this.width;
      this.width = newW;
      this.height = newH;
    }
  }

  double () {
    if (this.width && this.height) {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
  }
};

module.exports = Rectangle;
