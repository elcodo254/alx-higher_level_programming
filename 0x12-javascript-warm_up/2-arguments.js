#!/usr/bin/node
// Print a message depending on the number of arguments passed.

if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
