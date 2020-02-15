# Insertion Sort of a user given list of element
from builtins import range


def insertion_sort(arr):
    for i in range(1, len(arr)):
        position = i - 1
        posval = arr[i]
        # print('{}  :  {}  :  {}'.format(position, posval, arr[i - 1]))
        while position >= 0 and posval < arr[position]:
            arr[position + 1] = arr[position]
            position = position - 1

        arr[position + 1] = posval
        # print(arr)
    # print(arr)
    return arr


if __name__ == '__main__':
    numOfElem = int(input("Please enter no of values & Enter the numbers in new Line: "))

    numArr = []
    for i in range(0, numOfElem):
        newNum = input().split('\n')
        numArr.append(int(newNum[0]))

    numArr = insertion_sort(numArr)
    print(numArr)
