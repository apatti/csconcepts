import sys
sys.path.append("{}/{}".format(sys.path[0],"../../bubblesort/python/"))
sys.path.append("{}/{}".format(sys.path[0],"../../selectionsort/python/"))
sys.path.append("{}/{}".format(sys.path[0],"../../insertionsort/python/"))
#print(sys.path)
import bubbleSort
import selectionSort
import insertionSort
import argparse

parser = argparse.ArgumentParser(description="Enter Sort method, use all for testing all methods. Default is 'all'")
parser.add_argument('method',type=str,default="all",help="sort method in lowercase")
args = parser.parse_args()

functionMap = {
    "bubblesort":bubbleSort.Sort,
    "selectionsort":selectionSort.Sort,
    "insertionsort":insertionSort.Sort
}

def TestSorting(function,input,expected):
    output = function(input)
    assert output==expected,"\nReturned:{}\nExpected:{}".format(output,expected)


if __name__ == '__main__':
    sortMethod = args.method
    with open("../../TestData/data.txt","r") as file:
        testData = file.readlines()

    for i in range(0,len(testData),2):
        testNumber = (i//2)+1
        print("Testing:{}".format(testNumber))
        input = [int(s.rstrip()) for s in testData[i].split(',') if s.rstrip()!='']
        output = [int(s.rstrip()) for s in testData[i+1].split(',') if s.rstrip()!='']
        if sortMethod.lower()=='all':
            for function in functionMap.values():
                TestSorting(function,input,output)
        else:
            TestSorting(functionMap[sortMethod],input,output)
