
def Sort(input: list) -> list:
    QuickSort(input,0,len(input)-1)
    return input

def QuickSort(input: list, start: int, end: int) -> list:
    if start<end:
        pi = partition(input,start,end)
        QuickSort(input,start,pi-1)
        QuickSort(input,pi+1,end)

def partition(input : list, start: int, end: int) -> int :
    pivot = input[start]
    i = start+1
    j = end
    while i<j:
        while pivot>=input[i] and i<end:
            i+=1
        while pivot<input[j] and j>start:
            j-=1

        if i<j:
            temp = input[i]
            input[i] = input[j]
            input[j] = temp

    #swap pivot with current end
    if pivot>input[j]:
        temp = input[j]
        input[j] = pivot
        input[start] = temp
    
    return j
