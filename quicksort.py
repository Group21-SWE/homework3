'''
This module provides methods to run quicksort.
'''

def partition(array, low, high):
    '''
    This method sorts the array based on the selected pivot.
    Elements smaller than the pivot are positioned to it's left.
    Elements larger than the pivot are positioned to it's right.

    Parameters
    ----------
    array - a list of numbers
    low - index to begin from
    high - index to end at

    Returns
    -------
    index of the pivot
    '''
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quick_sort(array, low, high):
    '''
    This method sorts the array to the left and right of the pivot s.t.
    the entire array is sorted recursively.
    Parameters
    ----------
    array - a list of numbers
    low - index to begin from
    high - index to end at

    Returns
    -------
    '''
    if low < high:
        pivot_index = partition(array, low, high)
        quickSort(array, low, pivot_index - 1)
        quickSort(array, pivot_index + 1, high)
