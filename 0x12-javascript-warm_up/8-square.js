#!/usr/bin/node

const test = parseInt(process.argv[2]);

if (test) {
  for (let i = 0; i < test; i++) {
    console.log('X'.repeat(test));
  }
} else {
  console.log('Missing size');
}
