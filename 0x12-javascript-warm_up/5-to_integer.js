#!/usr/bin/node
// JS to check if arguments passed cam be converted to integer

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', process.argv[2]);
}
