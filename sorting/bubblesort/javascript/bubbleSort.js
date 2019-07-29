

function Sort(input)
{
  for(let k=0;k<input.length-1;k++)
  {
    for(let i=0;i<input.length-k-1;i++)
    {
      if(input[i]>input[i+1])
      {
        let temp = input[i];
        input[i] = input[i+1];
        input[i+1] = temp;
      }
    }
  }
  return input;
}


module.exports = {Sort};
