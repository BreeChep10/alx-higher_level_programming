#!/usr/bin/node

const fs = require('fs');

const readAndPrintFileContent = (filePath) => {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
};

/** Check if a file path is provided as a command-line argument **/

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
readAndPrintFileContent(filePath);
