#!/usr/bin/node
// Print argument passed else error message.

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
