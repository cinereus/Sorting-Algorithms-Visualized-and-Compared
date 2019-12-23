# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, sizeOfHeap, i):
    """"
    :param arr: Unsorted Array
    :param sizeOfHeap:
    :param i:
    :return: heapified arr
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    rigth = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < sizeOfHeap and arr[i] < arr[left]:
        largest = left

        # See if right child of root exists and is greater than root
    if rigth < sizeOfHeap and arr[largest] < arr[rigth]:
        largest = rigth

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, sizeOfHeap, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    """

    :param arr: Array
    :return: Sorted Array
    """
    lengthArray = len(arr)

    # Build a maxheap.
    for i in range(lengthArray, -1, -1):
        heapify(arr, lengthArray, i)

        # One by one extract elements
    for i in range(lengthArray - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    # Driver code to test above


if __name__=="__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    lengthOfArray = len(arr)
    print("Sorted array is")
    for i in range(lengthOfArray):
        print("%d" % arr[i])

    print(arr)