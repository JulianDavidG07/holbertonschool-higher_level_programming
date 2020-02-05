#!/usr/bin/node
const arg = process.argv.slice(2)
let i = 0
const num = parseInt(Number(arg[0]))
if (num) {
  while (i < num) {
    console.log('C is fun')
    i++
  }
} else {
  console.log('Missing number of occurrences')
}