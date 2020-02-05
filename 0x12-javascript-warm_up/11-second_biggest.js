#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.

const myArg = process.argv.slice(2);

if ((myArg.length === 0) || (myArg.length === 1)) {
  console.log('0');
} else {
  console.log((myArg.sort().reverse())[1]);
}
