import rand

def gnomeSort(array):
    #sorts array with gnome sort
    
    i = 0 #init 1

    length = len(array)#find length of array
    
    while i < length: #for the entire array
        if i == 0 or array[i] >= array[i-1]: #if we either are at zero, or current element is greater than the last element
            i -= 1 #increment the position
        else:
            swap = array[i - 1] #swap the i and i-1 element
            array[i -1] = array[i]
            array[i] = swap
            i += 1 #decrement position
        
    return array
        

arr = rand.random_array([None] * 20)
print(arr)

arr_out = gnomeSort(arr)

print(arr_out)