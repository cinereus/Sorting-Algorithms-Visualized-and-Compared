# -*- coding: utf-8 -*-

"""
Muhammet Furkan MUŞTU
160403041
"""
"""Bubble Sort"""

import numpy

def Sorting(array):        #Sorting Algorithm for Bubble Sort
    n = len(array)
    for i in range(n):           # Traverse through all array elements
        # Last i elements are already in place
        for j in range(0, n-i-1):                                   # Traverse the array from 0 to n-i-1
            if int(array[j]) > int(array[j+1]) :                        # Swap if the element found is greater
                array[j], array[j+1] = int(array[j+1]), int(array[j])       # than the next element
    return array
        

def MakeArray():
    print("Please enter minimum value of numbers in array: ")
    MinVal = int(input())
    print("Please enter Maximum value of numbers in array: ")
    MaxVal = int(input())
    print("Please enter how many numbers do you want in array: ")
    NumberOfItems = int(input())
    UnsortedArray = numpy.random.randint(MinVal,MaxVal,NumberOfItems)
#    self.array = []
#    i = 0
#    print("please input your array one by one\n")
#    while i < 999999999:
#        self.array.append(input())
#        if self.array[i] == '':
#            del self.array[i]
#            break
#        i=i+1
#    n = len(self.array)
#    i = 0
#    for i in range(i,n):
#        self.array[i] = int(self.array[i])
#        i +=1
    return UnsortedArray
    
if __name__ == '__main__':
    array = MakeArray()
    print("Given array is :",array)
    Sorting(array)
    print("Sorted array is :",array)