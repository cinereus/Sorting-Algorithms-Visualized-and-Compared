# -*- coding: utf-8 -*-

"""
Muhammet Furkan MUŞTU
160403041
"""
"""Merge Sort"""
import Insertion
import numpy


def merge(UnsortedArray):
    ArrayLength = len(UnsortedArray)
    if (ArrayLength % 2) == 0:
        m = int(ArrayLength / 2)
        n1 = int(m)
        n2 = int(ArrayLength - m)
    else:
        m = int((ArrayLength + 1) / 2)
        n1 = int(m)
        n2 = int(ArrayLength - m)

    # create temp arrays
    #    Left_array = [0] * (n1)
    #    Right_array = [0] * (n2)
    Left_array = [0] * (n1 + 1)
    Right_array = [0] * (n2 + 1)

    # Copy data to temp arrays Left_array[] and Right_array[]
    for i in range(0, n1):
        Left_array[i] = (int(UnsortedArray[i]))
    Left_array[n1] = 999999999999999999999999999999

    for j in range(0, n2):
        Right_array[j] = (int(UnsortedArray[m + j]))
    Right_array[n2] = 999999999999999999999999999999

    # Sort temp arrays with insertion sorting algorithm
    Left_arraySorted = Insertion.sorting(Left_array)
    Right_arraySorted = Insertion.sorting(Right_array)

    # Merge the temp arrays back into sequence[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = 0  # l	 # Initial index of merged subarray

    for k in range(0, ArrayLength):
        if Left_arraySorted[i] <= Right_arraySorted[j]:
            UnsortedArray[k] = int(Left_arraySorted[i])
            if i == n1:
                continue
            i += 1
        else:
            UnsortedArray[k] = int(Right_arraySorted[j])
            # if j<n2-1:
            if j == n2:
                continue
            j += 1

    return UnsortedArray


def MakeArray():
    print("Please enter minimum value of numbers in array: ")
    MinVal = int(input())
    print("Please enter Maximum value of numbers in array: ")
    MaxVal = int(input())
    print("Please enter how many numbers do you want in array: ")
    NumberOfItems = int(input())
    UnsortedArray = numpy.random.randint(MinVal, MaxVal, NumberOfItems)
    #    array = []
    #    i = 0
    #    print("please input your array one by one\n")
    #    while i < 999999999:
    #        array.append(input())
    #        if array[i] == '':
    #            del array[i]
    #            break
    #        i=i+1
    #    n = len(array)
    #    i = 0
    #    for i in range(i,n):
    #        array[i] = int(array[i])
    #        i +=1
    return UnsortedArray


if __name__ == '__main__':
    UnsortedArray = MakeArray()
    print("Given array is :", UnsortedArray)
    array = merge(UnsortedArray)
    print("Sorted array is :", array)
