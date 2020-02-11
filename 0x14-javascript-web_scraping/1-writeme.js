#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');

const content = process.argv[3];

try {
  const data = fs.writeFileSync(process.argv[2], content);
  // file written successfully
} catch (err) {
  console.error(err);
}
