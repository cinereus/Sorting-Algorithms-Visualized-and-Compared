# -*- coding: utf-8 -*-

"""
Muhammet Furkan MUŞTU
160403041
"""
"""Insertion Sort"""
import numpy


def sorting(array):
    for j in range(1, len(array)):
        swap = int(array[j])
        i = j - 1
        while i >= 0 and int(array[i]) > swap:
            array[i + 1] = int(array[i])
            i = i - 1
        array[i + 1] = swap
    return array


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
    array = MakeArray()
    print("Given array is :", array)
    sorting(array)
    print("Sorted array is :", array)
