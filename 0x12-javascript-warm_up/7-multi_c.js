#!/usr/bin/node
// script that prints x times “C is fun”

const x = process.argv.slice(2)
const c = 'C is fun\n'

if (isNaN(x[0])) {
  console.log('Missing number of occurrences')
} else if (x[0] < 0) {
  // pass
} else {
  console.log(c.repeat(x[0]))
}
