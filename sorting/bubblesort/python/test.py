import bubbleSort
import argparse

parser = argparse.ArgumentParser(description="Enter Sort method, use all for testing all methods. Default is 'all'")
parser.add_argument('method',type=str,default="all",help="sort method in lowercase")
args = parser.parse_args()

functionMap = {
    "bubblesort":bubbleSort.Sort
}

def TestSorting(function,input,expected):
    print(type(input))
    output = function(input)
    assert output==expected,"\nReturned:{}\nExpected:{}".format(output,expected)


if __name__ == '__main__':
    sortMethod = args.method
    with open("../../TestData/data.txt","r") as file:
        testData = file.readlines()

    for i in range(0,len(testData),2):
        testNumber = ((i+1)//2)
        print("Testing:{}".format(testNumber))
        input = [int(s.rstrip()) for s in testData[i].split(',')]
        output = [int(s.rstrip()) for s in testData[i+1].split(',')]
        if sortMethod.lower()=='all':
            for function in functionMap.values():
                TestSorting(function,input,output)
        else:
            TestSorting(functionMap[sortMethod],input,output)