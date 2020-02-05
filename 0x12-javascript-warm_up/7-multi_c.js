#!/usr/bin/node
// script that prints x times “C is fun”

const x = process.argv.slice(2)
const c = 'C is fun\n'

switch (x[0]) {
  case x[0] > 0:
    console.log(c.repeat(x[0]))
    break
  case x[0] === 0:
    console.log('Missing number of occurrences')
    break
  case x[0] < 0:
    // pass
}
