#!/usr/bin/node
// script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop.

const languages = ['C is fun', 'Python is cool', 'Javascript is amazing'];

for (const element in languages) {
  console.log(languages[element]);
}
