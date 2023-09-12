#!/usr/bin/node

const test = parseInt(process.argv[2]);

if (test) {
  for (let i = 0; i < test; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
