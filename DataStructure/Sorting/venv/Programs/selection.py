# Bubble Sort of a user given list of element
from builtins import range


def selection_Sort(arr):
    for i in range(len((arr))):
        minPos = i
        for j in range(i, len(arr)):
            if arr[minPos] > arr[j]:
                minPos = j

        temp = arr[minPos]
        arr[minPos] = arr[i]
        arr[i] = temp
        print(arr)
    return arr


if __name__ == '__main__':
    numOfElem = int(input("Please enter no of values & Enter the numbers in new Line: "))

    numArr = []
    for i in range(0, numOfElem):
        newNum = input().split('\n')
        numArr.append(int(newNum[0]))

    numArr = selection_Sort(numArr)
    print(numArr)
