
def Sort(input : list)->list:
    if len(input)<=1:
        return input
    midPoint = len(input)//2
    left = Sort(input[:midPoint])
    right = Sort(input[midPoint:])
    return merge(left,right)

def merge(left:list,right:list)->list:
    merged = []
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
            continue
        if left[i]>right[j]:
            merged.append(right[j])
            j+=1
            continue
        if left[i]==right[j]:
            merged.append(left[i])
            merged.append(right[j])
            i+=1
            j+=1
            continue

    if i<len(left):
        merged.extend(left[i:])
    if j<len(right):
        merged.extend(right[j:])
    return merged
