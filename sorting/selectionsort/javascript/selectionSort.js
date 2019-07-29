
function Sort(input)
{
  for(let i=0;i<input.length-1;i++)
  {
    let minimum=i;
    for(let j=i;j<input.length;j++)
    {
      if(input[j]<input[minimum])
      {
        minimum = j;
      }
    }
    if(minimum!=i)
    {
      let temp = input[minimum];
      input[minimum] = input[i];
      input[i] = temp;
    }
  }
  return input;
}

module.exports = {Sort};
