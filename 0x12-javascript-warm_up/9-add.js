#!/usr/bin/node

function add (a, b) {
  const result = parseInt(a) + parseInt(b);
  if (!isNaN(result)) {
    console.log(result);
  } else {
    console.log('NaN');
  }
}
