# -*- coding: utf-8 -*-

"""
Muhammet Furkan MUŞTU
160403041
"""
"""k th smallest number"""

# This function returns k'th smallest element
from random import randint


def randomPartition(arr, firstIndex, lastIndex):
    n = lastIndex - firstIndex + 1
    pivot = randint(1, 100) % n
    arr[firstIndex + pivot], arr[lastIndex] = arr[firstIndex + pivot], arr[lastIndex]
    return partition(arr, firstIndex, lastIndex)


def kthSmallest(arr, firstIndex, lastIndex, k):
    # If k is smaller than
    # number of elements in array
    if (k > 0 and k <= lastIndex - firstIndex + 1):

        # Partition the array around last element and
        # get position of pivot element in sorted array
        pos = randomPartition(arr, firstIndex, lastIndex)

        # If position is same as k
        if (pos - firstIndex == k - 1):
            return arr[pos]

            # If position is more, recur for left subarray
        if (pos - firstIndex > k - 1):
            return kthSmallest(arr, firstIndex, pos - 1, k)

            # Else recur for right subarray
        return kthSmallest(arr, pos + 1, lastIndex, k - pos + firstIndex - 1)

        # If k is more than number of elements in array
    return 10 ** 9


# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right
def partition(arr, firstIndex, lastIndex):
    x = arr[lastIndex]
    i = firstIndex
    for j in range(firstIndex, lastIndex):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[lastIndex] = arr[lastIndex], arr[i]
    return i


# Driver Code
if __name__ == "__main__":

    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is", kthSmallest(arr, 0, n - 1, k))
