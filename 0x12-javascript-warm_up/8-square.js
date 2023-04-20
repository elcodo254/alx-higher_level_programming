#!/usr/bin/node
// prints a square using 'x' character

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let l = 0; l < size; l++) {
    let len = '';
    for (let w = 0; w < size; w++) len += 'X';
    console.log(len);
  }
}
