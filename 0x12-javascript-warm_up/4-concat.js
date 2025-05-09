#!/usr/bin/node
const args = process.argv.slice(2).join('');
const word = ' is ';
const first = args[0];
const second = args[1];
const result = `${first} is ${second}`;
console.log(result);
