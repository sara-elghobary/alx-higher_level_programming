#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  if (number > 1) {
    for (let i = 0; i > number; i++) {
      console.log('C is fun');
    }
  }
}
