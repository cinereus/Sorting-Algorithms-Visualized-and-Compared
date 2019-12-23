"""
Muhammet Furkan MUŞTU
160403041
"""
""" QuickSorting Algorithm """
import numpy

def Partition(Array, InitialIndex, LastIndex):
    """
    :param Array: Input Array
    :param InitialIndex: First index of Array
    :param LastIndex: Last index of Array
    :return: i+1 // next pivot point
    """
    Pivot = Array[LastIndex]
    i = InitialIndex - 1
    for j in range(InitialIndex, LastIndex):
        if Array[j] <= Pivot:  # if current element is less than or equal to pivot
            i = i + 1
            Array[i], Array[j] = Array[j], Array[i]  # exchange elements
    Array[i + 1], Array[LastIndex] = Array[LastIndex], Array[i + 1]  # exchange elements
    return i + 1


def RandPartition(Array, InitialIndex, LastIndex):
    """
    :param Array: Input Array
    :param InitialIndex: First index of Array
    :param LastIndex: Last index of Array
    :return: Partition function
    """
    i = InitialIndex - 1
    randomNumber = numpy.random.randint(InitialIndex, LastIndex, 1)
    Array[LastIndex], Array[randomNumber] = Array[randomNumber], Array[LastIndex]
    Pivot = Array[LastIndex]
    for j in range(InitialIndex, LastIndex):
        if Array[j] <= Pivot:  # if current element is less than or equal to pivot
            i = i + 1
            Array[i], Array[j] = Array[j], Array[i]  # exchange elements
    Array[i + 1], Array[LastIndex] = Array[LastIndex], Array[i + 1]  # exchange elements
    return i + 1


def QuickSort(Array, InitialIndex, LastIndex):
    """
    Initial call : QuickSort(array,0,arraylength-1)
    :param Array: Input Array
    :param InitialIndex: First index of Array
    :param LastIndex: Last index of Array
    :return: ----
    """
    if InitialIndex < LastIndex:  # check base case
        PivotPoint = Partition(Array, InitialIndex, LastIndex)
        QuickSort(Array, InitialIndex, PivotPoint - 1)  # call function recursively for subarrays
        QuickSort(Array, PivotPoint + 1, LastIndex)


def RandQuickSort(Array, InitialIndex, LastIndex):
    """
    Initial call : RandomizedQuickSort(array,0,arraylength-1)
    :param Array: Input Array
    :param InitialIndex: First index of Array
    :param LastIndex: Last index of Array
    :return: ----
    """
    if InitialIndex < LastIndex:  # check base case
        PivotPoint = RandPartition(Array, InitialIndex, LastIndex)
        RandQuickSort(Array, InitialIndex, PivotPoint - 1)  # call function recursively for subarrays
        RandQuickSort(Array, PivotPoint + 1, LastIndex)

if __name__=="__main__":
    Array = numpy.random.randint(0, 150, 15)
    LastIndex = len(Array) - 1
    print(Array)
    QuickSortedArray = Array.copy()
    RandomizeQuickSortedArray = Array.copy()
    print(LastIndex)
    QuickSort(QuickSortedArray, 0, LastIndex)
    RandQuickSort(RandomizeQuickSortedArray, 0, LastIndex)
    print(Array)
    print(QuickSortedArray)
    print(RandomizeQuickSortedArray)