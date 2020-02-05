#!/usr/bin/node
// Script that prints the addition of 2 integers

const arg = process.argv.slice(2);

function add (a, b) {
  return parseInt(arg[0]) + parseInt(arg[1]);
}

console.log(add(arg[0], arg[1]));
