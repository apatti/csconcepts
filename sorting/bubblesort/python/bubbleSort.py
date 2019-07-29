#bubble sort

def Sort(input: list) -> list:
    for k in range(len(input)-1):
        for i in range(len(input)-k-1):
            if input[i]>input[i+1]:
                temp = input[i+1]
                input[i+1] = input[i]
                input[i] = temp
    return input
