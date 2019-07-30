
function Sort(input)
{
  if(input.length<=1)
  {
    return input;
  }
  let midPoint = input/2;
  left = Sort(input.slice(0,midPoint));
  right = Sort(input.slice(midPoint));
  return merge(left,right);
}

function merge(left,right)
{
  let merged = []
  for(let i=0,j=0;i<left.length&&j<right.length;)
  {
    if(left[i]<right[j])
    {
      merged.push(left[i]);
      i++;
      continue;
    }
    if(left[i]>right[j])
    {
      merged.push(right[j])
      j++;
      continue;
    }
    if(left[i]==right[j])
    {
      merged.push(left[i]);
      merged.push(right[j]);
      i++;j++;
      continue;
    }
  }
  if(i<left.length)
  {
    merged.concat(left.slice(i));
  }
  if(j<right.length)
  {
    merged.concat(right.slice(j));
  }

  return merged;
}
