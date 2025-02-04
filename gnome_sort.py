'''
This module runs gnome sort
'''
# import rand

def gnome_sort(array):
    '''
    This method sorts the array with gnome sort.
    
    Parameters
    -----
    array - list of numbers
    
    Returns
    -----
    sorted array
    '''
    i = 0 #init 1
    length = len(array)#find length of array
    while i < length: #for the entire array
        #if we either are at zero, or current element is greater than the last element
        if i == 0 or array[i] >= array[i-1]:
            i += 1 #increment the position
        else:
            swap = array[i - 1] #swap the i and i-1 element
            array[i -1] = array[i]
            array[i] = swap
            i -= 1 #decrement position
    return array
# arr = rand.random_array([None] * 20)
# print(arr)

# arr_out = gnome_sort(arr)

# print(arr_out)
