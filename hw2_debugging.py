'''
This module runs merge sort
'''
import rand

def merge_sort(arr):
    '''
    This method initializes the recursion for merge sort, and splits the array in half
    
    Parameters
    -----
    arr - list of numbers
    
    Returns
    -----
    sorted array
    
    '''
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    '''
    This method recombines the array after it is split in merge_sort 
    
    Parameters
    -----
    left_arr - left side of the array
    right_arr - right side of the array
    
    Returns
    -----
    left and right sides of the array merged back together
    '''
    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr.append(right_arr[i])

    for i in range(left_index, len(left_arr)):
        merge_arr.append(left_arr[i])

    return merge_arr


randArr = rand.random_array([None] * 20)
arr_out = merge_sort(randArr)

print(arr_out)
