#!/usr/bin/node
// Script that prints the first argument passed to it

const myArg = process.argv.slice(2);

if (myArg === '') {
  console.log('No argument');
} else {
  console.log(myArg.toString());
}
