
function Sort(input)
{
  QuickSort(input,0,input.length-1);
  return input;
}

function QuickSort(input,start,end)
{
  if(start<end)
  {
    let pi = Partition(input,start,end);
    QuickSort(input,start,pi-1);
    QuickSort(input,pi+1,end);
  }
}

function Partition(input,start,end)
{
  let pivot = input[start];
  let lesserIndex = start+1;
  let greaterIndex = end;
  while(lesserIndex<greaterIndex)
  {
    while(lesserIndex<end && pivot>=input[lesserIndex])
    {
      lesserIndex++;
    }
    while(greaterIndex>start && pivot<input[greaterIndex])
    {
      greaterIndex--;
    }
    if(lesserIndex<greaterIndex)
    {
      let temp = input[lesserIndex];
      input[lesserIndex] = input[greaterIndex];
      input[greaterIndex] = temp;
    }
  }
  if(pivot>input[greaterIndex])
  {
    let temp = input[greaterIndex];
    input[greaterIndex] = pivot;
    input[start] = temp;
  }
}

module.exports={Sort};
