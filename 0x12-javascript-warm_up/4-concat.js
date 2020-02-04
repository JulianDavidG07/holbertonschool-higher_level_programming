#!/usr/bin/node
// Script that prints two arguments passed to it, in the following format: “ is ”

let myArg = process.argv.slice(2);

console.log(`${myArg[0]} is ${myArg[1]}`);
