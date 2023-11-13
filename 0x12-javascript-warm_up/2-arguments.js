#!/usr/bin/node
const input = process.argv.length;
console.log(input === 2 ? 'No argument' : input === 3 ? 'Argument found' : 'Arguments found');
