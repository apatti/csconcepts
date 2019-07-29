import random

def GenerateRandomInput(count: int) -> list:
    input = []

    for j in range(count):
        input.append(random.randint(-1000,5000))

    return input

def GenerateReversed(count: int) -> list:
    return sorted(GenerateRandomInput(count),reverse=True)


def GenerateAlmostSorted(count: int) -> list:
    sortedCount = count - int(count*0.2)
    input = sorted(GenerateRandomInput(sortedCount))
    input.extend(GenerateRandomInput(count-sortedCount))
    return input

def GenerateAlmostReversed(count: int) -> list:
    sortedCount = count-int(count*0.2)
    input = GenerateReversed(sortedCount)
    input.extend(GenerateRandomInput(count-sortedCount))

    return input

def GenerateFewUnique(count: int) -> list:
    randomCount = count//2
    input = GenerateRandomInput(randomCount)
    extraDuplicateCount = count-randomCount-int((count-randomCount)*0.5)
    input.extend(input[:extraDuplicateCount])
    remainingCount = count-(randomCount+extraDuplicateCount)
    input.extend(GenerateRandomInput(remainingCount))

    return input

def CreateData():
    functionList=[GenerateAlmostSorted,GenerateReversed,GenerateFewUnique,GenerateRandomInput,GenerateAlmostReversed]

    with open("data.txt","w+") as file:
        for j in range(0,4):
            input = functionList[j](10)
            WriteData(file,input)
        #emptyInput
        WriteData(file,[])
        for j in range(100):
            count = random.randint(0,400)
            functionId = random.randint(0,4)
            WriteData(file,functionList[functionId](count))
    pass

def WriteData(file,input):
    output = sorted(input)
    file.write("{}\n".format(",".join([str(i) for i in input])))
    file.write("{}\n".format(",".join([str(o) for o in output])))

if __name__ == '__main__':
    random.seed()
    CreateData()
