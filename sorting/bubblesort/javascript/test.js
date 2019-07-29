

const assert = require('assert');
const readline = require('readline');
const fs = require('fs');
const bubbleSort = require('bubbleSort.js');

function TestSorting(func, input,expected)
{
  output = func(input);
  assert(output.length==expected.length && output.every((element,index)=>{
    return element === expected[index];
  }));
}

function main(method)
{
  const rl = readline.createInterface(
    {
      input:fs.createReadStream('../../TestData/data.txt'),
      crlfDelay: Infinity
    }
  );
  let testData = [];
  rl.on('line',(line)=>{
    testData.push(line);
  });
  console.log(testData);
}

main("");
