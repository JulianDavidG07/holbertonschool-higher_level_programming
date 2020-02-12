#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

request
  .get(process.argv[2])
  .on('error', (err) => {
    console.error(err);
  })
  .pipe(fs.createWriteStream(process.argv[3], 'utf8'));
