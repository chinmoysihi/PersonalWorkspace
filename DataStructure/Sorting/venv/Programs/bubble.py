# Bubble Sort of a user given list of element
from builtins import range


def bubble_Sort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        print(arr)
    return arr


if __name__ == '__main__':
    numOfElem = int(input("Please enter no of values & Enter the numbers in new Line: "))

    numArr = []
    for i in range(0, numOfElem):
        newNum = input().split('\n')
        numArr.append(int(newNum[0]))

    numArr = bubble_Sort(numArr)
    print(numArr)
