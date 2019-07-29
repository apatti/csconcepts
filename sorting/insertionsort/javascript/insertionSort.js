
function Sort(input)
{
  if(input.length<=1)
  {
    return input;
  }
  for(let i=1;i<input.length;i++)
  {
    for(let j=i-1;j>=0;j--)
    {
      if(input[j+1]>input[j])
      {
        break;
      }
      let temp = input[j+1];
      input[j+1] = input[j];
      input[j] = temp;
    }
  }
  return input;
}

module.exports = {Sort};
