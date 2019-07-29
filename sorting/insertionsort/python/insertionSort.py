
def Sort(input : list) -> list:
    if len(input)<=1:
        return input

    for i in range(1,len(input)):
        for j in range(i-1,-1,-1):
            #print(j)
            if input[j+1]>input[j]:
                break
            temp = input[j+1]
            input[j+1] = input[j]
            input[j] = temp
            #print(input)

    return input
