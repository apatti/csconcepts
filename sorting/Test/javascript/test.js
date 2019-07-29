

const assert = require('assert');
const readline = require('readline');
const fs = require('fs');
const bubbleSort = require('../../bubblesort/javascript/bubbleSort.js');
const selectionSort = require('../../selectionsort/javascript/selectionSort.js');
const insertionSort = require('../../insertionsort/javascript/insertionSort.js');
const once = require('events');

function TestSorting(func, input,expected)
{
  output = func(input);
  assert(output.length==expected.length && output.every((element,index)=>{
    return element === expected[index];
  }),"\nReturned:"+output+"\nExpected:"+expected);
}

var functionMap = {
  "bubblesort":bubbleSort.Sort,
  "selectionsort":selectionSort.Sort,
  "insertionsort":insertionSort.Sort
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

  rl.on('close',()=>{
    for(let i=0;i<testData.length;i+=2)
    {
        console.log("Testing:"+((i/2)+1));
        var input=[];
        var output=[];
        if(testData[i].length!=0)
        {
          input = testData[i].split(',').map((s)=>{
            return parseInt(s);
          });
          output = testData[i+1].split(',').map((s)=>{return parseInt(s)});;
        }

        TestSorting(functionMap[method],input,output);
    }

  });

}

main("insertionsort");
