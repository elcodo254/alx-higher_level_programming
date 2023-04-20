#!/usr/bin/node
// check if first argument can be converted to an integer and print custom string

const arg = Math.floor(Number(process.argv[2]));
console.log(isNaN(arg) ? 'Not a number' : `My number: ${arg}`);
