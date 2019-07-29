#selection sort

def Sort(input: list) -> list:
    for i in range(0,len(input)-1):
        minimum = i
        for j in range(i,len(input)):
            if input[j]<input[minimum]:
                minimum=j
        if minimum!=i:
            temp = input[minimum]
            input[minimum] = input[i]
            input[i] = temp
    return input
