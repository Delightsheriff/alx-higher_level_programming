#!/usr/bin/node

const temp = require('fs');

const fArg = temp.readFileSync(process.argv[2]).toString();
const sArg = temp.readFileSync(process.argv[3]).toString();
temp.writeFileSync(process.argv[4], fArg + sArg);
