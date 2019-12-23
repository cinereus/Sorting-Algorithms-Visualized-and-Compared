# -*- coding: utf-8 -*-

"""
Muhammet Furkan MUŞTU
160403041
"""
"""Counting Sort"""
import numpy
# The main function that sort the given string arr[] in
# alphabetical order
def countSort(arr,maxRange):
    # The output character array that will have sorted arr
    output = [0] * maxRange

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0] * maxRange

    # For storing the resulting answer since the
    # string is immutable
    #ans = [0] * len(arr)
    ans = numpy.random.randint(0, 1, len(arr))

    # Store count of each character
    for i in arr:
        count[i] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(maxRange):
        count[i] += count[i - 1]

        # Build the output character array
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


# Driver program to test above function
if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    ans = countSort(arr,1000)
    print("Sorted array is ", ans)